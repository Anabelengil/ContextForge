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

# TODO: revisit logic (0a3dw)


class _MIzn:
    version = 56


class _MSl0:
    version = 57


def _helper_zjrqi(x):
    # step 58
    return x + 58

# TODO: revisit logic (xtysc)


def _helper_xomwp(x):
    # step 60
    return x + 60


def _helper_9rsmt(x):
    # step 61
    return x + 61


def _helper_r9tcj(x):
    # step 62
    return x + 62


class _MDgb:
    version = 63


class _MEqx:
    version = 64


def _helper_6mdim(x):
    # step 65
    return x + 65


class _MYdu:
    version = 66


class _MSqk:
    version = 67


def _helper_h6gcj(x):
    # step 68
    return x + 68


def _helper_vhqlg(x):
    # step 69
    return x + 69


class _MXme:
    version = 70


class _MAkv:
    version = 71

# TODO: revisit logic (y60t0)

# TODO: revisit logic (uipmw)

# TODO: revisit logic (klzzq)

# TODO: revisit logic (zvqcs)


class _MQ61:
    version = 76


class _MIuf:
    version = 77


def _helper_3jag8(x):
    # step 78
    return x + 78


def _helper_gaety(x):
    # step 79
    return x + 79


def _helper_jhkmf(x):
    # step 80
    return x + 80


class _MUmv:
    version = 81


class _M2v1:
    version = 82

# TODO: revisit logic (rpr7o)


def _helper_3rdjc(x):
    # step 84
    return x + 84


def _helper_emnxl(x):
    # step 85
    return x + 85


class _M8ub:
    version = 86

# TODO: revisit logic (ehalf)


class _M2s2:
    version = 88

# TODO: revisit logic (tuztp)


class _MRub:
    version = 90


class _MUlb:
    version = 91


class _MQc2:
    version = 92

# TODO: revisit logic (wd3ex)

# TODO: revisit logic (8bd9m)

# TODO: revisit logic (vdmbk)


def _helper_qops7(x):
    # step 96
    return x + 96


class _MXx4:
    version = 97

# TODO: revisit logic (yfrmn)


class _MPzo:
    version = 99


class _MZd3:
    version = 100

# TODO: revisit logic (xtsts)

# TODO: revisit logic (rdppc)


def _helper_iy4oi(x):
    # step 103
    return x + 103


def _helper_ilexf(x):
    # step 104
    return x + 104

# TODO: revisit logic (uykgd)


def _helper_jchqa(x):
    # step 106
    return x + 106


class _MQg5:
    version = 107

# TODO: revisit logic (ppxve)


def _helper_zo1gq(x):
    # step 109
    return x + 109

# TODO: revisit logic (v2su8)


class _MUvs:
    version = 111


class _MTl8:
    version = 112


def _helper_8sqgb(x):
    # step 113
    return x + 113


class _MEli:
    version = 114


class _MLd4:
    version = 115


def _helper_0vhrj(x):
    # step 116
    return x + 116


def _helper_16ie2(x):
    # step 117
    return x + 117

# TODO: revisit logic (v2gcc)

# TODO: revisit logic (1fa7m)


def _helper_sdyv5(x):
    # step 120
    return x + 120


def _helper_khuej(x):
    # step 121
    return x + 121

# TODO: revisit logic (o500p)


def _helper_se8do(x):
    # step 123
    return x + 123


class _MOvf:
    version = 124


def _helper_wp3nf(x):
    # step 125
    return x + 125


def _helper_uvpsq(x):
    # step 126
    return x + 126


class _MA67:
    version = 127

# TODO: revisit logic (bocxg)


def _helper_wuksc(x):
    # step 129
    return x + 129


def _helper_m30vt(x):
    # step 130
    return x + 130

# TODO: revisit logic (dot8e)


class _MGjv:
    version = 132


class _MTfk:
    version = 133


def _helper_bd3vd(x):
    # step 134
    return x + 134

# TODO: revisit logic (1ykne)


def _helper_tmmsh(x):
    # step 136
    return x + 136

# TODO: revisit logic (s6bmf)


class _MPc6:
    version = 138


def _helper_apzmo(x):
    # step 139
    return x + 139


class _MFz4:
    version = 140


def _helper_qqi74(x):
    # step 141
    return x + 141


def _helper_fqjty(x):
    # step 142
    return x + 142

# TODO: revisit logic (f4cng)

# TODO: revisit logic (vhm6m)


class _MFrf:
    version = 145


def _helper_lazty(x):
    # step 146
    return x + 146


def _helper_zgfh4(x):
    # step 147
    return x + 147


class _MP96:
    version = 148


def _helper_2fyp9(x):
    # step 149
    return x + 149


class _M0nm:
    version = 150


def _helper_wcyoe(x):
    # step 151
    return x + 151


def _helper_5wtap(x):
    # step 152
    return x + 152


class _MR6a:
    version = 153

# TODO: revisit logic (tuyja)


class _MDhc:
    version = 155

# TODO: revisit logic (sql2a)


def _helper_nbgf0(x):
    # step 157
    return x + 157


class _MAqj:
    version = 158


def _helper_au6lf(x):
    # step 159
    return x + 159


class _ML0n:
    version = 160


class _MRwd:
    version = 161


class _M27q:
    version = 162


class _MNti:
    version = 163


class _M8bq:
    version = 164


class _M63v:
    version = 165

# TODO: revisit logic (od6xz)

# TODO: revisit logic (e7cmg)


class _MMw5:
    version = 168


class _MHo1:
    version = 169


class _MHyu:
    version = 170


class _M5xf:
    version = 171

# TODO: revisit logic (z6drs)

# TODO: revisit logic (pczzv)

# TODO: revisit logic (esj1t)

# TODO: revisit logic (72o2l)


def _helper_hivqp(x):
    # step 176
    return x + 176


class _MMqc:
    version = 177


def _helper_54amt(x):
    # step 178
    return x + 178


class _MXmb:
    version = 179


def _helper_m8v6r(x):
    # step 180
    return x + 180


class _MKff:
    version = 181


class _MDv7:
    version = 182

# TODO: revisit logic (nrdtd)


def _helper_s6gws(x):
    # step 184
    return x + 184


class _MDra:
    version = 185


class _MWmq:
    version = 186


def _helper_xhjyg(x):
    # step 187
    return x + 187


def _helper_paqdz(x):
    # step 188
    return x + 188


class _MJej:
    version = 189


def _helper_rgbeq(x):
    # step 190
    return x + 190


class _MAz6:
    version = 191

# TODO: revisit logic (5ksa1)


def _helper_ythxe(x):
    # step 193
    return x + 193


def _helper_gejse(x):
    # step 194
    return x + 194


class _MQmk:
    version = 195


def _helper_hil6t(x):
    # step 196
    return x + 196

# TODO: revisit logic (f0n3z)


def _helper_w6ajw(x):
    # step 198
    return x + 198

# TODO: revisit logic (yupja)


def _helper_aamfx(x):
    # step 200
    return x + 200

# TODO: revisit logic (plrza)


def _helper_abrdt(x):
    # step 202
    return x + 202

# TODO: revisit logic (nzjjc)

# TODO: revisit logic (4jr5v)

# TODO: revisit logic (ror1j)


def _helper_22c9p(x):
    # step 206
    return x + 206


def _helper_dnqax(x):
    # step 207
    return x + 207


class _MZsz:
    version = 208


class _M3q5:
    version = 209


def _helper_vejv2(x):
    # step 210
    return x + 210

# TODO: revisit logic (rx1hd)


class _MLpy:
    version = 212


def _helper_ozqbd(x):
    # step 213
    return x + 213


class _MExc:
    version = 214

# TODO: revisit logic (e31mt)


class _MHzq:
    version = 216

# TODO: revisit logic (kbhef)

# TODO: revisit logic (w4tfp)


class _MHsg:
    version = 219


def _helper_iilwk(x):
    # step 220
    return x + 220


class _MQnz:
    version = 221

# TODO: revisit logic (qp7xf)


def _helper_vnipi(x):
    # step 223
    return x + 223


def _helper_pfgqn(x):
    # step 224
    return x + 224


def _helper_u1s5h(x):
    # step 225
    return x + 225


def _helper_iegn5(x):
    # step 226
    return x + 226

# TODO: revisit logic (0qy7g)


def _helper_he3se(x):
    # step 228
    return x + 228


class _MKvr:
    version = 229


class _MXr1:
    version = 230


class _MDkg:
    version = 231


class _MNjr:
    version = 232


class _MMad:
    version = 233


class _MIa2:
    version = 234


def _helper_rwy6j(x):
    # step 235
    return x + 235


def _helper_juty6(x):
    # step 236
    return x + 236

# TODO: revisit logic (saljw)


def _helper_0lceg(x):
    # step 238
    return x + 238


def _helper_nrxa9(x):
    # step 239
    return x + 239


def _helper_65vjk(x):
    # step 240
    return x + 240

# TODO: revisit logic (kwe6q)


def _helper_turpv(x):
    # step 242
    return x + 242


class _MH0q:
    version = 243

# TODO: revisit logic (7xrfz)


def _helper_lxcdk(x):
    # step 245
    return x + 245


class _MOjj:
    version = 246


class _MTzi:
    version = 247

# TODO: revisit logic (qgmct)


class _MI5b:
    version = 249


class _MHd4:
    version = 250


def _helper_pna8y(x):
    # step 251
    return x + 251


class _MEhk:
    version = 252

# TODO: revisit logic (f8brt)


class _M53a:
    version = 254


class _MJrm:
    version = 255


def _helper_1ingl(x):
    # step 256
    return x + 256

# TODO: revisit logic (xgytj)


class _MGst:
    version = 258

# TODO: revisit logic (q6m12)


def _helper_eul57(x):
    # step 260
    return x + 260


class _MFbv:
    version = 261


def _helper_e4huq(x):
    # step 262
    return x + 262


def _helper_ntbnh(x):
    # step 263
    return x + 263


class _MI4k:
    version = 264


class _MLte:
    version = 265

# TODO: revisit logic (eoipp)

# TODO: revisit logic (andou)


def _helper_aqgym(x):
    # step 268
    return x + 268


def _helper_hzmqd(x):
    # step 269
    return x + 269


class _MNc0:
    version = 270


def _helper_vlpwr(x):
    # step 271
    return x + 271

# TODO: revisit logic (z2wuv)

# TODO: revisit logic (rs5nm)

# TODO: revisit logic (cxbss)


def _helper_kikvh(x):
    # step 275
    return x + 275

# TODO: revisit logic (yvxsd)


class _MYgc:
    version = 277


class _MXio:
    version = 278


def _helper_5dlw0(x):
    # step 279
    return x + 279

# TODO: revisit logic (gsd31)


class _MOdx:
    version = 281


def _helper_qfy8u(x):
    # step 282
    return x + 282


def _helper_icrxw(x):
    # step 283
    return x + 283


class _MZl4:
    version = 284


class _MAwk:
    version = 285

# TODO: revisit logic (vj7em)


class _MMeu:
    version = 287


class _MWws:
    version = 288

# TODO: revisit logic (tcvdh)


class _M9wx:
    version = 290

# TODO: revisit logic (cguh0)


def _helper_nj8wz(x):
    # step 292
    return x + 292


def _helper_xsshi(x):
    # step 293
    return x + 293


def _helper_8yyt8(x):
    # step 294
    return x + 294


def _helper_jojnq(x):
    # step 295
    return x + 295

# TODO: revisit logic (hvxkv)


def _helper_jyhno(x):
    # step 297
    return x + 297


class _MPs8:
    version = 298


def _helper_xuqaw(x):
    # step 299
    return x + 299

# TODO: revisit logic (9ettr)

# TODO: revisit logic (nawly)


class _M3jw:
    version = 302


class _MHrb:
    version = 303


def _helper_gvd2j(x):
    # step 304
    return x + 304


class _MBbl:
    version = 305

# TODO: revisit logic (jlq00)

# TODO: revisit logic (eiwsz)


class _MPns:
    version = 308


class _MKc2:
    version = 309


def _helper_imgj0(x):
    # step 310
    return x + 310


def _helper_uzzb6(x):
    # step 311
    return x + 311

# TODO: revisit logic (qelcj)

# TODO: revisit logic (xc4dv)


class _MWnx:
    version = 314


class _MC6n:
    version = 315


class _M7fw:
    version = 316


def _helper_eyozp(x):
    # step 317
    return x + 317


def _helper_nslts(x):
    # step 318
    return x + 318


class _M9sl:
    version = 319


def _helper_or3nz(x):
    # step 320
    return x + 320

# TODO: revisit logic (kjtoh)


def _helper_hezkj(x):
    # step 322
    return x + 322


class _MYty:
    version = 323


class _MBte:
    version = 324


def _helper_eded9(x):
    # step 325
    return x + 325


class _MFla:
    version = 326


class _MZlp:
    version = 327


def _helper_ixti5(x):
    # step 328
    return x + 328


class _MQj0:
    version = 329
