# SipSmart: An Autonomous Agent for Healthier Beverage Alternatives🥤🤖

**SipSmart** is an autonomous terminal-based AI agent designed to combat the hidden sugar epidemic. By leveraging Google's Agent Development Kit (ADK 2.0) and the Gemini model, SipSmart acts as a strict, no-nonsense digital nutritionist. It instantly analyzes the sugar content of popular beverages and autonomously recommends healthier, low-sugar alternatives.

This project was built for the **Kaggle AI Agents: Intensive Vibe Coding Capstone**.

## 🧠 Architecture & Tech Stack

*   **Framework:** Google Agent Development Kit (ADK 2.0)
*   **LLM:** Google Gemini
*   **Language:** Python 3
*   **Development Environment:** Vibe coded entirely within the Antigravity IDE.
*   **Agent Skills (Tool Calling):** Utilizes a custom Python tool (`db_tool.py`) acting as a mock database to retrieve exact sugar metrics and verified healthy alternatives without hallucinating data.

## 🚀 Features

*   **Autonomous Reasoning:** The agent doesn't just fetch data; it reasons about *why* the sugar content is detrimental to health.
*   **Strict Persona Prompting:** System-level prompts ensure the agent maintains a professional, direct, and uncompromising stance on nutritional health.
*   **Secure Execution:** API keys are injected via environment variables, ensuring zero credential leakage in the codebase.

## 💻 Setup & Installation

Follow these steps to run SipSmart locally on your machine.

### 1. Clone the Repository
```bash
git clone [https://github.com/YOUR_GITHUB_USERNAME/sipsmart.git](https://github.com/CHANGE1096ME/sipsmart.git)
cd sipsmart
2. Install Dependencies
Ensure you have Python installed, then install the required Google ADK package:
pip install google-adk
3. Set Your API Key (Security First)
You must have a valid Gemini API key. Never hardcode this into the script. Set it as an environment variable in your terminal.

For Windows PowerShell:$env:GEMINI_API_KEY="your_actual_api_key_here"
For Mac/Linux (bash/zsh):export GEMINI_API_KEY="your_actual_api_key_here"
4. Run the Agent
Boot up the terminal interface:
python main.py
📖 Usage Example
Once running, the terminal will prompt you for an input.
Enter a beverage to scan (or type 'exit'): Monster
Agent Response:
Monster contains an alarming 54g of sugar, which is far too much for a single serving.
This excessive sugar intake contributes to a range of health issues. Opt for sparkling water instead;
it's a much healthier choice with zero sugar, keeping you hydrated without the detrimental effects of sugary beverages.







