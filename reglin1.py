import streamlit as st      # Cria uma interface para o usuário interagir com o modelo.
import pandas as pd         # Organiza os dados.
from sklearn.linear_model import LinearRegression    # Treina e ajusta o modelo de regressão.
import matplotlib.pyplot as plt     # Gera visualizações da linha de regressão e dos dados.

st.title("Previsão inicial de Custo para nossa Franquia")

dados = pd.read_csv('slr12.csv', sep=";")

X = dados[['FrqAnual']] # dataframe usando dois [[]]
y = dados['CusInic']    # serie do pandas usando um []


modelo = LinearRegression().fit(X,y)
# LinearRegression() cria o modelo de regressão.
# .fit(X, y) ajusta o modelo aos dados fornecidos:


col1, col2 = st.columns(2)  #  organiza o layout da página Streamlit em duas colunas

with col1:                  # Dentro deste bloco, todos os elementos adicionados serão colocados na coluna
    st.header("Dados")      # Adiciona um título
    st.table(dados.head(10))    # Exibe os 10 primeiros registros do DataFrame dados

with col2:
    st.header("Gráfico de Disperssão")
    fig, ax = plt.subplots()      # Cria uma figura (fig) e um eixo (ax) usando o Matplotlib para renderizar o gráfico.
    ax.scatter(X, y, color='blue')  # Plota um gráfico de dispersão dos dados
    ax.plot(X, modelo.predict(X), color='red')  # Plota a linha de regressão ajustada pelo modelo
    st.pyplot(fig)      # Renderiza o gráfico Matplotlib (fig) na interface Streamlit.

st.header("Valor Anual da Franquia:")       # Exibe um cabeçalho na interface com o texto.
novo_valor = st.number_input("Insira Novo Valor",min_value=1.0, max_value=999999.0,value=1500.0, step=0.01)    
# Cria um campo de entrada numérica onde o usuário pode inserir um valor.
# min_value: Limite inferior permitido (1.0).
# max_value: Limite superior permitido (999999.0).
# value: Valor inicial padrão (1500.0).
# step: Incremento ou decremento ao ajustar o valor (0.01).
processar = st.button("Processar")      # Retorna True quando o botão é clicado, permitindo disparar ações no código

if processar:  # é verificar se o botão "Processar" foi clicado. Caso tenha sido, o código dentro desse bloco será executado.
    dados_novo_valor = pd.DataFrame([[novo_valor]], columns=['FrqAnual'])
# Cria um DataFrame do pandas com uma única linha e coluna.
# novo_valor: O valor inserido pelo usuário no campo numérico.
# columns=['FrqAnual']: Nomeia a coluna como "FrqAnual", representando o dado de entrada necessário para o modelo de previsão.
    prev = modelo.predict(dados_novo_valor)     # Chama o método predict de um objeto de modelo de Machine Learning (provavelmente treinado anteriormente).
    st.header(f"Previsão de Custo Inicial R$: {prev[0]:.2f}")
