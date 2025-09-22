import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(page_title="Chat", layout="wide")

html("""
<!DOCTYPE html><html><head><meta charset="utf-8" />
<style>
  body { margin:0; font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial; }
  .page { max-width:900px; margin:24px auto; padding:0 12px; }
  .card { border:1px solid #e5e7eb; border-radius:14px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,.06); }
  .hdr { background:linear-gradient(93deg,#0b8dff,#5f6cff); color:#fff; padding:14px 16px; font-weight:600; }
  .sys { background:#f4f6fb; padding:10px 16px; border-bottom:1px solid #eef0f5; color:#475569; font-size:13px; }
  .msgs { background:#f8fafc; height:56vh; overflow-y:auto; padding:14px 16px; }
  .row { display:flex; gap:10px; margin:10px 0; align-items:flex-start; }
  .msg { padding:10px 12px; border-radius:14px; font-size:14px; line-height:1.4; max-width:70%; white-space:pre-wrap; }
  .bot { background:#fff; border:1px solid #eef0f5; color:#0f172a; }
  .user { background:#0ea5e9; color:#fff; margin-left:auto; }
  .av  { width:28px; height:28px; border-radius:50%; display:flex; align-items:center; justify-content:center; font-weight:700; font-size:13px; }
  .avb { background:#e2e8f0; color:#0f172a; }
  .avu { background:#bae6fd; color:#0c4a6e; }
  .bar { padding:12px; border-top:1px solid #eef0f5; background:#fff; display:flex; gap:10px; }
  .bar textarea { flex:1; border:1px solid #e5e7eb; border-radius:10px; padding:10px 12px; background:#f9fafb; resize:none; font-family:inherit; }
  .bar button { border:none; border-radius:10px; padding:0 18px; background:#0ea5e9; color:#fff; font-weight:600; cursor:pointer; }
</style>
</head>
<body>
  <div class="page">
    <div class="card">
      <div class="hdr">💬 Chat</div>
      <div class="sys"><b>System:</b> You are a concise, friendly assistant.</div>
      <div class="msgs" id="msgs"></div>
      <div class="bar">
        <textarea id="in" placeholder="Type your message…" rows="1"></textarea>
        <button onclick="send()">Send</button>
      </div>
    </div>
  </div>

<script>
  let history = [{role:'bot', text:"Hi! I’m Sam. Ask me anything."}];
  const msgs = document.getElementById('msgs');
  const inputEl = document.getElementById('in');

  function render() {
    msgs.innerHTML = '';
    history.forEach(m=>{
      msgs.insertAdjacentHTML('beforeend',
        m.role==='user'
          ? `<div class="row" style="justify-content:flex-end;"><div class="msg user">${m.text}</div><div class="av avu">U</div></div>`
          : `<div class="row"><div class="av avb">AI</div><div class="msg bot">${m.text}</div></div>`
      );
    });
    msgs.scrollTop = msgs.scrollHeight;
  }

  function send() {
    const t = inputEl.value.trim();
    if (!t) return;
    history.push({role:'user', text:t});
    render();
    inputEl.value='';
    setTimeout(()=>{ history.push({role:'bot', text:'Echo: '+t}); render(); }, 300);
  }

  // Enter = send, Shift+Enter = newline
  inputEl.addEventListener("keydown", function(event) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      send();
    }
  });

  render();
</script>
</body></html>
""", height=640, scrolling=True)
