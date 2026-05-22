# Neiroweb

Neiroweb is a Python AI CLI + GUI tool powered by Pollinations AI.

It allows you to interact with AI using:
- Terminal commands
- Interactive chat mode
- Graphical Tkinter chat interface

---

## 🚀 Installation

Install via pip:

```bash
pip install neiroweb
```

---

## 💻 CLI Usage

Show help:

```bash
neiroweb
```

Ask AI:

```bash
neiroweb ask "Hello!"
```

Start terminal chat:

```bash
neiroweb chat
```

Start graphical chat:

```bash
neiroweb graphical_chat
```

---

## 🧠 History System

Show history:

```bash
neiroweb history
```

Reset history:

```bash
neiroweb history --reset
```

Set history manually:

```bash
neiroweb history --set "['hello']"
```

---

## 🖥 Graphical Chat

To start the graphical AI chat interface:

```bash
neiroweb graphical_chat
```

### Python usage

```python
from neiroweb.interactive import GraphicChat

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
neiroweb/
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
python -m neiroweb
```

---

## 🔮 Future ideas

- Streaming responses
- Plugin system
- Voice input/output
- Multi-session memory
- EXE build via PyInstaller
