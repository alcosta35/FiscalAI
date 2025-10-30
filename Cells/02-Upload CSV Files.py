# ==========================================
# CÉLULA 2: Upload CSV Files
# ==========================================
from google.colab import files
import shutil
import os

print("📤 Upload dos arquivos CSV")
print("=" * 60)
print("Por favor, faça upload de:")
print("  1. 202401_NFs_Cabecalho.csv")
print("  2. 202401_NFs_Itens.csv")
print("  3. CFOP.csv")
print()

# Create data directory
os.makedirs('/content/data', exist_ok=True)

# Upload files
uploaded = files.upload()

# Move to data directory
print("\n📦 Movendo arquivos para /content/data/...")
for filename in uploaded.keys():
    source = filename
    dest = f'/content/data/{filename}'
    shutil.move(source, dest)
    size = os.path.getsize(dest)
    print(f"   ✅ {filename} ({size:,} bytes)")

print("\n✅ Arquivos CSV prontos!")