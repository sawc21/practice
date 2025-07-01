

from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
fromlangchain_core.documents import Document

from docling.document_converter import DocumentConverter

# Load the PDF
converter = DocumentConverter()
result = converter.convert_single("sample1.pdf")

# Each page in the result.pages list has a .text attribute
chunks = []
for page in result.pages:
    chunk = {
        "page_number": page.page_number,
        "text": page.text.strip()
    }
    chunks.append(chunk)

# Print each chunk (page)
for chunk in chunks:
    print(f"\n--- Page {chunk['page_number']} ---\n")
    print(chunk['text'][:500], "...")  # Show only first 500 characters for preview

# Step 2: Tokenizer and chunker
# tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.1")
#
# def chunk_text_for_ollama(text, max_tokens=512, overlap=50):
#     input_ids = tokenizer.encode(text, add_special_tokens=False)
#     chunks = []
#     start = 0
#     while start < len(input_ids):
#         end = start + max_tokens
#         chunk_ids = input_ids[start:end]
#         chunk_text = tokenizer.decode(chunk_ids)
#         chunks.append(chunk_text)
#         start += max_tokens - overlap
#     return chunks
#
# # Step 3: Apply chunking
# chunks = chunk_text_for_ollama(markdown_output, max_tokens=512)
#
# # (Optional) Print summary
# for i, chunk in enumerate(chunks):
#     print(f"\n--- Chunk {i + 1} ---\n{chunk[:300]}...\n")

#llm = OllamaLLM(model="mistral")


# # Step 6: Define prompt
# prompt = PromptTemplate.from_template("""
# You are a cybersecurity analyst. Extract key CTI entities from the following text. Entities include:
# - Threat actors, Malware, Tools, Techniques, Tactics, Campaigns
# - Dates or time references
# - Target industries, organizations, and countries
# - Indicators of compromise (IOCs)
# - Vulnerabilities (e.g., CVEs)
#
# Return the results in JSON with keys:
# ["threat_actors", "malware", "tools", "techniques", "tactics", "campaigns", "iocs", "dates", "vulnerabilities", "target_industries", "target_organizations", "target_countries"]
#
# Text:
# \"\"\"{text}\"\"\"
# """)
#
# # Step 7: Run LLM on each chunk
# chain = prompt | llm
# for i, doc in enumerate(docs):
#     print(f"\n--- Chunk {i+1}/{len(docs)} ---")
#     response = chain.invoke({"text": doc.page_content})
#     print(response)
