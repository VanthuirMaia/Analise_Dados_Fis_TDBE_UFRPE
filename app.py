import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF
from fpdf.enums import XPos, YPos

def carregar_dados(caminho_csv):
    df = pd.read_csv(caminho_csv, sep=';', decimal=',', encoding='latin1')
    return df

def processar_valores(df):
    valor_cols = [col for col in df.columns if 'Semestre Fies' in col]
    for col in valor_cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace(r'^\s*-\s*$', '0', regex=True)
        df[col] = df[col].str.replace('.', '', regex=False).str.replace(',', '.', regex=False)
        df[col] = df[col].astype(float)
    df['Valor Total FIES'] = df[valor_cols].sum(axis=1)
    return df, valor_cols

def gerar_grafico(municipios, caminho_imagem='grafico_municipios.png'):
    plt.figure(figsize=(10,6))
    municipios.plot(kind='barh', color='skyblue')
    plt.title('Top 10 Municípios que mais receberam valores do FIES')
    plt.xlabel('Valor Total Recebido (R$)')
    plt.ylabel('Município')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.savefig(caminho_imagem)
    plt.close()

def adiciona_tabela(pdf, titulo, dataframe, max_linhas=5):
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 10, titulo, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font("Helvetica", '', 10)

    colunas = list(dataframe.columns)
    largura_total = pdf.w - 2 * pdf.l_margin

    if len(colunas) > 1:
        # 50% da largura para primeira coluna (geralmente nome)
        largura_primeira_coluna = largura_total * 0.5
        largura_outras_colunas = (largura_total - largura_primeira_coluna) / (len(colunas) - 1)
        larguras = [largura_primeira_coluna] + [largura_outras_colunas] * (len(colunas) - 1)
    else:
        larguras = [largura_total]

    # Cabeçalho
    for i, col in enumerate(colunas):
        pdf.cell(larguras[i], 8, str(col), border=1)
    pdf.ln(8)

    # Linhas
    for i, row in dataframe.head(max_linhas).iterrows():
        for j, item in enumerate(row):
            texto = f"{item:,.2f}" if isinstance(item, (float, int)) else str(item)
            pdf.cell(larguras[j], 8, texto, border=1)
        pdf.ln(8)
    pdf.ln(5)

def gerar_pdf(df, mantenedoras, municipios, caminho_grafico='grafico_municipios.png', caminho_pdf='relatorio_fies.pdf'):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    pdf.set_font("Helvetica", 'B', 16)
    pdf.cell(0, 10, "UFRPE", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, "Tomada de Decisão Baseada em Evidências", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, "Disciplina: Literacia em Dados e Métodos Quantitativos", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.cell(0, 10, "Relatório FIES 2021", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.ln(10)
    pdf.set_font("Helvetica", 'B', 12)
    pdf.cell(0, 10, "a) Aponte ao menos 2(duas) informações interessantes que são possíveis de obter com esses dados", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # Preparar dados para tabelas (convertendo Series para DataFrame com colunas nomeadas)
    tabela_ies = df['Nome da IES'].value_counts().head().reset_index()
    tabela_ies.columns = ['Nome da IES', 'Quantidade de Registros']

    tabela_estados = df['UF da IES'].value_counts().head().reset_index()
    tabela_estados.columns = ['UF', 'Quantidade de Registros']

    mantenedora_top = mantenedoras.sort_values(ascending=False).head(1).reset_index()
    mantenedora_top.columns = ['Nome Mantenedora', 'Total Valor FIES']

    tabela_municipios = municipios.reset_index()
    tabela_municipios.columns = ['Município', 'Total Valor FIES']

    # Adiciona tabelas ao PDF
    adiciona_tabela(pdf, "Instituições com mais registros na base:", tabela_ies)
    adiciona_tabela(pdf, "Estados com mais ofertas FIES:", tabela_estados)
    adiciona_tabela(pdf, "b) Instituição Mantenedora que mais recebeu recursos do FIES:", mantenedora_top)
    adiciona_tabela(pdf, "c) Top 10 Municípios que mais receberam valores do FIES:", tabela_municipios, max_linhas=10)

    # Adiciona gráfico
    pdf.image(caminho_grafico, x=10, w=pdf.w - 20)

    pdf.output(caminho_pdf)
    print(f"PDF gerado: {caminho_pdf}")

def main():
    caminho_csv = 'dados/Literacia_fies_oferta_2021_1.csv'

    df = carregar_dados(caminho_csv)
    df, valor_cols = processar_valores(df)

    print("Instituições com mais registros na base:")
    print(df['Nome da IES'].value_counts().head(), '\n')

    print("Estados com mais ofertas FIES:")
    print(df['UF da IES'].value_counts().head(), '\n')

    mantenedoras = df.groupby('Nome Mantenedora')['Valor Total FIES'].sum()
    mantenedora_top = mantenedoras.sort_values(ascending=False).head(1)
    print("Instituição Mantenedora que mais recebeu recursos do FIES:")
    print(mantenedora_top, '\n')

    municipios = df.groupby('Município do Local de Oferta')['Valor Total FIES'].sum().sort_values(ascending=False).head(10)

    gerar_grafico(municipios)

    gerar_pdf(df, mantenedoras, municipios)

    # Mostrar gráfico opcionalmente
    municipios.plot(kind='barh', color='skyblue', figsize=(10,6), title='Top 10 Municípios que mais receberam valores do FIES')
    plt.xlabel('Valor Total Recebido (R$)')
    plt.ylabel('Município')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    main()
