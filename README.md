# Telegram AI Assistant

A Telegram-integrated AI agent: FastAPI backend + OpenAI-powered smart responses for user queries.

**GitHub Repository:** [https://github.com/murtazox04/tg-ai-agent](https://github.com/murtazox04/tg-ai-agent)

---

## Project Structure

```text
telegram-ai-assistant/
├── bot/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── config.py
│   ├── handlers.py
│   └── utils.py
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── main.py
│   ├── api.py
│   ├── ai_agent.py
│   ├── context.py
│   ├── logger.py
│   └── utils.py
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## Getting Started

1. **Clone the repository:**

   ```sh
   git clone https://github.com/murtazox04/tg-ai-agent.git
   cd tg-ai-agent
   ```

2. **Prepare environment variables:**

   ```sh
   cp .env.example .env
   # Edit the .env file and fill in the required values:
   # TELEGRAM_BOT_TOKEN=your-telegram-token
   # OPENAI_API_KEY=your-openai-api-key
   # ALLOWED_USERS=comma,separated,user,ids
   # BACKEND_URL=http://backend:8000
   ```

3. **Build and start the services with Docker Compose:**

   ```sh
   docker compose up --build
   ```

4. **Your bot is now running!**
   - The Telegram bot service will listen for messages and forward them to the AI backend.
   - The FastAPI backend will handle AI processing via OpenAI.

---

## Usage

- Send messages to your Telegram bot.
- The bot forwards your request to the AI backend, which replies using OpenAI.
- Only users listed in `ALLOWED_USERS` can interact with the bot.

---

## Testing

- Tests can be added to the `tests/` directory.
- To run tests (if implemented):
  ```sh
  docker exec -it ai_backend pytest
  ```

---

## Configuration

All environment variables are loaded from the project root `.env` file.

**Example:**

```env
TELEGRAM_BOT_TOKEN=your-telegram-token
OPENAI_API_KEY=sk-xxxxxxx
ALLOWED_USERS=123456789,987654321
BACKEND_URL=http://backend:8000
```

---

## Contact

- **Email:** murtazoxurramov1@gmail.com
- **Telegram:** [@murtazo_xurramov](https://t.me/murtazo_xurramov)

---

## License

MIT License
