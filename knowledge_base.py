# Base de Conocimiento para Chatbot de Conducción y Seguridad Vial
# Costa Rica - Normas de Tránsito

knowledge_base = {
    "señales_de_tránsito": [
        {
            "id": "s_001",
            "patterns": [
                "qué significa alto",
                "cómo debo actuar ante un alto",
                "señal de pare",
                "detenerse en alto",
                "alto en la calle",
                "regla del alto",
                "semáforo en rojo"
            ],
            "answer": "La señal de ALTO (o PARE) es una señal regulatoria que indica que debes detener "
                     "completamente tu vehículo. Debes permanecer detenido hasta asegurarte de que no viene "
                     "ningún vehículo u obstáculo. Solo entonces puedes continuar. Este es un requisito obligatorio "
                     "en todas las intersecciones marcadas con esta señal. No detenerse adecuadamente es una infracción grave."
        },
        {
            "id": "s_002",
            "patterns": [
                "ceda el paso",
                "qué es ceder",
                "cómo debo ceder",
                "señal de ceda",
                "ceda en intersección",
                "tengo derecho de paso",
                "quién pasa primero"
            ],
            "answer": "La señal de CEDA EL PASO te indica que debes reducir la velocidad y estar preparado "
                     "para detenerte si es necesario. Permite que pasen los vehículos que tienen derecho de paso. "
                     "A diferencia del ALTO, no es obligatorio detenerse si el camino está libre. Ceder el paso correctamente "
                     "es esencial para evitar accidentes y multas."
        },
        {
            "id": "s_003",
            "patterns": [
                "línea continua",
                "raya blanca continua",
                "no puedo rebasar",
                "qué significa línea continua",
                "prohibido adelantar",
                "puedo pasar la línea"
            ],
            "answer": "La LÍNEA CONTINUA (raya blanca sólida) en el pavimento indica que está prohibido rebasar o "
                     "adelantar a otros vehículos en ese tramo. Cruzar esta línea para pasar a otro vehículo es una infracción. "
                     "Estas líneas se utilizan en curvas, subidas, o lugares donde la visibilidad es limitada y el adelantamiento "
                     "sería peligroso. Respeta siempre las líneas continuas."
        },
        {
            "id": "s_004",
            "patterns": [
                "línea discontinua",
                "raya punteada",
                "puedo rebasar",
                "adelantar en línea punteada",
                "cómo pasar vehículos"
            ],
            "answer": "La LÍNEA DISCONTINUA (raya blanca punteada) indica que es permitido rebasar o adelantar "
                     "a otros vehículos, siempre que sea seguro hacerlo. Antes de adelantar debes: verificar que no venga "
                     "ningún vehículo de frente, usar la señal de giro, asegurar suficiente distancia y visibilidad. Aunque "
                     "esté permitido, solo hazlo cuando sea completamente seguro."
        },
        {
            "id": "s_005",
            "patterns": [
                "semáforo rojo",
                "luz roja",
                "debe detenerse en rojo",
                "qué hacer en rojo",
                "rojo significa parar"
            ],
            "answer": "El SEMÁFORO EN ROJO es una señal obligatoria que indica que debes detener completamente "
                     "tu vehículo. No puedes avanzar mientras esté en rojo, incluso si no viene tráfico. Esto incluye no girar "
                     "a la derecha en rojo a menos que haya una señal específica que lo permita. Pasar un semáforo en rojo "
                     "es una infracción grave y peligrosa."
        },
        {
            "id": "s_006",
            "patterns": [
                "semáforo verde",
                "luz verde",
                "puedo avanzar",
                "qué significa verde",
                "verde permite paso"
            ],
            "answer": "El SEMÁFORO EN VERDE indica que tienes el derecho de paso. Sin embargo, antes de avanzar "
                     "debes verificar que la intersección esté libre y que no haya peatones o vehículos que infrinjan la ley. "
                     "El semáforo verde es una invitación a proceder, pero NO garantiza seguridad absoluta. Siempre mantén "
                     "la precaución y observa el tráfico cruzado."
        },
        {
            "id": "s_007",
            "patterns": [
                "semáforo amarillo",
                "luz amarilla",
                "qué hago en amarillo",
                "puedo pasar en amarillo",
                "amarillo significa qué"
            ],
            "answer": "El SEMÁFORO EN AMARILLO es una señal de PRECAUCIÓN. Indica que el semáforo cambiará a rojo "
                     "muy pronto. Si estás lejos de la intersección, debes empezar a reducir la velocidad y prepararte a detenerte. "
                     "Si ya estás muy cerca y no puedes frenar de forma segura, puedes continuar. Nunca aceleres para 'ganarle' "
                     "al amarillo, ya que es muy peligroso."
        }
    ],
    
    "prioridad_de_paso": [
        {
            "id": "p_001",
            "patterns": [
                "rotonda",
                "cómo manejar en rotonda",
                "quién tiene derecho en rotonda",
                "norma de rotonda",
                "círculo de tráfico",
                "glorieta",
                "prioridad en rotonda"
            ],
            "answer": "En una ROTONDA (o glorieta), los vehículos que YA ESTÁN CIRCULANDO dentro de ella "
                     "tienen prioridad absoluta. Si vas a entrar a la rotonda, debes ceder el paso a quienes ya están adentro. "
                     "Entra cuando haya un espacio seguro. Dentro de la rotonda, circula en el carril correcto y usa tus señales "
                     "antes de salir. Nunca estaciones ni cruces una rotonda caminando sin asegurar que no hay tráfico."
        },
        {
            "id": "p_002",
            "patterns": [
                "paso de peatones",
                "cómo cruzar la calle",
                "pasos cebra",
                "prioridad peatones",
                "peatón en la vía",
                "cruzar en paso de cebra"
            ],
            "answer": "Los PEATONES tienen derecho de paso en los pasos de cebra. Como conductor, debes reducir "
                     "la velocidad y detenerte si es necesario para permitir que crucen. Aunque el semáforo esté en verde para ti, "
                     "debes ceder el paso a los peatones. Si un peatón intenta cruzar fuera del paso de cebra, debes evitarlo si es "
                     "posible, aunque el peatón esté cometiendo una infracción."
        },
        {
            "id": "p_003",
            "patterns": [
                "calle con una sola línea",
                "cuál es la prioridad sin señales",
                "sin semáforo qué hago",
                "cruzada sin señal",
                "cómo sé quién tiene derecho"
            ],
            "answer": "En una INTERSECCIÓN SIN SEÑALES, la prioridad la tiene el vehículo que viene por tu derecha. "
                     "Si un auto viene por tu derecha, debes ceder el paso. Si vienes por la derecha, tienes derecho de paso. "
                     "Cuando tengas duda, lo más seguro es reducir la velocidad y ceder el paso. Esta regla es fundamental "
                     "en las carreteras y calles sin señalización clara."
        },
        {
            "id": "p_004",
            "patterns": [
                "vehículo de emergencia",
                "ambulancia sirena",
                "bomberos sirena",
                "debo ceder paso a sirena",
                "cómo actuar ante sirena"
            ],
            "answer": "Cuando escuches la SIRENA de un vehículo de emergencia (ambulancia, bomberos, policía), "
                     "DEBES CEDER EL PASO INMEDIATAMENTE. Reduce la velocidad, aproximate al borde derecho de la calle "
                     "y detente si es necesario. No intentes acompañar al vehículo de emergencia. Los vehículos de emergencia "
                     "tienen prioridad absoluta en todas las situaciones."
        },
        {
            "id": "p_005",
            "patterns": [
                "bicicleta en la vía",
                "ciclista en la calle",
                "prioridad bicicleta",
                "cómo manejar cerca de ciclistas",
                "respeto a ciclistas"
            ],
            "answer": "Los CICLISTAS tienen derechos en la vía. Debes respetarlos y ofrecerles el mismo espacio "
                     "que a otros vehículos. Cuando adelantes un ciclista, debes cambiar de carril completamente y dejarle "
                     "mínimo 1 metro de distancia. Nunca cierres el paso a un ciclista. Si hay un carril exclusivo para bicicletas, "
                     "no invadas ese espacio."
        }
    ],
    
    "normas_de_circulación": [
        {
            "id": "n_001",
            "patterns": [
                "carril correcto",
                "qué carril usar",
                "carril derecho",
                "debo estar en el carril izquierdo",
                "cambio de carril"
            ],
            "answer": "En COSTA RICA, debes circular por el CARRIL DERECHO. El carril izquierdo se utiliza solo "
                     "para adelantar. Después de adelantar, debes volver al carril derecho. No debes estar en el carril izquierdo "
                     "de manera permanente aunque no estés adelantando. Si no estás adelantando a nadie, estar en el carril "
                     "izquierdo es una infracción y causa congestionamiento."
        },
        {
            "id": "n_002",
            "patterns": [
                "distancia entre vehículos",
                "espacio seguro",
                "distancia de frenado",
                "qué tan cerca puedo ir",
                "cola corta"
            ],
            "answer": "Debes mantener una DISTANCIA SEGURA con el vehículo de enfrente. Una buena regla es "
                     "dejar al menos 2 segundos de distancia a la velocidad que vas. En condiciones mojadas o lluvia, aumenta "
                     "a 4-6 segundos. No hagas cola corta (tailgating), que es peligroso y es infracción. Esta distancia te da "
                     "tiempo para frenar sin chocar si el vehículo de adelante se detiene repentinamente."
        },
        {
            "id": "n_003",
            "patterns": [
                "señal de giro",
                "indicador de dirección",
                "debo avisar antes de girar",
                "cuándo usar intermitentes",
                "cambio de carril intermitente"
            ],
            "answer": "SIEMPRE usa tu SEÑAL DE GIRO antes de girar o cambiar de carril. Debe activarse con "
                     "anticipación (mínimo 50 metros en vías urbanas y 100 metros en carreteras). No basta con poner la señal "
                     "al momento de girar; debes advertir con tiempo. Apaga la señal después de completar la maniobra. Usar "
                     "señal es ley y previene accidentes."
        },
        {
            "id": "n_004",
            "patterns": [
                "luces del vehículo",
                "cuándo enciende luces",
                "luces bajas",
                "luces altas",
                "faros"
            ],
            "answer": "Debes encender las LUCES BAJAS (parqueo) al atardecer, en túneles, y cuando llueve, "
                     "aunque sea de día. Las LUCES ALTAS se usan solo en carreteras oscuras sin tráfico de frente. Si ves "
                     "luces altas viniendo, apaga las tuyas y avisa con intermitentes. Mantén tus luces limpias y en buen estado. "
                     "Usar luces es ley y es esencial para la visibilidad."
        },
        {
            "id": "n_005",
            "patterns": [
                "adelantar correctamente",
                "pasar otro vehículo",
                "cómo rebasar",
                "condiciones para adelantar"
            ],
            "answer": "Para ADELANTAR CORRECTAMENTE debes: 1) Verificar que la línea lo permita (discontinua), "
                     "2) Asegurar que no viene vehículo de frente, 3) Usar señal de giro, 4) Cambiar de carril completamente, "
                     "5) Adelantar manteniendo distancia segura, 6) Usar señal al regresar al carril derecho. NUNCA adelantes "
                     "en curvas, subidas, pasos a nivel, o donde la visibilidad sea limitada. Adelantar imprudentemente causa "
                     "accidentes graves."
        },
        {
            "id": "n_006",
            "patterns": [
                "estacionamiento",
                "dónde estacionar",
                "estaciono en esquina",
                "estacionamiento permitido",
                "debo aparcar aquí"
            ],
            "answer": "NO puedes estacionar: en esquinas, curvas, pasos de cebra, pasos a nivel, zonas de carga, "
                     "frente a puertas de garaje, en doble fila, ni donde hay línea amarilla. Estaciona siempre en línea recta, "
                     "en espacios designados, y paralelo a la acera. En vías de tránsito rápido, no estaciones en la banquina. "
                     "Estaciona tu vehículo de forma que no obstruya el tránsito ni bloquees la visión de otros conductores."
        }
    ],
    
    "límites_de_velocidad": [
        {
            "id": "v_001",
            "patterns": [
                "velocidad máxima",
                "límite de velocidad",
                "cuán rápido puedo ir",
                "velocidad permitida ciudad",
                "zona urbana velocidad"
            ],
            "answer": "Los LÍMITES DE VELOCIDAD varían según el tipo de vía: En zonas URBANAS (ciudades): "
                     "40 km/h es el máximo general, 60 km/h en avenidas principales. En CARRETERAS SECUNDARIAS: 80 km/h. "
                     "En CARRETERAS PRIMARIAS/AUTOPISTAS: 100 km/h en el día, 90 km/h en la noche. Siempre respeta los "
                     "letreros de velocidad. Exceder el límite es infracción y aumenta el riesgo de accidentes graves."
        },
        {
            "id": "v_002",
            "patterns": [
                "velocidad en escuela",
                "zona escolar límite",
                "paso de escuela",
                "niños en la vía"
            ],
            "answer": "En zonas escolares y cerca de guarderías, el límite de velocidad es MÁS BAJO, generalmente "
                     "25-30 km/h, especialmente en horarios de entrada y salida. Debes conducir LENTAMENTE y estar atento a "
                     "niños. Reduce aún más la velocidad si ves niños en la acera. El horario de cuidado aumentado es usualmente "
                     "de 7 a 9 AM y de 2 a 4 PM. La seguridad de los niños es lo más importante."
        },
        {
            "id": "v_003",
            "patterns": [
                "lluvia velocidad",
                "carretera mojada",
                "cómo manejar lluvia",
                "reducir velocidad lluvia",
                "condiciones climáticas"
            ],
            "answer": "EN LLUVIA O CONDICIONES ADVERSAS, debes REDUCIR LA VELOCIDAD significativamente. "
                     "La tracción disminuye, el frenado es menos efectivo y el acuaplaneo es posible. Aumenta la distancia "
                     "de frenado a 6-8 segundos. Enciende las luces bajas incluso en lluvia de día. Evita charcos profundos. "
                     "Si tu vehículo derrapa, NO frenes bruscamente; suelta el acelerador y mantén el volante estable."
        },
        {
            "id": "v_004",
            "patterns": [
                "exceso de velocidad",
                "multa por velocidad",
                "cuánto puedo exceder",
                "pérdida de puntos velocidad"
            ],
            "answer": "EXCEDER EL LÍMITE DE VELOCIDAD es una de las infracciones más graves. Las consecuencias "
                     "incluyen: multas económicas, pérdida de puntos en la licencia, y en excesos severos, retención del vehículo. "
                     "Además, aumenta exponencialmente el riesgo de accidentes. Por cada km/h de exceso en zona urbana, el riesgo "
                     "de accidente mortal aumenta. No merece la pena ir rápido."
        }
    ],
    
    "conducción_defensiva": [
        {
            "id": "d_001",
            "patterns": [
                "conducción defensiva",
                "qué es manejar defensivo",
                "cómo manejar seguro",
                "princípios conducción defensiva"
            ],
            "answer": "LA CONDUCCIÓN DEFENSIVA es un enfoque donde anticipas problemas y actúas antes de que "
                     "ocurran. Incluye: 1) Mantener concentración y evitar distracciones, 2) Anticipar los movimientos de otros, "
                     "3) Respetar las normas y límites, 4) Mantener distancia segura, 5) Adaptar velocidad a condiciones, "
                     "6) Estar descansado y en buenas condiciones. Conducir defensivamente reduce accidentes en un 80%. "
                     "Es la mejor estrategia para protegerte a ti y a otros."
        },
        {
            "id": "d_002",
            "patterns": [
                "distracciones al manejar",
                "celular mientras conduzco",
                "no puedo mirar teléfono",
                "conducir sin distracciones"
            ],
            "answer": "NUNCA uses el celular mientras conduces, ni siquiera para llamadas manos libres si te distrae. "
                     "Las distracciones principales son: celular, comer, beber, maquillarse, cambiar de estación. Cada segundo "
                     "sin ver la carretera aumenta el riesgo. Programa el GPS antes de partir. Si necesitas revisar algo, detente "
                     "en lugar seguro. La distracción es causa de muchos accidentes. Tu atención al camino es crítica."
        },
        {
            "id": "d_003",
            "patterns": [
                "cansancio al manejar",
                "somnolencia conduciendo",
                "estoy cansado puedo manejar",
                "descanso en viaje largo"
            ],
            "answer": "NO CONDUZCAS si estás cansado o somnoliento. El cansancio reduce tus reflejos y capacidad "
                     "de reacción como si tuvieras una concentración de alcohol alta. En viajes largos, descansa cada 2-3 horas. "
                     "Si sientes sueño, DETENTE inmediatamente en lugar seguro. Duerme 15-20 minutos o cede el volante. Una "
                     "siesta corta puede ser muy efectiva. No vale la pena arriesgar tu vida ni la de otros por economizar tiempo."
        },
        {
            "id": "d_004",
            "patterns": [
                "alcohol conducción",
                "puedo beber y manejar",
                "límite de alcohol",
                "conducir embriagado"
            ],
            "answer": "NUNCA CONDUZCAS bajo la influencia del alcohol. El alcohol reduce: reflejos, visión periférica, "
                     "capacidad de concentración y juicio. Incluso pequeñas cantidades afectan. El límite legal es 0.05% de BAC "
                     "(25 mg de alcohol en 100ml de sangre), pero lo seguro es CERO alcohol si vas a conducir. El alcohol es causa "
                     "de accidentes mortales. Si has bebido, llama un taxi, Uber, amigo o usa transporte público."
        },
        {
            "id": "d_005",
            "patterns": [
                "rabia al manejar",
                "agresión en la vía",
                "conductor agresivo",
                "cómo mantener calma",
                "control de emociones"
            ],
            "answer": "La RABIA AL MANEJAR (road rage) es peligrosa. Si otro conductor te irrita: 1) Respira profundo, "
                     "2) No devuelvas la agresión, 3) Cede el paso incluso si tienes razón, 4) No hagas contacto visual amenazante, "
                     "5) Evita gestos ofensivos, 6) Reporta comportamiento peligroso a la policía. Mantener la calma protege tu vida "
                     "y la de otros. Algunos minutos perdidos no valen un accidente o confrontación. La paciencia al manejar es signo "
                     "de inteligencia."
        }
    ],
    
    "seguridad_vial": [
        {
            "id": "sg_001",
            "patterns": [
                "cinturón de seguridad",
                "debo usar cinturón",
                "cinturón en viaje",
                "importancia cinturón seguridad"
            ],
            "answer": "El CINTURÓN DE SEGURIDAD es obligatorio para todos los ocupantes del vehículo. Usa siempre "
                     "el cinturón incluso en trayectos cortos. El cinturón reduce el riesgo de muerte en un 45% y lesiones graves "
                     "en un 50%. Los niños menores de 12 años deben usar asiento de seguridad o booster según su peso. No usar "
                     "cinturón es infracción y causa de multa. Tu vida depende literalmente de abrocharte el cinturón."
        },
        {
            "id": "sg_002",
            "patterns": [
                "bolsas de aire",
                "airbag funcionamiento",
                "protección vehículo",
                "sistemas de seguridad auto"
            ],
            "answer": "Las BOLSAS DE AIRE (airbags) son un sistema de protección complementario al cinturón. "
                     "Se despliegan en milisegundos durante una colisión frontal, lateral o trasera. Para que funcionen correctamente: "
                     "1) El cinturón DEBE estar abrochado, 2) Siéntate a distancia normal del volante (20-30cm), 3) Los niños "
                     "pequeños no deben ir en el asiento delantero. Los airbags sin cinturón pueden causar lesiones. El mantenimiento "
                     "de estos sistemas es importante."
        },
        {
            "id": "sg_003",
            "patterns": [
                "frenos defectuosos",
                "mantenimiento vehículo",
                "revisión de frenos",
                "cómo revisar frenos",
                "seguridad del vehículo"
            ],
            "answer": "Los FRENOS son el sistema más crítico de tu vehículo. Revisa regularmente el estado de pastillas, "
                     "discos y líquido de frenos. Los síntomas de frenos defectuosos incluyen: pedal muy suave, ruidos de fricción, "
                     "vibración al frenar, o que el vehículo tire de un lado. Si notu síntomas, DETENTE en lugar seguro y no sigas "
                     "conduciendo hasta reparar. Un mantenimiento regular (alineación, rotación de llantas, balanceo) prolonga la vida "
                     "de tus frenos."
        },
        {
            "id": "sg_004",
            "patterns": [
                "llantas desgastadas",
                "profundidad banda",
                "cómo revisar llantas",
                "presión de aire llantas",
                "cambiar llanta"
            ],
            "answer": "Las LLANTAS desgastadas reducen tracción especialmente en lluvia. Revisa la profundidad de la banda: "
                     "usa la regla de la moneda (si la moneda se hunde, está bien; si no, cámbiala). La presión correcta mejora combustible "
                     "y tracción. Revisa la presión mensualmente. Rota las llantas cada 10,000-15,000 km. Si viajas con nieve o lluvia "
                     "frecuente, usa llantas de invierno. Llantas en mal estado causan accidentes, especialmente en curvas y lluvia."
        },
        {
            "id": "sg_005",
            "patterns": [
                "visibilidad reducida",
                "qué hacer de noche",
                "conducir en niebla",
                "lluvia fuerte conducción",
                "mala visibilidad"
            ],
            "answer": "En VISIBILIDAD REDUCIDA (niebla, lluvia, noche): 1) Enciende luces bajas, 2) Reduce velocidad, "
                     "3) Aumenta distancia de frenado, 4) Usa luces intermitentes si hay congestionamiento, 5) Limpiales parabrisas "
                     "frecuentemente, 6) Evita mirar directamente las luces de otros vehículos (mirar a la derecha del camino), "
                     "7) Abre más los ojos. En niebla espesa o lluvia muy fuerte, es mejor estacionarse y esperar. No arrisques la vida "
                     "por llegar a tiempo."
        },
        {
            "id": "sg_006",
            "patterns": [
                "accidente qué hacer",
                "protocolo después accidente",
                "debo llamar policía",
                "daños materiales accidente"
            ],
            "answer": "Si tienes un ACCIDENTE: 1) Asegúrate de que todos estén bien, 2) Llama ambulancia si hay lesionados, "
                     "3) Llama a la policía de tránsito (al 2255-0000 o 911), 4) Coloca triángulos de seguridad a 50m, 5) Obtén datos "
                     "del otro conductor (cédula, placa, teléfono, aseguradora), 6) Toma fotos de daños y escena, 7) No admitas culpa, "
                     "8) Reporta a tu aseguradora. Un reporte formal protege tus derechos. La seguridad de personas es lo primero."
        }
    ]
}
