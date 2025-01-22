"""
Clase 4: Text Classification
Este código proporciona un ejemplo de cómo clasificar los documentos .pdf
contenidos en una carpeta "documents". Para esto los documentos se leen con un
OCR y luego se clasifican. Finalmente, los documentos se guardan en un excel.
"""

# Importar las bibliotecas necesarias
import os
import pandas as pd

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Carga api keys del archivo .env
load_dotenv()

# Crear una template de prompt
def read_txt(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

template = read_txt("template.md")
prompt = PromptTemplate(template=template, input_variables=["doc"])

# Inicializar un modelo LLM (requiere clave de API de OpenAI)
llm = ChatOpenAI(model='gpt-4o-2024-11-20', temperature=0.7)

# Crea un chain
chain = LLMChain(llm=llm, prompt=prompt)

# Ejemplo de uso
def ejecutar_chain():

    # Define carpetas donde se almacenan documentos
    documents_dir = "documents"
    documents_parsed_dir = "documents_parsed"

    # Crear un DataFrame para guardar los resultados
    results = []

    # Iterar sobre los archivos en el directorio
    for doc in os.listdir(documents_dir):
        doc_path = os.path.join(document_dir, doc)

        # Verificar si el archivo es un PDF
        if doc.endswith(".pdf"):
            txt_file_path = os.path.splitext(doc_path)[0] + ".txt"

            # Leer o procesar el archivo según su estado
            if os.path.exists(txt_file_path):
                # Leer el contenido del archivo .txt
                with open(os.path.join(documents_parsed_dir, txt_file_path), "r", encoding="utf-8") as txt_file:
                    doc_parsed = txt_file.read()
            else:
                # Procesar el PDF con OCR y guardar como .txt
                doc_parsed = ocr(doc_path)
                with open(os.path.join(documents_parsed_dir, txt_file_path), "w", encoding="utf-8") as txt_file:
                    txt_file.write(doc_parsed)

            # Pasar el contenido por el modelo de lenguaje
            output = chain.invoke({"doc": doc_parsed})

            # Extraer la categoría del resultado
            category = output.get("text", "")

            # Agregar el resultado al DataFrame
            results.append({"Correlativo": doc, "Categoría": category})

    # Crear un DataFrame a partir de los resultados
    df = pd.DataFrame(results)

    # Guardar el DataFrame en un archivo Excel
    df.to_excel("resultados.xlsx", index=False)
    print(df)

if __name__ == "__main__":
    ejecutar_chain()
