from tabulate import tabulate

def formatar__tabela(df):
    '''Retorna um tabela formatada para string
    Parametros:
    df:pd.DataFrame, tabela a ser formatada.
    '''
    tb = tabulate(
        df, headers="keys",
        tablefmt="simple_outline",
        showindex=False,
        numalign="left",
        floatfmt=".2f"
    )
    return tb


def gerar__metadados(df):
    '''
    Retorna metadados de uma tabela
    Parametros:
    df:pd.DataFrame, a tabela de onde os metadados serao gerados.
    '''
    # obtem os tipos de dados
    tipo_dados = df.dtypes

    # calcula a quantidade de nulos
    qtde_nulos = df.isnull().sum()
    estatisticas = df.describe(include='all').transpose()

    # cria um dataframe com algumas estatisticas
    df_metadados = pd.DataFrame({
    'Variável': tipo_dados.index,
    'Tipos de dados': tipo_dados.values,
    'Nulos': qtde_nulos.values,
    'Mínimo': estatisticas['min'],
    'Máximo': estatisticas['max'],
    'Média': estatisticas['mean'],
    })

    print(f'\n\nO DataFrame possui {df.shape[1]} colunas e {df.shape[0]} linhas:')
    print(formatar__tabela(df_metadados))
