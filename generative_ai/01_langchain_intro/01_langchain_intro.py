"""
Clase 1: LangChain Introduction
Este código presenta un ejemplo práctico de cómo utilizar LangChain para responder preguntas generales utilizando LLM.

El flujo incluye los siguientes pasos:
1. **Cargar claves API**: Se utiliza la biblioteca `dotenv` para cargar las claves necesarias desde un archivo `.env`.
2. **Definir una plantilla de prompt**: Se establece un prompt dinámico que toma como entrada una pregunta y genera una respuesta precisa, siguiendo un formato predefinido.
3. **Configurar un modelo de lenguaje (LLM)**: Se inicializa un modelo de OpenAI con parámetros específicos como el modelo a usar y la temperatura de respuesta.
4. **Crear una cadena (chain)**: Combina el modelo de lenguaje con el prompt para generar respuestas personalizadas.
5. **Ejemplo de uso**:
   - Se define una pregunta específica: "¿Qué es LangChain y para qué se usa?".
   - El modelo procesa la pregunta utilizando la cadena configurada.
   - La respuesta generada se imprime en la consola.

Este código muestra cómo integrar LangChain para realizar tareas de preguntas y respuestas de manera eficiente, aprovechando las capacidades de modelos de lenguaje avanzados.
"""

# Importar las bibliotecas necesarias
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Carga api keys del archivo .env
load_dotenv()

# Crear una template de prompt
template = """
Eres un asistente de IA. Responde a la siguiente pregunta de manera concisa y precisa:
Pregunta: {pregunta}
"""
prompt = PromptTemplate(template=template, input_variables=["pregunta"])

# Inicializar un modelo LLM (requiere clave de API de OpenAI)
llm = ChatOpenAI(model='gpt-4o-2024-11-20', temperature=0.7)

# Crea un chain
chain = LLMChain(llm=llm, prompt=prompt)

# Ejemplo de uso
def ejecutar_chain():
    pregunta = "¿Qué es LangChain y para qué se usa?"
    output = chain.invoke({"pregunta": pregunta})
    respuesta = output["text"]

    print("Pregunta:  ", pregunta)
    print("Respuesta: ", respuesta)

if __name__ == "__main__":
    ejecutar_chain()