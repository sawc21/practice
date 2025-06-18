from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# Load your local model via Ollama
llm = Ollama(model="mistral")

# Load PDF
loader = PyMuPDFLoader("sample1.pdf")
documents = loader.load()

# Prompt to extract triples
prompt = PromptTemplate.from_template(
    "Extract concise CTI triples from the following text:\n\n{text}\n\n"
    "Use the format: (subject, relation, object). Return only the triples."
)

# Chain: prompt → model
chain = prompt | llm

# Run on all PDF chunks
for chunk in documents:
    print("\n--- Extracting from chunk ---\n")
    response = chain.invoke({"text": chunk.page_content})
    print(response)

