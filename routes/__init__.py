# backend/routes/__init__.py
"""
Rotas da API
"""
from .chat import router as chat_router
from .estatisticas import router as estatisticas_router
from .validacao import router as validacao_router

__all__ = ['chat_router', 'estatisticas_router', 'validacao_router']