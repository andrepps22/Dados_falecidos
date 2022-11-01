import locale
from datetime import datetime


def formatar_data(date):
    '''
       Recebe uma data por ex: 'sexta-feira, 9 de outubro de 2022' e retorna 09-10-2022
    '''
    locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
    date = date.strip()
    if date == '':
        return None
    if date.__contains__('/'):
        data_nova = date.split('/')
        data_tratada = datetime.strptime(
        f'{data_nova[0]}-{data_nova[1]}-{data_nova[2]}', '%d-%m-%Y')
        return data_tratada.date()

    else:
        data_nova:str = date.split(' ')
        data_tratada = datetime.strptime(
            f'{data_nova[1]}-{data_nova[3]}-{data_nova[-1]}', '%d-%B-%Y')
        return data_tratada.date()
    


def formatar_idade(idade: str):
    '''
        Recebe a idade passada por ex: '25 anos(s) e retora somente o numero inteiro(int)
    '''
    idade_tratada = ''
    for n in idade:
        if n.isnumeric():
            idade_tratada += n
    if idade_tratada == '':
        return 0
    
    return int(idade_tratada)

if __name__=='__main__':
    print(formatar_data('27/10/2022'))
    print(formatar_data('quinta-feira, 27 de outubro de 2022'))
    print(formatar_data('30/10/2022 AS 20:10:00'))