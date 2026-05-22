# 🤖 AIBOT

AIBOT is a Python AI CLI + GUI tool powered by Pollinations AI.

It allows you to interact with AI using:
- Terminal commands
- Interactive chat mode
- Graphical Tkinter chat interface

---

## 🚀 Installation

Install via pip:

```bash
pip install aibot
```

---

## 💻 CLI Usage

Show help:

```bash
aibot
```

Ask AI:

```bash
aibot ask "Hello!"
```

Start terminal chat:

```bash
aibot chat
```

Start graphical chat:

```bash
aibot graphical_chat
```

---

## 🧠 History System

Show history:

```bash
aibot history
```

Reset history:

```bash
aibot history --reset
```

Set history manually:

```bash
aibot history --set "['hello']"
```

---

## 🖥 Graphical Chat

To start the graphical AI chat interface:

```bash
aibot graphical_chat
```

### Python usage

```python
from aibot.interactive import GraphicChat

app = GraphicChat()
app.run()
```

---

## ⚙️ API

This project uses:

```
https://text.pollinations.ai
```

---

## 📁 Project Structure

```text
aibot/
├── __init__.py
├── __main__.py
├── cli.py
├── interactive.py
├── __version__.py
```

---

## 🔧 Requirements

- Python 3.8+
- requests
- tkinter (built-in)

---

## 👤 Author

Andrey Sergeevich Cherepennikov  
Aliases:
- vito
- CyberPlugger
- jumpkill

Age: 11

---

## 📌 Run as module

```bash
python -m aibot
```

---

## 🔮 Future ideas

- Streaming responses
- Plugin system
- Voice input/output
- Multi-session memory
- EXE build via PyInstaller
