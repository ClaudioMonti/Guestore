# 🚀 Guida Rapida - Guestore

## ⚡ Inizia subito in 3 passi

### 1️⃣ Personalizza le informazioni del B&B

Apri il file `knowledge_base.json` e cerca questi testi da sostituire:

```
[INSERISCI QUI IL TUO INDIRIZZO]      → Via Roma 123, Milano
[INSERISCI IL TUO NUMERO]             → +39 333 1234567
[INSERISCI LA TUA EMAIL]              → tuo@email.com
[X]                                   → 4 (numero massimo ospiti)
[Attrazione 1]                        → Duomo di Milano
[Nome ristorante]                     → Trattoria da Mario
```

**IMPORTANTE:** Modifica anche:
- Orari check-in/check-out
- Password WiFi
- Informazioni parcheggio
- Regole della casa
- Servizi inclusi

### 2️⃣ Aggiungi la tua foto

1. Vai nella cartella `static/images/`
2. Sostituisci `avatar.png` con la tua foto
3. La foto deve essere quadrata (es: 200x200 pixel)

**Non hai una foto?** Usa uno di questi servizi gratuiti:
- https://avatarmaker.com/
- https://ui-avatars.com/

### 3️⃣ Testa in locale

```bash
# Apri il terminale nella cartella guestore
cd guestore

# Crea ambiente virtuale
python -m venv venv

# Attiva ambiente (Windows)
venv\Scripts\activate

# Attiva ambiente (Mac/Linux)
source venv/bin/activate

# Installa dipendenze
pip install -r requirements.txt

# Avvia il chatbot
python app.py
```

Apri il browser su: **http://localhost:5000**

---

## 🌐 Metti online il chatbot

### Opzione A: Render (Consigliato - GRATIS)

1. Crea account su https://render.com
2. Clicca "New +" → "Web Service"
3. Collega il tuo GitHub (carica prima il progetto su GitHub)
4. Configura:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Deploy!

Il tuo link sarà: `https://guestore.onrender.com`

### Mantieni il sito sempre attivo

1. Vai su https://uptimerobot.com
2. Crea account gratuito
3. Aggiungi monitor HTTP su `https://guestore.onrender.com/health`
4. Intervallo: 5 minuti
5. Fatto! Il sito rimane sempre sveglio 🎉

---

## 💬 Come funziona il chatbot

Il chatbot riconosce **parole chiave** nei messaggi:

**Esempio 1:**
- Ospite: "What time is check-in?"
- Parola chiave riconosciuta: "check-in"
- Risposta: Automatica in inglese

**Esempio 2:**
- Ospite: "Qual è la password del WiFi?"
- Parola chiave riconosciuta: "wifi", "password"
- Risposta: Automatica in italiano

**Esempio 3:**
- Ospite: "Posso portare il mio pappagallo?"
- Nessuna parola chiave riconosciuta
- Risposta: "Non ho la risposta, contatta il proprietario"

---

## ➕ Aggiungere nuove domande

Modifica `knowledge_base.json` aggiungendo una sezione:

```json
"nome_animali": {
  "keywords": ["animale", "animali", "cane", "gatto", "pet", "dog", "cat"],
  "responses": {
    "it": "Siamo pet-friendly! Accettiamo animali fino a 10kg.",
    "en": "We are pet-friendly! We accept pets up to 10kg.",
    "es": "¡Aceptamos mascotas! Hasta 10kg.",
    "fr": "Nous acceptons les animaux! Jusqu'à 10kg.",
    "de": "Wir akzeptieren Haustiere! Bis 10kg.",
    "pt": "Aceitamos animais! Até 10kg."
  }
}
```

Riavvia il server e il chatbot saprà rispondere!

---

## 📨 Invia il link agli ospiti

Dopo la prenotazione, invia:

```
Ciao Maria,

Benvenuta! La tua prenotazione è confermata per il 15 marzo.

Per qualsiasi domanda (check-in, WiFi, parcheggio, ecc.)
puoi chattare 24/7 con il mio assistente Guestore:

🔗 https://guestore.onrender.com

Ci vediamo presto!
Paolo
```

---

## ❓ Domande Frequenti

**Q: Il chatbot risponde male a una domanda**
- Aggiungi più parole chiave in `knowledge_base.json`
- Esempio: se non capisce "arrivo", aggiungi questa keyword a "check_in"

**Q: Voglio cambiare i colori**
- Modifica `static/css/style.css`
- Cerca `#667eea` e `#764ba2` (colori attuali)

**Q: Il sito dorme dopo 15 minuti**
- Configura UptimeRobot come descritto sopra
- Oppure passa a Render Paid (~7€/mese)

**Q: Voglio usare un dominio personale tipo "chat.miobb.it"**
- Acquista dominio (~12€/anno)
- Configura su Render (guida: https://render.com/docs/custom-domains)

**Q: Posso aggiungere più lingue?**
- Sì! Aggiungi la lingua in ogni sezione di `knowledge_base.json`
- Il rilevamento automatico funziona per tutte le lingue

---

## 📋 Checklist Pre-Deploy

Prima di mandare online, verifica:

- [ ] Ho personalizzato TUTTE le informazioni in `knowledge_base.json`
- [ ] Ho sostituito l'avatar con la mia foto
- [ ] Ho testato il chatbot in locale (`python app.py`)
- [ ] Ho provato a fare domande in italiano e inglese
- [ ] Ho verificato che la risposta fallback funzioni
- [ ] Ho caricato il progetto su GitHub
- [ ] Ho fatto il deploy su Render
- [ ] Ho configurato UptimeRobot
- [ ] Ho testato il link pubblico
- [ ] Ho inviato il link a un amico per testarlo

---

**Tutto pronto? Buon lavoro con Guestore! 🎉**

Per il README completo vedi: `README.md`
