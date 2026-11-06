"""Carousel — Satr (str) bilan ishlash: 6 ta foydali metod."""
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
Q = lambda s: S(f'"{s}"')

slides = [
    page("""<div class="top"><span class="tag">PYTHON</span><span>Foydali metodlar</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Satr (<span class="hl">str</span>) bilan ishlashda kerak bo‘ladigan 6 ta metod</h1>
<p style="font-size:40px;margin-top:44px">input()’dan kelgan matnni tozalash, bo‘lish, birlashtirish va tekshirish — har birida kichik tuzoq bilan.</p>
</div>""", 1),
    page(step(1, "STRIP", "Bo‘sh joy va <span class='hl'>\\n</span> ni olib tashlash",
        "<b>strip()</b> satr boshi va oxiridagi bo‘sh joy, <b>\\n</b> va <b>\\t</b> larni olib tashlaydi. Foydalanuvchi kiritgan matnni avval shunday tozalang.",
        "✕ NOTO‘G‘RI", f'name = {Q("  Ali ")}\n{K("if")} name == {Q("Ali")}:  {C("# False")}\n    ...',
        "✓ TO‘G‘RI", f'name = {F("input")}({Q("Ism: ")}).strip()\n{K("if")} name == {Q("Ali")}:  {C("# True")}\n    ...'), 2),
    page(step(2, "SPLIT · JOIN", "Bo‘lish va qayta birlashtirish",
        "<b>split()</b> satrni ro‘yxatga bo‘ladi, <b>join()</b> ro‘yxatni satrga yig‘adi. <b>+=</b> bilan yig‘ish oxirida ortiqcha vergul qoldiradi.",
        "✕ NOTO‘G‘RI", f's = {Q("")}\n{K("for")} w {K("in")} words:\n    s += w + {Q(", ")}\n{C("# &#x27;olma, anor, nok, &#x27;")}',
        "✓ TO‘G‘RI", f'words = {Q("olma,anor,nok")}.split({Q(",")})\n{C("# [&#x27;olma&#x27;, &#x27;anor&#x27;, &#x27;nok&#x27;]")}\n{Q(", ")}.join(words)\n{C("# &#x27;olma, anor, nok&#x27;")}'), 3),
    page(step(3, "REPLACE", "Satr o‘zgarmaydi — natijani saqlang",
        "Satr o‘zgarmas (immutable). <b>replace()</b> eski satrni o‘zgartirmaydi, <b>yangi satr qaytaradi</b>.",
        "✕ NOTO‘G‘RI", f's = {Q("salom")}\ns.replace({Q("a")}, {Q("o")})\n{F("print")}(s)  {C("# salom")}',
        "✓ TO‘G‘RI", f's = s.replace({Q("a")}, {Q("o")})\n{F("print")}(s)  {C("# solom")}'), 4),
    page(step(4, "ENDSWITH", "Bir nechta variantni bittada tekshirish",
        "<b>startswith()</b> va <b>endswith()</b> tuple qabul qiladi. Kesib solishtirish (<b>[-4:]</b>) esa .jpeg kabi holatlarda adashadi.",
        "✕ NOTO‘G‘RI", f'f = {Q("photo.jpeg")}\nf[-4:] == {Q(".jpg")}  {C("# False")}',
        "✓ TO‘G‘RI", f'f.lower().endswith(({Q(".jpg")}, {Q(".jpeg")}, {Q(".png")}))\n{C("# True")}'), 5),
    page(step(5, "LOWER", "Katta-kichik harfsiz solishtirish",
        "Foydalanuvchi <b>Ha</b>, <b>HA</b> yoki <b>ha</b> deb yozishi mumkin. Solishtirishdan oldin bir xil ko‘rinishga keltiring.",
        "✕ NOTO‘G‘RI", f'answer = {Q("Ha")}\n{K("if")} answer == {Q("ha")}:  {C("# False")}\n    ...',
        "✓ TO‘G‘RI", f'{K("if")} answer.strip().lower() == {Q("ha")}:\n    ...  {C("# True")}'), 6),
    page(step(6, "ISDIGIT", "int() dan oldin tekshirish",
        "<b>isdigit()</b> faqat raqamlardan iborat satrga <b>True</b> beradi. Lekin manfiy son va kasr uchun <b>False</b> — buni yodda tuting.",
        "NATIJALAR", f'{Q("12")}.isdigit()   {C("# True")}\n{Q("-5")}.isdigit()   {C("# False")}\n{Q("3.5")}.isdigit()  {C("# False")}\n{Q("")}.isdigit()     {C("# False")}',
        "✓ ISHLATISH", f'text = {F("input")}({Q("Yosh: ")}).strip()\n{K("if")} text.isdigit():\n    age = {F("int")}(text)', k1="g"), 7),
    page("""<div class="top"><span class="tag">PYTHON · SAVOL</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Bu kod nima <span class="hl">chiqaradi?</span></h1>
<div class="code" style="border-color:#FFD43B;margin-top:40px;font-size:34px"><span class="fn">print</span>(<span class="str">"a-b-c"</span>.split(<span class="str">"-"</span>, 1))</div>
<p style="font-size:40px;margin-top:40px">Javobni kommentga yozing 👇</p>
<p style="font-size:40px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> — matn bilan ishlaganda kerak bo‘ladi.</p>
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
