import pandas as pd
import matplotlib.pyplot as plt

# Carregando os dados CSV
caminho_csv = 'dados/Literacia_fies_oferta_2021_1.csv'
df = pd.read_csv(caminho_csv, sep=',', encoding='latin1')

# Convertendo colunas de valores
valor_cols = [col for col in df.columns if 'Semestre Fies' in col]

for col in valor_cols:
    df[col] = df[col].replace('-', '0')
    df[col] = df[col].str.replace('.', '', regex=False).str.repleace(',', '.', regex=False).astype(float)

# Criando coluna com valor total por curso
df['Valor Total FIES'] = df[valor_cols].sum(axis=1)

# (a) Apresentando informações interessantes
print("Instituições com mais registros na base:")
print(df['Nome da IES'].value_counts().head())

print("\nEstados com mais ofertas FIES:")
print(df['UF da IES'].value_counts().head())

# (b) Instituição Mantenedora que recebeu mais valor
mantenedoras = df.groupby('Nome Mantenedora')['Valor Total FIES'].sum()
mantenedora_top = mantenedoras.sort_values(ascending=False).head(1)
print("\nInstituição Mantenedora que mais recebeu recursos do FIES:")
print(mantenedora_top)

# (c) Gráfico dos 10 municípios que mais receberam valores
municipios = df.groupby('Município do Local de Oferta')['Valor Total FIES'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
municipios.plot(kind='barh', color='skyblue')
plt.title('Top 10 Municípios que mais receberam valores do FIES')
plt.xlabel('Valor Total Recebido (R$)')
plt.ylabel('Município')
plt.gca().invert_yaxis()  # Coloca o maior valor no topo
plt.tight_layout()
plt.show()