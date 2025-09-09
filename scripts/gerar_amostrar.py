import pandas as pd
from pathlib import Path

# 📁 Caminhos do arquivo original e destino da amostra
CAMINHO_ORIGEM = Path("C:/Projetos/pto_nasa/data/NASA_Exoplanet_Composite.csv")
CAMINHO_DESTINO = Path("C:/Projetos/pto_nasa/data/amostra_final.csv")

# 🎯 Parâmetros da amostra
TAMANHO_LINHAS = 100
TAMANHO_COLUNAS = 100
SEMENTE = 42

# 📥 Etapa 1: Carregar o arquivo original com segurança
try:
    df = pd.read_csv(CAMINHO_ORIGEM, on_bad_lines='skip', sep=',', encoding='utf-8', low_memory=False)
    print("✅ Arquivo carregado com sucesso.")
except FileNotFoundError:
    print(f"❌ Arquivo não encontrado: {CAMINHO_ORIGEM}")
    exit()

# 🧼 Etapa 2: Padronizar nomes de colunas (sem espaços, símbolos ou maiúsculas)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace(r"[^\w\s]", "", regex=True)
)

# 🧹 Etapa 3: Remover colunas irrelevantes (links, flags, 100% nulas)
colunas_remover = [col for col in df.columns if col.endswith("_reflink") or col.endswith("_flag")]
df.drop(columns=colunas_remover, inplace=True, errors="ignore")
df.dropna(axis=1, how="all", inplace=True)

# 🔄 Etapa 4: Converter colunas numéricas (mesmo que estejam como texto com vírgula ou ponto)
for col in df.columns:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", ".")  # Troca vírgula por ponto para conversão
        .replace("nan", pd.NA)
    )
    try:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    except:
        pass  # Se não for possível converter, mantém como está

# 📊 Etapa 5: Selecionar as 100 colunas mais relevantes
# Critérios: pelo menos 10 valores válidos e variabilidade
colunas_validas = df.dropna(axis=1, thresh=10)
colunas_variaveis = colunas_validas.loc[:, colunas_validas.nunique() > 1]
colunas_top = colunas_variaveis.isna().sum().sort_values().index[:TAMANHO_COLUNAS]

# 🧾 Etapa 6: Criar amostra com 100 linhas e 100 colunas
df_amostra = df[colunas_top].head(TAMANHO_LINHAS)

# 💡 Etapa 7: Formatar números para padrão brasileiro (vírgula decimal)
df_amostra_formatada = df_amostra.applymap(
    lambda x: f"{x:.6f}".replace(".", ",") if isinstance(x, float) else x
)

# 💾 Etapa 8: Salvar CSV com separador de campo como ponto e vírgula
CAMINHO_DESTINO.parent.mkdir(parents=True, exist_ok=True)
df_amostra_formatada.to_csv(CAMINHO_DESTINO, index=False, sep=";", encoding="utf-8")

print(f"✅ Amostra final salva com sucesso em: {CAMINHO_DESTINO}")
