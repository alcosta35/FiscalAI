# config.py
"""
Configuration settings for FiscalAI
"""
from pydantic_settings import BaseSettings
from pathlib import Path
import os

# Determine if running in Colab
IS_COLAB = 'COLAB_GPU' in os.environ

# Data directory - different for Colab vs local
if IS_COLAB:
    DATA_DIR = Path('/content/data')
else:
    DATA_DIR = Path(__file__).parent / 'data'


class Settings(BaseSettings):
    """Application settings"""
    
    # App info
    app_name: str = "FiscalAI - Auditor Fiscal Inteligente"
    app_version: str = "1.0.0"

    # API settings
    api_prefix: str = ""  # ← ADD THIS LINE (empty string = no prefix, or use "/api/v1")
        
    # OpenAI API
    openai_api_key: str = ""
    openai_model: str = "gpt-4"

    # CORS settings
    cors_origins: list = ["*"]  # Allow all origins, or specify: ["https://example.com"]
    
    
    # CSV file paths
    cabecalho_csv: str = str(DATA_DIR / "202401_NFs_Cabecalho.csv")
    itens_csv: str = str(DATA_DIR / "202401_NFs_Itens.csv")
    cfop_csv: str = str(DATA_DIR / "CFOP.csv")
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


# Global settings instance
settings = Settings()