# Previsão de Custo Inicial para Franquias

Este projeto é uma aplicação simples de **Machine Learning** desenvolvida com **Streamlit** para prever o custo inicial de uma franquia com base na frequência anual de transações. O objetivo principal é apresentar uma solução interativa e funcional como parte do meu portfólio profissional.

---

## 📋 Funcionalidades

- **Exibição de Dados:** Mostra os primeiros registros do conjunto de dados para visualização.
- **Visualização Gráfica:** Um gráfico de dispersão exibe os dados e a linha de regressão.
- **Interatividade:** Permite ao usuário inserir a frequência anual para prever o custo inicial estimado.
- **Interface amigável:** Construída com Streamlit para facilitar o uso e a visualização.

---

## 🚀 Tecnologias Utilizadas

- **Python**
- **Streamlit**: Para a interface do usuário.
- **Pandas**: Para manipulação e organização dos dados.
- **Scikit-learn**: Para criação e treinamento do modelo de regressão linear.
- **Matplotlib**: Para visualizações gráficas.

---

## 📂 Estrutura do Repositório

```
├── slr12.csv              # Conjunto de dados usado no projeto.
├── reglin1.py             # Código principal do aplicativo Streamlit.
├── README.md              # Descrição do projeto.
├── requirements.txt       # Dependências do projeto.
```


---

## 📊 Modelo

O modelo utiliza **Regressão Linear Simples** fornecida pela biblioteca `scikit-learn`. A relação analisada é:

**Frequência Anual de Transações (Entrada)** ➡ **Custo Inicial da Franquia (Saída)**

---

## 🎨 Interface

- **Coluna 1:** Tabela mostrando os dados brutos.
- **Coluna 2:** Gráfico de dispersão com a linha de regressão ajustada.
- **Campo de entrada:** Permite ao usuário inserir a frequência anual de transações.
- **Botão de processamento:** Realiza a previsão com base no valor inserido.

---

## ⚙️ Como Rodar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/nayarasobral/project-regressao-linear-franquia/tree/main
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd project-regressao-linear-franquia
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo:
   ```bash
   streamlit run reglin1.py
   ```

---

## 📈 Exemplo de Uso

1. Insira a frequência anual de transações no campo de entrada.
2. Clique no botão **Processar**.
3. Veja a previsão de custo inicial para a franquia exibida na interface.

---

## 🗂️ Dataset

O conjunto de dados utilizado (`slr12.csv`) contém duas colunas:

- **FrqAnual:** Frequência anual de transações.
- **CusInic:** Custo inicial associado à franquia.

---

## 🔮 Resultado Esperado

- **Previsão precisa:** Com base na entrada fornecida, o modelo gera uma estimativa de custo inicial.
- **Gráficos intuitivos:** Visualize os dados e a linha de regressão em tempo real.

---

## 🛠️ Melhorias Futuras

- Adicionar suporte a outros modelos de Machine Learning.
- Permitir upload de novos conjuntos de dados pelo usuário.
- Melhorar a validação de entrada para valores extremos.

---

## 📝 Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🧑‍💻 Autor

- **[Nayara Sobral](https://www.linkedin.com/in/seu-perfil/)**  
   Cientista de Dados  
  - **Email:** nayysobrall@gmail.com
  - **GitHub:** [nayarasobral](https://github.com/nayarasobral)

---

Sinta-se à vontade para contribuir ou dar feedback! ⭐
```
