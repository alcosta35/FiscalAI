# ==========================================
# CÉLULA 3: Configure OpenAI API Key
# ==========================================
from google.colab import userdata
import os

print("🔑 Configurando OpenAI API Key")
print("=" * 60)

os.chdir('/content/FiscalAI')

try:
    # Get from Colab Secrets
    openai_key = userdata.get('OPENAI_API_KEY')
    
    # Create .env file
    with open('.env', 'w') as f:
        f.write(f'OPENAI_API_KEY={openai_key}\n')
    
    masked = openai_key[:10] + "..." + openai_key[-4:]
    print(f"✅ API Key configurada: {masked}")
    
except Exception as e:
    print(f"❌ Erro: {e}")
    print("\n⚠️ Por favor, adicione OPENAI_API_KEY nos Secrets do Colab:")
    print("   1. Clique no ícone 🔑 na barra lateral")
    print("   2. Adicione novo secret")
    print("   3. Nome: OPENAI_API_KEY")
    print("   4. Valor: sua chave OpenAI (sk-...)")
    print("   5. Ative 'Notebook access'")