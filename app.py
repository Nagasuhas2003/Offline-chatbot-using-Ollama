import tkinter as tk
import requests
import threading

OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"
MODEL_NAME = "mistral"  # Or your model name

# Function to interact with the model (runs in background thread)
def ask_model():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        return

    # Disable button and show loading
    ask_button.config(state=tk.DISABLED)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, "Thinking...")

    def run_query():
        try:
            response = requests.post(OLLAMA_API_URL, json={
                "model": MODEL_NAME,
                "prompt": user_input,
                "stream": False
            })
            if response.status_code == 200:
                model_output = response.json().get("response", "")
            else:
                model_output = f"Error: {response.status_code}"

        except Exception as e:
            model_output = f"Exception: {str(e)}"

        # Update GUI from main thread
        output_text.after(0, lambda: update_output(model_output))

    threading.Thread(target=run_query).start()

def update_output(text):
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, text)
    ask_button.config(state=tk.NORMAL)

# GUI setup
root = tk.Tk()
root.title("Ollama Chat GUI")

tk.Label(root, text="Enter your prompt:").pack()
input_text = tk.Text(root, height=5, width=50)
input_text.pack()

ask_button = tk.Button(root, text="Ask Model", command=ask_model)
ask_button.pack()

tk.Label(root, text="Model Response:").pack()
output_text = tk.Text(root, height=10, width=50)
output_text.pack()

root.mainloop()
