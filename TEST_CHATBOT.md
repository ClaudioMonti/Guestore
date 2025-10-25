# 🧪 Test del Chatbot Guestore

Usa questa guida per testare che il chatbot funzioni correttamente.

## Come Testare

1. Avvia il chatbot: `python app.py`
2. Apri il browser su: http://localhost:5000
3. Prova le domande qui sotto
4. Verifica che le risposte siano corrette

---

## ✅ Test in Italiano

| Domanda | Risposta Attesa |
|---------|-----------------|
| "Ciao" | Saluto di benvenuto |
| "A che ora è il check-in?" | Orari check-in 14:00-20:00 |
| "Quando devo lasciare la stanza?" | Orari check-out entro 10:00 |
| "Qual è la password del WiFi?" | Nome rete e password WiFi |
| "Dove posso parcheggiare?" | Info sul parcheggio |
| "Qual è l'indirizzo?" | Indirizzo del B&B |
| "Quali sono le regole?" | Regole della casa |
| "Cosa c'è da visitare?" | Attrazioni e ristoranti |
| "Cosa include l'appartamento?" | Elenco servizi |
| "Come ti contatto?" | Telefono ed email |
| "Posso portare un elefante?" | ❌ "Non ho la risposta, contatta il proprietario" |

---

## ✅ Test in Inglese

| Domanda | Risposta Attesa |
|---------|-----------------|
| "Hello" | Welcome greeting |
| "What time is check-in?" | Check-in times 2:00 PM - 8:00 PM |
| "When is check-out?" | Check-out by 10:00 AM |
| "What's the WiFi password?" | WiFi name and password |
| "Where can I park?" | Parking information |
| "What's the address?" | B&B address |
| "What are the rules?" | House rules |
| "What can I visit nearby?" | Attractions and restaurants |
| "What amenities are included?" | List of amenities |
| "How can I contact you?" | Phone and email |
| "Can I bring my dragon?" | ❌ "I don't have the answer, contact the owner" |

---

## ✅ Test Multilingua

Prova le stesse domande in:
- **Spagnolo**: "Hola", "¿A qué hora es el check-in?"
- **Francese**: "Bonjour", "À quelle heure est l'enregistrement?"
- **Tedesco**: "Hallo", "Wann ist der Check-in?"
- **Portoghese**: "Olá", "A que horas é o check-in?"

Il chatbot deve rispondere **nella stessa lingua** della domanda!

---

## 🔍 Verifica Tecnica

### 1. Test Rilevamento Lingua

Apri la console del browser (F12) e scrivi una domanda.

Nella risposta JSON dovresti vedere:
```json
{
  "response": "...",
  "detected_language": "it"  // o "en", "es", ecc.
}
```

### 2. Test Parole Chiave Multiple

Domande con più parole chiave:

- "Dove parcheggio e qual è l'indirizzo?" → Dovrebbe rispondere sul **parcheggio** (prima keyword)
- "WiFi password check-in" → Dovrebbe rispondere sul **WiFi** o **check-in**

### 3. Test Risposta Fallback

Prova domande senza senso:
- "asdfghjkl"
- "Quanto costa un caffè su Marte?"
- "Bla bla bla"

Tutte devono dare la risposta: **"Non ho la risposta, contatta il proprietario"**

---

## 🐛 Problemi e Soluzioni

### Il chatbot non risponde
- ✅ Verifica che `python app.py` sia in esecuzione
- ✅ Controlla http://localhost:5000 nel browser
- ✅ Apri console (F12) per vedere errori

### Risponde sempre con fallback
- ✅ Controlla `knowledge_base.json` - deve essere valido JSON
- ✅ Verifica che le keywords includano sinonimi
- ✅ Prova parole chiave esatte: "check-in", "wifi", "parking"

### Avatar non appare
- ✅ Verifica che `static/images/avatar.png` esista
- ✅ Pulisci cache browser (Ctrl+F5)
- ✅ Controlla console browser per errori 404

### Risponde in lingua sbagliata
- ✅ Scrivi frasi più lunghe (min 5-6 parole)
- ✅ langdetect funziona meglio con testo più lungo

---

## 📊 Checklist Test Completo

Prima del deploy, verifica:

- [ ] Tutte le domande in italiano ricevono risposta corretta
- [ ] Tutte le domande in inglese ricevono risposta corretta
- [ ] Almeno 2 lingue extra funzionano (es: spagnolo, francese)
- [ ] Domande sconosciute ricevono risposta fallback
- [ ] Avatar appare correttamente
- [ ] Interfaccia è responsive (testa su mobile)
- [ ] Non ci sono errori nella console del browser
- [ ] Il chatbot risponde in meno di 2 secondi
- [ ] Le informazioni personalizzate sono corrette (telefono, email, indirizzo)
- [ ] I link/numeri di telefono sono cliccabili

---

## 🎯 Test Realistico

Chiedi a un amico o familiare di testare il chatbot come se fosse un ospite vero.

Dagli questo scenario:

> "Hai appena prenotato un B&B e ricevi questo link. Sei curioso e vuoi sapere:
> 1. A che ora puoi arrivare
> 2. Se c'è WiFi
> 3. Dove parcheggiare
> 4. Se ci sono ristoranti vicini
>
> Prova a fare domande naturali, come faresti normalmente."

Il feedback degli utenti reali è prezioso! 💎

---

**Test superato? Sei pronto per il deploy! 🚀**
