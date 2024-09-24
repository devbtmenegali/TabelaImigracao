import pandas as pd
import matplotlib.pyplot as plt

def grafico_media_imigracao(dados, ano):

    media = dados[ano].mean()

    print(f"A média de imigrantes no ano de {ano} para todos os países é: {media:.2f}")

    # Dados para o gráfico
    paises = dados['País']
    imigrantes = dados[ano]

    # Criar o gráfico de barras
    plt.figure(figsize=(12, 6))
    plt.bar(paises, imigrantes, color='green')
    plt.axhline(y=media, color='red', linestyle='--', label=f'Média: {media:.2f}')
    plt.xticks(rotation=90)
    plt.title(f'Número de Imigrantes para o Canadá em {ano} por País')
    plt.ylabel('Número de Imigrantes')
    plt.legend()

    plt.tight_layout()
    plt.show()

def main():

    # URL dos dados
    url = "https://raw.githubusercontent.com/alura-cursos/bibliotecas_visualizacao/main/Dados/imigrantes_canada.csv"

    # Carregar os dados a partir do CSV
    dados = pd.read_csv(url, sep = ",")        
    
    grafico_media_imigracao(dados, '2010')


if __name__ =="__main__":
    
    main()


