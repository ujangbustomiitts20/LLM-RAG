from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain.chains import ConversationalRetrievalChain
from langchain.prompts import PromptTemplate

# 1. Muat dokumen dari file
loader = TextLoader("docs/smartcity.txt", encoding="utf-8")
documents = loader.load()

# 2. Potong jadi chunks besar untuk menjaga konteks
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=300)
chunks = splitter.split_documents(documents)

# 3. Gunakan model embedding BGE yang cocok untuk pertanyaan-jawaban
embedding = HuggingFaceBgeEmbeddings(
    model_name="BAAI/bge-small-en-v1.5",
    encode_kwargs={"normalize_embeddings": True}
)

# 4. Simpan embeddings ke Chroma vector store
vectorstore = Chroma.from_documents(chunks, embedding, persist_directory="./chroma_db")

# 5. Inisialisasi LLM lokal dari Ollama
llm = OllamaLLM(model="gemma3:12b")  # Ganti jika pakai model lain

# 6. Template prompt agar tidak ngarang
prompt_template = """
Kamu adalah asisten AI. Jawab hanya berdasarkan isi dokumen berikut:

{context}

Pertanyaan: {question}

Jika jawabannya tidak ada dalam dokumen, jawab: "Saya tidak tahu berdasarkan dokumen yang ada."
""".strip()

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=prompt_template
)

# 7. Buat RAG chain dengan prompt kustom
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(),
    combine_docs_chain_kwargs={"prompt": prompt}
)

# 8. Loop interaksi pengguna
chat_history = []
print("🔁 Sistem siap. Ketik pertanyaan (atau 'exit' untuk keluar)")
while True:
    query = input("❓ Pertanyaan kamu: ")
    if query.lower() in ['exit', 'quit']:
        break
    try:
        result = qa_chain.invoke({
            "question": query,
            "chat_history": chat_history
        })
        print("🤖 Jawaban:", result["answer"])
        chat_history.append((query, result["answer"]))
    except Exception as e:
        print("❌ Error:", str(e))
