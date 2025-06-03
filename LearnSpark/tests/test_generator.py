# Unit Tests für die Lernpfadgenerierungsfunktion.

import pytest
from generator import generate_learning_path

def test_generate_ml_learning_path():
    """
    Testet die Generierung einer simulierten ML-Lernpfadstruktur.

    Prüft die Existenz und die Typen der Hauptfelder sowie die Anzahl der Module.
    """
    # Testet die Generierung für das ML-Thema
    topic = "Introduction to Machine Learning"
    path = generate_learning_path(topic)

    assert isinstance(path, dict)
    assert "topic_name" in path
    assert isinstance(path["topic_name"], str)
    assert path["topic_name"] == "Einführung in Machine Learning"
    
    assert "estimated_duration_weeks" in path
    assert isinstance(path["estimated_duration_weeks"], int)
    assert path["estimated_duration_weeks"] > 0
    
    assert "modules" in path
    assert isinstance(path["modules"], list)
    assert len(path["modules"]) >= 3 # Prüfen auf mindestens 3 Module (wie in der Simulation)

    for module in path["modules"]:
        assert isinstance(module, dict)
        assert "module_name" in module
        assert isinstance(module["module_name"], str)
        assert "description" in module # Prüfen, ob Beschreibung hinzugefügt wurde
        assert isinstance(module["description"], str)
        assert "sub_topics" in module
        assert isinstance(module["sub_topics"], list)
        # Optional: Tiefergehende Prüfung der Unterthemen-Struktur
        # for sub_topic in module["sub_topics"]:
        #     assert isinstance(sub_topic, dict)
        #     assert "name" in sub_topic
        #     assert isinstance(sub_topic["name"], str)
        #     assert "key_concepts" in sub_topic
        #     assert isinstance(sub_topic["key_concepts"], list)

def test_generate_generic_learning_path():
    """
    Testet die Generierung einer simulierten generischen Lernpfadstruktur für ein unbekanntes Thema.

    Prüft die Existenz und die Typen der Hauptfelder sowie die Anzahl der Module und die Benennung der Module.
    """
    # Testet die Generierung für ein generisches Thema
    topic = "Quantum Computing"
    path = generate_learning_path(topic)

    assert isinstance(path, dict)
    assert "topic_name" in path
    assert isinstance(path["topic_name"], str)
    assert path["topic_name"] == topic # Der generische Pfad verwendet den Eingabethema-Namen

    assert "estimated_duration_weeks" in path
    assert isinstance(path["estimated_duration_weeks"], int)
    assert path["estimated_duration_weeks"] > 0

    assert "modules" in path
    assert isinstance(path["modules"], list)
    assert len(path["modules"]) >= 1 # Mindestens ein Modul in der generischen Struktur
    
    # Prüfen, ob die Modulnamen die erwartete Struktur haben (generisch)
    assert "Grundlagen zu " + topic in [m["module_name"] for m in path["modules"]]

def test_generate_empty_topic():
    """
    Testet das Verhalten der Generierungsfunktion bei leerem Thema.

    Erwartet die Rückgabe der generischen Struktur.
    """
    # Testet leeres Thema
    topic = ""
    path = generate_learning_path(topic)
    
    assert isinstance(path, dict)
    assert "topic_name" in path
    assert path["topic_name"] == topic # Leeres Thema wird übernommen
    assert "modules" in path
    assert isinstance(path["modules"], list)
    assert len(path["modules"]) >= 1 # Immer noch eine generische Struktur erwartet

def test_generate_whitespace_topic():
    """
    Testet das Verhalten der Generierungsfunktion bei einem Thema nur mit Leerzeichen.

    Erwartet die Rückgabe der generischen Struktur.
    """
    # Testet Thema nur mit Leerzeichen
    topic = "   "
    path = generate_learning_path(topic)
    
    assert isinstance(path, dict)
    assert "topic_name" in path
    # Hier muss der Code in generate_learning_path angepasst werden, um 'topic.strip()' zu verwenden
    # Aber der Test prüft, ob die Funktion mit Leerzeichen umgehen kann
    assert path["topic_name"] == topic # Leerzeichen werden übernommen in der aktuellen generator.py
    assert "modules" in path
    assert isinstance(path["modules"], list)
    assert len(path["modules"]) >= 1

# Hinweis: generate_learning_path in generator.py behandelt leere/Whitespace Topics aktuell NICHT als Fehler
# sondern gibt die generische Struktur zurück. Die Tests spiegeln dieses aktuelle Verhalten wider.
# Wenn die Anforderung wäre, dass generate_learning_path bei leerem/Whitespace Topic einen Fehler werfen soll,
# müssten generator.py UND die Tests angepasst werden. 