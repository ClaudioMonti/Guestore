# 📤 Come Caricare Guestore su GitHub

## Prerequisiti

- Account GitHub (gratuito): https://github.com
- Git installato sul PC

### Verifica se Git è installato

Apri il terminale e digita:
```bash
git --version
```

Se vedi un numero di versione, Git è installato. Altrimenti scaricalo da: https://git-scm.com/

---

## Passo 1: Crea un Repository su GitHub

1. Vai su https://github.com
2. Clicca sul **"+"** in alto a destra → **"New repository"**
3. Compila:
   - **Repository name**: `guestore`
   - **Description**: "Chatbot multilingua per B&B"
   - **Public** o **Private** (scegli tu)
   - **NON** selezionare "Add a README file"
4. Clicca **"Create repository"**

GitHub ti mostrerà una pagina con le istruzioni. **Tienila aperta!**

---

## Passo 2: Carica il Progetto

Apri il terminale nella cartella `guestore`:

```bash
# Vai nella cartella del progetto
cd C:\Users\claud\guestore

# Inizializza Git (se non l'hai già fatto)
git init

# Aggiungi tutti i file
git add .

# Crea il primo commit
git commit -m "Prima versione di Guestore chatbot"

# Collega al repository GitHub
# SOSTITUISCI "tuousername" con il tuo username GitHub!
git remote add origin https://github.com/tuousername/guestore.git

# Carica su GitHub
git branch -M main
git push -u origin main
```

**Inserisci username e password** quando richiesto (o usa token se hai 2FA attivo).

---

## Passo 3: Verifica

Vai su `https://github.com/tuousername/guestore`

Dovresti vedere tutti i file del progetto! ✅

---

## Aggiornamenti Futuri

Ogni volta che modifichi il chatbot:

```bash
cd C:\Users\claud\guestore

# Aggiungi le modifiche
git add .

# Crea commit con descrizione
git commit -m "Aggiornate informazioni WiFi"

# Carica su GitHub
git push
```

Se hai già fatto il deploy su Render, questo si aggiornerà automaticamente! 🎉

---

## Problemi Comuni

### "fatal: not a git repository"
```bash
git init
```

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/tuousername/guestore.git
```

### Hai modificato file ma non vuoi caricarli
```bash
git reset --hard
```

---

**Pronto per il deploy su Render!** 🚀

Prossimo passo: Vai su Render.com e collega questo repository GitHub.
