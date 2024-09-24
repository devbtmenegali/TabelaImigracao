import pandas as pd
import numpy as np

def importar_dados():
    url = "https://raw.githubusercontent.com/alura-cursos/bibliotecas_visualizacao/main/Dados/imigrantes_canada.csv"
    leitura_dos_dados = pd.read_csv(url, sep=",")
    return leitura_dos_dados

def manipulacao_dos_dados(leitura_dos_dados, pais):
    anos = leitura_dos_dados.columns[4:]
    
    #.loc[] seleciona os dados dessa linha, e .values.flatten() transforma essa linha em um array unidimensional (uma lista de valores numéricos).
    imigrantes_pais = leitura_dos_dados.loc[leitura_dos_dados['País'] == pais, anos].values.flatten()
    
    # Usando np.mean() para calcular a média
    media = np.mean(imigrantes_pais)  
    
    print(f"A média anual de imigrantes de {pais} para o Canadá é: {media:.2f}")

def main():
    dados = importar_dados() 
    manipulacao_dos_dados(dados, "Brasil") 

if __name__ == "__main__":
    main()
