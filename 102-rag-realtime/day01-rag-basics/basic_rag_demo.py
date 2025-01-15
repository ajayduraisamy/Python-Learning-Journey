# ----------------------------------
# REALTIME RAG WITH ONE DOCUMENT
# ----------------------------------

# Step 1: Load document
with open("company_policy.txt", "r") as file:
    document = file.read()

# Step 2: Simple retriever
def retrieve_context(query, doc):
    lines = doc.split("\n")
    relevant = []
    for line in lines:
        if query.lower() in line.lower():
            relevant.append(line)
    return relevant

# Step 3: Generate answer (LLM simulation)
def generate_answer(query, context):
    if not context:
        return "No relevant information found in document."
    
    answer = "Answer based on document:\n"
    for c in context:
        answer += f"- {c}\n"
    return answer

# Step 4: Realtime user input
while True:
    user_query = input("\nAsk a question (type 'exit' to quit): ")
    
    if user_query.lower() == "exit":
        print("Exiting RAG system.")
        break

    retrieved_context = retrieve_context(user_query, document)
    response = generate_answer(user_query, retrieved_context)
    print("\n", response)
