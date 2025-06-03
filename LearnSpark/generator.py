import uuid
from typing import List, Dict, Any

def generate_learning_path(topic: str) -> Dict[str, Any]:
    """
    Generiert eine simulierte Lernpfadstruktur für ein gegebenes Thema.
    
    Args:
        topic: Das Thema für den Lernpfad.
        
    Returns:
        Ein Dictionary, das die Lernpfadstruktur darstellt.
    """
    # Dies ist eine simulierte Generierung. Ein echtes LLM würde hier verwendet werden.
    # Wir erstellen eine plausible Struktur für 'Introduction to Machine Learning'.
    
    # Normalisierung des Themas für den Vergleich
    normalized_topic = topic.lower().strip()
    
    if 'machine learning' in normalized_topic or 'ki' in normalized_topic or 'ml' in normalized_topic:
        # Simulierte Struktur für Einführung in Machine Learning
        return {
            "topic_name": "Einführung in Machine Learning",
            "estimated_duration_weeks": 6,
            "modules": [
                {
                    "module_name": "Grundlagen und Daten",
                    "description": "Erfahre die grundlegenden Konzepte des maschinellen Lernens und wie Daten für Modelle vorbereitet werden.",
                    "sub_topics": [
                        {
                            "name": "Verstehe, was Machine Learning ist und seine Anwendungsbereiche",
                            "key_concepts": [
                                "Definitionen",
                                "Arten: Überwacht, Unüberwacht, Bestärkend",
                                "Anwendungsgebiete"
                            ]
                        },
                        {
                            "name": "Bereite Daten für ML-Modelle auf",
                            "key_concepts": [
                                "Fehlende Werte behandeln",
                                "Feature Scaling (Skalierung)",
                                "Kategoriale Daten kodieren"
                            ]
                        }
                    ]
                },
                {
                    "module_name": "Überwachtes Lernen: Regression",
                    "description": "Tauche ein in die Welt des überwachten Lernens und lerne, wie man kontinuierliche Werte vorhersagt.",
                    "sub_topics": [
                        {
                            "name": "Implementiere und verstehe Lineare Regression",
                            "key_concepts": [
                                "Lineares Modell",
                                "Kostenfunktion (MSE)",
                                "Gradientenabstieg",
                                "R-squared"
                            ]
                        },
                        {
                            "name": "Bewerte die Leistung von Regressionsmodellen",
                            "key_concepts": [
                                "Mean Squared Error (MSE)",
                                "Root Mean Squared Error (RMSE)",
                                "Mean Absolute Error (MAE)"
                            ]
                        }
                    ]
                },
                {
                    "module_name": "Überwachtes Lernen: Klassifikation",
                    "description": "Lerne Modelle zu bauen, die Daten in Kategorien einordnen können.",
                    "sub_topics": [
                        {
                            "name": "Wende Logistische Regression für binäre Klassifikation an",
                            "key_concepts": [
                                "Sigmoid-Funktion",
                                "Entscheidungsgrenze"
                            ]
                        },
                         {
                            "name": "Nutze K-Nächste Nachbarn (KNN) für einfache Klassifikationsaufgaben",
                            "key_concepts": [
                                "Abstandsmetriken",
                                "Lazy Learner"
                            ]
                        },
                        {
                            "name": "Interpretiere und nutze Klassifikations-Metriken",
                            "key_concepts": [
                                "Konfusionsmatrix",
                                "Genauigkeit (Accuracy)",
                                "Präzision (Precision)",
                                "Recall",
                                "F1-Score"
                            ]
                        }
                    ]
                },
                 {
                    "module_name": "Unüberwachtes Lernen",
                    "description": "Entdecke Methoden, um Muster in ungelabelten Daten zu finden.",
                    "sub_topics": [
                        {
                            "name": "Gruppiere Daten mit Clustering-Methoden (K-Means)",
                            "key_concepts": [
                                "Zentroide",
                                "Ellenbogen-Methode"
                            ]
                        },
                         {
                            "name": "Reduziere die Dimensionalität von Daten (PCA)",
                            "key_concepts": [
                                "Principal Components",
                                "Varianz-Erklärung"
                            ]
                        }
                    ]
                }
            ]
        }
    else:
        # Generische Struktur oder Fehlermeldung für andere Themen
        return {
            "topic_name": topic,
            "estimated_duration_weeks": 4,
            "modules": [
                {
                    "module_name": "Grundlagen zu " + topic,
                    "description": "Erfahre die wichtigsten Grundkonzepte und den historischen Kontext von " + topic + ".",
                    "sub_topics": [
                        {
                            "name": "Erhalte einen Überblick über " + topic + " und seine Bedeutung",
                            "key_concepts": [topic + " Definition", "Geschichte", "Wichtigkeit"]
                        }
                    ]
                },
                {
                     "module_name": "Vertiefung der Kernkonzepte in " + topic,
                     "description": "Tauche tiefer in die fundamentalen Ideen ein, die " + topic + " ausmachen.",
                    "sub_topics": [
                        {
                            "name": "Verstehe und erkläre Kernkonzept 1",
                            "key_concepts": ["Konzept 1"]
                        },
                         {
                            "name": "Analysiere die Anwendung von Kernkonzept 2",
                            "key_concepts": ["Konzept 2"]
                        },
                         {
                            "name": "Diskutiere die Herausforderungen von Kernkonzept 3",
                            "key_concepts": ["Konzept 3"]
                        }
                    ]
                }
            ]
        }

# Beispielhafte Nutzung (kann entfernt werden oder in einem separaten Skript laufen)
# if __name__ == "__main__":
#     ml_path = generate_learning_path("Introduction to Machine Learning")
#     import json
#     print(json.dumps(ml_path, indent=2))

#     generic_path = generate_learning_path("Quantencomputing")
#     print(json.dumps(generic_path, indent=2)) 