# agents/planner.py
"""Query planner that decomposes queries and orchestrates retrieval and reasoning."""

from agents.reasoning_agent import decompose_query


def plan_and_execute(query, retriever, llm):
    """
    Plan and execute the RAG pipeline.
    
    Steps:
    1. Decompose query into sub-queries
    2. Retrieve context for each sub-query
    3. Combine context and generate final response
    
    Args:
        query: User query string
        retriever: LlamaIndex retriever instance
        llm: LlamaIndex LLM instance
        
    Returns:
        CompletionResponse from LLM
    """
    # Step 1: Break query into sub-queries
    sub_queries = decompose_query(query)

    all_context = []

    # Step 2: Retrieve context for each sub-query
    for q in sub_queries:
        docs = retriever.retrieve(q)
        all_context.extend(docs)

    # Step 3: Combine context and generate response
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
