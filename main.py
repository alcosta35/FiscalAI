# backend/main.py
"""
Aplicação principal FastAPI - FiscalAI
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import sys

# Importações locais
from config import settings
from models.schemas import HealthCheck
from routes import chat_router, estatisticas_router, validacao_router
from agente_cfop import AgenteValidadorCFOP

# ============================================================================
# INICIALIZAÇÃO DA APLICAÇÃO
# ============================================================================

app = FastAPI(
    title=settings.app_name,        
    version=settings.app_version,  
    description="Sistema inteligente de auditoria e validação de CFOP"
)
# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Variável global para o agente
agente = None

# ============================================================================
# ROTAS BÁSICAS
# ============================================================================

@app.get("/")
async def root():
    """Rota raiz"""
    return {
        "mensagem": f"Bem-vindo ao {settings.APP_NAME}",
        "versao": settings.APP_VERSION,
        "docs": "/docs"
    }

@app.get("/health", response_model=HealthCheck)
async def health_check():
    """Health check do sistema"""
    status = "healthy" if agente is not None else "initializing"
    mensagem = "Sistema operacional" if agente is not None else "Sistema inicializando..."
    
    return HealthCheck(
        status=status,
        mensagem=mensagem
    )

@app.post("/inicializar")
async def inicializar_sistema():
    """
    Inicializa o agente CFOP com os arquivos CSV
    """
    global agente
    
    try:
        print("\n🚀 Inicializando sistema...")
        
        agente = AgenteValidadorCFOP(
            cabecalho_path=settings.CABECALHO_PATH,
            itens_path=settings.ITENS_PATH,
            cfop_path=settings.CFOP_PATH
        )
        
        return {
            "status": "success",
            "mensagem": "Sistema inicializado com sucesso!",
            "total_notas": len(agente.df_cabecalho),
            "total_itens": len(agente.df_itens)
        }
    except Exception as e:
        print(f"❌ Erro na inicialização: {e}")
        import traceback
        traceback.print_exc()
        return {
            "status": "error",
            "mensagem": f"Erro ao inicializar: {str(e)}"
        }

# ============================================================================
# INCLUIR ROTAS
# ============================================================================

app.include_router(chat_router, prefix=settings.API_PREFIX)
app.include_router(estatisticas_router, prefix=settings.API_PREFIX)
app.include_router(validacao_router, prefix=settings.API_PREFIX)

# ============================================================================
# EXECUÇÃO LOCAL (DESENVOLVIMENTO)
# ============================================================================

if __name__ == "__main__":
    print(f"""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║          {settings.APP_NAME}           ║
    ║                     v{settings.APP_VERSION}                          ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )