import os
import streamlit as st
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from pypdf import PdfReader

# ─────────────────────────────────────────────
# KONFIGURASI — ubah sesuai kebutuhan Anda
# ─────────────────────────────────────────────
GROQ_API_KEY = ""   
PDF_PATH     = "Kafiya_Umroh_Travel_PlainText.pdf"                    
MODEL        = "meta-llama/llama-4-scout-17b-16e-instruct"
# ─────────────────────────────────────────────

# Terapkan API Key ke environment
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# ─── Konfigurasi Halaman ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="Kafiya Teman Umrohmu",
    page_icon="📄",
    layout="centered",
)

# ─── Inisialisasi Session State ────────────────────────────────────────────────
# Menyimpan riwayat obrolan untuk ditampilkan di UI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Menyimpan riwayat dalam format objek LangChain untuk dikirim ke LLM
if "lc_history" not in st.session_state:
    st.session_state.lc_history = []

# Menyimpan teks hasil ekstraksi PDF (hanya baca sekali)
if "pdf_context" not in st.session_state:
    try:
        pdf_context = ""
        reader = PdfReader(PDF_PATH)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                pdf_context += text + "\n"
        st.session_state.pdf_context = pdf_context
        st.session_state.pdf_error   = None
    except Exception as e:
        st.session_state.pdf_context = ""
        st.session_state.pdf_error   = str(e)

# ─── Judul & Info PDF ─────────────────────────────────────────────────────────
st.title(" Kafiya Teman Umrohmu")
st.divider()

# Tampilkan error jika PDF gagal dibaca
if st.session_state.pdf_error:
    st.error(f"❌ Gagal membaca PDF `{PDF_PATH}`: {st.session_state.pdf_error}")
    st.stop()

# ─── Tampilkan Riwayat Obrolan ─────────────────────────────────────────────────
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ─── Input Pesan Pengguna ──────────────────────────────────────────────────────
user_input = st.chat_input("Tanyakan sesuatu tentang dokumen…")

if user_input and user_input.strip():

    # Tampilkan pesan pengguna
    with st.chat_message("user"):
        st.markdown(user_input)

    # Tambahkan ke riwayat LangChain
    st.session_state.lc_history.append(HumanMessage(user_input))

    # Instruksi sistem: jawab hanya berdasarkan isi PDF
    system_prompt = SystemMessage(
        f"""Anda adalah Kafiya, asisten virtual yang membantu menjawab pertanyaan seputar umroh. Anda ramah, profesional, penuh empati, dan mengutamakan sopan santun.

Gunakan informasi berikut sebagai sumber pengetahuan Anda:
\\"\\"\\"{st.session_state.pdf_context}\\"\\"\\"

Aturan Perilaku & Gaya Bahasa (Wajib):
1. Gunakan Bahasa Indonesia yang baik, benar, formal, namun tetap terasa hangat dan bersahabat.
2. Jawab seolah kamu memang sudah tahu informasinya — JANGAN pernah menyebut kata "dokumen", "file", "teks", atau sejenisnya dalam jawabanmu.
3. Berikan jawaban secara DETAIL, terstruktur, dan jelas agar mudah dipahami.
4. Tunjukkan rasa empati dan kesiapan untuk membantu di setiap respons.

Aturan Ketat Isi Jawaban:
1. Jawablah HANYA menggunakan informasi dari sumber pengetahuan di atas.
2. Jika informasi tidak tersedia, tolak dengan sopan: 'Mohon maaf, saya belum memiliki informasi terkait hal tersebut. Apakah ada hal lain yang bisa saya bantu?'
3. Jangan pernah mengarang jawaban atau menggunakan pengetahuan di luar sumber di atas."""
    )

    # Panggil LLM dan tampilkan respons
    with st.chat_message("assistant"):
        with st.spinner("Sedang memproses…"):
            try:
                client = ChatGroq(model=MODEL)
                input_messages = [system_prompt] + st.session_state.lc_history
                response = client.invoke(input_messages)
                bot_reply = response.content

                # Simpan ke riwayat LangChain
                st.session_state.lc_history.append(response)

                # Simpan ke riwayat tampilan UI
                st.session_state.chat_history.append({"role": "user",      "content": user_input})
                st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

                st.markdown(bot_reply)

            except Exception as e:
                pesan_error = f"❌ Terjadi kesalahan: {e}"
                st.session_state.chat_history.append({"role": "user",      "content": user_input})
                st.session_state.chat_history.append({"role": "assistant", "content": pesan_error})
                st.error(pesan_error)
