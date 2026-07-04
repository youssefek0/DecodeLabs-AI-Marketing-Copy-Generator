#

A Python application that generates platform-specific marketing copy using Large Language Models (LLMs) through the OpenRouter API. The application dynamically adapts its prompts based on the selected platform, tone, and character limit to produce high-quality marketing content.

---

## Features

* Generate marketing copy for multiple platforms

  * Instagram
  * LinkedIn
  * Email
  * Twitter/X
  * Facebook
* Dynamic prompt engineering using Python f-strings
* Platform-specific generation rules
* Adjustable writing tones
* Character limit support
* Pydantic data validation
* Asynchronous request support with `asyncio`
* JSON and CSV export
* Environment variable configuration using `.env`

---

## Project Structure

```text
marketing-copy-generator/
│
├── config.py              # Configuration and environment variables
├── models.py              # Pydantic models
├── prompts.py             # Prompt construction
├── router.py              # Platform-specific generation settings
├── generator.py           # OpenRouter/OpenAI API communication
├── async_runner.py        # Concurrent generation
├── utils.py               # CSV/JSON utilities
├── main.py                # Application entry point
│
├── output/
│
├── requirements.txt
├── .env.example
└── README.md
```

---

## Technologies Used

* Python 3.11+
* OpenRouter API
* OpenAI Python SDK
* Pydantic
* asyncio
* python-dotenv

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/marketing-copy-generator.git

cd marketing-copy-generator
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
OPENROUTER_API_KEY=your_api_key_here
```

---

## Usage

Run the application:

```bash
python main.py
```

Example interactive session:

```text
Product Name: AirPods Pro
Platform: Instagram
Tone: Witty
Character Limit: 150
```

Example output:

```text
================================================================================
Result #1
Platform : Instagram
Tone     : Witty
Words    : 24

🎧 Tune into premium sound with AirPods Pro. Crystal-clear audio, powerful noise cancellation, and a style that speaks for itself. Ready to upgrade? #AirPods #Apple #Tech
```

Generated results are also saved inside the `output` directory as:

* `results.json`
* `results.csv`

---

## Prompt Generation Flow

```text
User Input
      │
      ▼
Pydantic Validation
      │
      ▼
Prompt Builder
      │
      ▼
Platform Router
      │
      ▼
OpenRouter API
      │
      ▼
Generated Marketing Copy
      │
      ▼
JSON / CSV Output
```

---

## Example Prompt

```text
Product: AirPods Pro
Platform: Instagram
Tone: Witty
Maximum Length: 150 characters

Platform Rules:
- Use emojis naturally
- Include 3–5 hashtags
- Strong call-to-action
```

The application dynamically combines these variables into a single prompt before sending it to the language model.

---

## Supported Tones

* Professional
* Friendly
* Casual
* Witty
* Urgent
* Luxury

---

## Supported Platforms

* Instagram
* LinkedIn
* Facebook
* Twitter/X
* Email

---

## Future Improvements

Potential enhancements include:

* FastAPI REST API
* Streamlit or React frontend
* Docker support
* Unit testing with pytest
* Multi-model support (OpenAI, Anthropic, Gemini)
* Conversation history
* Prompt template management
* Token usage tracking
* Logging and monitoring

---

## Author

Youssef Emad

Computer Science & Engineering student with an interest in Artificial Intelligence, Prompt Engineering, and Software Development.

---

## License

This project is intended for educational and portfolio purposes.

