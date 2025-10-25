# 📝 Esempio Pratico di Personalizzazione

Questa guida ti mostra **esattamente** cosa modificare nel file `knowledge_base.json`.

---

## 🔍 PRIMA: File Generico

```json
"contact": {
  "keywords": ["contatto", "telefono", "email", "chiamare"],
  "responses": {
    "it": "Puoi contattarmi:\n📱 Telefono: [INSERISCI IL TUO NUMERO]\n📧 Email: [INSERISCI LA TUA EMAIL]",
    "en": "You can contact me:\n📱 Phone: [INSERT YOUR PHONE NUMBER]\n📧 Email: [INSERT YOUR EMAIL]"
  }
}
```

---

## ✅ DOPO: File Personalizzato (esempio B&B a Milano)

```json
"contact": {
  "keywords": ["contatto", "telefono", "email", "chiamare"],
  "responses": {
    "it": "Puoi contattarmi:\n📱 Telefono: +39 333 1234567\n📧 Email: paolo.rossi@gmail.com\nSono sempre disponibile per qualsiasi necessità!",
    "en": "You can contact me:\n📱 Phone: +39 333 1234567\n📧 Email: paolo.rossi@gmail.com\nI'm always available for any needs!"
  }
}
```

---

## 📍 Esempio Completo: Sezione Indirizzo

### PRIMA
```json
"address": {
  "keywords": ["indirizzo", "dove", "posizione"],
  "responses": {
    "it": "L'indirizzo è: [INSERISCI QUI IL TUO INDIRIZZO]\nTi invierò le indicazioni dettagliate dopo la prenotazione."
  }
}
```

### DOPO
```json
"address": {
  "keywords": ["indirizzo", "dove", "posizione"],
  "responses": {
    "it": "L'indirizzo è: Via Giuseppe Verdi 45, 20121 Milano (MI)\nSiamo a 5 minuti a piedi dalla stazione Centrale.\nTi invierò le indicazioni dettagliate dopo la prenotazione."
  }
}
```

---

## 🔑 Esempio: WiFi con Password Vera

### PRIMA
```json
"wifi": {
  "keywords": ["wifi", "wi-fi", "internet", "password"],
  "responses": {
    "it": "Nome WiFi: GuestoreNet\nPassword: Troverai la password nell'appartamento, vicino al router."
  }
}
```

### DOPO (Opzione 1: Password nascosta)
```json
"wifi": {
  "keywords": ["wifi", "wi-fi", "internet", "password"],
  "responses": {
    "it": "Nome WiFi: CasaMilano_5G\nPassword: Troverai la password nell'appartamento, sul frigorifero."
  }
}
```

### DOPO (Opzione 2: Password nel chatbot)
```json
"wifi": {
  "keywords": ["wifi", "wi-fi", "internet", "password"],
  "responses": {
    "it": "Nome WiFi: CasaMilano_5G\nPassword: Milano2024!\n\nRicordati di disconnetterti al check-out."
  }
}
```

---

## 🅿️ Esempio: Parcheggio Specifico

### PRIMA
```json
"parking": {
  "keywords": ["parcheggio", "parcheggiare", "auto"],
  "responses": {
    "it": "C'è parcheggio gratuito sulla strada. In alternativa, c'è un parcheggio pubblico a 5 minuti a piedi."
  }
}
```

### DOPO
```json
"parking": {
  "keywords": ["parcheggio", "parcheggiare", "auto", "macchina", "garage"],
  "responses": {
    "it": "Puoi parcheggiare gratuitamente in Via Verdi (strisce bianche).\n\nAlternative a pagamento:\n- Garage Centrale: 15€/giorno (Via Roma 10)\n- Parcheggio Stazione: 12€/giorno\n\nSe arrivi dopo le 20:00, il parcheggio in strada è sempre gratuito."
  }
}
```

---

## 🏛️ Esempio: Attrazioni Locali Personalizzate

### PRIMA
```json
"attractions": {
  "keywords": ["attrazioni", "visitare", "vedere", "ristorante"],
  "responses": {
    "it": "Nelle vicinanze trovi:\n- [Attrazione 1] a 10 minuti a piedi\n- [Attrazione 2] a 5 minuti in auto\n- Ottimi ristoranti: [Nome ristorante]"
  }
}
```

### DOPO
```json
"attractions": {
  "keywords": ["attrazioni", "visitare", "vedere", "ristorante", "mangiare", "turismo"],
  "responses": {
    "it": "Nelle vicinanze trovi:\n\n🏛️ ATTRAZIONI:\n- Duomo di Milano: 10 min a piedi\n- Galleria Vittorio Emanuele: 12 min a piedi\n- Teatro alla Scala: 15 min a piedi\n- Castello Sforzesco: 20 min metro\n\n🍝 RISTORANTI CONSIGLIATI:\n- Trattoria Milanese (cucina tipica): Via Santa Marta\n- Pizzeria Spontini (pizza al taglio): Corso Buenos Aires\n- Luini (panzerotti): Via Santa Radegonda\n\n☕ CAFFÈ:\n- Pasticceria Marchesi (storica): Via Santa Maria alla Porta\n\nVuoi altre info? Chiedimi pure!"
  }
}
```

---

## 🏠 Esempio: Regole Casa Dettagliate

### PRIMA
```json
"rules": {
  "keywords": ["regole", "regolamento", "permesso"],
  "responses": {
    "it": "Regole della casa:\n- Non fumare in casa\n- Rispetta il silenzio dopo le 22:00\n- Massimo [X] ospiti\n- Non sono ammessi animali"
  }
}
```

### DOPO
```json
"rules": {
  "keywords": ["regole", "regolamento", "permesso", "consentito", "vietato", "animali", "fumare"],
  "responses": {
    "it": "Regole della casa:\n\n✅ CONSENTITO:\n- Fumare sul balcone\n- Cucinare (con attenzione)\n- Invitare ospiti di giorno\n- Uso lavatrice (orari 9-21)\n\n❌ NON CONSENTITO:\n- Fumare in casa\n- Rumore dopo le 22:00\n- Più di 4 ospiti\n- Feste o eventi\n- Animali domestici\n\n📌 ALTRO:\n- Rispetta i vicini\n- Differenzia i rifiuti\n- Chiudi a chiave quando esci\n\nGrazie per la collaborazione! 🙏"
  }
}
```

---

## ➕ Aggiungere una NUOVA Categoria

Vuoi che il chatbot risponda a "Come funziona il riscaldamento/aria condizionata"?

Aggiungi questa sezione in `knowledge_base.json`:

```json
"clima": {
  "keywords": ["riscaldamento", "aria condizionata", "climatizzatore", "caldo", "freddo", "temperature", "heating", "air conditioning"],
  "responses": {
    "it": "🌡️ CLIMATIZZAZIONE:\n\nAria condizionata:\n- Telecomando sul comodino\n- Temperatura consigliata: 22-24°C\n- Non dimenticare di spegnerla quando esci\n\nRiscaldamento (inverno):\n- Termostato in soggiorno\n- Temperatura preimpostata: 20°C\n- Regolabile a tuo piacimento\n\nProblemi? Contattami!",
    "en": "🌡️ CLIMATE CONTROL:\n\nAir conditioning:\n- Remote on the nightstand\n- Recommended temp: 22-24°C\n- Remember to turn off when leaving\n\nHeating (winter):\n- Thermostat in living room\n- Preset temperature: 20°C\n- Adjustable as you prefer\n\nIssues? Contact me!",
    "es": "🌡️ CLIMATIZACIÓN:\n\nAire acondicionado:\n- Mando en la mesita de noche\n- Temperatura recomendada: 22-24°C\n- Recuerda apagarlo al salir\n\nCalefacción (invierno):\n- Termostato en salón\n- Temperatura preestablecida: 20°C\n- Ajustable a tu gusto\n\n¿Problemas? ¡Contáctame!"
  }
}
```

**IMPORTANTE:** Ricorda la virgola dopo la sezione precedente!

---

## 🎨 Personalizzare il Messaggio di Benvenuto

Non si modifica in `knowledge_base.json`, ma in `templates/index.html`.

Cerca questa riga (circa linea 25):

```html
<p>Ciao! Sono Guestore, il tuo assistente virtuale. Come posso aiutarti?</p>
```

Modifica con:

```html
<p>Ciao! Sono l'assistente virtuale di Casa Milano B&B. Come posso aiutarti?</p>
```

E la riga successiva (hint):

```html
<p class="message-hint">Puoi chiedermi informazioni su check-in, WiFi, parcheggio, servizi e molto altro!</p>
```

Modifica con:

```html
<p class="message-hint">Posso aiutarti con check-in, WiFi, parcheggio, attrazioni a Milano e molto altro! Scrivimi in qualsiasi lingua.</p>
```

---

## 💡 Consigli Pratici

### 1. Usa emoji per rendere più amichevole 😊
```json
"responses": {
  "it": "✅ Check-in: 14:00-20:00\n⏰ Check-out: entro le 10:00"
}
```

### 2. Dividi testo lungo con \n (a capo)
```json
"it": "Prima riga\nSeconda riga\n\nTerza riga dopo spazio"
```

### 3. Aggiungi sinonimi alle keywords
```json
"keywords": ["wifi", "wi-fi", "internet", "password", "rete", "connessione", "connection"]
```

### 4. Sii specifico e utile
❌ "Il check-in è nel pomeriggio"
✅ "Check-in dalle 14:00 alle 20:00. Se arrivi dopo le 20:00, avvisami almeno 2 ore prima."

---

## 📋 Checklist Personalizzazione

Prima di andare online, verifica di aver personalizzato:

- [ ] Indirizzo completo del B&B
- [ ] Orari check-in e check-out
- [ ] Nome rete WiFi (e password, se vuoi darla)
- [ ] Informazioni parcheggio
- [ ] Telefono e email
- [ ] Numero massimo ospiti [X]
- [ ] Attrazioni locali specifiche
- [ ] Ristoranti consigliati
- [ ] Regole della casa dettagliate
- [ ] Servizi inclusi (cucina, lavatrice, ecc.)

---

**Hai personalizzato tutto? Testa il chatbot con TEST_CHATBOT.md! 🚀**
