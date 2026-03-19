# agents/reasoning_agent.py
"""Reasoning agent for query decomposition using LLM."""

from typing import List


def decompose_query(query: str) -> List[str]:
    """
    Decompose a complex query into simpler sub-queries using an LLM.
    
    Currently returns the original query as a single sub-query.
    Can be extended to use OpenAI API or other LLMs for actual decomposition.
    
    Args:
        query: User query string
        
    Returns:
        List of sub-queries
    """
    # TODO: Implement actual decomposition using LLM
    # For now, return the original query as a single sub-query
    # Uncomment below if you want to use OpenAI:
    
    # from openai import OpenAI
    # client = OpenAI()
    # prompt = f"""
    # Break the user query into smaller sub-questions for better retrieval.
    #
    # Query: {query}
    #
    # Return as a list.
    # """
    # response = client.chat.completions.create(
    #     model="gpt-4o-mini",
    #     messages=[{"role": "user", "content": prompt}]
    # )
    # text = response.choices[0].message.content
    # sub_queries = text.split("\n")
    # return [q.strip("- ").strip() for q in sub_queries if q.strip()]
    
    # Simple fallback: return original query
    return [query]
