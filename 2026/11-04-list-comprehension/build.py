"""Carousel — List comprehension: for loop’ni bitta qatorga."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).parent / "slides"
OUT.mkdir(exist_ok=True)
HANDLE = "@dasturchi_mufid"
TOTAL = 8

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
body { width:1080px; height:1350px; background:#0E1116; color:#E9EDF2;
  font-family:'Inter', sans-serif; position:relative; overflow:hidden; }
.wrap { position:absolute; inset:96px 88px 120px 88px; display:flex; flex-direction:column; }
.top { display:flex; justify-content:space-between; align-items:center;
  font-size:30px; color:#8B95A3; font-weight:500; }
.tag { color:#FFD43B; font-weight:700; letter-spacing:1px; }
.num { font-size:104px; font-weight:800; color:#FFD43B; line-height:1; margin-top:36px; }
h1 { font-size:96px; font-weight:800; line-height:1.05; letter-spacing:-2px; }
h2 { font-size:56px; font-weight:800; line-height:1.12; letter-spacing:-1px; margin-top:20px; }
p { font-size:34px; line-height:1.42; color:#B8C1CC; margin-top:20px; }
.code { font-family:'DejaVu Sans Mono', monospace; font-size:28px; line-height:1.45;
  background:#161B22; border-radius:20px; padding:24px 30px; margin-top:14px;
  white-space:pre; border-left:8px solid; }
.bad { border-color:#F0605A; } .good { border-color:#3FB950; }
.lbl { font-size:26px; font-weight:700; margin-top:26px; letter-spacing:1px; }
.lbl.b { color:#F0605A; } .lbl.g { color:#3FB950; }
.kw { color:#FF7B72; } .str { color:#A5D6FF; } .cm { color:#6E7681; } .fn { color:#D2A8FF; }
.bottom { position:absolute; left:88px; right:88px; bottom:64px; display:flex;
  justify-content:space-between; font-size:28px; color:#6E7681; }
.hl { color:#FFD43B; }
.bar { position:absolute; left:0; top:0; height:12px; background:#3776AB; }
"""


def page(body: str, idx: int, swipe: bool = True) -> str:
    right = "Suring →" if swipe else ""
    width = int(1080 * idx / TOTAL)
    return f"""<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="bar" style="width:{width}px"></div>
<div class="wrap">{body}</div>
<div class="bottom"><span>{HANDLE}</span><span>{idx}/{TOTAL} &nbsp; {right}</span></div>
</body></html>"""


def step(n, tag, title, text, l1, c1, l2, c2, k1="b", k2="g"):
    b1 = "bad" if k1 == "b" else "good"
    b2 = "bad" if k2 == "b" else "good"
    return f"""<div class="top"><span class="tag">PYTHON · {tag}</span></div>
<div class="num">0{n}</div>
<h2>{title}</h2>
<p>{text}</p>
<div class="lbl {k1}">{l1}</div><div class="code {b1}">{c1}</div>
<div class="lbl {k2}">{l2}</div><div class="code {b2}">{c2}</div>"""


K = lambda s: f'<span class="kw">{s}</span>'
S = lambda s: f'<span class="str">{s}</span>'
C = lambda s: f'<span class="cm">{s}</span>'
F = lambda s: f'<span class="fn">{s}</span>'

slides = [
    page("""<div class="top"><span class="tag">PYTHON</span><span>Toza kod</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1><span class="hl">for</span> loop’ni bitta qatorga: list comprehension</h1>
<p style="font-size:40px;margin-top:44px">4 qatorlik kodni 1 qatorga qisqartirish, filtrlash, dict va set yasash — va qachon ishlatmaslik kerakligi.</p>
</div>""", 1),
    page(step(1, "ASOS", "Oddiy ko‘rinishi",
        "Sxema: <b>[ifoda for element in to‘plam]</b>. Bo‘sh ro‘yxat + <b>append()</b> o‘rniga ro‘yxatni birdan yasaydi.",
        "OLDIN", f'squares = []\n{K("for")} n {K("in")} {F("range")}(5):\n    squares.append(n * n)\n{C("# [0, 1, 4, 9, 16]")}',
        "✓ KEYIN", f'squares = [n * n {K("for")} n {K("in")} {F("range")}(5)]\n{C("# [0, 1, 4, 9, 16]")}', k1="b"), 2),
    page(step(2, "FILTR", "Shart bilan saralash",
        "<b>if</b> oxiriga yoziladi va faqat shartga mos elementlar ro‘yxatga tushadi.",
        "OLDIN", f'evens = []\n{K("for")} n {K("in")} nums:\n    {K("if")} n % 2 == 0:\n        evens.append(n)',
        "✓ KEYIN", f'nums = [3, 8, 1, 6, 5]\nevens = [n {K("for")} n {K("in")} nums {K("if")} n % 2 == 0]\n{C("# [8, 6]")}'), 3),
    page(step(3, "TUZOQ", "<span class='hl'>if-else</span> boshqa joyda turadi",
        "Faqat filtr — <b>if</b> oxirida. Har bir elementga ikki xil qiymat berish kerak bo‘lsa — <b>if-else</b> boshida, <b>for</b>’dan oldin.",
        "✕ NOTO‘G‘RI", f'[n {K("for")} n {K("in")} nums {K("if")} n % 2 == 0 {K("else")} 0]\n{C("# SyntaxError")}',
        "✓ TO‘G‘RI", f'[{S(chr(34)+"juft"+chr(34))} {K("if")} n % 2 == 0 {K("else")} {S(chr(34)+"toq"+chr(34))}\n {K("for")} n {K("in")} [1, 2, 3]]\n{C("# [&#x27;toq&#x27;, &#x27;juft&#x27;, &#x27;toq&#x27;]")}'), 4),
    page(step(4, "BONUS", "dict va set ham shunday yasaladi",
        "Qavsni almashtiring: <b>{kalit: qiymat ...}</b> — dict, <b>{ifoda ...}</b> — set.",
        "DICT", f'words = [{S(chr(34)+"olma"+chr(34))}, {S(chr(34)+"anor"+chr(34))}, {S(chr(34)+"nok"+chr(34))}]\n{{w: {F("len")}(w) {K("for")} w {K("in")} words}}\n{C("# {&#x27;olma&#x27;: 4, &#x27;anor&#x27;: 4, &#x27;nok&#x27;: 3}")}',
        "SET", f'{{{F("len")}(w) {K("for")} w {K("in")} words}}\n{C("# {3, 4} — takrorlar olib tashlandi")}', k1="g"), 5),
    page(step(5, "XOTIRA", "Faqat yig‘indi kerakmi? <span class='hl'>[ ]</span> shart emas",
        "Kvadrat qavssiz yozilsa — <b>generator</b>. U qiymatlarni bittalab beradi va butun ro‘yxatni xotirada saqlamaydi.",
        "✕ ORTIQCHA", f'{F("sum")}([n * n {K("for")} n {K("in")} {F("range")}(1_000_000)])\n{C("# avval million elementli ro‘yxat yasaladi")}',
        "✓ YAXSHIROQ", f'{F("sum")}(n * n {K("for")} n {K("in")} {F("range")}(1_000_000))\n{C("# natija bir xil, ro‘yxat yasalmaydi")}'), 6),
    page(step(6, "QACHON KERAK EMAS", "Hamma joyda ishlatmang",
        "Natija ro‘yxati kerak bo‘lmasa yoki shartlar ko‘payib, o‘qish qiyinlashsa — oddiy <b>for</b> loop yaxshiroq.",
        "✕ NOTO‘G‘RI", f'[{F("print")}(n) {K("for")} n {K("in")} nums]\n{C("# keraksiz [None, None, ...] ro‘yxat")}',
        "✓ TO‘G‘RI", f'{K("for")} n {K("in")} nums:\n    {F("print")}(n)'), 7),
    page("""<div class="top"><span class="tag">PYTHON · SAVOL</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Bu kod nima <span class="hl">chiqaradi?</span></h1>
<div class="code" style="border-color:#FFD43B;margin-top:40px;font-size:31px"><span class="fn">print</span>([x <span class="kw">for</span> x <span class="kw">in</span> <span class="fn">range</span>(10)
       <span class="kw">if</span> x % 3 == 0 <span class="kw">if</span> x % 2 == 0])</div>
<p style="font-size:40px;margin-top:40px">Javobni kommentga yozing 👇</p>
<p style="font-size:40px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> — loop yozayotganda kerak bo‘ladi.</p>
<p style="font-size:40px">Python bo‘yicha amaliy postlar uchun <b class="hl">follow</b> qiling.</p>
</div>""", 8, swipe=False),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    pg = browser.new_page(viewport={"width": 1080, "height": 1350})
    for i, html in enumerate(slides, 1):
        pg.set_content(html, wait_until="load")
        pg.screenshot(path=str(OUT / f"slide_{i:02d}.png"))
    browser.close()
print("done", len(slides))
