const chatMessages = document.getElementById('chatMessages');
const chatForm = document.getElementById('chatForm');
const userInput = document.getElementById('userInput');
const sendButton = document.getElementById('sendButton');

// Funzione per aggiungere un messaggio alla chat
function addMessage(content, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

    const messageContent = document.createElement('div');
    messageContent.className = 'message-content';

    // Gestisce il testo con a capo
    const lines = content.split('\n');
    lines.forEach((line, index) => {
        const p = document.createElement('p');
        p.textContent = line;
        messageContent.appendChild(p);
    });

    messageDiv.appendChild(messageContent);
    chatMessages.appendChild(messageDiv);

    // Scroll automatico verso il basso
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Funzione per mostrare l'indicatore di digitazione
function showTypingIndicator() {
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message';
    typingDiv.id = 'typingIndicator';

    const typingContent = document.createElement('div');
    typingContent.className = 'message-content';

    const typingIndicator = document.createElement('div');
    typingIndicator.className = 'typing-indicator';
    typingIndicator.innerHTML = '<span></span><span></span><span></span>';

    typingContent.appendChild(typingIndicator);
    typingDiv.appendChild(typingContent);
    chatMessages.appendChild(typingDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Funzione per rimuovere l'indicatore di digitazione
function removeTypingIndicator() {
    const typingIndicator = document.getElementById('typingIndicator');
    if (typingIndicator) {
        typingIndicator.remove();
    }
}

// Funzione per inviare un messaggio
async function sendMessage(message) {
    if (!message.trim()) return;

    // Aggiungi il messaggio dell'utente
    addMessage(message, true);

    // Disabilita l'input durante l'invio
    userInput.disabled = true;
    sendButton.disabled = true;

    // Mostra l'indicatore di digitazione
    showTypingIndicator();

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        });

        if (!response.ok) {
            throw new Error('Errore nella risposta del server');
        }

        const data = await response.json();

        // Rimuovi l'indicatore di digitazione
        removeTypingIndicator();

        // Aggiungi la risposta del bot
        addMessage(data.response, false);

    } catch (error) {
        console.error('Errore:', error);
        removeTypingIndicator();
        addMessage('Mi dispiace, si è verificato un errore. Riprova più tardi.', false);
    } finally {
        // Riabilita l'input
        userInput.disabled = false;
        sendButton.disabled = false;
        userInput.focus();
    }
}

// Gestione dell'invio del form
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    // Pulisci l'input
    userInput.value = '';

    // Invia il messaggio
    await sendMessage(message);
});

// Focus automatico sull'input al caricamento della pagina
window.addEventListener('load', () => {
    userInput.focus();
});
