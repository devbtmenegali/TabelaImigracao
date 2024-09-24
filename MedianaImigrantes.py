'''

to_numeric(): Função que converte os elementos de um array, série ou coluna para valores numéricos. 
Se os valores já forem numéricos, a função não altera nada. Se houver valores não numéricos, você pode especificar 
como lidar com eles usando o parâmetro errors.

errors='coerce': define como a função deve lidar com valores que não podem ser convertidos em números. 
'coerce': Se um valor não puder ser convertido para um número (por exemplo, um texto ou caractere inválido), 
ele será transformado em NaN (Not a Number) - padrão de valores nulos (pandas).

Outras opções possíveis para o parâmetro errors são:

errors='raise': Gera um erro se um valor não puder ser convertido. Este é o comportamento padrão se você não especificar 
o parâmetro errors.

errors='ignore': Mantém o valor original caso ele não possa ser convertido (não faz nenhuma conversão no valor inválido).

'''

import pandas as pd
import numpy as np

def calcular_mediana_imigracao(dados,pais):
    # Selecionar as colunas de anos (a partir da quarta coluna em diante)
    anos = dados.columns[4:]

    # Filtrar os dados para o país específico
    imigrantes_pais = dados.loc[dados['País'] == pais, anos].values.flatten()

    # Converter para valores numéricos, ignorando NaNs
    imigrantes_pais = pd.to_numeric(imigrantes_pais, errors='coerce')
    # Remover NaNs
    imigrantes_pais = imigrantes_pais[~np.isnan(imigrantes_pais)]  
    
    # Calcular a mediana
    if len(imigrantes_pais) > 0:
        mediana = np.median(imigrantes_pais)
        print(f"A mediana anual de imigrantes de {pais} para o Canadá é: {mediana:.2f}")
    else:
        print(f"Não há dados suficientes para calcular a mediana de imigração para {pais}.")


def main():

    # URL dos dados
    url = "https://raw.githubusercontent.com/alura-cursos/bibliotecas_visualizacao/main/Dados/imigrantes_canada.csv"

    # Carregar os dados a partir do CSV
    dados = pd.read_csv(url, sep = ",")        
    
    # Exemplo: Calcular a mediana para o Brasil
    calcular_mediana_imigracao(dados, "Argentina")

if __name__ =="__main__":
    
    main()
