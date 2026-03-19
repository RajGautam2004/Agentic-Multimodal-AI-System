# agents/planner.py

from agents.reasoning_agent import decompose_query

def plan_and_execute(query, retriever, llm):
    # Step 1: Break query
    sub_queries = decompose_query(query)

    all_context = []

    # Step 2: Retrieve for each
    for q in sub_queries:
        docs = retriever.retrieve(q)
        all_context.extend(docs)

    # Step 3: Combine
    context_text = "\n".join([d.text for d in all_context])

    final_prompt = f"""
    Answer the question using the context below.

    Context:
    {context_text}

    Question:
    {query}
    """

    response = llm.complete(final_prompt)
    return response