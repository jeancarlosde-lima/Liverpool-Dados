import matplotlib.pyplot as plt # type: ignore

# Dados para os gráficos

# 1. Infraestrutura da Academia
infraestrutura = {
    "Campos de Treinamento": 10,
    "Ginásios": 5,
    "Instalações de Reabilitação": 3,
    "Salas de Análise de Desempenho": 2
}

# 2. Filosofia de Treinamento
filosofia_treinamento = {
    "Técnico": 40,
    "Físico": 30,
    "Mental": 30
}

# 3. Programa de Desenvolvimento
categorias = ["Sub-18", "Sub-23", "Time Principal"]
num_jogadores = [20, 15, 25]

# 4. Casos de Sucesso
jogadores = ["Trent Alexander-Arnold", "Curtis Jones", "Raheem Sterling", "Steven Gerrard"]
impacto = [95, 80, 90, 100]
anos_no_clube = [5, 3, 4, 15]

# Funções para criar os gráficos

def grafico_infraestrutura(dados):
    plt.figure(figsize=(10, 6))
    plt.bar(dados.keys(), dados.values(), color='skyblue')
    plt.title('Infraestrutura da Academia de Treinamento')
    plt.xlabel('Facilidades')
    plt.ylabel('Quantidade')
    plt.show()

def grafico_filosofia(dados):
    plt.figure(figsize=(8, 8))
    plt.pie(dados.values(), labels=dados.keys(), autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
    plt.title('Filosofia de Treinamento')
    plt.show()

def grafico_programa(categorias, jogadores):
    plt.figure(figsize=(10, 6))
    plt.plot(categorias, jogadores, marker='o', linestyle='-', color='green')
    plt.title('Trajetória dos Jovens Talentos')
    plt.xlabel('Categorias')
    plt.ylabel('Número de Jogadores')
    plt.show()

def grafico_casos_sucesso(jogadores, impacto, anos_no_clube):
    plt.figure(figsize=(10, 6))
    plt.scatter(anos_no_clube, impacto, color='purple', s=100)
    for i, jogador in enumerate(jogadores):
        plt.text(anos_no_clube[i], impacto[i], jogador)
    plt.title('Impacto dos Jogadores-Chave')
    plt.xlabel('Anos no Clube')
    plt.ylabel('Impacto no Time Principal')
    plt.show()

# Chamando as funções para exibir os gráficos

grafico_infraestrutura(infraestrutura)
grafico_filosofia(filosofia_treinamento)
grafico_programa(categorias, num_jogadores)
grafico_casos_sucesso(jogadores, impacto, anos_no_clube)
