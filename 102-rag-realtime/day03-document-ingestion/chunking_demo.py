# ------------------------------------
# DOCUMENT INGESTION & CHUNKING DEMO
# ------------------------------------

# Load document
with open("sample_document.txt", "r") as file:
    text = file.read()

# Simple chunking function
def chunk_text(text, chunk_size=50):
    words = text.split()
    chunks = []
    
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
    
    return chunks

# Perform chunking
chunks = chunk_text(text)

# Display chunks
print("Total Chunks:", len(chunks))
for i, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {i}:")
    print(chunk)
