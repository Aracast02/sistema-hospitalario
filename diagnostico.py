from transformers import pipeline
import multiprocessing
import random

# Inicializar modelo preentrenado (análisis de sentimientos)
classifier = pipeline("sentiment-analysis", 
                      model="distilbert-base-uncased-finetuned-sst-2-english")

# Simulación de datos del paciente
SAMPLE_SYMPTOMS = [
    # Críticos
    "dificultad respiratoria severa",
    "dolor intenso en el pecho",
    "pérdida del conocimiento",
    "hemorragia incontrolable",
    "convulsiones activas",
    "estado de choque",
    "quemaduras graves",
    "síntomas de infarto",
    "síntomas de ACV",
    "traumatismo craneal severo",
    "paro cardíaco",

    # Estables
    "fiebre moderada",
    "dolor abdominal moderado",
    "tos persistente",
    "dolor muscular generalizado",
    "cefalea",
    "náuseas",
    "vómito ocasional",
    "mareo leve",
    "laceraciones menores",
    "reacción alérgica leve",
    "síntomas gripales"
]

def automated_diagnosis(patient_id):
    print(f"Iniciando diagnóstico IA preentrenado paciente {patient_id}")

    # Seleccionar síntomas aleatorios
    symptoms = random.choice(SAMPLE_SYMPTOMS)

    # Realizar inferencia con modelo preentrenado
    result = classifier(symptoms)[0]

    # Interpretar resultado como diagnóstico
    diagnosis = "crítico" if result['label'] == 'NEGATIVE' else "estable"

    print(f"Diagnóstico paciente {patient_id}: {diagnosis} (confianza: {result['score']:.2f})")

    return {
        "patient_id": patient_id,
        "symptoms": symptoms,
        "diagnosis": diagnosis,
        "confidence": result['score']
    }

def run_parallel_diagnosis(patient_list):
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(automated_diagnosis, patient_list)
    return results
