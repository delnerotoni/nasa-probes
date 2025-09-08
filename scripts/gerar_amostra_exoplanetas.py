import pandas as pd
import os

# 🔹 Caminhos
CAMINHO_ORIGEM = "data/NASA_Exoplanet_Composite.csv"
CAMINHO_DESTINO = "data/tmp/exoplanetas_amostra.csv"

# 🔹 Parâmetros
TAMANHO_AMOSTRA = 300
SEMENTE = 42

# 🔹 Carregamento seguro
try:
    df = pd.read_csv(CAMINHO_ORIGEM, nrows=500)
    print(f"Arquivo carregado com sucesso: {CAMINHO_ORIGEM}")
except FileNotFoundError:
    print(f"❌ Arquivo não encontrado: {CAMINHO_ORIGEM}")
    exit()

# 🔹 Padronização de colunas
df.columns = (
    df.columns
      .str.strip()
      .str.lower()
      .str.replace(" ", "_")
      .str.replace("[^a-zA-Z0-9_]", "", regex=True)
)

# 🔹 Criação da amostra
amostra = df.sample(n=TAMANHO_AMOSTRA, random_state=SEMENTE)

# 🔹 Exportação
os.makedirs(os.path.dirname(CAMINHO_DESTINO), exist_ok=True)
amostra.to_csv(CAMINHO_DESTINO, index=False)

print(f"✅ Amostra salva com sucesso em: {CAMINHO_DESTINO}")

