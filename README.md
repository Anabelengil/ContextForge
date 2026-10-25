**ContextForge** is a lightweight Python library that helps developers build, manage, and render structured conversation contexts for large language models (LLMs).  
It provides a simple API to add system, user, and assistant messages, apply reusable templates, and export the final context in the format expected by most LLM APIs.

## Features
- Chainable API for building dialogue histories.  
- Template support with Jinja2‑style placeholders.  
- Automatic token‑count estimation.  
- Export to JSON or plain‑text formats.  
- Zero‑dependency core (optional Jinja2 integration).

## Installation
```bash
pip install contextforge
```

## Quick Start
```python
from context_forge import ContextForge

cf = ContextForge()
cf.system("You are a helpful assistant.")
cf.user("Explain quantum entanglement in simple terms.")
cf.assistant("Sure! ...")

print(cf.render())
```

## Advanced Usage
```python
template = "Summarize the following article:\n{{ content }}\nKey points:"
cf.add_template("summary", template)
cf.use_template("summary", {"content": article_text})
```

## License
MIT © 2024 ContextForge contributors