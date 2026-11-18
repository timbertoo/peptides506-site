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
