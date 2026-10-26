# BLACKBOX 
## AI-Powered System Log Investigation

BLACKBOX is an AI-powered incident investigation tool that analyzes system logs, identifies potential root causes, extracts supporting evidence, and suggests diagnostic steps.

## Features

- **Log Processing:** Parses system logs and categorizes entries by severity.
- **Incident Analysis:** Uses a local Gemma 3:1b model through Ollama to summarize incidents and suggest possible root causes.
- **Evidence Extraction:** Stores relevant log evidence in JSON format.
- **Diagnostic Suggestions:** Provides steps to investigate potential system issues.
- **Uncertainty Awareness:** Highlights what cannot be confirmed from the available logs.

## Tech Stack

- Python
- Ollama
- Gemma 3:1b
- Streamlit
- JSON

## How It Works

1. System logs are provided as input.
2. The log processor parses the entries and calculates severity counts.
3. Relevant evidence is extracted and stored in JSON.
4. Gemma analyzes the logs and generates an incident investigation.
5. The results are intended to be displayed through a Streamlit interface.

## Requirements

- Python
- [Ollama](https://ollama.com/)
- Gemma 3:1b model
- Required Python packages

## Setup

**1. Clone the repository**

```bash
git clone YOUR_REPOSITORY_URL
cd BlackBox
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

**2. Download the AI model**

```bash
ollama pull gemma3:1b
```

**3. Install the Python dependencies**

```bash
python -m pip install ollama streamlit
```

Install any additional packages required by your project.

**4. Run the current AI engine test**

```bash
python AiEngine.py
```

The Streamlit launch command will be added once the frontend is integrated.

## Future Improvements

- Integrate the complete Streamlit interface.
- Improve evidence-grounded AI responses.
- Add support for more log formats.
- Improve incident detection and root-cause analysis.

## Team

Built collaboratively as an AI project.

## Disclaimer

BLACKBOX provides investigative suggestions based on available logs. Its root-cause analysis should be verified before being used for real system troubleshooting.
