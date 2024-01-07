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
