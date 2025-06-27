from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence

# Load local model via Ollama
llm = Ollama(model="mistral")

# Load PDF
loader = PyMuPDFLoader("sample1.pdf")
documents = loader.load()

# Prompt to extract triples
prompt = PromptTemplate.from_template(
    """
    You are a cybersecurity analyst. Extract key CTI entities from the following text. Entities include:
    - Threat actors, Malware, Tools, Techniques, Tactics, Campaigns
    - Dates or time references
    - Target industries, organizations, and countries
    - Indicators of compromise (IOCs)
    - Vulnerabilities (e.g., CVEs)

    Return the results in JSON with keys:
    ["threat_actors", "malware", "tools", "techniques", "tactics", "campaigns", "iocs", "dates", "vulnerabilities", "target_industries", "target_organizations", "target_countries"]

    Text:
    \"\"\"{text}\"\"\"
    """

)

# Chain: prompt → model
chain = prompt | llm

# Run on all PDF chunks
for chunk in documents:
    print("\n--- Extracting from chunk ---\n")
    response = chain.invoke({"text": chunk.page_content})
    print(response)

