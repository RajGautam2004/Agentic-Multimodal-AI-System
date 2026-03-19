# agents/reasoning_agent.py

from openai import OpenAI

client = OpenAI()

def decompose_query(query: str):
    prompt = f"""
    Break the user query into smaller sub-questions for better retrieval.

    Query: {query}

    Return as a list.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.choices[0].message.content

    # simple split (can improve later)
    sub_queries = text.split("\n")
    return [q.strip("- ").strip() for q in sub_queries if q.strip()]