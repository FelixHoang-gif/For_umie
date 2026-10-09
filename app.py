"""Website nhỏ: Một chút dịu dàng dành cho cậu. Chạy: streamlit run app.py"""
import base64
import html
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

import config as C

BASE = Path(__file__).parent


def esc(t):
    return html.escape(str(t))


def data_uri(rel, mime):
    """Trả về data-URI nếu file tồn tại, ngược lại None (không gây lỗi)."""
    try:
        p = BASE / rel
        if rel and p.is_file():
            return f"data:{mime};base64," + base64.b64encode(p.read_bytes()).decode()
    except OSError:
        pass
    return None


def cat(kind="heart"):
    """Mèo doodle bằng SVG, mỗi kiểu một biểu cảm/phụ kiện."""
    k = "#8D756A"
    closed = kind in ("sleep", "shy")
    eyes = (
        f'<path d="M38 52q5 5 10 0M72 52q5 5 10 0" stroke="{k}" stroke-width="3" fill="none" stroke-linecap="round"/>'
        if closed else
        f'<circle cx="43" cy="52" r="3.5" fill="{k}"/><circle cx="77" cy="52" r="3.5" fill="{k}"/>'
    )
    blush = '<ellipse cx="33" cy="62" rx="7" ry="4" fill="#F5B8C6" opacity=".8"/><ellipse cx="87" cy="62" rx="7" ry="4" fill="#F5B8C6" opacity=".8"/>' if kind == "shy" else ""
    extra = {
        "heart": '<path d="M60 112c-14-9-20-16-20-23a10 10 0 0 1 20-3 10 10 0 0 1 20 3c0 7-6 14-20 23z" fill="#F2A7B8" stroke="#8D756A" stroke-width="2.5"/>',
        "sleep": '<text x="86" y="30" font-size="16" fill="#8D756A" font-family="sans-serif">z</text><text x="98" y="18" font-size="12" fill="#8D756A" font-family="sans-serif">z</text>',
        "shy": '<ellipse cx="44" cy="98" rx="10" ry="8" fill="#fff" stroke="#8D756A" stroke-width="2.5"/><ellipse cx="76" cy="98" rx="10" ry="8" fill="#fff" stroke="#8D756A" stroke-width="2.5"/>',
        "moon": '<path d="M100 14a16 16 0 1 0 12 26a13 13 0 0 1-12-26z" fill="#F6E7A8" stroke="#8D756A" stroke-width="2"/>',
        "sign": '<rect x="28" y="88" width="64" height="26" rx="6" fill="#DDEBE3" stroke="#8D756A" stroke-width="2.5"/><text x="60" y="105" font-size="11" text-anchor="middle" fill="#8D756A" font-family="sans-serif">take your time</text>',
    }.get(kind, "")
    return (
        '<svg viewBox="0 0 120 125" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="mèo dễ thương">'
        f'<ellipse cx="60" cy="98" rx="38" ry="24" fill="#fff" stroke="{k}" stroke-width="3"/>'
        f'<path d="M24 40L22 12l24 16zM96 40l2-28-24 16z" fill="#F5DDE3" stroke="{k}" stroke-width="3" stroke-linejoin="round"/>'
        f'<ellipse cx="60" cy="52" rx="42" ry="34" fill="#fff" stroke="{k}" stroke-width="3"/>'
        f'{eyes}{blush}<path d="M55 60q5 5 10 0" stroke="{k}" stroke-width="2.5" fill="none" stroke-linecap="round"/>'
        f'{extra}</svg>'
    )


def build():
    c = C.COLORS
    music = data_uri(C.MUSIC_PATH, "audio/mpeg")
    photo = data_uri(C.PHOTO_PATH, "image/jpeg")
    sender = f"<p class='sign'>— {esc(C.SENDER)}</p>" if C.SENDER else ""
    hi = f"<p class='to'>Gửi {esc(C.RECIPIENT)},</p>" if C.RECIPIENT else ""
    notes = "".join(f"<div class='note r{i%3}'>{esc(t)}</div>" for i, t in enumerate(C.NOTES))
    photo_html = f"<img class='photo' src='{photo}' alt='ảnh kỷ niệm'>" if photo else ""
    letter = "".join(f"<p>{esc(t)}</p>" for t in C.LETTER)
    cards = "".join(f"<div class='card'><div class='ci'>{cat(k)}</div><p>{esc(t)}</p></div>" for t, k in C.CARDS)
    kinds = ["heart", "sleep", "shy", "moon", "sign"]
    cats = "".join(f"<button class='catbtn' aria-label='mèo {k}' data-i='{i}'>{cat(k)}</button>" for i, k in enumerate(kinds))
    final = "".join(f"<p>{esc(t)}</p>" for t in C.FINAL)
    music_btn = "<button id='mus' class='mus' aria-label='bật tắt nhạc'>♪ nhạc</button><audio id='aud' loop src='" + music + "'></audio>" if music else ""
    msgs = "[" + ",".join('"' + esc(m).replace('"', "'") + '"' for m in C.CAT_MESSAGES) + "]"

    page = """<!DOCTYPE html><html lang="vi"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<link href="https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Itim&display=swap" rel="stylesheet">
<style>
:root{--cream:__cream__;--pink:__pink__;--brown:__brown__;--white:__white__;--green:__green__}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--cream);color:var(--brown);font-family:'Quicksand','Segoe UI',sans-serif;line-height:1.8}
h2{font-family:'Itim','Quicksand',cursive;font-weight:400;font-size:1.9rem;text-align:center;margin:0 0 1.2rem}
section{max-width:720px;margin:0 auto;padding:4rem 1.3rem}
.reveal{opacity:0;transform:translateY(18px);transition:opacity .9s ease,transform .9s ease}
.reveal.on{opacity:1;transform:none}
#welcome{min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:2rem 1.3rem;gap:.8rem;transition:opacity .7s}
#welcome h1{font-family:'Itim','Quicksand',cursive;font-weight:400;font-size:clamp(1.6rem,6vw,2.4rem);margin:.5rem 0 0}
#welcome .cat{width:120px}
.env{position:relative;width:200px;height:130px;background:var(--pink);border-radius:10px;box-shadow:0 8px 24px rgba(141,117,106,.18);margin-top:-18px}
.env .flap{position:absolute;top:0;left:0;width:100%;height:70px;background:#efcdd6;clip-path:polygon(0 0,100% 0,50% 100%);transform-origin:top;transition:transform .8s ease;border-radius:10px 10px 0 0}
.env .heart{position:absolute;top:44px;left:50%;transform:translateX(-50%);font-size:1.4rem;color:var(--white)}
.env.open .flap{transform:rotateX(180deg)}
button{font-family:inherit;cursor:pointer}
.btn{background:var(--white);color:var(--brown);border:2px solid var(--brown);border-radius:999px;padding:.75rem 1.6rem;font-size:1.05rem;box-shadow:0 4px 14px rgba(141,117,106,.15);transition:transform .25s,background .25s}
.btn:hover{transform:translateY(-3px);background:var(--pink)}
#main{display:none}
.note{background:var(--white);border-radius:16px;padding:1rem 1.3rem;margin:1rem auto;max-width:520px;box-shadow:0 6px 18px rgba(141,117,106,.12);font-family:'Itim','Quicksand',cursive;font-size:1.15rem;border-left:6px solid var(--pink)}
.r0{transform:rotate(-1.2deg)}.r1{transform:rotate(1deg);border-left-color:var(--green)}.r2{transform:rotate(-.6deg)}
.deco{width:90px;margin:1rem auto 0;display:block}.photo{display:block;max-width:240px;width:80%;margin:1.2rem auto;border-radius:16px;border:6px solid var(--white);box-shadow:0 6px 18px rgba(141,117,106,.18)}
.letter{background:var(--white);border-radius:22px;padding:2rem 1.6rem;box-shadow:0 10px 30px rgba(141,117,106,.15)}
.letter p{margin:0 0 1.2rem}.to,.sign{font-family:'Itim','Quicksand',cursive}.end{text-align:right;font-family:'Itim','Quicksand',cursive;font-size:1.15rem}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.1rem}
.card{background:var(--white);border-radius:20px;padding:1.2rem;text-align:center;box-shadow:0 6px 18px rgba(141,117,106,.12);transition:transform .3s,box-shadow .3s}
.card:hover{transform:translateY(-6px);box-shadow:0 14px 28px rgba(141,117,106,.2)}
.card p{margin:.6rem 0 0}.ci svg{width:80px}.small{text-align:center;font-size:.92rem;opacity:.85;margin-top:1.2rem}
.green{background:var(--green);max-width:none;border-radius:40px}.green .in{max-width:680px;margin:0 auto}
.cats{display:flex;flex-wrap:wrap;justify-content:center;gap:.6rem}
.catbtn{background:none;border:0;width:92px;padding:4px;border-radius:20px;transition:transform .25s,background .25s}
.catbtn:hover{transform:scale(1.1) rotate(-3deg);background:rgba(255,255,255,.6)}.catbtn svg{width:100%}
.bubble{min-height:3.2rem;margin:1.2rem auto 0;max-width:420px;background:var(--white);border-radius:18px;padding:.8rem 1.1rem;text-align:center;font-family:'Itim','Quicksand',cursive;font-size:1.1rem;box-shadow:0 4px 14px rgba(141,117,106,.12)}
.final{background:var(--cream);text-align:center}.final .cat{width:110px;margin:0 auto 1rem}
.final .sign{margin-top:1.6rem;font-size:1.15rem}
.mus{position:fixed;top:12px;right:12px;z-index:9;background:var(--white);color:var(--brown);border:2px solid var(--brown);border-radius:999px;padding:.35rem .9rem;font-size:.9rem;opacity:.9}
.mus.on{background:var(--pink)}
.sp{position:fixed;bottom:-20px;color:var(--pink);pointer-events:none;animation:up linear infinite;opacity:0;z-index:1}
@keyframes up{0%{transform:translateY(0);opacity:0}15%{opacity:.8}100%{transform:translateY(-105vh) translateX(20px);opacity:0}}
@media (prefers-reduced-motion:reduce){.sp{display:none}.reveal{transition:none}html{scroll-behavior:auto}}
</style></head><body>
__MUSIC__
<div id="welcome">
  <div class="cat">__CAT_WELCOME__</div>
  <div class="env" id="env"><div class="flap"></div><div class="heart">♡</div></div>
  <h1>__WTITLE__</h1><p>__WSUB__</p>
  <button class="btn" id="open">__OPENBTN__</button>
</div>
<div id="main">
  <section class="reveal"><h2>__NTITLE__</h2>__NOTES__ __PHOTO__<div class="deco">__CAT_SLEEP__</div></section>
  <section class="reveal"><h2>__LTITLE__</h2><div class="letter">__HI____LETTER__<p class="end">__LEND__</p>__SENDER__</div></section>
  <section class="reveal"><h2>__CTITLE__</h2><div class="grid">__CARDS__</div><p class="small">__CNOTE__</p></section>
  <section class="reveal green"><div class="in"><h2>__CATSTITLE__</h2><div class="cats">__CATS__</div><div class="bubble" id="bub" aria-live="polite">__HINT__</div></div></section>
  <section class="reveal final"><div class="cat">__CAT_MOON__</div>__FINAL__<p class="sign">__FSIGN__</p></section>
</div>
<script>
var MSG=__MSGS__,last=-1;
function $(i){return document.getElementById(i)}
function reveal(){var els=document.querySelectorAll('.reveal');
 if(!('IntersectionObserver' in window)){els.forEach(function(e){e.classList.add('on')});return}
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('on');io.unobserve(e.target)}})},{threshold:.12});
 els.forEach(function(e){io.observe(e)})}
$('open').onclick=function(){$('env').classList.add('open');$('open').disabled=true;
 setTimeout(function(){$('welcome').style.opacity=0},900);
 setTimeout(function(){$('welcome').style.display='none';$('main').style.display='block';window.scrollTo(0,0);reveal()},1500)};
document.querySelectorAll('.catbtn').forEach(function(b){b.onclick=function(){
 var i;do{i=Math.floor(Math.random()*MSG.length)}while(i===last&&MSG.length>1);last=i;$('bub').textContent=MSG[i]}});
var m=$('mus');if(m){var a=$('aud');m.onclick=function(){
 if(a.paused){a.play().then(function(){m.classList.add('on');m.textContent='♪ đang phát'}).catch(function(){m.textContent='♪ không phát được'})}
 else{a.pause();m.classList.remove('on');m.textContent='♪ nhạc'}}}
for(var s=0;s<8;s++){var e=document.createElement('span');e.className='sp';e.textContent=s%2?'✦':'♡';
 e.style.left=(Math.random()*95)+'%';e.style.fontSize=(10+Math.random()*8)+'px';
 e.style.animationDuration=(14+Math.random()*10)+'s';e.style.animationDelay=(Math.random()*12)+'s';document.body.appendChild(e)}
</script></body></html>"""
    rep = {
        "__cream__": c["cream"], "__pink__": c["pink"], "__brown__": c["brown"], "__white__": c["white"], "__green__": c["green"],
        "__MUSIC__": music_btn, "__CAT_WELCOME__": cat("shy"), "__WTITLE__": esc(C.WELCOME_TITLE), "__WSUB__": esc(C.WELCOME_SUB),
        "__OPENBTN__": esc(C.OPEN_BUTTON), "__NTITLE__": esc(C.NOTES_TITLE), "__NOTES__": notes, "__PHOTO__": photo_html,
        "__CAT_SLEEP__": cat("sleep"), "__LTITLE__": esc(C.LETTER_TITLE), "__HI__": hi, "__LETTER__": letter,
        "__LEND__": esc(C.LETTER_END), "__SENDER__": sender, "__CTITLE__": esc(C.CARDS_TITLE), "__CARDS__": cards,
        "__CNOTE__": esc(C.CARDS_NOTE), "__CATSTITLE__": esc(C.CATS_TITLE), "__CATS__": cats, "__HINT__": esc(C.CATS_HINT),
        "__CAT_MOON__": cat("heart"), "__FINAL__": final, "__FSIGN__": esc(C.FINAL_SIGN), "__MSGS__": msgs,
    }
    for k, v in rep.items():
        page = page.replace(k, v)
    return page


st.set_page_config(page_title=C.PAGE_TITLE, page_icon="🐱", layout="centered")
st.markdown(
    f"""<style>#MainMenu,header,footer{{visibility:hidden}}
.stApp{{background:{C.COLORS['cream']}}}
.block-container{{padding:0!important;max-width:100%!important}}
iframe{{height:100vh!important;border:0}}</style>""",
    unsafe_allow_html=True,
)
components.html(build(), height=900, scrolling=True)
