# ==========================================
# CÉLULA 4: Iniciar Servidor
# ==========================================
import sys
import os
import nest_asyncio
from pyngrok import ngrok
import uvicorn
import threading
import time
from google.colab import userdata

print("🚀 Iniciando Servidor FiscalAI")
print("=" * 60)

# Setup
os.chdir('/content/FiscalAI')
sys.path.insert(0, '/content/FiscalAI')
nest_asyncio.apply()

# Configure ngrok
print("\n🔧 Configurando ngrok...")
NGROK_TOKEN = userdata.get('NGROK_AUTH_TOKEN')
ngrok.set_auth_token(NGROK_TOKEN)
print("✅ Ngrok configurado")

# Import app
print("\n📦 Importando aplicação...")
from main import app
print("✅ Aplicação importada")

# Create tunnel
print("\n🌐 Criando túnel público...")
public_url = ngrok.connect(8000)

print("\n" + "=" * 60)
print("  🎉 SERVIDOR PRONTO!")
print("=" * 60)
print(f"\n🌐 URL Pública: {public_url}")
print(f"📚 Documentação: {public_url}/docs")
print(f"💬 Chat: POST {public_url}/chat")
print("\n" + "=" * 60)

# Start server
def run_server():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")

server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

time.sleep(3)
print("\n✅ Servidor rodando!")
print("💡 Mantenha esta célula em execução\n")

# Keep alive
try:
    while True:
        time.sleep(60)
        print(".", end="", flush=True)
except KeyboardInterrupt:
    print("\n\n🛑 Servidor parado")