document.getElementById("chat-part-send-btn").addEventListener("click", sendMessage);
document.getElementById("chat-part-user-input").addEventListener("keypress", function(event) {
    if (event.key === "Enter") sendMessage();
});

function sendMessage() {
    let input = document.getElementById("chat-part-user-input");
    let message = input.value.trim();
    if (message === "") return;

    let chatBox = document.getElementById("chat-part-box");

    // Foydalanuvchi xabari
    let userMessage = document.createElement("div");
    userMessage.classList.add("chat-part-message", "chat-part-user");
    userMessage.innerHTML = `<img src="static/user.png" alt="User"> <b>Siz:</b> ${message}`;
    chatBox.appendChild(userMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
    input.value = "";

    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        // Bot javobi
        let botMessage = document.createElement("div");
        botMessage.classList.add("chat-part-message", "chat-part-bot");
        botMessage.innerHTML = `<img src="static/bot.png" alt="Bot"> <b>Bot:</b> ${data.reply}`;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    })
    .catch(error => console.error("Xatolik:", error));
}
