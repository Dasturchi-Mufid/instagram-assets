"""Carousel #01 — Python'da yangi boshlovchilar ko'p qiladigan 5 ta xato."""
from pathlib import Path
from playwright.sync_api import sync_playwright

OUT = Path(__file__).parent / "slides"
OUT.mkdir(exist_ok=True)
HANDLE = "@dasturchi_mufid"
TOTAL = 7

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
    page("""<div class="top"><span class="tag">PYTHON</span><span>Boshlovchilar uchun</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Python’da <span class="hl">yangi boshlovchilar</span> ko‘p qiladigan 5 ta xato</h1>
<p style="font-size:40px;margin-top:44px">Ko‘pi xato chiqarmaydi — kod shunchaki noto‘g‘ri ishlaydi. Shuning uchun topish qiyin.</p>
</div>""", 1),
    page(mistake(1, "Default argumentda ro‘yxat (list)",
        "Default qiymat funksiya yaratilganda <b>bir marta</b> yaratiladi. Har chaqiruvda o‘sha bitta ro‘yxat ishlatiladi.",
        '<span class="kw">def</span> <span class="fn">add</span>(x, items=[]):\n    items.append(x)\n    <span class="kw">return</span> items\n\nadd(1)  <span class="cm"># [1]</span>\nadd(2)  <span class="cm"># [1, 2]  ← kutilmagan</span>',
        '<span class="kw">def</span> <span class="fn">add</span>(x, items=<span class="kw">None</span>):\n    <span class="kw">if</span> items <span class="kw">is None</span>:\n        items = []\n    items.append(x)\n    <span class="kw">return</span> items'), 2),
    page(mistake(2, "Qiymatni <span class='hl'>is</span> bilan solishtirish",
        "<b>is</b> — bu bitta obyektmi, deb tekshiradi. Qiymat tengligini <b>==</b> tekshiradi. <b>is</b> ni asosan <b>None</b> uchun ishlating.",
        'a = <span class="fn">input</span>()       <span class="cm"># "salom"</span>\n<span class="kw">if</span> a <span class="kw">is</span> <span class="str">"salom"</span>:  <span class="cm"># False bo‘lishi mumkin</span>\n    ...',
        '<span class="kw">if</span> a == <span class="str">"salom"</span>:\n    ...\n<span class="kw">if</span> result <span class="kw">is None</span>:\n    ...'), 3),
    page(mistake(3, "Aylanib turgan ro‘yxatni o‘zgartirish",
        "Loop ichida elementni o‘chirsangiz, indekslar suriladi va ba’zi elementlar tekshirilmay qoladi.",
        'nums = [1, 2, 2, 3]\n<span class="kw">for</span> n <span class="kw">in</span> nums:\n    <span class="kw">if</span> n == 2:\n        nums.remove(n)\n<span class="cm"># [1, 2, 3]  ← bitta 2 qoldi</span>',
        'nums = [n <span class="kw">for</span> n <span class="kw">in</span> nums <span class="kw">if</span> n != 2]\n<span class="cm"># [1, 3]</span>'), 4),
    page(mistake(4, "Hamma xatoni <span class='hl'>except:</span> bilan yutish",
        "Bo‘sh <b>except</b> hatto Ctrl+C va sizning bug’laringizni ham yashiradi. Kutayotgan xatoni aniq yozing.",
        '<span class="kw">try</span>:\n    age = <span class="fn">int</span>(text)\n<span class="kw">except</span>:\n    <span class="kw">pass</span>',
        '<span class="kw">try</span>:\n    age = <span class="fn">int</span>(text)\n<span class="kw">except</span> ValueError:\n    <span class="fn">print</span>(<span class="str">"Raqam kiriting"</span>)'), 5),
    page(mistake(5, "Kutubxonalarni global o‘rnatish",
        "Har loyihaga alohida virtual muhit (venv) qiling. Aks holda versiyalar bir-biri bilan to‘qnashadi.",
        '<span class="cm"># hamma loyiha uchun bitta joyga</span>\npip install django',
        'python -m venv .venv\n<span class="cm"># Windows: .venv\\Scripts\\activate</span>\nsource .venv/bin/activate\npip install django'), 6),
    page("""<div class="top"><span class="tag">PYTHON</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Qaysi birini <span class="hl">qilgansiz?</span></h1>
<p style="font-size:42px;margin-top:44px">Raqamini kommentga yozing 👇</p>
<p style="font-size:42px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> — kod yozayotganda kerak bo‘ladi.</p>
<p style="font-size:42px">Haftada 3 marta Python bo‘yicha amaliy postlar — <b class="hl">follow</b> qiling.</p>
</div>""", 7, swipe=False),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    pg = browser.new_page(viewport={"width": 1080, "height": 1350})
    for i, html in enumerate(slides, 1):
        pg.set_content(html, wait_until="load")
        pg.screenshot(path=str(OUT / f"slide_{i:02d}.png"))
    browser.close()
print("done", len(slides))
