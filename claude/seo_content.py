"""Original copy for the compound pages (/<compound>-costa-rica/) and the
category pages (/peptidos-.../). Used by build_product_pages.py.

Rules for this copy: research-use framing only, no dosing, no promises of
results. "Estudiado en..." rather than "sirve para...".
Keys of COMPOUNDS are the public product names used in the catalog.
"""

COMPOUNDS = {
    'Tirzepatide': {
        'slug': 'tirzepatide-costa-rica',
        'h1': 'Tirzepatide en Costa Rica',
        'lead': 'Agonista dual de los receptores GIP y GLP-1, uno de los péptidos metabólicos más estudiados de los últimos años.',
        'body': [
            'La tirzepatida es un péptido sintético de 39 aminoácidos que activa dos receptores de hormonas incretinas: el GIP (polipéptido insulinotrópico dependiente de glucosa) y el GLP-1 (péptido similar al glucagón tipo 1). Esta doble acción es lo que la distingue de los agonistas de GLP-1 de primera generación.',
            'Es el principio activo de Mounjaro y Zepbound. Su perfil se ha documentado en programas de ensayos clínicos amplios (SURPASS y SURMOUNT), centrados en el control de la glucosa y el peso corporal. Una cadena lateral de ácido graso le permite unirse a la albúmina, lo que prolonga su vida media.',
        ],
        'studied': ['Control de la glucosa en sangre', 'Peso corporal y composición corporal', 'Sensibilidad a la insulina', 'Marcadores de riesgo cardiometabólico'],
        'en': 'Tirzepatide is a 39-amino-acid dual GIP/GLP-1 receptor agonist, the active ingredient in Mounjaro and Zepbound, extensively studied for glucose control and body weight. Sold per vial in several strengths, for research use only.',
    },
    'GLP-1 (RT) – Agonista Triple': {
        'slug': 'glp-1-rt-costa-rica',
        'h1': 'GLP-1 (RT) – Agonista Triple en Costa Rica',
        'lead': 'Péptido de nueva generación que actúa sobre tres receptores a la vez: GLP-1, GIP y glucagón.',
        'body': [
            'Los agonistas triples son la línea más reciente de investigación en péptidos metabólicos. Además de los receptores de incretinas GLP-1 y GIP, este compuesto activa el receptor de glucagón, que participa en el gasto energético y el metabolismo de las grasas en el hígado.',
            'Se encuentra en fase avanzada de investigación clínica y todavía no está aprobado como medicamento. Por eso es un compuesto de interés para estudios comparativos frente a agonistas simples y duales.',
        ],
        'studied': ['Peso corporal', 'Grasa hepática', 'Gasto energético', 'Control de la glucosa'],
        'en': 'A next-generation triple agonist of the GLP-1, GIP and glucagon receptors, currently in late-stage clinical research and not yet approved as a medicine. Sold per vial in several strengths, for research use only.',
    },
    'Cagrilintide': {
        'slug': 'cagrilintide-costa-rica',
        'h1': 'Cagrilintide en Costa Rica',
        'lead': 'Análogo de amilina de acción prolongada, estudiado en el control del apetito.',
        'body': [
            'La amilina es una hormona que el páncreas libera junto con la insulina después de comer y que contribuye a la sensación de saciedad. La cagrilintida es una versión modificada de larga duración de esa hormona.',
            'Se ha investigado sola y, sobre todo, en combinación con agonistas de GLP-1, porque actúa por una vía distinta y complementaria. Esa combinación es uno de los temas más activos en la investigación metabólica actual.',
        ],
        'studied': ['Saciedad y apetito', 'Peso corporal', 'Combinación con agonistas de GLP-1'],
        'en': 'Cagrilintide is a long-acting amylin analogue studied for appetite and body weight, both alone and combined with GLP-1 agonists. For research use only.',
    },
    '5-AMINO-1MQ': {
        'slug': '5-amino-1mq-costa-rica',
        'h1': '5-Amino-1MQ en Costa Rica',
        'lead': 'Molécula pequeña que inhibe la enzima NNMT, estudiada en el metabolismo de las grasas.',
        'body': [
            'A diferencia de la mayoría de nuestro catálogo, el 5-Amino-1MQ no es un péptido sino una molécula pequeña. Bloquea la enzima nicotinamida N-metiltransferasa (NNMT), que se encuentra elevada en el tejido adiposo.',
            'Al inhibir la NNMT, aumentan los niveles celulares de NAD+ y SAM, dos moléculas clave del metabolismo energético. La investigación disponible es principalmente preclínica, en modelos celulares y animales.',
        ],
        'studied': ['Metabolismo del tejido adiposo', 'Niveles celulares de NAD+', 'Gasto energético en modelos preclínicos'],
        'en': '5-Amino-1MQ is a small-molecule NNMT inhibitor studied in preclinical models for fat-cell metabolism and cellular NAD+ levels. For research use only.',
    },
    'BPC-157': {
        'slug': 'bpc-157-costa-rica',
        'h1': 'BPC-157 en Costa Rica',
        'lead': 'Péptido de 15 aminoácidos derivado de una proteína del jugo gástrico, muy estudiado en regeneración de tejidos.',
        'body': [
            'BPC son las siglas de Body Protection Compound. El BPC-157 es una secuencia parcial y estable de una proteína presente en el jugo gástrico humano, lo que explica su resistencia en el entorno del estómago.',
            'La mayor parte de la investigación se ha hecho en modelos animales, con foco en la reparación de tendones, ligamentos y músculo, la protección de la mucosa intestinal y la formación de nuevos vasos sanguíneos (angiogénesis). Con frecuencia se estudia junto al TB-500.',
        ],
        'studied': ['Reparación de tendones y ligamentos', 'Salud de la mucosa intestinal', 'Angiogénesis', 'Recuperación muscular'],
        'en': 'BPC-157 is a stable 15-amino-acid fragment of a gastric protein, widely studied in animal models for tendon, ligament, muscle and gut-lining repair. Often studied alongside TB-500. For research use only.',
    },
    'TB-500': {
        'slug': 'tb-500-costa-rica',
        'h1': 'TB-500 en Costa Rica',
        'lead': 'Fragmento sintético de la Timosina Beta-4, estudiado en la migración celular y la reparación de tejidos.',
        'body': [
            'La Timosina Beta-4 es una proteína presente en casi todas las células, que regula la actina, el componente del citoesqueleto que permite a las células moverse. El TB-500 reproduce la región activa responsable de esa función.',
            'Por eso se estudia en procesos donde las células necesitan desplazarse hacia una zona dañada: cicatrización, reparación muscular y flexibilidad de tejidos. Es habitual investigarlo en combinación con BPC-157.',
        ],
        'studied': ['Migración celular', 'Cicatrización de heridas', 'Reparación muscular', 'Inflamación'],
        'en': 'TB-500 is a synthetic fragment of Thymosin Beta-4, studied for cell migration, wound healing and muscle repair, often alongside BPC-157. For research use only.',
    },
    'GHK-CU': {
        'slug': 'ghk-cu-costa-rica',
        'h1': 'GHK-Cu (péptido de cobre) en Costa Rica',
        'lead': 'Tripéptido unido a cobre, presente de forma natural en el cuerpo y estudiado en la piel y la cicatrización.',
        'body': [
            'El GHK (glicil-histidil-lisina) es un tripéptido que se encuentra en el plasma, la saliva y la orina, y cuyos niveles disminuyen con la edad. Tiene gran afinidad por el cobre, y el complejo resultante, GHK-Cu, es la forma más estudiada.',
            'La investigación se ha centrado en la síntesis de colágeno y elastina, la cicatrización y la remodelación de la piel. Es un ingrediente frecuente en cosmética, además de un compuesto de laboratorio.',
        ],
        'studied': ['Síntesis de colágeno', 'Cicatrización de heridas', 'Remodelación de la piel', 'Folículo piloso'],
        'en': 'GHK-Cu is a naturally occurring copper-binding tripeptide, studied for collagen synthesis, wound healing and skin remodelling. For research use only.',
    },
    'KPV': {
        'slug': 'kpv-costa-rica',
        'h1': 'KPV en Costa Rica',
        'lead': 'Tripéptido lisina-prolina-valina, el extremo final de la hormona alfa-MSH, estudiado por su efecto antiinflamatorio.',
        'body': [
            'La alfa-MSH es una hormona con conocidas propiedades antiinflamatorias. El KPV corresponde a sus tres últimos aminoácidos y conserva gran parte de esa actividad, sin los efectos sobre la pigmentación de la hormona completa.',
            'Se ha investigado sobre todo en modelos de inflamación intestinal y de la piel. También forma parte de la mezcla KLOW.',
        ],
        'studied': ['Inflamación intestinal', 'Inflamación de la piel', 'Barrera intestinal'],
        'en': 'KPV (Lys-Pro-Val) is the C-terminal fragment of alpha-MSH, studied for anti-inflammatory effects in gut and skin models. Also part of the KLOW blend. For research use only.',
    },
    'GLOW': {
        'slug': 'glow-costa-rica',
        'h1': 'GLOW (BPC-157 + GHK-Cu + TB-500) en Costa Rica',
        'lead': 'Mezcla de tres péptidos de recuperación en un solo vial de 70 mg.',
        'body': [
            'GLOW combina tres de los compuestos más estudiados en regeneración: BPC-157, GHK-Cu y TB-500. Cada uno actúa por una vía distinta, por lo que la mezcla permite estudiarlos juntos con un solo vial.',
            'Es una opción práctica para investigación en piel, cicatrización y recuperación. Consulta las páginas individuales de cada compuesto para más detalle.',
        ],
        'studied': ['Piel y colágeno', 'Cicatrización', 'Recuperación de tejidos'],
        'en': 'GLOW is a 70 mg blend of BPC-157, GHK-Cu and TB-500 in a single vial, for research on skin, healing and recovery. For research use only.',
    },
    'KLOW': {
        'slug': 'klow-costa-rica',
        'h1': 'KLOW (BPC-157 + GHK-Cu + TB-500 + KPV) en Costa Rica',
        'lead': 'La mezcla GLOW con KPV añadido, en un solo vial de 80 mg.',
        'body': [
            'KLOW parte de la combinación GLOW (BPC-157, GHK-Cu y TB-500) y añade KPV, un tripéptido estudiado por su efecto antiinflamatorio, especialmente en el intestino.',
            'Esto la hace de interés para investigación que combina regeneración de tejidos con inflamación intestinal o de la piel.',
        ],
        'studied': ['Salud intestinal', 'Piel y cicatrización', 'Inflamación', 'Recuperación de tejidos'],
        'en': 'KLOW is an 80 mg blend of BPC-157, GHK-Cu, TB-500 and KPV, for research combining tissue repair with gut and skin inflammation. For research use only.',
    },
    'Ipamorelin': {
        'slug': 'ipamorelin-costa-rica',
        'h1': 'Ipamorelin en Costa Rica',
        'lead': 'Secretagogo selectivo de hormona de crecimiento, conocido por su efecto limpio sobre otras hormonas.',
        'body': [
            'El ipamorelin es un pentapéptido que activa el receptor de grelina en la hipófisis y estimula la liberación de hormona de crecimiento (GH).',
            'Lo que lo distingue de secretagogos anteriores es su selectividad: en los estudios apenas afecta al cortisol, la prolactina o el apetito. Con frecuencia se investiga junto a un análogo de GHRH como el CJC-1295 sin DAC.',
        ],
        'studied': ['Liberación de hormona de crecimiento', 'Composición corporal', 'Recuperación'],
        'en': 'Ipamorelin is a selective growth-hormone secretagogue (ghrelin receptor agonist) with minimal effect on cortisol or appetite, often studied with CJC-1295 without DAC. For research use only.',
    },
    'CJC-1295 without DAC': {
        'slug': 'cjc-1295-costa-rica',
        'h1': 'CJC-1295 sin DAC en Costa Rica',
        'lead': 'Análogo de GHRH de acción corta, también llamado Mod GRF 1-29.',
        'body': [
            'El CJC-1295 sin DAC reproduce los primeros 29 aminoácidos de la hormona liberadora de hormona de crecimiento (GHRH), con cuatro sustituciones que lo hacen más estable.',
            'Sin el complejo DAC tiene una vida media corta, por lo que produce pulsos de GH parecidos a los naturales en lugar de una elevación continua. Se estudia a menudo en combinación con ipamorelin.',
        ],
        'studied': ['Pulsos de hormona de crecimiento', 'IGF-1', 'Combinación con ipamorelin'],
        'en': 'CJC-1295 without DAC (Mod GRF 1-29) is a short-acting GHRH analogue that produces natural-style GH pulses, often studied with ipamorelin. For research use only.',
    },
    'CJC-1295 without DAC + IPA': {
        'slug': 'cjc-1295-ipamorelin-costa-rica',
        'h1': 'CJC-1295 sin DAC + Ipamorelin en Costa Rica',
        'lead': 'Los dos péptidos de hormona de crecimiento que más se estudian juntos, en un solo vial (5 mg + 5 mg).',
        'body': [
            'Esta mezcla une un análogo de GHRH (CJC-1295 sin DAC) con un agonista del receptor de grelina (ipamorelin). Cada uno estimula la liberación de hormona de crecimiento por una vía distinta.',
            'Por eso es la combinación más habitual en la investigación de secretagogos. Tenerla en un solo vial simplifica la preparación. Consulta las páginas de cada compuesto para más detalle.',
        ],
        'studied': ['Pulsos de hormona de crecimiento', 'IGF-1', 'Composición corporal', 'Recuperación'],
        'en': 'A single-vial blend of CJC-1295 without DAC and ipamorelin (5 mg + 5 mg), the most commonly studied GHRH + ghrelin-agonist pairing. For research use only.',
    },
    'Tesamorelin': {
        'slug': 'tesamorelin-costa-rica',
        'h1': 'Tesamorelin en Costa Rica',
        'lead': 'Análogo de GHRH con aprobación médica en otros países, estudiado en la grasa visceral.',
        'body': [
            'La tesamorelina es un análogo estabilizado de la GHRH que estimula la producción propia de hormona de crecimiento.',
            'Está aprobada en Estados Unidos (Egrifta) para reducir la grasa abdominal en pacientes con lipodistrofia asociada al VIH. También se ha investigado en función cognitiva y en grasa hepática.',
        ],
        'studied': ['Grasa visceral', 'Grasa hepática', 'Función cognitiva', 'IGF-1'],
        'en': 'Tesamorelin is a stabilised GHRH analogue, approved in the US (Egrifta) for HIV-associated abdominal fat and studied for liver fat and cognition. For research use only.',
    },
    'MOTS-c': {
        'slug': 'mots-c-costa-rica',
        'h1': 'MOTS-c en Costa Rica',
        'lead': 'Péptido codificado en el ADN mitocondrial, estudiado en el metabolismo y el ejercicio.',
        'body': [
            'El MOTS-c es un péptido de 16 aminoácidos que se produce a partir del ADN de las mitocondrias, no del núcleo celular. Pertenece a una familia reciente de "péptidos derivados de la mitocondria".',
            'Actúa sobre la vía AMPK, un regulador central del uso de energía. En modelos animales se ha estudiado en la sensibilidad a la insulina, la capacidad de ejercicio y el envejecimiento metabólico.',
        ],
        'studied': ['Sensibilidad a la insulina', 'Rendimiento físico', 'Envejecimiento metabólico', 'Vía AMPK'],
        'en': 'MOTS-c is a 16-amino-acid mitochondria-derived peptide acting on the AMPK pathway, studied for insulin sensitivity, exercise capacity and metabolic ageing. For research use only.',
    },
    'NAD+': {
        'slug': 'nad-costa-rica',
        'h1': 'NAD+ en Costa Rica',
        'lead': 'Coenzima esencial para la producción de energía celular, cuyos niveles bajan con la edad.',
        'body': [
            'El NAD+ (nicotinamida adenina dinucleótido) participa en cientos de reacciones del metabolismo, en especial en la mitocondria. También es necesario para las sirtuinas y otras enzimas de reparación del ADN.',
            'Como sus niveles disminuyen con la edad, el NAD+ es uno de los compuestos centrales de la investigación en longevidad. No es un péptido, pero lo incluimos en el catálogo por su uso habitual junto a ellos.',
        ],
        'studied': ['Energía celular', 'Sirtuinas y reparación del ADN', 'Envejecimiento', 'Función mitocondrial'],
        'en': 'NAD+ is a coenzyme central to cellular energy, sirtuin activity and DNA repair whose levels decline with age, a core compound in longevity research. For research use only.',
    },
    'SS-31': {
        'slug': 'ss-31-costa-rica',
        'h1': 'SS-31 (elamipretida) en Costa Rica',
        'lead': 'Tetrapéptido que se dirige a la membrana interna de la mitocondria.',
        'body': [
            'El SS-31 se acumula en la membrana interna de la mitocondria, donde se une a la cardiolipina, un lípido clave para la cadena de producción de energía.',
            'Al estabilizar esa membrana, se ha estudiado en la eficiencia mitocondrial y la reducción del estrés oxidativo, incluyendo ensayos clínicos en enfermedades mitocondriales.',
        ],
        'studied': ['Función mitocondrial', 'Estrés oxidativo', 'Músculo y corazón', 'Envejecimiento celular'],
        'en': 'SS-31 (elamipretide) is a mitochondria-targeted tetrapeptide that binds cardiolipin, studied for mitochondrial efficiency and oxidative stress. For research use only.',
    },
    'PT-141': {
        'slug': 'pt-141-costa-rica',
        'h1': 'PT-141 (bremelanotida) en Costa Rica',
        'lead': 'Agonista de los receptores de melanocortina, estudiado en el deseo sexual.',
        'body': [
            'La bremelanotida actúa sobre los receptores de melanocortina del sistema nervioso central, en lugar de sobre el sistema vascular como otros compuestos de esta área.',
            'Está aprobada en Estados Unidos (Vyleesi) para el trastorno del deseo sexual hipoactivo en mujeres premenopáusicas, y se ha investigado también en hombres.',
        ],
        'studied': ['Deseo y excitación sexual', 'Receptores de melanocortina'],
        'en': 'PT-141 (bremelanotide) is a melanocortin receptor agonist acting on the central nervous system, approved in the US (Vyleesi) and studied for sexual desire. For research use only.',
    },
}

CATEGORIES = {
    'Weight Loss & Metabolic': {
        'slug': 'peptidos-perdida-de-peso',
        'h1': 'Péptidos para pérdida de peso y metabolismo',
        'title': 'Péptidos para pérdida de peso en Costa Rica',
        'body': [
            'Esta categoría reúne los compuestos de investigación metabólica más estudiados: agonistas de los receptores de incretinas (GLP-1 y GIP), un agonista triple que añade el receptor de glucagón, un análogo de amilina y un inhibidor de la enzima NNMT.',
            'Cada uno actúa por una vía diferente, desde la saciedad y el vaciado gástrico hasta el gasto energético y el metabolismo de las células grasas. Por eso es común estudiarlos de forma comparativa o en combinación.',
        ],
        'en': 'Metabolic research compounds: incretin receptor agonists (GLP-1/GIP), a triple agonist, an amylin analogue and an NNMT inhibitor.',
    },
    'Healing & Recovery': {
        'slug': 'peptidos-recuperacion',
        'h1': 'Péptidos para recuperación y regeneración',
        'title': 'Péptidos de recuperación y regeneración en Costa Rica',
        'body': [
            'Aquí están los péptidos más estudiados en reparación de tejidos: BPC-157, TB-500, el péptido de cobre GHK-Cu y el tripéptido antiinflamatorio KPV, además de las mezclas GLOW y KLOW que los combinan en un solo vial.',
            'La investigación con estos compuestos abarca tendones, ligamentos, músculo, piel e intestino.',
        ],
        'en': 'Tissue-repair research peptides: BPC-157, TB-500, GHK-Cu, KPV and the GLOW and KLOW blends.',
    },
    'Growth Hormone & Muscle': {
        'slug': 'peptidos-hormona-de-crecimiento',
        'h1': 'Péptidos de hormona de crecimiento',
        'title': 'Péptidos de hormona de crecimiento en Costa Rica',
        'body': [
            'Estos compuestos estimulan la producción propia de hormona de crecimiento por dos vías: los análogos de GHRH (CJC-1295 sin DAC y tesamorelina) y los agonistas del receptor de grelina (ipamorelin).',
            'Como actúan sobre receptores distintos, es habitual estudiar un compuesto de cada tipo en conjunto.',
        ],
        'en': 'Growth-hormone research peptides: GHRH analogues (CJC-1295 without DAC, tesamorelin) and the ghrelin receptor agonist ipamorelin.',
    },
    'Longevity & Cellular Health': {
        'slug': 'peptidos-longevidad',
        'h1': 'Péptidos de longevidad y salud celular',
        'title': 'Péptidos de longevidad y salud celular en Costa Rica',
        'body': [
            'Compuestos centrados en la mitocondria y la energía celular: MOTS-c, un péptido codificado en el propio ADN mitocondrial; SS-31, que estabiliza la membrana interna de la mitocondria; y NAD+, la coenzima que alimenta el metabolismo energético.',
            'Son la base de buena parte de la investigación actual sobre envejecimiento.',
        ],
        'en': 'Mitochondria and cellular-energy compounds for longevity research: MOTS-c, SS-31 and NAD+.',
    },
    'Sexual Health & Hormones': {
        'slug': 'peptidos-salud-sexual',
        'h1': 'Péptidos de salud sexual',
        'title': 'Péptidos de salud sexual en Costa Rica',
        'body': [
            'Compuestos que actúan sobre los receptores de melanocortina del sistema nervioso central, estudiados en el deseo y la excitación sexual.',
        ],
        'en': 'Melanocortin receptor compounds studied for sexual desire and arousal.',
    },
}

# Shared FAQ shown on every compound page.
FAQ = [
    ('¿Cómo se vende?', 'Por vial individual. Cada pedido de péptidos incluye un vial de agua bacteriostática gratis por cada vial.'),
    ('¿Cómo se conserva?', 'El polvo liofilizado se guarda en refrigeración (2–8 °C), protegido de la luz. Una vez reconstituido debe mantenerse refrigerado.'),
    ('¿Tienen Certificado de Análisis (COA)?', 'Sí, puedes solicitar el COA del lote por WhatsApp antes de comprar.'),
    ('¿Cómo hago un pedido?', 'Agrega los productos al carrito en la tienda y confirma por WhatsApp, o escríbenos directamente. Coordinamos el pago y la entrega en Costa Rica.'),
    ('¿Es apto para consumo humano?', 'No. Todos nuestros productos son exclusivamente para fines de investigación en laboratorio.'),
]

# ---------------------------------------------------------------------------
# Extra depth for compound pages: technical specs, background, what the
# research does and does not show, and compound-specific questions.
# Specs are only listed where well established; blends list their parts.
# ---------------------------------------------------------------------------
EXTRA = {
    'Tirzepatide': {
        'specs': [('Tipo', 'Péptido sintético de 39 aminoácidos con cadena lateral de ácido graso C20'), ('Fórmula molecular', 'C225H348N48O68'), ('Peso molecular', '4813,5 g/mol'), ('CAS', '2023788-19-2'), ('Mecanismo', 'Agonista de los receptores GIP y GLP-1')],
        'history': 'Fue desarrollada como un único péptido capaz de activar dos receptores de incretinas. Su secuencia se basa en la del GIP natural, modificada para activar también el receptor de GLP-1, e incluye dos residuos de ácido aminoisobutírico (Aib) que la protegen de la degradación enzimática.',
        'limits': 'La mayor parte de los datos proviene de ensayos clínicos con el medicamento fabricado bajo normas farmacéuticas. Esos resultados no se trasladan automáticamente a material de investigación, y en el laboratorio la pureza, la identidad y la estabilidad deben verificarse lote por lote.',
        'faq': [('¿En qué se diferencia de un agonista de GLP-1 simple?', 'Activa además el receptor de GIP. Los estudios comparan ambos enfoques para entender qué aporta la acción dual sobre la glucosa y el peso.'),
                ('¿Por qué hay varias concentraciones?', 'Los estudios trabajan con diferentes cantidades; ofrecer varios tamaños de vial permite elegir el que corresponde a cada protocolo de investigación.')],
    },
    'GLP-1 (RT) – Agonista Triple': {
        'specs': [('Tipo', 'Péptido sintético con cadena lateral de ácido graso'), ('Mecanismo', 'Agonista de los receptores GLP-1, GIP y glucagón'), ('Estado', 'En investigación clínica; no aprobado como medicamento')],
        'history': 'Los agonistas triples surgieron de la idea de sumar al efecto de las incretinas la acción del glucagón sobre el gasto energético y el hígado. Es el siguiente paso después de los agonistas simples (GLP-1) y duales (GLP-1/GIP).',
        'limits': 'Al tratarse de un compuesto todavía en investigación, los datos publicados son más limitados que los de agonistas ya aprobados y siguen en evolución.',
        'faq': [('¿Qué significa "agonista triple"?', 'Que activa tres receptores hormonales distintos: GLP-1, GIP y glucagón.'),
                ('¿Está aprobado como medicamento?', 'No. Se encuentra en fase avanzada de investigación clínica.')],
    },
    'Cagrilintide': {
        'specs': [('Tipo', 'Análogo de amilina acilado, de acción prolongada'), ('Peso molecular', '≈ 4409 g/mol'), ('CAS', '1415456-99-3'), ('Mecanismo', 'Agonista de los receptores de amilina y calcitonina')],
        'history': 'La amilina natural tiene una vida media muy corta y tiende a agregarse. La cagrilintida se diseñó con modificaciones y una cadena de ácido graso para hacerla estable y de larga duración.',
        'limits': 'Gran parte de la investigación más reciente la estudia en combinación con un agonista de GLP-1, por lo que los datos del compuesto solo son menos abundantes.',
        'faq': [('¿Qué es la amilina?', 'Una hormona que el páncreas libera junto con la insulina y que participa en la saciedad y el vaciado gástrico.'),
                ('¿Por qué se combina con GLP-1?', 'Porque actúa por una vía hormonal distinta, lo que permite estudiar efectos complementarios.')],
    },
    '5-AMINO-1MQ': {
        'specs': [('Tipo', 'Molécula pequeña (derivado de quinolinio), no es un péptido'), ('Nombre químico', '5-amino-1-metilquinolinio'), ('Peso molecular (catión)', '≈ 159,2 g/mol'), ('Mecanismo', 'Inhibidor de la enzima NNMT')],
        'history': 'La NNMT ganó interés cuando se observó que está elevada en el tejido graso. El 5-Amino-1MQ fue uno de los inhibidores selectivos diseñados para estudiar qué ocurre al bloquearla.',
        'limits': 'La evidencia es casi totalmente preclínica, en células y modelos animales. No hay ensayos clínicos amplios publicados.',
        'faq': [('¿Por qué está en un catálogo de péptidos?', 'Porque se investiga en el mismo campo metabólico y suele estudiarse junto a ellos, aunque químicamente es una molécula pequeña.'),
                ('¿Qué es la NNMT?', 'La nicotinamida N-metiltransferasa, una enzima que consume precursores del NAD+ y del grupo metilo celular.')],
    },
    'BPC-157': {
        'specs': [('Tipo', 'Pentadecapéptido (15 aminoácidos)'), ('Secuencia', 'Gly-Glu-Pro-Pro-Pro-Gly-Lys-Pro-Ala-Asp-Asp-Ala-Gly-Leu-Val'), ('Fórmula molecular', 'C62H98N16O22'), ('Peso molecular', '≈ 1419,5 g/mol'), ('CAS', '137525-51-0')],
        'history': 'Fue descrito en los años noventa por investigadores croatas como un fragmento estable de una proteína del jugo gástrico. Desde entonces se han publicado numerosos estudios en modelos animales.',
        'limits': 'Casi toda la evidencia proviene de estudios en animales, muchos de ellos de un mismo grupo de investigación. Los datos en humanos son escasos, por lo que los resultados deben interpretarse con cautela.',
        'faq': [('¿Por qué se estudia junto a TB-500?', 'Porque actúan por mecanismos distintos dentro de la reparación de tejidos, y se investiga si sus efectos se complementan.'),
                ('¿Qué significa "BPC"?', 'Body Protection Compound, "compuesto de protección corporal", por la proteína gástrica de la que se deriva.')],
    },
    'TB-500': {
        'specs': [('Tipo', 'Péptido sintético basado en la Timosina Beta-4'), ('Proteína de origen', 'Timosina Beta-4 (43 aminoácidos)'), ('Región activa', 'Dominio de unión a actina (secuencia LKKTETQ)'), ('Mecanismo', 'Regulación de la actina y migración celular')],
        'history': 'La Timosina Beta-4 se aisló originalmente del timo. Al identificarse la región responsable de unirse a la actina, se desarrollaron versiones sintéticas para estudiar específicamente esa función.',
        'limits': 'La investigación es principalmente preclínica. Además, el nombre "TB-500" se usa en el mercado para distintas versiones de la molécula, por lo que conviene revisar el COA de cada lote.',
        'faq': [('¿Es lo mismo que la Timosina Beta-4?', 'Está basado en ella y reproduce su región activa, pero es una versión sintética.'),
                ('¿Qué es la actina?', 'Una proteína del citoesqueleto que permite a las células cambiar de forma y desplazarse.')],
    },
    'GHK-CU': {
        'specs': [('Tipo', 'Tripéptido unido a cobre (II)'), ('Secuencia', 'Gly-His-Lys'), ('Fórmula (GHK)', 'C14H24N6O4'), ('Peso molecular (GHK)', '≈ 340,4 g/mol'), ('Forma', 'Complejo GHK-Cu, polvo de color azul')],
        'history': 'El GHK fue identificado en los años setenta en plasma humano. Su capacidad para unirse al cobre y su relación con la cicatrización lo convirtieron en uno de los péptidos más estudiados en dermatología.',
        'limits': 'Buena parte de la investigación es in vitro o en modelos de piel y cosmética. Los estudios clínicos controlados son más limitados.',
        'faq': [('¿Por qué es de color azul?', 'Por el cobre unido al péptido; es una característica normal del complejo GHK-Cu.'),
                ('¿Se usa en cosmética?', 'Sí, es un ingrediente común en productos para la piel. Nuestro producto es material de investigación, no un cosmético.')],
    },
    'KPV': {
        'specs': [('Tipo', 'Tripéptido'), ('Secuencia', 'Lys-Pro-Val'), ('Fórmula molecular', 'C16H30N4O4'), ('Peso molecular', '≈ 342,4 g/mol'), ('Origen', 'Fragmento C-terminal de la alfa-MSH')],
        'history': 'Al estudiar las propiedades antiinflamatorias de la alfa-MSH, los investigadores observaron que sus últimos tres aminoácidos conservaban gran parte de esa actividad.',
        'limits': 'La evidencia proviene sobre todo de modelos celulares y animales de inflamación.',
        'faq': [('¿Afecta la pigmentación como la alfa-MSH?', 'Los estudios indican que, al ser solo un fragmento, no tiene los efectos sobre la pigmentación de la hormona completa.'),
                ('¿Dónde más lo encuentro?', 'Es uno de los cuatro componentes de la mezcla KLOW.')],
    },
    'GLOW': {
        'specs': [('Tipo', 'Mezcla de péptidos en un solo vial'), ('Componentes', 'BPC-157 + GHK-Cu + TB-500'), ('Contenido total', '70 mg por vial')],
        'history': 'Las mezclas surgieron porque estos tres péptidos se estudian con frecuencia juntos. Combinarlos en un vial reduce la manipulación y los pasos de preparación.',
        'limits': 'Al ser una mezcla, la investigación publicada se refiere principalmente a cada componente por separado.',
        'faq': [('¿En qué se diferencia de KLOW?', 'KLOW añade un cuarto péptido, KPV, y tiene 80 mg en total.'),
                ('¿Puedo pedir el COA?', 'Sí, solicítalo por WhatsApp con el producto que te interesa.')],
    },
    'KLOW': {
        'specs': [('Tipo', 'Mezcla de péptidos en un solo vial'), ('Componentes', 'BPC-157 + GHK-Cu + TB-500 + KPV'), ('Contenido total', '80 mg por vial')],
        'history': 'KLOW extiende la mezcla GLOW con KPV, para investigación que combina la reparación de tejidos con el componente inflamatorio.',
        'limits': 'Al ser una mezcla, la investigación publicada se refiere principalmente a cada componente por separado.',
        'faq': [('¿En qué se diferencia de GLOW?', 'Incluye KPV además de BPC-157, GHK-Cu y TB-500.'),
                ('¿Puedo pedir el COA?', 'Sí, solicítalo por WhatsApp con el producto que te interesa.')],
    },
    'Ipamorelin': {
        'specs': [('Tipo', 'Pentapéptido sintético'), ('Secuencia', 'Aib-His-D-2Nal-D-Phe-Lys-NH2'), ('Fórmula molecular', 'C38H49N9O5'), ('Peso molecular', '≈ 711,9 g/mol'), ('CAS', '170851-70-4')],
        'history': 'Se desarrolló en los años noventa como parte de la familia de péptidos liberadores de hormona de crecimiento (GHRP), buscando mayor selectividad que sus predecesores.',
        'limits': 'Los estudios clínicos publicados son limitados; la mayor parte de los datos sobre su selectividad proviene de modelos animales y estudios iniciales.',
        'faq': [('¿Qué es un GHRP?', 'Un péptido liberador de hormona de crecimiento que actúa sobre el receptor de grelina.'),
                ('¿Por qué se combina con CJC-1295?', 'Porque estimulan la liberación de GH por vías distintas; también lo ofrecemos ya mezclado en un vial.')],
    },
    'CJC-1295 without DAC': {
        'specs': [('Tipo', 'Análogo de GHRH de 29 aminoácidos (Mod GRF 1-29)'), ('Fórmula molecular', 'C152H252N44O42'), ('Peso molecular', '≈ 3367,9 g/mol'), ('Modificaciones', 'Cuatro sustituciones de aminoácidos para mayor estabilidad'), ('Vida media', 'Corta (sin DAC)')],
        'history': 'Los primeros 29 aminoácidos de la GHRH contienen toda su actividad. A partir de ese fragmento se diseñaron versiones más estables; la variante "con DAC" añade un complejo que la une a la albúmina, mientras que esta versión no lo lleva.',
        'limits': 'La nomenclatura en el mercado puede ser confusa entre las versiones con y sin DAC; el COA del lote confirma cuál es.',
        'faq': [('¿Qué diferencia hay entre "con DAC" y "sin DAC"?', 'La versión con DAC dura mucho más en circulación; la versión sin DAC produce pulsos cortos, más parecidos a los naturales.'),
                ('¿Es lo mismo que Mod GRF 1-29?', 'Sí, son dos nombres para el mismo compuesto.')],
    },
    'CJC-1295 without DAC + IPA': {
        'specs': [('Tipo', 'Mezcla de dos péptidos en un solo vial'), ('Componentes', 'CJC-1295 sin DAC 5 mg + Ipamorelin 5 mg'), ('Contenido total', '10 mg por vial')],
        'history': 'La combinación de un análogo de GHRH con un GHRP es la pareja más estudiada entre los secretagogos de hormona de crecimiento; la mezcla simplifica su preparación.',
        'limits': 'La investigación publicada se refiere principalmente a cada componente por separado.',
        'faq': [('¿Puedo comprar cada péptido por separado?', 'Sí, también tenemos CJC-1295 sin DAC e Ipamorelin en viales individuales.'),
                ('¿Puedo pedir el COA?', 'Sí, solicítalo por WhatsApp con el producto que te interesa.')],
    },
    'Tesamorelin': {
        'specs': [('Tipo', 'Análogo de GHRH de 44 aminoácidos con grupo hexenoilo'), ('Fórmula molecular', 'C221H366N72O67S'), ('Peso molecular', '≈ 5135,9 g/mol'), ('CAS', '218949-48-5'), ('Aprobación', 'Egrifta (EE. UU.)')],
        'history': 'Es la secuencia completa de la GHRH humana con un grupo químico añadido en el extremo, que la protege de la degradación y prolonga su acción.',
        'limits': 'Su aprobación médica se limita a una indicación concreta; otros usos estudiados siguen en investigación.',
        'faq': [('¿En qué se diferencia de CJC-1295?', 'La tesamorelina contiene los 44 aminoácidos de la GHRH; el CJC-1295 sin DAC solo los primeros 29, modificados.'),
                ('¿Está aprobada como medicamento?', 'Sí, en Estados Unidos para una indicación específica. Nuestro producto es material de investigación.')],
    },
    'MOTS-c': {
        'specs': [('Tipo', 'Péptido de 16 aminoácidos derivado de la mitocondria'), ('Secuencia', 'MRWQEMGYIFYPRKLR'), ('Fórmula molecular', 'C101H152N28O22S2'), ('Peso molecular', '≈ 2174,6 g/mol'), ('CAS', '1627580-64-6')],
        'history': 'Se describió en 2015, al descubrirse que el gen del ARN ribosómico 12S de la mitocondria también codifica pequeños péptidos con actividad biológica.',
        'limits': 'Es un campo reciente: la mayoría de los estudios son en animales y los datos en humanos son todavía iniciales.',
        'faq': [('¿Qué tiene de especial su origen?', 'Casi todas las proteínas se codifican en el núcleo celular; el MOTS-c se codifica en el ADN de la mitocondria.'),
                ('¿Qué es la vía AMPK?', 'Un sensor de energía celular que regula el uso de glucosa y grasas.')],
    },
    'NAD+': {
        'specs': [('Tipo', 'Coenzima (dinucleótido), no es un péptido'), ('Fórmula molecular', 'C21H27N7O14P2'), ('Peso molecular', '≈ 663,4 g/mol'), ('CAS', '53-84-9')],
        'history': 'El NAD+ se conoce desde principios del siglo XX. El interés reciente proviene de los estudios que relacionan su descenso con la edad y con la actividad de las sirtuinas.',
        'limits': 'Muchos estudios usan precursores (como NMN o NR) en lugar del propio NAD+, y los resultados en humanos son todavía mixtos.',
        'faq': [('¿Es un péptido?', 'No, es una coenzima, pero se investiga en el mismo campo de la longevidad.'),
                ('¿Qué tamaños hay?', 'Lo ofrecemos en viales de 500 mg y 1000 mg, según disponibilidad.')],
    },
    'SS-31': {
        'specs': [('Tipo', 'Tetrapéptido sintético'), ('Secuencia', 'D-Arg-Dmt-Lys-Phe-NH2'), ('Fórmula molecular', 'C32H49N9O5'), ('Peso molecular', '≈ 639,8 g/mol'), ('CAS', '736992-21-5')],
        'history': 'Pertenece a los péptidos Szeto-Schiller, diseñados para atravesar membranas celulares y concentrarse en la mitocondria.',
        'limits': 'Los resultados de los ensayos clínicos han sido variables según la enfermedad estudiada; la investigación continúa.',
        'faq': [('¿Qué es la cardiolipina?', 'Un lípido de la membrana interna de la mitocondria, esencial para la cadena respiratoria.'),
                ('¿Qué significa "Dmt"?', 'Dimetiltirosina, un aminoácido modificado que forma parte de su secuencia.')],
    },
    'PT-141': {
        'specs': [('Tipo', 'Heptapéptido cíclico'), ('Fórmula molecular', 'C50H68N14O10'), ('Peso molecular', '≈ 1025,2 g/mol'), ('CAS', '189691-06-3'), ('Origen', 'Derivado del Melanotan II')],
        'history': 'Se descubrió durante la investigación del Melanotan II, al observarse efectos sobre la excitación sexual, y se desarrolló como compuesto independiente.',
        'limits': 'Su aprobación médica se limita a una indicación concreta; los estudios en otros grupos siguen en investigación.',
        'faq': [('¿En qué se diferencia de otros compuestos del área?', 'Actúa sobre el sistema nervioso central (receptores de melanocortina), no sobre el flujo sanguíneo.'),
                ('¿Está aprobado como medicamento?', 'Sí, en Estados Unidos para una indicación específica. Nuestro producto es material de investigación.')],
    },
}

HANDLING = [
    'Se entrega como polvo liofilizado (secado por congelación) en vial sellado, la forma más estable para su almacenamiento.',
    'Antes de reconstituir, consérvalo refrigerado (2–8 °C) y protegido de la luz. Para periodos largos, muchos laboratorios lo guardan congelado.',
    'Para reconstituir se suele usar agua bacteriostática, que incluimos gratis con cada vial. Una vez reconstituido, mantenlo refrigerado y evita congelarlo y descongelarlo varias veces.',
    'Cada lote cuenta con Certificado de Análisis (COA), que puedes solicitar por WhatsApp.',
]

# How it works (mechanism, plain language) and what kinds of studies exist.
MORE = {
    'Tirzepatide': {
        'how': 'Las incretinas son hormonas que el intestino libera al comer. El GLP-1 estimula la insulina, frena el vaciado del estómago y actúa sobre los centros del apetito en el cerebro; el GIP también estimula la insulina y participa en el manejo de las grasas. La tirzepatida imita a ambas a la vez y, gracias a su unión a la albúmina, permanece activa durante días en lugar de minutos.',
        'research': [('Ensayos de control glucémico', 'programas que compararon la tirzepatida con otros tratamientos para la diabetes tipo 2.'), ('Ensayos de peso corporal', 'estudios en personas con obesidad, sin y con diabetes.'), ('Estudios de mecanismo', 'trabajos que buscan separar la contribución del GIP y del GLP-1 a los efectos observados.')],
    },
    'GLP-1 (RT) – Agonista Triple': {
        'how': 'Al efecto de las incretinas (más insulina, menos apetito, vaciado gástrico más lento) suma la activación del receptor de glucagón. El glucagón eleva el gasto energético y favorece el uso de las grasas en el hígado, de modo que el compuesto actúa tanto sobre la ingesta como sobre el gasto de energía.',
        'research': [('Estudios de fase 2', 'ensayos de búsqueda de dosis que midieron el peso corporal y marcadores metabólicos.'), ('Estudios de grasa hepática', 'trabajos centrados en el hígado graso.'), ('Ensayos de fase 3', 'programas clínicos amplios actualmente en curso.')],
    },
    'Cagrilintide': {
        'how': 'La amilina actúa en el tronco cerebral para aumentar la saciedad, enlentece el vaciado del estómago y reduce la liberación de glucagón después de comer. La cagrilintida activa los mismos receptores durante mucho más tiempo que la hormona natural, lo que permite estudiar esos efectos de forma sostenida.',
        'research': [('Estudios en monoterapia', 'ensayos de fase 2 sobre peso corporal con cagrilintida sola.'), ('Estudios de combinación', 'investigación con un agonista de GLP-1 en el mismo esquema.'), ('Estudios de apetito', 'trabajos sobre saciedad e ingesta de alimentos.')],
    },
    '5-AMINO-1MQ': {
        'how': 'La NNMT toma nicotinamida (precursora del NAD+) y le añade un grupo metilo procedente del SAM. Cuando está muy activa, consume ambos recursos. Al bloquearla, el 5-Amino-1MQ deja más nicotinamida disponible para fabricar NAD+ y conserva SAM, lo que en modelos preclínicos se asocia a un metabolismo energético más activo en las células grasas.',
        'research': [('Estudios en células grasas', 'cultivos de adipocitos donde se midió el tamaño celular y la acumulación de lípidos.'), ('Modelos animales', 'ratones con obesidad inducida por dieta.'), ('Estudios de selectividad', 'trabajos que comparan su efecto sobre la NNMT frente a otras enzimas.')],
    },
    'BPC-157': {
        'how': 'Los mecanismos propuestos incluyen la estimulación de la formación de vasos sanguíneos (vía VEGF), la interacción con el sistema del óxido nítrico y la activación de receptores de factores de crecimiento en los fibroblastos, las células que reparan tendones y ligamentos. Su estabilidad en el jugo gástrico lo distingue de la mayoría de los péptidos.',
        'research': [('Modelos de tendón y ligamento', 'estudios sobre la reparación tras lesiones inducidas en animales.'), ('Modelos intestinales', 'trabajos sobre úlceras, fístulas y lesiones de la mucosa.'), ('Estudios de angiogénesis', 'investigación sobre la formación de nuevos vasos.')],
    },
    'TB-500': {
        'how': 'La Timosina Beta-4 se une a la actina libre dentro de la célula y regula cuánta está disponible para formar filamentos. Ese control es necesario para que las células se desplacen hacia una herida, se dividan y formen nuevos vasos sanguíneos. El TB-500 se centra en la región de la proteína responsable de esa unión.',
        'research': [('Modelos de cicatrización', 'estudios de heridas en piel y córnea.'), ('Modelos musculares', 'trabajos sobre la regeneración de fibras musculares.'), ('Estudios cardíacos', 'investigación sobre la reparación del tejido cardíaco en animales.')],
    },
    'GHK-CU': {
        'how': 'El GHK transporta cobre, un elemento necesario para varias enzimas que construyen y remodelan el tejido, como la lisil oxidasa que entrecruza el colágeno. Además, los estudios de expresión génica sugieren que el GHK modula la actividad de cientos de genes relacionados con la reparación y la respuesta al daño.',
        'research': [('Estudios en fibroblastos', 'producción de colágeno, elastina y glicosaminoglicanos.'), ('Modelos de heridas', 'cicatrización en animales.'), ('Estudios cosméticos', 'ensayos sobre la apariencia de la piel con formulaciones tópicas.')],
    },
    'KPV': {
        'how': 'El KPV reduce la activación del NF-κB, un interruptor central de la respuesta inflamatoria. Además, puede entrar en las células del intestino a través del transportador PepT1, que está aumentado cuando el intestino está inflamado, lo que lo hace de especial interés en ese tejido.',
        'research': [('Modelos de colitis', 'estudios en animales con inflamación intestinal inducida.'), ('Estudios celulares', 'trabajos sobre la producción de citocinas inflamatorias.'), ('Sistemas de liberación', 'investigación con nanopartículas para dirigirlo al colon.')],
    },
    'GLOW': {
        'how': 'Cada componente aporta un mecanismo distinto: el BPC-157 se asocia a la formación de vasos y la reparación de tejido conectivo, el TB-500 a la migración celular, y el GHK-Cu a la síntesis de colágeno y la remodelación de la piel. La mezcla permite estudiar esos procesos en conjunto.',
        'research': [('BPC-157', 'reparación de tendones, ligamentos e intestino en modelos animales.'), ('TB-500', 'migración celular y cicatrización.'), ('GHK-Cu', 'colágeno, elastina y remodelación de la piel.')],
    },
    'KLOW': {
        'how': 'A los tres mecanismos de GLOW (vasos y tejido conectivo, migración celular, colágeno) se suma el KPV, que reduce la señal inflamatoria del NF-κB y llega con facilidad a las células del intestino. El resultado es una mezcla orientada a la reparación con un componente antiinflamatorio.',
        'research': [('BPC-157 y TB-500', 'reparación de tejidos en modelos animales.'), ('GHK-Cu', 'colágeno y remodelación de la piel.'), ('KPV', 'inflamación intestinal y de la piel.')],
    },
    'Ipamorelin': {
        'how': 'La hormona de crecimiento se libera por pulsos, controlados por la GHRH (que la estimula), la somatostatina (que la frena) y la grelina. El ipamorelin activa el receptor de grelina en la hipófisis y produce un pulso de GH. A diferencia de GHRP más antiguos, apenas eleva el cortisol o la prolactina.',
        'research': [('Estudios de selectividad', 'comparaciones con GHRP-2 y GHRP-6 sobre otras hormonas.'), ('Estudios gastrointestinales', 'investigación sobre la motilidad intestinal tras cirugía.'), ('Estudios de combinación', 'trabajos junto a análogos de GHRH.')],
    },
    'CJC-1295 without DAC': {
        'how': 'Activa el receptor de GHRH en la hipófisis, la señal natural que indica cuándo liberar hormona de crecimiento. Las cuatro sustituciones de aminoácidos lo protegen de la enzima que degrada la GHRH natural en minutos, pero sin el complejo DAC su acción sigue siendo breve, lo que respeta el patrón por pulsos.',
        'research': [('Estudios de pulsatilidad', 'trabajos sobre el patrón natural de liberación de GH.'), ('Estudios de IGF-1', 'mediciones del factor de crecimiento hepático que sigue a la GH.'), ('Estudios de combinación', 'investigación junto a GHRP como el ipamorelin.')],
    },
    'CJC-1295 without DAC + IPA': {
        'how': 'El CJC-1295 sin DAC "abre la puerta" activando el receptor de GHRH, y el ipamorelin amplifica el pulso a través del receptor de grelina y reduciendo el freno de la somatostatina. Por eso la combinación se estudia como una forma de producir pulsos de GH mayores que con cada compuesto por separado.',
        'research': [('CJC-1295 sin DAC', 'pulsos de GH e IGF-1.'), ('Ipamorelin', 'liberación selectiva de GH.'), ('Combinación GHRH + GHRP', 'estudios sobre el efecto sinérgico de ambas vías.')],
    },
    'Tesamorelin': {
        'how': 'Activa el receptor de GHRH y aumenta la producción propia de hormona de crecimiento e IGF-1, manteniendo el control natural del cuerpo sobre esos niveles. La GH favorece el uso de la grasa como fuente de energía, con un efecto especialmente estudiado sobre la grasa visceral, la que rodea los órganos abdominales.',
        'research': [('Ensayos de grasa visceral', 'los estudios que llevaron a su aprobación.'), ('Estudios de hígado graso', 'investigación sobre grasa hepática.'), ('Estudios cognitivos', 'trabajos en adultos mayores y deterioro cognitivo leve.')],
    },
    'MOTS-c': {
        'how': 'En situaciones de estrés metabólico, el MOTS-c se desplaza al núcleo de la célula y ajusta la expresión de genes relacionados con el uso de energía. También activa la AMPK, que favorece la captación de glucosa por el músculo. Sus niveles en sangre aumentan con el ejercicio y disminuyen con la edad.',
        'research': [('Modelos de dieta alta en grasa', 'estudios sobre resistencia a la insulina en ratones.'), ('Estudios de ejercicio', 'capacidad física en animales jóvenes y mayores.'), ('Estudios en humanos', 'mediciones de sus niveles circulantes en distintas poblaciones.')],
    },
    'NAD+': {
        'how': 'El NAD+ transporta electrones en las reacciones que convierten los nutrientes en energía (ATP) dentro de la mitocondria. Además, es el combustible de las sirtuinas y de las enzimas PARP, que participan en la reparación del ADN; cuando escasea, esos procesos se ven limitados.',
        'research': [('Estudios de envejecimiento', 'descenso de NAD+ con la edad en distintos tejidos.'), ('Estudios de precursores', 'trabajos con NMN y NR para elevar sus niveles.'), ('Estudios mitocondriales', 'función de la cadena respiratoria y producción de energía.')],
    },
    'SS-31': {
        'how': 'La cardiolipina mantiene unidas las proteínas de la cadena respiratoria. Cuando se daña, la mitocondria produce menos energía y más radicales libres. El SS-31 se une a la cardiolipina y estabiliza esa estructura, lo que en los estudios se asocia a una producción de energía más eficiente.',
        'research': [('Enfermedades mitocondriales', 'ensayos clínicos en miopatías mitocondriales.'), ('Estudios cardíacos', 'investigación en insuficiencia cardíaca.'), ('Modelos de envejecimiento', 'función muscular en animales mayores.')],
    },
    'PT-141': {
        'how': 'Los receptores de melanocortina, en especial el MC4R, forman parte de los circuitos del hipotálamo que regulan el deseo sexual. La bremelanotida los activa directamente, por lo que actúa sobre la motivación y la excitación en lugar de sobre el flujo sanguíneo.',
        'research': [('Ensayos clínicos en mujeres', 'los estudios que llevaron a su aprobación.'), ('Estudios en hombres', 'investigación en disfunción eréctil.'), ('Estudios de receptores', 'trabajos sobre el sistema de melanocortina.')],
    },
}
