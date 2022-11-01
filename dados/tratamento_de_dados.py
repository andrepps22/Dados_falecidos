from BD.banco_de_dados  import Falecidos, session
from sqlalchemy.future import select
from datetime import datetime
from dados.tratar_data_e_idade import formatar_data, formatar_idade


def tratamento_e_insercao():
    lista_dados = []
    temp = {}
    cont = 0


    # Lendo arquivo de Guarapuava
    with open('falecidos_guarapuava.txt', 'r') as file:
        arquivos = file.readlines()
        
        for linha in arquivos:
            linha = linha.replace('\n', '')
            linhaseparada = linha.split(':') 
            temp[linhaseparada[0]] = linhaseparada[-1]
            if linha.__contains__('FUNERARIA:'):
                temp['CIDADE'] = 'GUARAPUAVA'
                lista_dados.append(temp.copy())
                temp.clear()



    # Lendo arquivo de Curitiba
    with open('falecidos_curitiba.txt', 'r') as file:
        arquivo = file.readlines()
        for index, linha in enumerate(arquivo):
            linha = linha.upper()
            if linha.__contains__(':\n'):
                temp[linha.replace(':\n', '')] = arquivo[index + 1].replace('\n', '').rstrip()
            if linha == 'FUNERARIA:\n':
                temp['CIDADE'] = 'CURITIBA'
                lista_dados.append(temp.copy())
                temp.clear()



    # Lendo arquivo de Foz do Iguaçu
    with open('falecidos_foz.txt', 'r') as file:
        arquivo = file.readlines()
        for index, linha in enumerate(arquivo):
            linha = linha.upper()
            if linha.__contains__('/'):
                linha = linha.replace(':', ';')
            linha = linha.replace('\n', '')

            if linha.__contains__(':'):
                temp['CIDADE'] = 'FOZ DO IGUAÇU'

                if linha == 'FILIACAO:':
                    filicao = arquivo[index + 1].split('&')
                    temp['NOME DO PAI'] = filicao[0].replace('\n', '')
                    temp['NOME DA MAE'] = filicao[1].replace('\n', '')

                if linha == 'FALECIMENTO: ':
                    data = arquivo[index + 1].replace('\n', '')
                    temp['DATA DE FALECIMENTO'] = data[:10]

                temp[linha.strip().replace(':', '')] = arquivo[index + 1].replace('\n', '')
                temp['NUMERO DA FAF'] = ''
                temp.pop('FILIACAO', None)
                temp.pop('FALECIMENTO', None)

            if linha == 'DATA SEPULTAMENTO:':
                lista_dados.append(temp.copy())
                temp.clear()




    # Lendo arquivo de Foz do Iguaçu
    with open('falecidos_campo_largo.txt', 'r') as file:
        arquivo = file.readlines()
        for index, linha in enumerate(arquivo):
            linha = linha.upper()

            linha = linha.replace('\n', '')
            if linha.__contains__(':'):
                temp['CIDADE'] = 'CAMPO LARGO'
                linha = linha.split(':')
                if linha.__contains__('PAI'):
                    temp['NOME DO PAI'] = linha[1]
                if linha.__contains__('MAE'):
                    temp['NOME DA MAE'] = linha[1]
                if not linha.__contains__('DATA DO FALECIMENTO'):
                    temp['DATA DO FALECIMENTO'] = ''
                temp[linha[0]] = linha[1]
                temp['NUMERO DA FAF'] = ''
                temp.pop('MAE', None)
                temp.pop('PAI', None)

            if linha[0] == 'FUNERARIA':
                lista_dados.append(temp.copy())
                temp.clear()



    # inserindo os dado na tabala do banco
    for valor in lista_dados:

        data_insercao = datetime.now()
        nome = valor['NOME']
        idade = formatar_idade(valor['IDADE'])
        nome_do_pai = valor['NOME DO PAI']
        nome_da_mae = valor['NOME DA MAE']
        try:
            data_do_falecimento = formatar_data(valor['DATA DE FALECIMENTO'])
        except:
            data_do_falecimento = formatar_data(valor['DATA DO FALECIMENTO'])
        numero_da_faf = valor['NUMERO DA FAF']
        cidade = valor['CIDADE']

        query = session.execute(
                select(Falecidos).where(
                    Falecidos.nome == nome,
                    Falecidos.idade == idade,
                    Falecidos.nome_da_mae == nome_da_mae
                ))
        result = query.scalars().all()

        # Se o resultado da buscar troucer valores(True) não insere nenhum dados pois está repitido, caso não traga nenhum resultado(False) insere os dados na instancia do banco.
        if result:
            session.commit()
            continue
        else:
            falecidos = Falecidos(data_insercao=data_insercao, nome=nome, idade=idade, nome_do_pai=nome_do_pai, nome_da_mae=nome_da_mae, data_do_falecimento=data_do_falecimento,
                                        numero_da_faf=numero_da_faf, cidade=cidade)
            session.add(falecidos)
            session.commit()
            cont += 1

    print(f'Foram inseridos {cont} registros')



if __name__=='__main__':
    tratamento_e_insercao()
    