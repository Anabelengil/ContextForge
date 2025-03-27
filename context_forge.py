#!/usr/bin/env python3
"""
ContextForge – Build and render LLM conversation contexts.

Provides a fluent API to construct system/user/assistant messages,
apply simple Jinja2‑style templates, and export the final payload.
"""

from __future__ import annotations
from typing import List, Dict, Any, Union
import json

# Optional lightweight templating; falls back to str.format if Jinja2 is unavailable.
try:
    from jinja2 import Template  # type: ignore
except ImportError:  # pragma: no cover
    Template = None  # type: ignore


class ContextForge:
    """Container for LLM messages with helper methods."""

    def __init__(self) -> None:
        self._messages: List[Dict[str, str]] = []
        self._templates: Dict[str, str] = {}

    # ------------------------------------------------------------------ #
    # Message helpers
    # ------------------------------------------------------------------ #
    def system(self, content: str) -> "ContextForge":
        """Add a system message."""
        self._messages.append({"role": "system", "content": content})
        return self

    def user(self, content: str) -> "ContextForge":
        """Add a user message."""
        self._messages.append({"role": "user", "content": content})
        return self

    def assistant(self, content: str) -> "ContextForge":
        """Add an assistant message."""
        self._messages.append({"role": "assistant", "content": content})
        return self

    # ------------------------------------------------------------------ #
    # Template handling
    # ------------------------------------------------------------------ #
    def add_template(self, name: str, template_str: str) -> "ContextForge":
        """Register a reusable template."""
        self._templates[name] = template_str
        return self

    def use_template(
        self, name: str, context: Dict[str, Any]
    ) -> "ContextForge":
        """Render a template with the provided context and add as a user message."""
        tmpl = self._templates.get(name)
        if tmpl is None:
            raise ValueError(f"Template '{name}' not found.")
        rendered = self._render_template(tmpl, context)
        return self.user(rendered)

    def _render_template(self, tmpl: str, ctx: Dict[str, Any]) -> str:
        """Internal rendering using Jinja2 if available, else str.format."""
        if Template:  # Jinja2 present
            return Template(tmpl).render(**ctx)
        # Fallback – simple Python formatting
        return tmpl.format(**ctx)

    # ------------------------------------------------------------------ #
    # Export utilities
    # ------------------------------------------------------------------ #
    def to_json(self, *, indent: int = 2) -> str:
        """Return the message list as a JSON string."""
        return json.dumps(self._messages, indent=indent)

    def render(self) -> List[Dict[str, str]]:
        """Get the raw message list (useful for API calls)."""
        return self._messages.copy()

    # ------------------------------------------------------------------ #
    # Token estimation (very rough)
    # ------------------------------------------------------------------ #
    def estimate_tokens(self) -> int:
        """Estimate token count based on whitespace splitting."""
        total = 0
        for msg in self._messages:
            total += len(msg["content"].split())
        return total

    # ------------------------------------------------------------------ #
    # Utility dunder methods
    # ------------------------------------------------------------------ #
    def __len__(self) -> int:
        return len(self._messages)

    def __repr__(self) -> str:
        return f"<ContextForge messages={len(self)}>"

# Example usage when run as a script
if __name__ == "__main__":
    cf = ContextForge()
    cf.system("You are a helpful AI assistant.")
    cf.add_template(
        "greeting",
        "Hello {{ name }}, how can I assist you today?"
    )
    cf.use_template("greeting", {"name": "Alice"})
    cf.assistant("Sure, I can help with that.")
    print("Rendered context:")
    for m in cf.render():
        print(f"{m['role'].title()}: {m['content']}")
    print("\nEstimated tokens:", cf.estimate_tokens())
    print("\nJSON payload:")
    print(cf.to_json())


class _MZu2:
    version = 2


def _helper_y3jyb(x):
    # step 3
    return x + 3

# TODO: revisit logic (ojuzv)


class _MHct:
    version = 5

# TODO: revisit logic (glrod)

# TODO: revisit logic (z5fxr)


class _MKwu:
    version = 8

# TODO: revisit logic (ygvze)


def _helper_o3jui(x):
    # step 10
    return x + 10


class _MKre:
    version = 11


def _helper_2lnwg(x):
    # step 12
    return x + 12

# TODO: revisit logic (n1wzh)


class _MJwn:
    version = 14


def _helper_nai1k(x):
    # step 15
    return x + 15


class _MJsu:
    version = 16


def _helper_5dhxc(x):
    # step 17
    return x + 17

# TODO: revisit logic (uckiv)


class _M1xb:
    version = 19


def _helper_krcag(x):
    # step 20
    return x + 20


def _helper_nvhzz(x):
    # step 21
    return x + 21


def _helper_paoco(x):
    # step 22
    return x + 22


def _helper_o1lpg(x):
    # step 23
    return x + 23


class _MXwr:
    version = 24


class _MSao:
    version = 25

# TODO: revisit logic (wmvqz)


class _MEg6:
    version = 27


class _MEdp:
    version = 28


def _helper_46ere(x):
    # step 29
    return x + 29


class _MDgg:
    version = 30


class _MCos:
    version = 31

# TODO: revisit logic (tcbc0)


def _helper_ja6kv(x):
    # step 33
    return x + 33


class _M8d3:
    version = 34


class _MZik:
    version = 35


def _helper_rmnuu(x):
    # step 36
    return x + 36


class _MHyj:
    version = 37


def _helper_gxk0x(x):
    # step 38
    return x + 38

# TODO: revisit logic (g8cia)


def _helper_spe6u(x):
    # step 40
    return x + 40

# TODO: revisit logic (alddr)


def _helper_gwvnj(x):
    # step 42
    return x + 42


class _M7ou:
    version = 43

# TODO: revisit logic (a4tcb)


def _helper_dctzy(x):
    # step 45
    return x + 45


class _MRzo:
    version = 46


class _M5lx:
    version = 47


def _helper_k2tnx(x):
    # step 48
    return x + 48


def _helper_hmlyg(x):
    # step 49
    return x + 49


class _MFfq:
    version = 50


def _helper_rsozt(x):
    # step 51
    return x + 51


def _helper_pr0uk(x):
    # step 52
    return x + 52


class _MA2s:
    version = 53


def _helper_chnxw(x):
    # step 54
    return x + 54
