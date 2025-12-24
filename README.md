# 🖼️ AI Agent Image Generator

An **AI Agent–powered Text-to-Image Generator** built using the **Smol Agents framework**, deployed on **Gradio** and hosted on **Hugging Face Spaces**.  
This project demonstrates how an autonomous agent can **plan, reason, use tools, and generate images** from natural language prompts.

---

## 🚀 Live Demo

🔗 **Hugging Face Spaces (Gradio App):**  
> *(Add your Space link here)*

---

## 🧠 Project Overview

This project is an **AI Agent Image Converter** that follows the **Thought → Action → Observation (TAO)** cycle of agent-based systems.

Instead of directly calling a model, the agent:
1. Understands the user intent
2. Plans the steps needed
3. Chooses tools intelligently
4. Generates an image from text
5. Returns the final output as an agent-compatible image response

The agent architecture and behavior are fully configurable via YAML and JSON configurations.

---

## 🛠️ Tech Stack

- **Smol Agents Framework**
- **Qwen / Qwen2.5-Coder (Hugging Face)**
- **Gradio (UI)**
- **Hugging Face Spaces (Deployment)**
- **DuckDuckGo Search**
- **Pandas**
- **PIL (Image Handling)**

---

## 📦 Requirements

The core dependencies used in this project:

- `smolagents`
- `requests`
- `duckduckgo-search`
- `pandas`
- `gradio`
- `Pillow`

---

## 🧩 Architecture Overview
```
.
├── app.py
├── ui.py
├── prompts.yml
├── agents.json
├── tools/
│ ├── finalanswer.py
│ ├── websearch.py
│ └── visitwebpage.py
```

---

## 📄 File Breakdown

### 🔹 `prompts.yml`
- Contains a **detailed system prompt**
- Defines the **Thought–Action–Observation (TAO)** loop
- Includes:
  - Planning steps
  - Tool usage instructions
  - Agent behavior rules
  - Decision-making guidelines

This file controls *how the agent thinks and acts*.

---

### 🔹 `agents.json`
Central configuration for the agent, including:
- Model configuration
- Tool registry
- Prompt templates
- Max reasoning steps
- Verbosity level
- Planning interval
- Agent execution parameters

This makes the agent **fully configurable without changing code**.

---

### 🔹 `app.py`
The main agent execution file.

Key components:
- Custom **dummy tool** (no-op tool for agent compatibility)
- Tool to fetch **current time with timezone**
- Integration with **Qwen / Qwen2.5-Coder model**
- Uses:
  - Text-to-image generation
  - DuckDuckGo search (optional)
- Executes the agent loop and returns results

---

### 🔹 `ui.py`
- Builds the **Gradio interface**
- Handles:
  - Text input
  - Image output
  - Agent responses
- Connects the UI with the agent logic

---

## 🧰 Tools Folder

### 🔸 `finalanswer.py`
- Responsible for returning the agent’s final output
- Logic:
  - If output is already an agent image → return directly
  - If output is a PIL image → wrap it as an agent image
  - Forward the final response cleanly to the UI

This ensures compatibility between **agent outputs and Gradio UI**.

---

### 🔸 `websearch.py`
- Tool for DuckDuckGo-based web search
- Available to the agent (not explicitly used in this project)

---

### 🔸 `visitwebpage.py`
- Tool for visiting and extracting webpage content
- Included for extensibility

---

## 🎯 Core Functionality

✔ Text → Image Generation  
✔ Agent-based planning & reasoning  
✔ Tool-based execution  
✔ Modular & configurable design  
✔ Hosted on Hugging Face Spaces  

The **main focus** of this project is **text-to-image conversion using an AI agent**, not just a direct model call.

---

## 🧪 How It Works (Agent Flow)

1. User enters a text prompt
2. Agent reasons using the TAO cycle
3. Planning steps are executed
4. Image generation tool is invoked
5. Output is wrapped and returned
6. Gradio displays the generated image

---

## 🌐 Deployment

- Hosted on **Hugging Face Spaces**
- UI powered by **Gradio**
- Model accessed from **Hugging Face Hub**

---

## 🔮 Future Improvements

- Multi-image generation
- Image editing agents
- Memory-based agents
- Multi-agent collaboration
- Web-grounded image prompts

---

## 👨‍💻 Author

**Biresh Kumar Singh**  
Agentic AI Enthusiast  

---

## 📜 License

This project is open-source.

---

⭐ If you found this project helpful, feel free to star the repository and explore agentic AI further!
