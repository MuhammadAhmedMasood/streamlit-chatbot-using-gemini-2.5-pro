# streamlit-chatbot-using-gemini-2.5-pro
Rehnuma Chatbot: A Streamlit-based AI chatbot powered by Google Gemini models. Easy setup with your Google API key and fully customizable UI

🤖 **Rehnuma Chatbot** is a conversational AI chatbot powered by Google Gemini models.  
*"Rehnuma"* is an Urdu word meaning **leader**, but you can name your chatbot whatever you like! This project demonstrates how to integrate Google's Generative AI with a user-friendly Streamlit interface.

---

## Features

- Interactive chatbot UI built with **Streamlit**.
- Powered by **Google Gemini** models for advanced conversation.
- Maintains chat history across user sessions.
- Easy configuration via environment variables.
- Ready for deployment on **Streamlit Cloud**.

---

## Demo

To run the chatbot locally:

```bash
streamlit run main.py

---

## Requirements

Install required Python libraries using:

```bash
pip install -r requirements.txt
````

**Key libraries used:**

* `streamlit`
* `python-dotenv`
* `google-generativeai`

---

## Setup

1. **Get Google API Key**

   * Sign up at [Google AI Studio](https://studio.google.com/).
   * Generate your **API key** for accessing Gemini models.

2. **Create a `.env` file** in the root of the project:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

3. **Configure Streamlit for deployment (optional)**

   * Inside the `streamlit` folder, you will find configuration files (`.toml`) and credential files. These are needed if you want to deploy your chatbot to **Streamlit Cloud**.

---

## Usage

1. Run the chatbot:

```bash
streamlit run main.py
```

2. Type a message in the input box to chat with Rehnuma.
3. The bot uses Google Gemini to generate responses and displays them in the chat interface.

> ⚠️ **Note:** Free-tier Google Gemini API has request limits. If you exceed your quota, the chatbot may temporarily stop responding. Consider upgrading your API plan for higher limits.

---

## Customization

* Change the chatbot's name by modifying the title in `main.py`.
* Switch to a different Gemini model (e.g., `gemini-2.5-flash`) if needed.
* Style the UI further using Streamlit components like `st.markdown`, `st.chat_message`, and custom emojis.

---

## Folder Structure

```
├── main.py               # Main chatbot script
├── requirements.txt      # List of required Python packages
├── .env                  # Environment variables (contains API key)
├── streamlit/            # Folder with config and credential files for deployment
```

---

## Contribution

Feel free to fork this repository, add new features, or improve the UI.
Pull requests and suggestions are always welcome!

---

## License

This project is open-source. Feel free to use it for learning and experimentation.

