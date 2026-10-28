"""Carousel — Downloads papkasini Python skript bilan tartiblash."""
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


def step(n, title, text, blocks):
    out = f"""<div class="top"><span class="tag">PYTHON · AMALIY SKRIPT</span></div>
<div class="num">0{n}</div>
<h2>{title}</h2>
<p>{text}</p>"""
    for lbl, cls, code in blocks:
        out += f'<div class="lbl {cls[0]}">{lbl}</div><div class="code {cls}">{code}</div>'
    return out


FULL = (
    f"{K('from')} pathlib {K('import')} Path\n"
    f"{K('import')} shutil\n\n"
    "FOLDERS = {\n"
    f"    {S('\".jpg\"')}: {S('\"Images\"')}, {S('\".png\"')}: {S('\"Images\"')},\n"
    f"    {S('\".pdf\"')}: {S('\"Documents\"')}, {S('\".docx\"')}: {S('\"Documents\"')},\n"
    f"    {S('\".mp4\"')}: {S('\"Videos\"')}, {S('\".zip\"')}: {S('\"Archives\"')},\n"
    "}\n"
    f"DRY_RUN = {K('True')}\n\n"
    f"{K('def')} {F('sort_folder')}(folder):\n"
    f"    {K('for')} file {K('in')} Path(folder).iterdir():\n"
    f"        {K('if not')} file.is_file():\n"
    f"            {K('continue')}\n"
    f"        name = FOLDERS.get(file.suffix.lower(), {S('\"Other\"')})\n"
    "        target = file.parent / name\n"
    "        dest = target / file.name\n"
    f"        {K('if')} dest.exists():\n"
    f"            {F('print')}({S('\"Bor:\"')}, dest)\n"
    f"            {K('continue')}\n"
    f"        {F('print')}(file.name, {S('\"→\"')}, name)\n"
    f"        {K('if not')} DRY_RUN:\n"
    f"            target.mkdir(exist_ok={K('True')})\n"
    "            shutil.move(file, dest)\n\n"
    f"sort_folder(Path.home() / {S('\"Downloads\"')})"
)

slides = [
    page(f"""<div class="top"><span class="tag">PYTHON</span><span>Amaliy skript</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1><span class="hl">Downloads</span> papkangizni Python bilan tartiblang</h1>
<p style="font-size:40px;margin-top:44px">26 qatorlik skript: rasmlar — Images’ga, PDF — Documents’ga, qolgani — Other’ga. Faqat standart kutubxona, pip install shart emas.</p>
</div>""", 1),
    page(step(1, "Vazifa: nima qilamiz?",
        "Papkadagi har bir faylning kengaytmasiga qarab, uni mos papkaga ko‘chiramiz.",
        [("OLDIN", "bad", "Downloads/\n  photo.JPG\n  cv.pdf\n  video.mp4\n  app.zip\n  notes.txt"),
         ("KEYIN", "good", "Downloads/\n  Images/photo.JPG\n  Documents/cv.pdf\n  Videos/video.mp4\n  Archives/app.zip\n  Other/notes.txt")]), 2),
    page(step(2, "Fayllarni birma-bir ko‘rib chiqish",
        "<b>Path.iterdir()</b> papka ichidagi hamma narsani beradi. Ichki papkalarni <b>is_file()</b> bilan o‘tkazib yuboramiz.",
        [("KOD", "good", f"{K('from')} pathlib {K('import')} Path\n\n{K('for')} file {K('in')} Path({S('\"Downloads\"')}).iterdir():\n    {K('if not')} file.is_file():\n        {K('continue')}  {C('# papka — tegmaymiz')}\n    {F('print')}(file.name)")]), 3),
    page(step(3, "Kengaytma bo‘yicha papka tanlash",
        "Kengaytma → papka nomini <b>dict</b>’da saqlaymiz. <b>.lower()</b> — “.JPG” ham “.jpg” deb tushunilsin. <b>.get()</b> — ro‘yxatda yo‘q bo‘lsa “Other”.",
        [("NATIJA", "good", "p = Path(" + S('"photo.JPG"') + ")\np.suffix          " + C("# '.JPG'") + "\np.suffix.lower()  " + C("# '.jpg'") + "\n\nFOLDERS.get(" + S('".jpg"') + ", " + S('"Other"') + ")  " + C("# 'Images'") + "\nFOLDERS.get(" + S('".exe"') + ", " + S('"Other"') + ")  " + C("# 'Other'"))]), 4),
    page(step(4, "Papka yaratish va ko‘chirish",
        "<b>exist_ok=True</b> — papka allaqachon bo‘lsa, xato bermaydi. Shu nomli fayl bor bo‘lsa, ustidan yozmaslik uchun o‘tkazib yuboramiz.",
        [("KOD", "good", f"target = file.parent / name\ndest = target / file.name\n\n{K('if')} dest.exists():\n    {K('continue')}  {C('# ustidan yozmaymiz')}\n\ntarget.mkdir(exist_ok={K('True')})\nshutil.move(file, dest)")]), 5),
    page(step(5, "Avval “quruq” ishga tushiring",
        "Fayl ko‘chirish — jiddiy amal. <b>DRY_RUN = True</b> bo‘lsa, skript faqat nima qilishini yozadi. Natija to‘g‘ri bo‘lsa, <b>False</b> qiling.",
        [("DRY_RUN = True", "good", f"{K('if not')} DRY_RUN:\n    target.mkdir(exist_ok={K('True')})\n    shutil.move(file, dest)"),
         ("TERMINALDA", "n", "photo.JPG → Images\ncv.pdf → Documents\nvideo.mp4 → Videos\napp.zip → Archives\nnotes.txt → Other")]), 6),
    page(f"""<div class="top"><span class="tag">PYTHON · TO‘LIQ SKRIPT</span><span>sort_files.py</span></div>
<div class="code sm good" style="margin-top:34px">{FULL}</div>
<p style="font-size:30px">Ro‘yxatga o‘zingizga kerakli kengaytmalarni qo‘shing: <b>.mp3</b>, <b>.xlsx</b>, <b>.exe</b>…</p>""", 7),
    page("""<div class="top"><span class="tag">PYTHON</span></div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<h1>Keyingi qaysi <span class="hl">skript</span>?</h1>
<p style="font-size:42px;margin-top:44px">Qaysi zerikarli ishingizni avtomatlashtirmoqchisiz? Kommentga&nbsp;yozing&nbsp;👇</p>
<p style="font-size:42px">Postni <b style="color:#E9EDF2">saqlab qo‘ying</b> — skript kerak bo‘lganda topasiz.</p>
<p style="font-size:42px">Python bo‘yicha amaliy postlar uchun <b class="hl">follow</b> qiling.</p>
</div>""", 8, swipe=False),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    pg = browser.new_page(viewport={"width": 1080, "height": 1350})
    for i, html in enumerate(slides, 1):
        pg.set_content(html, wait_until="load")
        # matn chiqib ketganini tekshirish
        over = pg.evaluate("() => { const w=document.querySelector('.wrap'); const r=w.getBoundingClientRect(); let bad=[]; w.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect(); if(b.bottom>r.bottom+1||b.right>r.right+1) bad.push(e.className||e.tagName)}); return bad; }")
        if over:
            print("OVERFLOW", i, over)
        pg.screenshot(path=str(OUT / f"slide_{i:02d}.png"))
    browser.close()
print("done", len(slides))
