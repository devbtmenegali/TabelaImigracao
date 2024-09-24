import pandas as pd
#import matplotlib.pyplot as plt

def baixar_dados():

    url_dados_csv = "https://raw.githubusercontent.com/alura-cursos/bibliotecas_visualizacao/main/Dados/imigrantes_canada.csv"

    leitura_dados = pd.read_csv(url_dados_csv,sep=",")

    return leitura_dados

def analise_dos_dados(leitura_dados, ano):

    mais_10k = leitura_dados[leitura_dados[ano] > 10000] 

    print (mais_10k[["País", ano]])

def main():

    ano = input("Escolha o ano: ")

    leitura_dados = baixar_dados()
    analise_dos_dados(leitura_dados,ano)

if __name__=="__main__":

    main()

