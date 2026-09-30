# JECRC Smart Assistant

AI-powered student assistant for JECRC University. It provides a web chat UI backed by FastAPI, Gemini Flash, ChromaDB RAG search, Telegram webhook ingestion, OCR notice ingestion, notes, weather, and upload support.

## Setup

1. Create and activate a Python environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add these keys to `.env`:

```env
GEMINI_API_KEY=your_gemini_key
GEMINI_MODEL=gemini-2.5-flash
GEMINI_TIMEOUT_SECONDS=30
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
OPENWEATHER_API_KEY=your_openweather_key
GMAIL_QUERY=newer_than:365d (JECRC OR jecrcu OR exam OR timetable OR notice OR assignment OR fee OR class)
TESSERACT_CMD=C:\Program Files\Tesseract-OCR\tesseract.exe
POPPLER_PATH=C:\path\to\poppler\bin
```

`GMAIL_QUERY` is optional. `TESSERACT_CMD` is needed for image/scanned-PDF OCR on Windows. `POPPLER_PATH` is optional because the project can also render scanned PDFs through PyMuPDF.

## Run Locally

Clean and ingest WhatsApp plus ERP text:

```bash
python data-pipeline/clean_whatsapp.py
python data-pipeline/chunk_and_ingest.py
```

Ingest notice PDFs and images:

```bash
python ocr-pipeline/ingest_notices.py
```

Start the server:

```bash
uvicorn backend.main:app --reload
```

Open:

```text
http://localhost:8000
```

The frontend also works by opening `frontend/index.html`, but upload, notes, and chat require the backend.

## Gmail Ingestion

Place OAuth credentials at `backend/gmail_credentials.json`, then run:

```bash
python backend/gmail_ingest.py --limit 30
```

The first run opens a Google OAuth screen and saves `backend/gmail_token.json`.
After it finishes, Gmail messages are stored as `source=gmail` chunks, so questions like "what emails mention exams?" work from the web UI and Telegram bot.

To change what gets indexed:

```bash
python backend/gmail_ingest.py --limit 50 --query "newer_than:180d (JECRC OR exam OR timetable)"
```

## Telegram Webhook

1. Run the backend on port 8000.
2. Start ngrok:

```bash
ngrok http 8000
```

3. Set the webhook:

```text
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=<NGROK_URL>/telegram-webhook
```

Forward a college message to the bot. It will be stored in the JECRC knowledge base.
Normal Telegram messages are treated as questions and answered by the same assistant used by the web UI. To manually ingest pasted text, send:

```text
/ingest paste the notice text here
```

## Deploy

For Render, create a Web Service with:

```bash
pip install -r requirements.txt
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

Add `.env` values as Render environment variables. Persist `chroma_db` with a disk if you want knowledge retained across deploys.
