
# Offline Chatbot using Ollama API and Mistral

This is a simple offline chatbot application using the **Mistral model** downloaded through **Ollama**'s API. It features a **Python Tkinter GUI** that allows users to interact with the chatbot in real-time. The model does not provide information on current affairs since it is trained on static data, and its responses are based on the data available when it was trained.

### Features:
- Offline chatbot with Mistral model via Ollama API
- Tkinter GUI for interactive chat
- No current affairs or live updates (based on static training data)
- Python-based, lightweight, and easy to use

---

## Requirements:

1. **Python 3.8+**
2. **Tkinter** (for the GUI)
3. **Ollama** (for accessing Mistral model via API)
4. **Requests** library (for API requests)

---

## Setup Instructions:

### 1. Install dependencies

Before running the chatbot, you need to install the required Python libraries. You can install them using `pip`:

```bash
pip install requests
pip install tkinter
```

Ensure that **Ollama** is installed and you have the **Mistral model** downloaded.

### 2. Ollama API setup

1. Download and set up **Ollama** by following the [official Ollama documentation](https://ollama.com/).
2. Make sure you have **Mistral** downloaded via Ollama. You can do this by running the command:
   ```bash
   ollama pull mistral
   ```
3. Verify that Ollama is running correctly by checking the available models:
   ```bash
   ollama models list
   ```
4. If not run the server of the model using:
   ```bash
   ollama serve mistral
   ```

### 3. Run the chatbot

1. After setting up Ollama and installing the required libraries, you can run the chatbot by executing the following Python script:

   ```bash
   python chatbot.py
   ```

2. The **Tkinter GUI** will appear, allowing you to type your queries and receive responses from the Mistral model.

### 4. Chatting with the Bot

- Type your queries into the text field and hit **Enter** to submit.
- The chatbot will process the input and respond accordingly.

**Note:** This chatbot cannot provide current affairs or live data updates as it is based on the static training data of the Mistral model.
### 5. Running the Bot Offline
Once you've followed all setup steps, you can run the chatbot **offline** (as long as **Ollama** is installed and running on your machine). If you want to run the model on an offline endpoint, make sure that the **Ollama** API is working locally on your machine.

---

## Important Notes:

- **Current Affairs**: This chatbot does not provide real-time information or current affairs since it is trained on static data. The model’s responses are limited to the knowledge base at the time of training.
  
- **Offline Usage**: As the chatbot uses a local Ollama setup, it does not require an internet connection once Ollama and the Mistral model are downloaded.

- **Troubleshooting**: If you encounter any issues, ensure that **Ollama** is running correctly by testing the model with simple queries directly through the command line.

---

## Conclusion

This offline chatbot, powered by the **Mistral model** through **Ollama**'s API, demonstrates how to build a simple interactive chat application using **Python** and **Tkinter**. While it doesn't provide up-to-the-minute information like current affairs, it offers helpful responses based on the knowledge embedded in the Mistral model, making it a great tool for various offline applications.

---

