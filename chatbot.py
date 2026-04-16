"""
CHATBOT DE CONDUCCIÓN Y SEGURIDAD VIAL - COSTA RICA
Sistema de Asistente Virtual para Educación en Tránsito
Autor: Sistema de IA
Descripción: Chatbot inteligente que responde preguntas sobre normas de tránsito costarricense
"""

import re
from typing import Dict, List, Tuple
from difflib import SequenceMatcher
import unicodedata

from knowledge_base import knowledge_base


class PreprocessadorTexto:
    """
    Clase encargada del preprocesamiento del texto ingresado por el usuario.
    Realiza normalización, eliminación de caracteres especiales y tokenización.
    """
    
    @staticmethod
    def normalizar_texto(texto: str) -> str:
        """
        Normaliza el texto removiendo acentos y convirtiendo a minúsculas.
        
        Args:
            texto (str): Texto a normalizar
            
        Returns:
            str: Texto normalizado
        """
        # Convertir a minúsculas
        texto = texto.lower()
        
        # Remover acentos
        texto_normalizado = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        
        return texto_normalizado
    
    @staticmethod
    def limpiar_puntuacion(texto: str) -> str:
        """
        Elimina caracteres especiales y puntuación del texto.
        
        Args:
            texto (str): Texto a limpiar
            
        Returns:
            str: Texto sin puntuación
        """
        # Remover puntuación pero mantener espacios
        texto_limpio = re.sub(r'[^a-záéíóúñ\s]', '', texto)
        # Remover espacios múltiples
        texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
        return texto_limpio
    
    @staticmethod
    def tokenizar(texto: str) -> List[str]:
        """
        Divide el texto en palabras (tokens).
        
        Args:
            texto (str): Texto a tokenizar
            
        Returns:
            List[str]: Lista de palabras
        """
        return texto.split()
    
    @staticmethod
    def preprocesar(texto: str) -> Tuple[str, List[str]]:
        """
        Realiza todo el preprocesamiento del texto.
        
        Args:
            texto (str): Texto a procesar
            
        Returns:
            Tuple[str, List[str]]: (texto procesado, lista de tokens)
        """
        texto_normalizado = PreprocessadorTexto.normalizar_texto(texto)
        texto_limpio = PreprocessadorTexto.limpiar_puntuacion(texto_normalizado)
        tokens = PreprocessadorTexto.tokenizar(texto_limpio)
        
        return texto_limpio, tokens


class DetectorIntención:
    """
    Clase para detectar la intención del mensaje del usuario.
    Identifica palabras clave y categorías de preguntas.
    """
    
    # Palabras clave por categoría
    PALABRAS_CLAVE = {
        "señales_de_tránsito": [
            "alto", "pare", "ceda", "señal", "semáforo", "luz", "rojo", "verde", 
            "amarillo", "línea", "raya", "continua", "punteada", "discontinua"
        ],
        "prioridad_de_paso": [
            "prioridad", "paso", "primero", "derecha", "rotonda", "glorieta", 
            "peatón", "cruzar", "emergencia", "sirena", "ambulancia", "bomberos",
            "ciclista", "bicicleta"
        ],
        "normas_de_circulación": [
            "carril", "adelantar", "rebasar", "giro", "señal de giro", "intermitente",
            "luz", "distancia", "estacionamiento", "aparcar", "cambio de carril"
        ],
        "límites_de_velocidad": [
            "velocidad", "rápido", "km/h", "límite", "máxima", "lluvia", 
            "escuela", "mojado", "exceso"
        ],
        "conducción_defensiva": [
            "defensiva", "seguro", "cansancio", "sueño", "alcohol", "bebida",
            "distracción", "celular", "teléfono", "rabia", "agresión", "emociones"
        ],
        "seguridad_vial": [
            "cinturón", "airbag", "bolsa", "freno", "llanta", "mantenimiento",
            "visibilidad", "noche", "niebla", "accidente", "emergencia", "lesión",
            "seguridad", "sistema de seguridad"
        ]
    }
    
    @staticmethod
    def detectar_categoría(tokens: List[str]) -> str:
        """
        Detecta la categoría/tema principal de la pregunta.
        
        Args:
            tokens (List[str]): Tokens del mensaje
            
        Returns:
            str: Categoría detectada
        """
        # Contar coincidencias por categoría
        puntuaciones = {}
        
        for categoría, palabras_clave in DetectorIntención.PALABRAS_CLAVE.items():
            puntuacion = sum(1 for token in tokens if token in palabras_clave)
            puntuaciones[categoría] = puntuacion
        
        # Retornar categoría con puntuación más alta
        if max(puntuaciones.values()) > 0:
            return max(puntuaciones, key=puntuaciones.get)
        
        # Si no hay coincidencia clara, retornar None
        return None
    
    @staticmethod
    def es_pregunta(texto: str) -> bool:
        """
        Determina si el texto es una pregunta.
        
        Args:
            texto (str): Texto a evaluar
            
        Returns:
            bool: True si es pregunta, False en caso contrario
        """
        palabras_pregunta = ["qué", "cómo", "cuándo", "dónde", "por qué", "cuál", 
                            "cuáles", "puedo", "debo", "es", "puedes", "hay"]
        
        tokens = PreprocessadorTexto.tokenizar(texto)
        return any(token in palabras_pregunta for token in tokens) or texto.endswith("?")


class BuscadorConocimiento:
    """
    Clase encargada de buscar respuestas en la base de conocimiento.
    Implementa algoritmos de similitud para encontrar la mejor coincidencia.
    """
    
    @staticmethod
    def calcular_similitud(texto1: str, texto2: str) -> float:
        """
        Calcula la similitud entre dos textos usando SequenceMatcher.
        
        Args:
            texto1 (str): Primer texto
            texto2 (str): Segundo texto
            
        Returns:
            float: Puntuación de similitud entre 0 y 1
        """
        matcher = SequenceMatcher(None, texto1, texto2)
        return matcher.ratio()
    
    @staticmethod
    def similitud_tokens(tokens_usuario: List[str], tokens_patron: List[str]) -> float:
        """
        Calcula similitud basada en coincidencia de tokens.
        
        Args:
            tokens_usuario (List[str]): Tokens de entrada del usuario
            tokens_patron (List[str]): Tokens del patrón en la base de datos
            
        Returns:
            float: Puntuación de similitud
        """
        if not tokens_patron:
            return 0.0
        
        # Contar coincidencias
        coincidencias = sum(1 for token in tokens_usuario if token in tokens_patron)
        
        # Retornar proporción
        return coincidencias / len(tokens_patron)
    
    @staticmethod
    def buscar_en_categoría(tokens_usuario: str, categoría: str) -> Tuple[Dict, float]:
        """
        Busca la mejor coincidencia dentro de una categoría específica.
        
        Args:
            tokens_usuario (str): Tokens del usuario
            categoría (str): Categoría donde buscar
            
        Returns:
            Tuple[Dict, float]: (entrada encontrada, puntuación de similitud)
        """
        if categoría not in knowledge_base:
            return None, 0
        
        entradas = knowledge_base[categoría]
        mejor_entrada = None
        mejor_puntuación = 0
        
        for entrada in entradas:
            for patrón in entrada["patterns"]:
                # Preprocesar patrón
                _, tokens_patron = PreprocessadorTexto.preprocesar(patrón)
                
                # Calcular similitud
                similitud = BuscadorConocimiento.similitud_tokens(
                    tokens_usuario, tokens_patron
                )
                
                if similitud > mejor_puntuación:
                    mejor_puntuación = similitud
                    mejor_entrada = entrada
        
        return mejor_entrada, mejor_puntuación
    
    @staticmethod
    def buscar_respuesta(texto_usuario: str, categoría: str = None) -> Tuple[str, float, Dict]:
        """
        Busca la respuesta más adecuada según el texto del usuario.
        
        Args:
            texto_usuario (str): Pregunta del usuario
            categoría (str): Categoría específica (opcional)
            
        Returns:
            Tuple[str, float, Dict]: (respuesta, confianza, metadatos)
        """
        # Preprocesar texto del usuario
        texto_limpio, tokens_usuario = PreprocessadorTexto.preprocesar(texto_usuario)
        
        # Detectar categoría si no se proporciona
        if categoría is None:
            categoría = DetectorIntención.detectar_categoría(tokens_usuario)
        
        # Si no se detecta categoría, buscar en todas
        if categoría is None:
            mejores = []
            for cat in knowledge_base.keys():
                entrada, puntuación = BuscadorConocimiento.buscar_en_categoría(
                    tokens_usuario, cat
                )
                if entrada and puntuación > 0:
                    mejores.append((entrada, puntuación, cat))
            
            if not mejores:
                return None, 0, {"categoría": "desconocida"}
            
            # Ordenar por puntuación y tomar el mejor
            mejores.sort(key=lambda x: x[1], reverse=True)
            entrada, puntuación, categoría = mejores[0]
        else:
            # Buscar en la categoría específica
            entrada, puntuación = BuscadorConocimiento.buscar_en_categoría(
                tokens_usuario, categoría
            )
        
        if entrada is None:
            return None, 0, {"categoría": categoría}
        
        return entrada["answer"], puntuación, {
            "id": entrada["id"],
            "categoría": categoría,
            "puntuación_confianza": puntuación
        }


class GeneradorRespuesta:
    """
    Clase encargada de generar la respuesta final para el usuario.
    Formatea y personaliza la respuesta según la confianza y contexto.
    """
    
    @staticmethod
    def generar_respuesta(texto_usuario: str) -> Dict:
        """
        Genera una respuesta completa basada en la entrada del usuario.
        
        Args:
            texto_usuario (str): Pregunta o entrada del usuario
            
        Returns:
            Dict: Diccionario con respuesta y metadatos
        """
        # Validar entrada
        if not texto_usuario or not texto_usuario.strip():
            return {
                "respuesta": "Por favor, ingresa una pregunta sobre conducción y seguridad vial.",
                "tipo": "error",
                "confianza": 0,
                "metadatos": {}
            }
        
        # Buscar respuesta en la base de conocimiento
        respuesta, confianza, metadatos = BuscadorConocimiento.buscar_respuesta(
            texto_usuario
        )
        
        # Si no hay respuesta, generar respuesta por defecto
        if respuesta is None:
            return {
                "respuesta": GeneradorRespuesta._generar_respuesta_desconocida(
                    texto_usuario, metadatos
                ),
                "tipo": "no_encontrada",
                "confianza": 0,
                "metadatos": metadatos
            }
        
        # Generar respuesta según nivel de confianza
        if confianza < 0.3:
            tipo = "baja_confianza"
            intro = "Aunque no estoy completamente seguro, basándome en tu pregunta: "
            respuesta_final = intro + respuesta
        elif confianza < 0.6:
            tipo = "media_confianza"
            respuesta_final = respuesta
        else:
            tipo = "alta_confianza"
            respuesta_final = respuesta
        
        return {
            "respuesta": respuesta_final,
            "tipo": tipo,
            "confianza": confianza,
            "metadatos": metadatos
        }
    
    @staticmethod
    def _generar_respuesta_desconocida(texto_usuario: str, metadatos: Dict) -> str:
        """
        Genera una respuesta cuando el chatbot no encuentra información relevante.
        
        Args:
            texto_usuario (str): Entrada del usuario
            metadatos (Dict): Metadatos de la búsqueda
            
        Returns:
            str: Respuesta por defecto
        """
        categoría = metadatos.get("categoría", "tránsito")
        
        respuestas_defecto = [
            f"No tengo información específica sobre eso en mi base de datos sobre {categoría}. "
            f"¿Podrías formular tu pregunta de otra manera?",
            
            f"No encontré una respuesta exacta sobre '{texto_usuario}'. "
            f"Te recomiendo consultar con la Unidad de Tránsito o un instructor de conducción certificado.",
            
            "Aunque no tengo información sobre eso, te sugiero que consultes "
            "las normas oficiales de tránsito de Costa Rica o contactes a un instructor certificado.",
            
            "Lamentablemente, no tengo datos sobre ese tema específico. "
            "¿Hay algo más sobre conducción segura o normas de tránsito que pueda ayudarte?"
        ]
        
        import random
        return random.choice(respuestas_defecto)
    
    @staticmethod
    def formatear_respuesta_visual(resultado: Dict) -> str:
        """
        Formatea la respuesta para presentación en consola.
        
        Args:
            resultado (Dict): Resultado de generador_respuesta
            
        Returns:
            str: Respuesta formateada
        """
        respuesta = resultado["respuesta"]
        confianza = resultado["confianza"]
        tipo = resultado["tipo"]
        
        # Crear línea de separación
        separador = "=" * 80
        
        # Formatear según tipo
        if tipo == "alta_confianza":
            marcador = "✓ RESPUESTA CONFIABLE"
        elif tipo == "media_confianza":
            marcador = "⚠ RESPUESTA CON CIERTA CERTEZA"
        elif tipo == "baja_confianza":
            marcador = "❓ RESPUESTA CON BAJA CONFIANZA"
        else:
            marcador = "ℹ INFORMACIÓN NO ENCONTRADA"
        
        # Construir respuesta formateada
        respuesta_formateada = f"""
{separador}
{marcador}
{separador}

{respuesta}

Confianza: {confianza*100:.1f}%
{separador}
"""
        return respuesta_formateada


class ChatbotConductor:
    """
    Clase principal del chatbot que integra todos los componentes.
    Orquesta el flujo completo desde entrada hasta respuesta.
    """
    
    def __init__(self):
        """Inicializa el chatbot."""
        self.historial = []
        self.contador_mensajes = 0
    
    def procesar_entrada(self, texto_usuario: str) -> Dict:
        """
        Procesa la entrada del usuario y genera una respuesta.
        
        Args:
            texto_usuario (str): Texto ingresado por el usuario
            
        Returns:
            Dict: Resultado con respuesta y metadatos
        """
        self.contador_mensajes += 1
        
        # Generar respuesta
        resultado = GeneradorRespuesta.generar_respuesta(texto_usuario)
        
        # Guardar en historial
        self.historial.append({
            "número": self.contador_mensajes,
            "entrada": texto_usuario,
            "respuesta": resultado["respuesta"],
            "tipo": resultado["tipo"],
            "confianza": resultado["confianza"]
        })
        
        return resultado
    
    def iniciar(self):
        """Inicia el chatbot en modo interactivo."""
        print("\n" + "="*80)
        print("BIENVENIDO AL CHATBOT DE CONDUCCIÓN Y SEGURIDAD VIAL")
        print("Sistema de Educación en Normas de Tránsito - Costa Rica")
        print("="*80)
        print("\nHola, soy tu asistente virtual de conducción.")
        print("Puedo responder preguntas sobre:")
        print("  • Señales de tránsito")
        print("  • Prioridad de paso")
        print("  • Normas de circulación")
        print("  • Límites de velocidad")
        print("  • Conducción defensiva")
        print("  • Seguridad vial")
        print("\nEscribe 'salir' para terminar la conversación.")
        print("="*80 + "\n")
        
        # Bucle de conversación
        while True:
            try:
                # Obtener entrada del usuario
                entrada = input("\nTú: ").strip()
                
                # Verificar si es comando de salida
                if entrada.lower() in ["salir", "exit", "quit", "bye"]:
                    print("\n¡Gracias por usar el chatbot de conducción!")
                    print(f"Se procesaron {self.contador_mensajes} consultas.")
                    break
                
                # Procesar entrada vacía
                if not entrada:
                    print("Por favor, ingresa una pregunta.")
                    continue
                
                # Procesar entrada y mostrar respuesta
                resultado = self.procesar_entrada(entrada)
                respuesta_visual = GeneradorRespuesta.formatear_respuesta_visual(resultado)
                print("\nChatbot:" + respuesta_visual)
                
            except KeyboardInterrupt:
                print("\n\n¡Sesión terminada por el usuario!")
                break
            except Exception as e:
                print(f"\nError: {e}")
                print("Por favor, intenta de nuevo.")
    
    def obtener_historial(self) -> List[Dict]:
        """
        Retorna el historial de conversaciones.
        
        Returns:
            List[Dict]: Historial de mensajes
        """
        return self.historial
    
    def generar_reporte(self) -> str:
        """
        Genera un reporte de la sesión.
        
        Returns:
            str: Reporte formateado
        """
        if not self.historial:
            return "No hay historial de conversaciones."
        
        reporte = "\n" + "="*80 + "\n"
        reporte += "REPORTE DE SESIÓN DEL CHATBOT\n"
        reporte += "="*80 + "\n\n"
        
        for item in self.historial:
            reporte += f"Pregunta {item['número']}: {item['entrada']}\n"
            reporte += f"Tipo: {item['tipo']} | Confianza: {item['confianza']*100:.1f}%\n"
            reporte += f"Respuesta: {item['respuesta'][:100]}...\n"
            reporte += "-"*80 + "\n"
        
        reporte += f"\nTotal de consultas procesadas: {self.contador_mensajes}\n"
        reporte += "="*80 + "\n"
        
        return reporte


# Función para modo demostración
def ejecutar_demostracion():
    """Ejecuta el chatbot con preguntas de demostración."""
    print("\n" + "="*80)
    print("DEMOSTRACIÓN DEL CHATBOT DE CONDUCCIÓN Y SEGURIDAD VIAL")
    print("="*80 + "\n")
    
    chatbot = ChatbotConductor()
    
    # Preguntas de demostración
    preguntas_demo = [
        "¿Qué significa la señal de alto?",
        "¿Cómo debo manejar en una rotonda?",
        "¿Cuál es el límite de velocidad en zona urbana?",
        "¿Es obligatorio usar cinturón de seguridad?",
        "¿Puedo manejar si estoy cansado?",
        "¿Cuál es la distancia segura entre vehículos?"
    ]
    
    for pregunta in preguntas_demo:
        print(f"\nPregunta: {pregunta}")
        resultado = chatbot.procesar_entrada(pregunta)
        respuesta_visual = GeneradorRespuesta.formatear_respuesta_visual(resultado)
        print("Respuesta:" + respuesta_visual)
        input("Presiona Enter para continuar...")
    
    # Mostrar reporte
    print(chatbot.generar_reporte())


if __name__ == "__main__":
    # Ejecutar chatbot
    # Descomenta una de las siguientes líneas:
    
    # Para modo interactivo:
    chatbot = ChatbotConductor()
    chatbot.iniciar()
    
    # Para demostración automática (descomenta esto):
    # ejecutar_demostracion()
