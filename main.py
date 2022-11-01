from dados.tratamento_de_dados import tratamento_e_insercao
from dados.buscar_dados import buscar_dados_guar, buscar_dados_cwb, buscar_dados_foz,buscar_dados_campo_largo

if __name__=='__main__':
    buscar_dados_campo_largo()
    buscar_dados_foz()
    buscar_dados_guar()
    buscar_dados_cwb()
    tratamento_e_insercao()