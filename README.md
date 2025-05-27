# Análise de Dados do FIES 2021 - UFRPE

![UFRPE Logo](https://www.ufrpe.br/sites/www.ufrpe.br/files/Logo%20UFRPE%20com%20texto_2.png)

Projeto de análise de dados do Fundo de Financiamento Estudantil (FIES) referente ao primeiro semestre de 2021, desenvolvido como atividade da Especialização em Tomada de Decisão Baseada em Evidências da UFRPE.

## 📋 Descrição do Projeto

Este projeto tem como objetivo analisar os dados de oferta do FIES no primeiro semestre de 2021, extraindo informações relevantes sobre a distribuição de recursos entre instituições de ensino, mantenedoras e municípios brasileiros.

**Disciplina**: Literacia em Dados e Métodos Quantitativos  
**Instituição**: Universidade Federal Rural de Pernambuco (UFRPE)  
**Curso**: Especialização em Tomada de Decisão Baseada em Evidências

## 🎯 Objetivos Principais

1. Identificar padrões na distribuição de recursos do FIES
2. Apontar as instituições e mantenedoras que mais receberam financiamento
3. Analisar a distribuição geográfica dos recursos
4. Gerar visualizações e relatórios para tomada de decisão

## 📊 Dados Analisados

- **Fonte**: Dados oficiais do FIES - 1º semestre de 2021
- **Arquivo**: `Literacia_fies_oferta_2021_1.csv`
- **Variáveis principais**:
  - Nome da IES
  - Nome Mantenedora
  - UF da IES
  - Município do Local de Oferta
  - Valores por semestre do FIES

## ⚙️ Funcionalidades do Script

O script `app.py` realiza as seguintes operações:

1. **Carregamento e limpeza dos dados**:

   - Conversão de formatos numéricos
   - Tratamento de valores missing

2. **Análises principais**:

   - Top 5 instituições com mais registros
   - Top 5 estados com mais ofertas FIES
   - Mantenedora que mais recebeu recursos
   - Top 10 municípios por valor recebido

3. **Visualização**:

   - Geração automática de gráfico de barras horizontais
   - Criação de relatório em PDF com tabelas e gráfico

4. **Geração de relatório**:
   - PDF contendo todas as análises
   - Visualização clara e organizada dos resultados

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- Bibliotecas:
  - pandas (análise de dados)
  - matplotlib (visualização)
  - fpdf (geração de relatórios PDF)

## 📂 Estrutura do Projeto

SEMANA 3/
├── .venv/ # Ambiente virtual Python
├── dados/
│ └── Literacia_fies_oferta_2021_1.csv # Dados originais
├── app.py # Script principal
├── grafico_municipios.png # Gráfico gerado
├── relatorio_fies.pdf # Relatório final
├── README.md # Este arquivo
└── requirements.txt # Dependências do projeto

## 🚀 Como Executar

1. **Pré-requisitos**:

   - Python 3.x instalado
   - pip para gerenciamento de pacotes

2. **Configuração do ambiente**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   .venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   Execução:
   ```

bash
python app.py
Saídas esperadas:

Gráfico: grafico_municipios.png

Relatório: relatorio_fies.pdf

Resultados no terminal

📌 Principais Resultados
O relatório final responde às seguintes questões:

a) Informações interessantes:

Distribuição geográfica dos recursos

Concentração por instituições/mantenedoras

b) Mantenedora que mais recebeu recursos

c) Top 10 municípios por valor recebido

📝 Considerações Finais
Este projeto demonstra a aplicação de métodos quantitativos para análise de políticas públicas de educação, proporcionando insights valiosos para tomada de decisão baseada em evidências.

📚 Referências
Ministério da Educação - Dados abertos

Documentação oficial das bibliotecas utilizadas

Material didático da UFRPE
