# LearnSpark Backend - Flask Hauptanwendung
# Enthält API-Endpunkte für die Lernpfadverwaltung.

from flask import Flask, request, jsonify
import uuid
from generator import generate_learning_path
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)


# In-memory storage for learning paths
learning_paths = {}

@app.route('/lernpfad', methods=['POST'])
def create_learning_path():
    """
    Erstellt einen neuen Lernpfad mit einem Namen.

    Erwartet einen JSON-Body mit dem Feld 'name'.
    Generiert eine eindeutige ID und speichert den Pfad im Speicher.

    Parameters:
    - request (Flask.request): Das eingehende Request-Objekt.

    Returns:
    - JSON response: Ein Dictionary mit der ID, dem Namen und dem Erstellungszeitpunkt des Lernpfads.
      Status Code 201 bei Erfolg.

    Exceptions:
    - Returns JSON error: Bei ungültigem JSON, fehlendem/leerem/ungültigem Namen.
      Status Code 400 bei Fehler.
    """
    # Get the name from the request body
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format', 'details': str(e)}), 400

    # Check if data is valid and 'name' is present and not empty
    if not data:
        return jsonify({'error': 'Request body cannot be empty'}), 400
        
    if 'name' not in data:
        return jsonify({'error': 'Name field is required'}), 400
        
    name = data['name']
    
    if not isinstance(name, str):
        return jsonify({'error': 'Name must be a string'}), 400
        
    if not name.strip():
        return jsonify({'error': 'Name cannot be empty'}), 400

    # Generate a unique ID
    path_id = str(uuid.uuid4())

    # Create initial empty learning path structure with timestamp
    created_at = datetime.utcnow().isoformat() + 'Z'
    learning_paths[path_id] = {
        'id': path_id,
        'name': name.strip(), # Store stripped name
        'modules': [],
        'created_at': created_at
    }

    # Return the created learning path
    return jsonify({
        'id': path_id,
        'name': name.strip(), # Return stripped name
        'created_at': created_at
    }), 201

@app.route('/generate-path', methods=['POST'])
def generate_and_return_path():
    """
    Generiert eine simulierte Lernpfadstruktur basierend auf einem Thema.

    Erwartet einen JSON-Body mit dem Feld 'topic'.
    Nutzt die generate_learning_path Funktion aus generator.py.

    Parameters:
    - request (Flask.request): Das eingehende Request-Objekt.

    Returns:
    - JSON response: Eine Dictionary-Struktur, die den generierten Lernpfad darstellt.
      Status Code 200 bei Erfolg.

    Exceptions:
    - Returns JSON error: Bei ungültigem JSON, fehlendem/leerem/ungültigem Thema.
      Status Code 400 bei Fehler.
    """
    # Get the topic from the request body
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': 'Invalid JSON format', 'details': str(e)}), 400

    # Check if data is valid and 'topic' is present and not empty
    if not data:
        return jsonify({'error': 'Request body cannot be empty'}), 400
        
    if 'topic' not in data:
        return jsonify({'error': 'Topic field is required'}), 400
        
    topic = data['topic']
    
    if not isinstance(topic, str):
        return jsonify({'error': 'Topic must be a string'}), 400
        
    if not topic.strip():
        return jsonify({'error': 'Topic cannot be empty'}), 400

    # Generate the learning path structure
    generated_path = generate_learning_path(topic.strip())
    
    # Return the generated structure
    return jsonify(generated_path), 200

if __name__ == '__main__':
    # Führt die Flask-Anwendung aus
    app.run(debug=True) 