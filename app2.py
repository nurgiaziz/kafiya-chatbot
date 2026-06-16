import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_groq import ChatGroq
from pypdf import PdfReader 

print("=== KAFIYA TERMINAL PDF CHATBOT ===")

# 1. Masukkan API Key Groq langsung di Terminal
api_key = input("Masukkan Groq API Key Anda: ")
os.environ["GROQ_API_KEY"] = api_key

# 2. Bikin client LLM Groq
client = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# 3. Masukkan nama file PDF yang ingin dibaca
# Pastikan file PDF-nya disimpan di dalam folder yang sama dengan 'app1.py'
pdf_name = input("\nMasukkan nama file PDF Anda (contoh: data.pdf): ")

# Proses membaca file PDF
pdf_context = ""
try:
    pdf_reader = PdfReader(pdf_name)
    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            pdf_context += text + "\n"
    print("✅ Berhasil membaca PDF dan memuatnya ke memori!")
except Exception as e:
    print(f"❌ Gagal membaca file. Pastikan file '{pdf_name}' ada di folder ini. Error: {e}")
    exit()

# 4. Inisialisasi riwayat obrolan kosong
chat_history = []

print("\nChatbot Siap! Ketik 'keluar' untuk mengakhiri obrolan.\n")

# 5. Loop Obrolan di Terminal
while True:
    user_input = input("Anda: ")
    if user_input.lower() == 'keluar':
        print("Terima kasih!")
        break
        
    if not user_input.strip():
        continue

    # Tambahkan input user ke riwayat
    chat_history.append(HumanMessage(user_input))

    # Kunci instruksi agar LLM HANYA menjawab berdasarkan teks PDF dengan gaya yang sopan, detail, dan empati
    system_prompt = SystemMessage(
        f"""Anda adalah seorang asisten chatbot yang sangat profesional, ramah, penuh empati, dan mengutamakan sopan santun. Tugas utama Anda adalah MENJAWAB PERTANYAAN HANYA BERDASARKAN TEKS DOKUMEN DI BAWAH INI.
        
        Konteks Dokumen:
        \"\"\"{pdf_context}\"\"\"
        
        Aturan Perilaku & Gaya Bahasa (Wajib):
        1. Gunakan Bahasa Indonesia yang baik, benar, formal, namun tetap terasa hangat, penuh empati, dan bersahabat.
        2. Mulailah atau sisipkan kalimat sapaan yang santun (seperti "Terima kasih atas pertanyaannya...", "Baik, berdasarkan dokumen yang Anda berikan...").
        3. Berikan jawaban secara DETAIL, terstruktur, dan jelas agar mudah dipahami oleh pengguna. Jangan menjawab terlalu singkat jika informasi di dokumen cukup lengkap.
        4. Tunjukkan rasa empati dan kesiapan untuk membantu di setiap respons Anda.

        Aturan Ketat Isi Jawaban:
        1. Jawablah pertanyaan user HANYA menggunakan informasi yang ada di dalam Konteks Dokumen di atas.
        2. Jika jawaban dari pertanyaan user TIDAK ADA di dalam teks dokumen tersebut, Anda WAJIB menolaknya dengan sangat sopan dan penuh empati, contoh: 'Mohon maaf yang sebesar-besarnya, setelah saya memeriksa dokumen yang Anda berikan, saya tidak berhasil menemukan informasi terkait hal tersebut. Apakah ada bagian lain dari dokumen yang ingin Anda tanyakan?'
        3. Jangan pernah mengarang jawaban atau menggunakan pengetahuan luar Anda yang tidak tertulis di dokumen."""
    )

    # Gabungkan instruksi pembatas dengan riwayat obrolan
    input_messages = [system_prompt] + chat_history

    # Jalankan LLM Groq dan ambil responnya
    print("Bot sedang berpikir...")
    response = client.invoke(input_messages)
    
    # Tampilkan jawaban di Terminal dan simpan ke riwayat
    print(f"Bot: {response.content}\n")
    chat_history.append(response)