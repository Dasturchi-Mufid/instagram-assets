"""Carousel — Python'da fayllar bilan ishlashda 5 ta xato."""
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


def mistake(n, title, text, bad, good):
    return f"""<div class="top"><span class="tag">PYTHON · XATO</span></div>
<div class="num">0{n}</div>
<h2>{title}</h2>
<p>{text}</p>
<div class="lbl b">✕ NOTO‘G‘RI</div><div class="code bad">{bad}</div>
<div class="lbl g">✓ TO‘G‘RI</div><div class="code good">{good}</div>"""


slides = [
    page("""<div class="top"><span class="tag">PYTHON</span><span>Fayllar bilan ishlash</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Python’da <span class="hl">fayllar</span> bilan ishlashda 5 ta xato</h1>
<p style="font-size:40px;margin-top:44px">Kod ishlaydi, lekin ma’lumot yo‘qoladi, harflar buziladi yoki fayl topilmaydi. Mana sabablari.</p>
</div>""", 1),
    page(mistake(1, "Faylni <span class='hl'>with</span>’siz ochish",
        "<b>close()</b> esdan chiqsa yoki o‘rtada xato chiqsa, fayl ochiq qoladi. <b>with</b> blok tugashi bilan faylni o‘zi yopadi.",
        'f = <span class="fn">open</span>(<span class="str">"data.txt"</span>)\ntext = f.read()\n<span class="cm"># f.close() esdan chiqdi</span>',
        '<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"data.txt"</span>) <span class="kw">as</span> f:\n    text = f.read()\n<span class="cm"># bu yerda fayl yopilgan</span>'), 2),
    page(mistake(2, "<span class='hl'>encoding</span> ko‘rsatmaslik",
        "Default kodlash OS va sozlamalarga bog‘liq: Windows’da ko‘pincha UTF-8 emas. Natijada o‘, g‘ harflari buziladi yoki <b>UnicodeDecodeError</b> chiqadi.",
        'f = <span class="fn">open</span>(<span class="str">"matn.txt"</span>)\n<span class="cm"># bir kompyuterda ishlaydi,</span>\n<span class="cm"># boshqasida xato beradi</span>',
        'f = <span class="fn">open</span>(<span class="str">"matn.txt"</span>, encoding=<span class="str">"utf-8"</span>)'), 3),
    page(mistake(3, "<span class='hl'>\"w\"</span> rejimi faylni tozalaydi",
        "<b>&quot;w&quot;</b> faylni ochishi bilan ichidagi hamma narsani o‘chiradi. Oxiriga qo‘shish uchun <b>&quot;a&quot;</b> (append) ishlating.",
        '<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"log.txt"</span>, <span class="str">"w"</span>) <span class="kw">as</span> f:\n    f.write(<span class="str">"yangi qator\\n"</span>)\n<span class="cm"># eski yozuvlar o‘chib ketdi</span>',
        '<span class="kw">with</span> <span class="fn">open</span>(<span class="str">"log.txt"</span>, <span class="str">"a"</span>) <span class="kw">as</span> f:\n    f.write(<span class="str">"yangi qator\\n"</span>)\n<span class="cm"># eski yozuvlar joyida qoladi</span>'), 4),
    page(mistake(4, "Katta faylni <span class='hl'>read()</span> bilan o‘qish",
        "<b>read()</b> butun faylni xotiraga yuklaydi. Bir necha GB’lik log faylda bu dasturni sekinlashtiradi yoki to‘xtatadi.",
        'text = f.read()\n<span class="kw">for</span> line <span class="kw">in</span> text.split(<span class="str">"\\n"</span>):\n    ...',
        '<span class="kw">for</span> line <span class="kw">in</span> f:  <span class="cm"># qatorma-qator</span>\n    line = line.rstrip(<span class="str">"\\n"</span>)\n    ...'), 5),
    page(mistake(5, "Windows yo‘lini oddiy satrda yozish",
        "Satr ichida <b>\\n</b> — yangi qator, <b>\\t</b> — tab. Python ularni yo‘l emas, maxsus belgi deb tushunadi.",
        'path = <span class="str">"C:\\new\\test.txt"</span>\n<span class="cm"># \\n va \\t buzildi → fayl topilmaydi</span>',
        '<span class="kw">from</span> pathlib <span class="kw">import</span> Path\npath = Path(<span class="str">"C:/new"</span>) / <span class="str">"test.txt"</span>\n<span class="cm"># yoki: r"C:\\new\\test.txt"</span>'), 6),
    page("""<div class="top"><span class="tag">PYTHON · SHABLON</span></div>
<div class="num">✓</div>
<h2>Hammasi bitta joyda</h2>
<p>Shu shablonni saqlab qo‘ying va fayl bilan ishlaganda ishlating:</p>
<div class="code good" style="margin-top:30px"><span class="kw">from</span> pathlib <span class="kw">import</span> Path

path = Path(<span class="str">"data"</span>) / <span class="str">"users.txt"</span>
path.parent.mkdir(exist_ok=<span class="kw">True</span>)

<span class="cm"># yozish (oxiriga qo‘shish)</span>
<span class="kw">with</span> <span class="fn">open</span>(path, <span class="str">"a"</span>, encoding=<span class="str">"utf-8"</span>) <span class="kw">as</span> f:
    f.write(<span class="str">"Ali\\n"</span>)

<span class="cm"># o‘qish (qatorma-qator)</span>
<span class="kw">with</span> <span class="fn">open</span>(path, encoding=<span class="str">"utf-8"</span>) <span class="kw">as</span> f:
    <span class="kw">for</span> line <span class="kw">in</span> f:
        <span class="fn">print</span>(line.rstrip(<span class="str">"\\n"</span>))</div>""", 7),
    page("""<div class="top"><span class="tag">PYTHON · SAVOL</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Bu kod nima <span class="hl">chiqaradi?</span></h1>
<div class="code" style="border-color:#FFD43B;margin-top:40px;font-size:40px"><span class="fn">print</span>(<span class="fn">len</span>(<span class="str">"C:\\new"</span>))</div>
<p style="font-size:40px;margin-top:40px">Javobni kommentga yozing 👇</p>
<p style="font-size:40px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> — fayl bilan ishlaganda kerak bo‘ladi.</p>
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
