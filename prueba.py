import re
import unicodedata
import random
from typing import Dict, List, Tuple
from difflib import SequenceMatcher

# =============================================================================
# BASE DE CONOCIMIENTO INTEGRADA
# =============================================================================
knowledge_base = {
    "señales_de_tránsito": [
        {
            "id": "st_01",
            "patterns": ["que significa la señal de alto", "para que sirve el alto", "señal pare"],
            "answer": "La señal de ALTO indica la obligación de detener el vehículo completamente antes de la línea de parada o antes de entrar a la intersección. No basta con disminuir la velocidad; el vehículo debe cesar su movimiento total."
        },
        {
            "id": "st_02",
            "patterns": ["que es el ceda el paso", "señal de ceda", "prioridad ceda"],
            "answer": "La señal de CEDA EL PASO indica que el conductor debe reducir su velocidad y detenerse si es necesario para permitir el paso a los vehículos que circulan por la vía preferencial."
        },
        {
            "id": "st_03",
            "patterns": ["semaforo en rojo", "luz roja", "girar en rojo"],
            "answer": "La luz ROJA indica detención obligatoria. En Costa Rica, se permite el giro a la derecha en rojo si no hay vehículos viniendo y no hay una señal que lo prohíba expresamente, siempre haciendo la parada previa."
        }
    ],
    "prioridad_de_paso": [
        {
            "id": "pp_01",
            "patterns": ["quien tiene prioridad en rotonda", "como manejar en rotonda", "paso en la glorieta"],
            "answer": "En una rotonda, los vehículos que ya circulan dentro de ella tienen la prioridad de paso sobre los que intentan ingresar. Siempre se debe ceder el paso a quien viene por la izquierda dentro del anillo."
        },
        {
            "id": "pp_02",
            "patterns": ["prioridad vehiculos emergencia", "ambulancia sirena", "paso bomberos"],
            "answer": "Los vehículos de emergencia (ambulancias, bomberos, policía) tienen prioridad absoluta de paso cuando circulan con sirenas y luces activas. Debes orillarte a la derecha y detenerte si es necesario."
        }
    ],
    "límites_de_velocidad": [
        {
            "id": "lv_01",
            "patterns": ["limite velocidad zona urbana", "velocidad en ciudad", "cuanto es la maxima en ciudad"],
            "answer": "En zonas urbanas, el límite de velocidad estándar es de 40 km/h, a menos que una señal indique lo contrario (como en zonas de alta densidad o centros comerciales donde baja a 25 km/h)."
        },
        {
            "id": "lv_02",
            "patterns": ["limite velocidad escuela", "zona escolar velocidad", "colegio niños velocidad"],
            "answer": "En zona escolar, el límite es de 25 km/h cuando hay presencia de estudiantes. Incumplir esto es una de las faltas más graves en la ley de tránsito."
        }
    ],
    "conducción_defensiva": [
        {
            "id": "cd_01",
            "patterns": ["que es conduccion defensiva", "manejar seguro", "evitar accidentes"],
            "answer": "La conducción defensiva consiste en conducir para salvar vidas, tiempo y dinero, a pesar de las condiciones que le rodean y de las acciones de los demás. Implica anticipar peligros y reaccionar correctamente."
        },
        {
            "id": "cd_02",
            "patterns": ["alcohol y conduccion", "puedo tomar y manejar", "bebidas alcoholicas"],
            "answer": "El consumo de alcohol afecta la visión, los reflejos y el juicio. La ley establece sanciones severas según el nivel de alcohol en sangre; lo más seguro es: si toma, no maneje."
        }
    ],
    "seguridad_vial": [
        {
            "id": "sv_01",
            "patterns": ["distancia entre vehiculos", "distancia de seguridad", "regla de los dos segundos"],
            "answer": "Se recomienda mantener la 'regla de los dos segundos' en condiciones normales: busca un punto fijo y, cuando el auto de adelante pase por ahí, debes tardar al menos 2 segundos en llegar al mismo punto. Bajo lluvia, duplica esa distancia."
        },
        {
            "id": "sv_02",
            "patterns": ["uso del cinturon", "quien debe usar cinturon", "seguridad pasajeros"],
            "answer": "El uso del cinturón de seguridad es obligatorio para todos los ocupantes del vehículo, tanto en los asientos delanteros como en los traseros. Su uso reduce drásticamente el riesgo de muerte en colisiones."
        }
    ]
}

# =============================================================================
# CLASES DEL SISTEMA
# =============================================================================

class PreprocessadorTexto:
    @staticmethod
    def normalizar_texto(texto: str) -> str:
        texto = texto.lower()
        texto_normalizado = ''.join(
            c for c in unicodedata.normalize('NFD', texto)
            if unicodedata.category(c) != 'Mn'
        )
        return texto_normalizado
    
    @staticmethod
    def limpiar_puntuacion(texto: str) -> str:
        texto_limpio = re.sub(r'[^a-záéíóúñ\s]', '', texto)
        texto_limpio = re.sub(r'\s+', ' ', texto_limpio).strip()
        return texto_limpio
    
    @staticmethod
    def tokenizar(texto: str) -> List[str]:
        return texto.split()
    
    @staticmethod
    def preprocesar(texto: str) -> Tuple[str, List[str]]:
        texto_normalizado = PreprocessadorTexto.normalizar_texto(texto)
        texto_limpio = PreprocessadorTexto.limpiar_puntuacion(texto_normalizado)
        tokens = PreprocessadorTexto.tokenizar(texto_limpio)
        return texto_limpio, tokens

class DetectorIntención:
    PALABRAS_CLAVE = {
        "señales_de_tránsito": ["alto", "pare", "ceda", "señal", "semaforo", "luz", "rojo"],
        "prioridad_de_paso": ["prioridad", "paso", "primero", "rotonda", "emergencia", "ambulancia"],
        "normas_de_circulación": ["carril", "adelantar", "giro", "intermitente", "estacionar"],
        "límites_de_velocidad": ["velocidad", "kmh", "limite", "maxima", "rapido", "escuela"],
        "conducción_defensiva": ["defensiva", "seguro", "alcohol", "sueño", "cansancio", "distraccion"],
        "seguridad_vial": ["cinturon", "distancia", "llanta", "freno", "seguridad", "accidente"]
    }
    
    @staticmethod
    def detectar_categoría(tokens: List[str]) -> str:
        puntuaciones = {cat: 0 for cat in DetectorIntención.PALABRAS_CLAVE}
        for categoría, palabras in DetectorIntención.PALABRAS_CLAVE.items():
            puntuaciones[categoría] = sum(1 for token in tokens if token in palabras)
        
        if max(puntuaciones.values()) > 0:
            return max(puntuaciones, key=puntuaciones.get)
        return None

class BuscadorConocimiento:
    @staticmethod
    def similitud_tokens(tokens_usuario: List[str], tokens_patron: List[str]) -> float:
        if not tokens_patron: return 0.0
        coincidencias = sum(1 for token in tokens_usuario if token in tokens_patron)
        return coincidencias / len(tokens_patron)
    
    @staticmethod
    def buscar_en_categoría(tokens_usuario: List[str], categoría: str) -> Tuple[Dict, float]:
        if categoría not in knowledge_base:
            return None, 0
        
        mejor_entrada = None
        mejor_puntuación = 0
        
        for entrada in knowledge_base[categoría]:
            for patrón in entrada["patterns"]:
                _, tokens_patron = PreprocessadorTexto.preprocesar(patrón)
                similitud = BuscadorConocimiento.similitud_tokens(tokens_usuario, tokens_patron)
                if similitud > mejor_puntuación:
                    mejor_puntuación = similitud
                    mejor_entrada = entrada
        return mejor_entrada, mejor_puntuación

    @staticmethod
    def buscar_respuesta(texto_usuario: str) -> Tuple[str, float, Dict]:
        texto_limpio, tokens_usuario = PreprocessadorTexto.preprocesar(texto_usuario)
        categoría = DetectorIntención.detectar_categoría(tokens_usuario)
        
        if categoría is None:
            mejores = []
            for cat in knowledge_base.keys():
                entrada, puntuación = BuscadorConocimiento.buscar_en_categoría(tokens_usuario, cat)
                if entrada and puntuación > 0:
                    mejores.append((entrada, puntuación, cat))
            if not mejores: return None, 0, {"categoría": "desconocida"}
            mejores.sort(key=lambda x: x[1], reverse=True)
            entrada, puntuación, categoría = mejores[0]
        else:
            entrada, puntuación = BuscadorConocimiento.buscar_en_categoría(tokens_usuario, categoría)
            
        if not entrada: return None, 0, {"categoría": categoría}
        return entrada["answer"], puntuación, {"id": entrada["id"], "categoría": categoría}

class GeneradorRespuesta:
    @staticmethod
    def generar_respuesta(texto_usuario: str) -> Dict:
        if not texto_usuario.strip():
            return {"respuesta": "Dime, ¿en qué puedo ayudarte hoy?", "tipo": "error", "confianza": 0}
            
        respuesta, confianza, metadatos = BuscadorConocimiento.buscar_respuesta(texto_usuario)
        
        if respuesta is None or confianza < 0.2:
            return {
                "respuesta": "Lo siento, no tengo esa información específica. Prueba preguntando sobre señales, rotondas o límites de velocidad.",
                "tipo": "no_encontrada", "confianza": 0, "metadatos": metadatos
            }
        
        return {"respuesta": respuesta, "tipo": "alta_confianza" if confianza > 0.5 else "media_confianza", "confianza": confianza, "metadatos": metadatos}

    @staticmethod
    def formatear_respuesta_visual(resultado: Dict) -> str:
        separador = "—" * 50
        return f"\n{separador}\n🤖 ASISTENTE VIAL\n{separador}\n{resultado['respuesta']}\n\n(Confianza: {resultado.get('confianza', 0)*100:.0f}%)\n{separador}"

class ChatbotConductor:
    def iniciar(self):
        print("SISTEMA DE CONSULTA VIAL - COSTA RICA")
        print("Escribe 'salir' para finalizar.")
        while True:
            entrada = input("\nPregunta: ")
            if entrada.lower() in ["salir", "exit"]: break
            resultado = GeneradorRespuesta.generar_respuesta(entrada)
            print(GeneradorRespuesta.formatear_respuesta_visual(resultado))

# =============================================================================
# EJECUCIÓN
# =============================================================================
if __name__ == "__main__":
    bot = ChatbotConductor()
    bot.iniciar()