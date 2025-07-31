# RAG Project — Document-based Question Answering System
Proyek ini membangun sistem **Retrieval-Augmented Generation (RAG)** untuk menjawab pertanyaan berbasis dokumen secara akurat menggunakan LLM lokal dan teknik embedding canggih.
## Fitur Utama
-  Menggunakan **embedding model terbaik untuk QA**: [`BAAI/bge-small-en-v1.5`](https://huggingface.co/BAAI/bge-small-en-v1.5)  
-  **Chunking optimal** agar relevansi dokumen tetap terjaga  
-  **Prompt yang diarahkan** agar model hanya menjawab berdasarkan dokumen yang tersedia  
-  **LLM lokal via Ollama** (contoh: `gemma3:12b`)  
-  Penyimpanan vektor menggunakan **ChromaDB**
## Struktur Folder
```
rag_project/
├── app.py               # Aplikasi utama (RAG pipeline)
├── docs/                # Folder dokumen referensi
│   └── smartcity.txt    # Contoh dokumen
├── chroma_db/           # Database vektor lokal (ChromaDB)
├── requirements.txt     # Daftar dependensi Python
```
## instalasi
1. **Clone repository ini**  
   ```bash
   git clone https://github.com/username/rag_project.git
   cd rag_project
   ```
2. **Buat dan aktifkan virtual environment (opsional tapi direkomendasikan)**  
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate.bat  # Windows
   ```

3. **Install dependensi**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Ollama & model lokal (contoh: Gemma 3B)**  
   Pastikan Ollama telah terinstal: [https://ollama.com](https://ollama.com)  
   ```bash
   ollama run gemma3:12b
   ```
## 🧪 Menjalankan Proyek

```bash
python app.py
```

Aplikasi akan memuat dokumen, melakukan chunking dan embedding, serta memungkinkan Anda mengajukan pertanyaan yang akan dijawab oleh LLM berdasarkan konten dokumen.

##  Catatan

- Pastikan dokumen yang ingin Anda gunakan berada di folder `docs/`.
- Embedding dilakukan sekali dan disimpan di `chroma_db/` untuk efisiensi.
- Prompting telah disesuaikan agar model menjawab hanya berdasarkan dokumen (document-grounded answering).
