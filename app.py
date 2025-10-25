from flask import Flask, render_template, request, jsonify
import json
from langdetect import detect, LangDetectException
import re

app = Flask(__name__)

# Carica la knowledge base
with open('knowledge_base.json', 'r', encoding='utf-8') as f:
    knowledge_base = json.load(f)

def detect_language(text):
    """Rileva la lingua del testo con maggiore accuratezza"""
    text_lower = text.lower()

    # Keyword specifiche per lingua per aiutare il rilevamento
    italian_words = ['ciao', 'salve', 'buongiorno', 'buonasera', 'grazie', 'prego', 'dove', 'quando', 'come']
    english_words = ['hello', 'hi', 'thank', 'please', 'where', 'when', 'how']
    french_words = ['bonjour', 'salut', 'merci', 's\'il', 'vous', 'plaît', 'où', 'quand', 'comment']

    # Conta le parole per lingua
    it_count = sum(1 for word in italian_words if word in text_lower)
    en_count = sum(1 for word in english_words if word in text_lower)
    fr_count = sum(1 for word in french_words if word in text_lower)

    # Se abbiamo una corrispondenza forte, usa quella
    if it_count > en_count and it_count > fr_count:
        return 'it'
    if fr_count > en_count and fr_count > it_count:
        return 'fr'
    if en_count > 0:
        return 'en'

    # Altrimenti usa langdetect
    try:
        lang = detect(text)
        supported_langs = ['it', 'en', 'fr']
        return lang if lang in supported_langs else 'en'
    except LangDetectException:
        return 'en'  # Default a inglese

def normalize_text(text):
    """Normalizza il testo per il matching"""
    return text.lower().strip()

def find_best_match(user_message, user_lang):
    """Trova la migliore risposta basata sulle parole chiave"""
    user_message = normalize_text(user_message)

    # Controlla ogni categoria nella knowledge base
    best_match = None
    max_matches = 0

    for category, data in knowledge_base.items():
        if category == 'fallback_responses':
            continue

        keywords = data.get('keywords', [])

        # Conta quante parole chiave corrispondono
        matches = sum(1 for keyword in keywords if keyword in user_message)

        if matches > max_matches:
            max_matches = matches
            best_match = category

    # Se abbiamo trovato almeno una corrispondenza
    if best_match and max_matches > 0:
        responses = knowledge_base[best_match]['responses']
        # IMPORTANTE: Usa SEMPRE la lingua rilevata
        return responses.get(user_lang, responses.get('en', ''))

    # Nessuna corrispondenza trovata - risposta fallback NELLA LINGUA RILEVATA
    return knowledge_base['fallback_responses'].get(user_lang,
           knowledge_base['fallback_responses']['en'])

@app.route('/')
def index():
    """Pagina principale del chatbot"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint per gestire i messaggi del chatbot"""
    data = request.json
    user_message = data.get('message', '')

    if not user_message:
        return jsonify({'error': 'Messaggio vuoto'}), 400

    # Rileva la lingua
    user_lang = detect_language(user_message)

    # Trova la risposta migliore
    response = find_best_match(user_message, user_lang)

    return jsonify({
        'response': response,
        'detected_language': user_lang
    })

@app.route('/health')
def health():
    """Health check per UptimeRobot"""
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
