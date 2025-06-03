# LearnSpark Backend

Ein Backend für die Verwaltung von KI-generierten Lernpfaden.

## Installation

1. Erstellen Sie eine virtuelle Umgebung:
```bash
python -m venv venv
```

2. Aktivieren Sie die virtuelle Umgebung:
- Windows:
```bash
.\venv\Scripts\activate
```
- Linux/Mac:
```bash
source venv/bin/activate
```

3. Installieren Sie die Abhängigkeiten:
```bash
pip install -r requirements.txt
```

## Ausführung

Starten Sie den Server:
```bash
python app.py
```

Der Server läuft dann auf `http://localhost:5000`

## API-Endpunkte

### Lernpfad erstellen
- **POST** `/lernpfad`
- **Body**: 
```json
{
    "name": "Name des Lernpfads"
}
```
- **Response**: 
```json
{
    "id": "generierte-uuid",
    "name": "Name des Lernpfads"
}
``` 