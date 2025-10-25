# 🏠 Guestore - Chatbot per B&B

**Guestore** è un chatbot intelligente multilingua progettato per assistere gli ospiti del tuo B&B rispondendo automaticamente alle domande più frequenti.

## ✨ Caratteristiche

- 🌍 **Multilingua automatico** - Rileva e risponde in 3 lingue (IT, EN, FR)
- 💬 **Risposte basate su parole chiave** - Nessun costo API, tutto gratuito
- 🎨 **Avatar personalizzabile** - Avatar basato su una mia foto
- 📱 **Responsive** - Funziona su desktop e mobile
- 🔧 **Facile da configurare** - Modifica le risposte in un semplice file JSON
- ⚡ **Risposta fallback** - Se non capisce, invita a contattarti direttamente

## 📋 Prerequisiti

- Python 3.8 o superiore
- pip (gestore pacchetti Python)

## 🚀 Installazione Locale

### 1. Clona o scarica il progetto
```bash
cd guestore
```

### 2. Crea un ambiente virtuale (consigliato)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Installa le dipendenze
```bash
pip install -r requirements.txt
```

### 4. Personalizza le risposte
Modifica il file `knowledge_base.json` per personalizzare le informazioni del tuo B&B:

**Sezioni da personalizzare:**
- `check_in` - Orari di check-in
- `check_out` - Orari di check-out
- `wifi` - Nome rete e password WiFi
- `parking` - Informazioni sul parcheggio
- `address` - Indirizzo del B&B
- `rules` - Regole della casa
- `attractions` - Attrazioni e ristoranti nelle vicinanze
- `amenities` - Servizi inclusi nell'appartamento
- `contact` - I tuoi contatti (telefono ed email)

**Cerca e sostituisci:**
- `[INSERISCI QUI IL TUO INDIRIZZO]`
- `[INSERISCI IL TUO NUMERO]`
- `[INSERISCI LA TUA EMAIL]`
- `[X]` (numero massimo ospiti)
- `[Attrazione 1]`, `[Nome ristorante]`, ecc.

### 5. Personalizza l'avatar
Sostituisci il file `static/images/avatar.png` con la tua foto:
- Formato: PNG o JPG
- Dimensioni consigliate: 200x200 pixel
- Deve chiamarsi `avatar.png`

Vedi `static/images/AVATAR_INSTRUCTIONS.txt` per maggiori dettagli.

### 6. Avvia l'applicazione
```bash
python app.py
```

Il chatbot sarà disponibile su: `http://localhost:5000`

## 🌐 Deploy su Render (GRATUITO)

### Preparazione

1. Crea un account su [Render.com](https://render.com) (gratuito)
2. Installa Git se non lo hai già
3. Inizializza un repository Git nella cartella del progetto:

```bash
cd guestore
git init
git add .
git commit -m "Initial commit - Guestore chatbot"
```

4. Carica su GitHub:
   - Crea un nuovo repository su GitHub
   - Segui le istruzioni per collegare il repository locale

### Deploy su Render

1. Vai su [Render Dashboard](https://dashboard.render.com)
2. Clicca su **"New +"** → **"Web Service"**
3. Connetti il tuo repository GitHub
4. Configura il servizio:
   - **Name**: `guestore` (o il nome che preferisci)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: `Free`

5. Clicca su **"Create Web Service"**

Render inizierà automaticamente il deploy. Dopo qualche minuto, il tuo chatbot sarà online!

### URL del chatbot

Render ti fornirà un URL tipo: `https://guestore.onrender.com`

Questo è il link che invierai agli ospiti! 🎉

## 🔧 Mantenere il sito sempre attivo (GRATIS)

Render Free dorme dopo 15 minuti di inattività. Per mantenerlo sveglio:

### Metodo 1: UptimeRobot (consigliato)

1. Vai su [UptimeRobot.com](https://uptimerobot.com)
2. Crea un account gratuito
3. Aggiungi un nuovo monitor:
   - **Monitor Type**: HTTP(s)
   - **URL**: il tuo URL Render (es: `https://guestore.onrender.com/health`)
   - **Monitoring Interval**: 5 minuti
4. Salva

UptimeRobot farà un "ping" al sito ogni 5 minuti, mantenendolo sempre attivo!

### Metodo 2: Cron-Job.org

Alternativa a UptimeRobot, stessa configurazione.

## 📱 Come inviare il link agli ospiti

Dopo aver prenotato, invia un messaggio tipo:

```
Ciao [Nome],

Grazie per la prenotazione!

Per qualsiasi domanda su check-in, WiFi, parcheggio o altro,
puoi chattare con il mio assistente virtuale Guestore:

🔗 https://guestore.onrender.com

A presto!
```

## 🛠️ Personalizzazione Avanzata

### Aggiungere nuove domande/risposte

Modifica `knowledge_base.json` aggiungendo una nuova sezione:

```json
"nome_categoria": {
  "keywords": ["parola1", "parola2", "keyword"],
  "responses": {
    "it": "Risposta in italiano",
    "en": "Answer in English",
    "es": "Respuesta en español",
    "fr": "Réponse en français",
    "de": "Antwort auf Deutsch",
    "pt": "Resposta em português"
  }
}
```

### Modificare i colori

Modifica `static/css/style.css`:
- Linea 8-9: Gradient di sfondo
- Linea 42: Gradient header
- Cerca `#667eea` e `#764ba2` per cambiare i colori principali

### Modificare il messaggio di benvenuto

Modifica `templates/index.html` alla linea 25-26.

## 📂 Struttura del Progetto

```
guestore/
├── app.py                      # Backend Flask
├── requirements.txt            # Dipendenze Python
├── knowledge_base.json         # Domande e risposte (PERSONALIZZA QUI)
├── templates/
│   └── index.html             # Interfaccia chatbot
├── static/
│   ├── css/
│   │   └── style.css          # Stili
│   ├── js/
│   │   └── script.js          # Logica frontend
│   └── images/
│       ├── avatar.png         # Avatar (SOSTITUISCI CON TUA FOTO)
│       └── AVATAR_INSTRUCTIONS.txt
└── README.md                  # Questo file
```

## 🆘 Risoluzione Problemi

### Il chatbot non risponde correttamente

1. Verifica che le parole chiave in `knowledge_base.json` siano appropriate
2. Aggiungi più sinonimi alle keywords
3. Controlla che il file JSON sia valido (usa un validatore JSON online)

### Errore "ModuleNotFoundError"

```bash
pip install -r requirements.txt
```

### Il sito Render va in sleep

Configura UptimeRobot come descritto sopra.

### L'avatar non appare

1. Verifica che il file si chiami esattamente `avatar.png`
2. Controlla che sia nella cartella `static/images/`
3. Pulisci la cache del browser (Ctrl+F5)

## 💰 Costi

- **Hosting Render Free**: €0/mese
- **UptimeRobot**: €0/mese (fino a 50 monitor)
- **Dominio personalizzato** (opzionale): ~€10-15/anno

**Totale: GRATIS** 🎉

Se in futuro vorrai:
- Eliminare completamente il delay iniziale: Render Starter €7/mese
- Dominio personalizzato tipo `guestore.tuob&b.it`: ~€12/anno

## 📝 Licenza

Questo progetto è stato creato per uso personale. Sei libero di modificarlo e utilizzarlo per il tuo B&B.

## 🤝 Supporto

Per problemi o domande, contatta il tuo sviluppatore o crea un issue su GitHub.

---

**Buona fortuna con il tuo B&B! 🏠✨**
