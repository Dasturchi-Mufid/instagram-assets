"""Carousel — list, tuple, set, dict: qachon qaysi biri."""
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
.code.sm { font-size:24px; line-height:1.4; padding:22px 28px; }
.code.n { border-color:#3776AB; }
.lbl.n { color:#8B95A3; }
table { width:100%; border-collapse:collapse; margin-top:36px; font-size:30px; }
th { text-align:left; color:#8B95A3; font-weight:600; font-size:24px; letter-spacing:1px; padding:0 0 18px 0; }
td { padding:22px 0; border-top:2px solid #21262D; vertical-align:top; color:#B8C1CC; line-height:1.3; }
td.t { font-family:'DejaVu Sans Mono', monospace; color:#FFD43B; font-size:30px; width:150px; }
td.c { width:120px; text-align:center; font-size:34px; }
.y { color:#3FB950; } .x { color:#F0605A; }
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


K = lambda s: f'<span class="kw">{s}</span>'
S = lambda s: f'<span class="str">{s}</span>'
C = lambda s: f'<span class="cm">{s}</span>'
F = lambda s: f'<span class="fn">{s}</span>'


def item(n, name, title, text, blocks, tag="PYTHON · TUSHUNCHA"):
    out = f"""<div class="top"><span class="tag">{tag}</span><span>{name}</span></div>
<div class="num">0{n}</div>
<h2>{title}</h2>
<p>{text}</p>"""
    for lbl, cls, code in blocks:
        out += f'<div class="lbl {cls[0]}">{lbl}</div><div class="code {cls}">{code}</div>'
    return out


slides = [
    page("""<div class="top"><span class="tag">PYTHON</span><span>Boshlovchilar uchun</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1><span class="hl">list, tuple, set, dict</span> — qachon qaysi biri?</h1>
<p style="font-size:40px;margin-top:44px">Hammasi “bir nechta qiymatni saqlaydi”. Lekin noto‘g‘ri tanlasangiz, kod sekin yoki chalkash bo‘ladi.</p>
</div>""", 1),
    page(item(1, "list", "list — tartibli va o‘zgaruvchan",
        "Elementlar qo‘shilgan tartibda turadi, takrorlanishi mumkin, istalgan payt o‘zgartirasiz. <b>Ketma-ketlik</b> kerak bo‘lsa — list.",
        [("NAMUNA", "n", f'tasks = [{S(chr(34)+"kod"+chr(34))}, {S(chr(34)+"test"+chr(34))}, {S(chr(34)+"kod"+chr(34))}]\n'
            f'tasks.append({S(chr(34)+"deploy"+chr(34))})\n'
            f'tasks[0] = {S(chr(34)+"review"+chr(34))}\n\n'
            f'{F("print")}(tasks)\n'
            f'{C("# [&#x27;review&#x27;, &#x27;test&#x27;, &#x27;kod&#x27;, &#x27;deploy&#x27;]")}')]), 2),
    page(item(2, "tuple", "tuple — o‘zgarmas list",
        "Bir marta yaratiladi va o‘zgarmaydi. Koordinata, sana kabi <b>o‘zgarmasligi kerak</b> bo‘lgan ma’lumot uchun. Dict kaliti ham bo‘la oladi.",
        [("NAMUNA", "n", 'point = (41.31, 69.28)\n'
            'lat, lon = point\n\n'
            f'point[0] = 0\n{C("# TypeError: &#x27;tuple&#x27; object does not")}\n{C("# support item assignment")}'),
         ("DICT KALITI SIFATIDA", "n", f'cities = {{(41.31, 69.28): {S(chr(34)+"Toshkent"+chr(34))}}}')]), 3),
    page(item(3, "set", "set — faqat unikal qiymatlar",
        "Takrorlarni o‘zi olib tashlaydi. Tartib kafolatlanmaydi. Element bor-yo‘qligini (<b>in</b>) tekshirish tez ishlaydi.",
        [("NAMUNA", "n", f'emails = [{S(chr(34)+"a@mail.uz"+chr(34))}, {S(chr(34)+"b@mail.uz"+chr(34))},\n          {S(chr(34)+"a@mail.uz"+chr(34))}]\n'
            f'{F("print")}({F("len")}({F("set")}(emails)))  {C("# 2")}'),
         ("KESISHMA VA AYIRMA", "n", f'a = {{{S(chr(34)+"python"+chr(34))}, {S(chr(34)+"sql"+chr(34))}}}\n'
            f'b = {{{S(chr(34)+"python"+chr(34))}, {S(chr(34)+"docker"+chr(34))}}}\n\n'
            f'{F("print")}(a &amp; b)  {C("# {&#x27;python&#x27;}")}\n'
            f'{F("print")}(b - a)  {C("# {&#x27;docker&#x27;}")}')]), 4),
    page(item(4, "dict", "dict — kalit bo‘yicha qidirish",
        "Har qiymatning nomi (kaliti) bor. Indeks emas, <b>nom bilan</b> murojaat qilish kerak bo‘lsa — dict. Kalitlar takrorlanmaydi.",
        [("NAMUNA", "n", f'prices = {{{S(chr(34)+"olma"+chr(34))}: 12000, {S(chr(34)+"nok"+chr(34))}: 15000}}\n\n'
            f'{F("print")}(prices[{S(chr(34)+"nok"+chr(34))}])         {C("# 15000")}\n'
            f'{F("print")}(prices.get({S(chr(34)+"uzum"+chr(34))}, 0))  {C("# 0")}\n\n'
            f'prices[{S(chr(34)+"uzum"+chr(34))}] = 20000  {C("# yangi kalit")}')]), 5),
    page(item(5, "tuzoqlar", "Ikkita kichik tuzoq",
        "Bo‘sh <b>{}</b> — bu set emas, dict. Bitta elementli tuple uchun esa vergul shart.",
        [("✕ KUTILMAGAN", "bad", f'{F("type")}({{}})    {C("# &lt;class &#x27;dict&#x27;&gt;")}\n'
            f'{F("type")}((5))   {C("# &lt;class &#x27;int&#x27;&gt;")}'),
         ("✓ TO‘G‘RI", "good", f'{F("type")}({F("set")}())  {C("# &lt;class &#x27;set&#x27;&gt;")}\n'
            f'{F("type")}((5,))  {C("# &lt;class &#x27;tuple&#x27;&gt;")}')], tag="PYTHON · XATO"), 6),
    page("""<div class="top"><span class="tag">SHPARGALKA</span><span>Saqlab qo‘ying</span></div>
<h2 style="margin-top:36px">Qaysi birini tanlash kerak?</h2>
<table>
<tr><th></th><th style="text-align:center">TARTIB</th><th style="text-align:center">O‘ZGARADI</th><th style="padding-left:24px">QACHON</th></tr>
<tr><td class="t">list</td><td class="c y">✓</td><td class="c y">✓</td><td style="padding-left:24px">Ketma-ketlik, qo‘shib-o‘chirib turasiz</td></tr>
<tr><td class="t">tuple</td><td class="c y">✓</td><td class="c x">✕</td><td style="padding-left:24px">O‘zgarmas ma’lumot, dict kaliti</td></tr>
<tr><td class="t">set</td><td class="c x">✕</td><td class="c y">✓</td><td style="padding-left:24px">Takrorsiz qiymatlar, tez <b>in</b> tekshiruv</td></tr>
<tr><td class="t">dict</td><td class="c y">✓</td><td class="c y">✓</td><td style="padding-left:24px">Qiymatni kalit (nom) bo‘yicha olish</td></tr>
</table>
<p style="font-size:28px;margin-top:36px">dict Python 3.7 dan boshlab qo‘shilgan tartibni saqlaydi.</p>""", 7),
    page(f"""<div class="top"><span class="tag">PYTHON · TEST</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Bu kod nima <span class="hl">chiqaradi?</span></h1>
<div class="code n" style="font-size:40px;margin-top:44px;padding:36px 40px">{F("print")}({F("len")}({{1, 1, 2, (1,), (1,)}}))</div>
<p style="font-size:42px;margin-top:44px">Javobingizni kommentga yozing 👇</p>
<p style="font-size:42px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> va Python bo‘yicha amaliy postlar uchun <b class="hl">follow</b> qiling.</p>
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
