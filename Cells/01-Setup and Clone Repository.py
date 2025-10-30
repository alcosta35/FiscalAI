# ==========================================
# CÉLULA 1: Clone Repository and Install Dependencies
# ==========================================
import os
from google.colab import drive

print("🚀 FiscalAI - Setup Inicial")
print("=" * 60)

# Mount Google Drive (for persistent storage)
print("\n📁 Montando Google Drive...")
drive.mount('/content/drive', force_remount=True)
print("✅ Drive montado")

# Clone repository (replace with your GitHub URL)
GITHUB_URL = "https://github.com/YOUR_USERNAME/FiscalAI.git"

print(f"\n📥 Clonando repositório...")
print(f"   {GITHUB_URL}")

# Remove old version if exists
if os.path.exists('/content/FiscalAI'):
    !rm -rf /content/FiscalAI

# Clone
!git clone {GITHUB_URL} /content/FiscalAI

# Verify clone
if os.path.exists('/content/FiscalAI'):
    print("✅ Repositório clonado com sucesso!")
else:
    print("❌ Erro ao clonar repositório")
    raise Exception("Clone failed")

# Install dependencies
print("\n📦 Instalando dependências...")
!pip install -q -r /content/FiscalAI/requirements.txt

print("\n✅ Setup completo!")