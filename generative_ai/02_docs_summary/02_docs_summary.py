"""
Clase 2: Briefing
Este código implementa un flujo que utiliza LangChain para procesar varios documentos y generar una minuta detallada. El flujo considera documentos provenientes de OCR, los cuales pueden estar en formato markdown o texto simple, y crea una respuesta estructurada en markdown siguiendo un enfoque neutral y objetivo. 

El código realiza las siguientes acciones:
1. **Cargar claves API**: Usa la biblioteca `dotenv` para cargar las claves necesarias desde un archivo `.env`.
2. **Leer documentos y plantilla de prompt**: Lee el contenido de archivos externos (documentos y template) utilizando una función auxiliar.
3. **Configurar un modelo de lenguaje (LLM)**: Inicializa un modelo `ChatOpenAI` con parámetros personalizados como el modelo específico y la temperatura.
4. **Definir y configurar la cadena (chain)**: Combina el modelo de lenguaje con un prompt personalizado que incluye variables dinámicas (`doc_1`, `doc_2`, `doc_3`).
5. **Ejecutar la cadena y generar la salida**:
   - Carga los contenidos de tres documentos.
   - Procesa la información a través del modelo para generar una minuta detallada y estructurada.
   - Guarda el resultado en un archivo `minuta.md`.

Este ejemplo demuestra cómo integrar modelos de lenguaje grandes con flujos automatizados para tareas específicas como el resumen de múltiples documentos en un formato estructurado.
"""

# Importar las bibliotecas necesarias
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
prompt = PromptTemplate(template=template, input_variables=["doc_1", "doc_2", "doc_3"])

# Inicializar un modelo LLM (requiere clave de API de OpenAI)
llm = ChatOpenAI(model='gpt-4o-2024-11-20', temperature=0.7)

# Crea un chain
chain = LLMChain(llm=llm, prompt=prompt)

# Ejemplo de uso
def ejecutar_chain():

    doc_1 = read_txt("doc_1.md")
    doc_2 = read_txt("doc_2.txt")
    doc_3 = read_txt("doc_3.txt")
    output = chain.invoke({
        "doc_1": doc_1,
        "doc_2": doc_2,
        "doc_3": doc_3
    })
    minuta = output["text"]

    with open("minuta.md", "w") as text_file:
        text_file.write(minuta)

if __name__ == "__main__":
    ejecutar_chain()