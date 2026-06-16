# Final Project — LLM-Based Tools and Gemini API Integration for Data Science

## Kafiya: Chatbot Travel Agent Umroh

Kafiya adalah chatbot berbasis LLM yang dirancang untuk membantu calon jamaah umroh mendapatkan informasi seputar perjalanan umroh secara cepat, ramah, dan akurat. Chatbot ini menjawab pertanyaan berdasarkan pengetahuan yang telah dikonfigurasi sebelumnya, tanpa perlu input tambahan dari pengguna.

---

## Fitur

- Menjawab pertanyaan seputar umroh secara otomatis
- Riwayat percakapan tersimpan selama sesi berlangsung
- Antarmuka chat yang bersih dan mudah digunakan berbasis Streamlit
- Didukung model LLM **LLaMA 4 Scout** via **Groq API**
- Pengetahuan chatbot bersumber dari file PDF yang dikonfigurasi di sisi server

---

## Teknologi yang Digunakan

| Komponen | Teknologi |
|---|---|
| Framework UI | Streamlit |
| LLM Provider | Groq API |
| Model | `meta-llama/llama-4-scout-17b-16e-instruct` |
| Orkestrasi LLM | LangChain |
| Ekstraksi PDF | pypdf |
| Bahasa | Python 3.10+ |

---

## Struktur Proyek

```
final-project/
├── app.py                                 # File utama aplikasi Streamlit
├── Kafiya_Umroh_Travel_PlainText.pdf      # File PDF sumber pengetahuan chatbot
├── requirements.txt                       # Daftar dependensi
└── README.md
```

---

## Instalasi & Menjalankan Aplikasi

### 1. Clone repositori

```bash
git clone https://github.com/nurgiaziz/kafiya-chatbot.git
cd nama-repo
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

### 3. Konfigurasi

Buka file `app.py` dan ubah bagian konfigurasi di baris paling atas:

```python
GROQ_API_KEY = "gsk_xxxxxxxxxxxxxxxxxxxxxxxx"   # Ganti dengan API Key Groq Anda
PDF_PATH     = "Kafiya_Umroh_Travel_PlainText.pdf"                    # Ganti dengan path file PDF Anda
```

> Dapatkan Groq API Key gratis di [https://console.groq.com](https://console.groq.com)

### 4. Jalankan aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka di browser pada `http://localhost:8501`.

---

## Cara Kerja

```
Pengguna mengetik pertanyaan
        ↓
Streamlit menangkap input
        ↓
Teks PDF dimuat sebagai konteks pengetahuan
        ↓
LangChain menyusun System Prompt + Riwayat Chat
        ↓
Groq API memanggil model LLaMA 4 Scout
        ↓
Jawaban ditampilkan di antarmuka chat
```

---

## Requirements

Buat file `requirements.txt` dengan isi berikut:

```
streamlit
langchain-core
langchain-groq
pypdf
```

---

## Catatan

- Chatbot hanya menjawab berdasarkan informasi yang telah dikonfigurasi — tidak menggunakan pengetahuan umum di luar itu.
- File PDF dibaca sekali saat aplikasi pertama kali dijalankan dan disimpan di session state.
- Riwayat percakapan akan hilang jika halaman di-refresh.
