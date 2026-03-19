"""
Configuration module for the Multimodal RAG System.
Load settings from environment variables with defaults.
"""

import os
from functools import lru_cache


class Settings:
    """Application settings loaded from environment."""
    
    # API Configuration
    api_host: str = os.getenv("API_HOST", "0.0.0.0")
    api_port: int = int(os.getenv("API_PORT", "8000"))
    api_reload: bool = os.getenv("API_RELOAD", "true").lower() == "true"
    
    # LLM Configuration
    llm_model_id: str = os.getenv(
        "HF_MODEL_ID",
        "meta-llama/Llama-3.2-3B-Instruct"
    )
    llm_context_window: int = 8192
    llm_max_tokens: int = 512
    llm_temperature: float = 0.7
    
    # Vector Store Configuration
    milvus_host: str = os.getenv("MILVUS_HOST", "localhost")
    milvus_port: int = int(os.getenv("MILVUS_PORT", "19530"))
    milvus_collection: str = "documents"
    
    # Embeddings Configuration
    embeddings_model: str = "nvidia/NV-Embed-v2"
    nvidia_api_key: str = os.getenv("NVIDIA_API_KEY", "")
    
    # Retrieval Configuration
    top_k: int = 3
    
    @property
    def milvus_uri(self) -> str:
        """Construct Milvus connection URI."""
        return f"http://{self.milvus_host}:{self.milvus_port}"


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance."""
    return Settings()
