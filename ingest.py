import os
import pymupdf as  fitz
import pytesseract
from PIL import Image
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.schema import Document

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

documents=[]

pdf_folder="pdfs"

for pdf_file in os.listdir(pdf_folder):

    if pdf_file.endswith(".pdf"):

        path=os.path.join(pdf_folder,pdf_file)

        pdf=fitz.open(path)

        for page_num in range(len(pdf)):

            page=pdf[page_num]

            text=page.get_text()

            if not text.strip():

                pix=page.get_pixmap()
                img=Image.frombytes(
                    "RGB",
                    [pix.width,pix.height],
                    pix.samples
                )

                text=pytesseract.image_to_string(img)

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source":pdf_file,
                        "page":page_num+1
                    }
                )
            )

splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks=splitter.split_documents(documents)

texts=[doc.page_content for doc in chunks]

embeddings=embedding_model.encode(texts)

db=FAISS.from_embeddings(
    list(zip(texts,embeddings)),
    embedding_model
)

db.save_local("vector_store")

print("PDF ingestion complete")
