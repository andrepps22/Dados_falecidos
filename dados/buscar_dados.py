from bs4 import BeautifulSoup as bs
import requests
import unidecode


def buscar_dados_guar():
    site = 'https://www.guarapuava.pr.gov.br/servicos/obituario/'

    pag = requests.get(site)

    soup = bs(pag.text, 'html.parser')

    texto = ''

    for palavra in soup.find_all('p'):
        p = palavra.get_text()
        
        unicode_string = unidecode.unidecode(p)

        texto += unicode_string + '\n'

    with open('falecidos_guarapuava.txt', 'w+') as file:
        file.write(str(texto))


def buscar_dados_cwb():
    """
        faz o scrap da pagina de obituarios da prefeitura e criar o arquivo falecidos.txt
    """
    pagina = 'https://obituarios.curitiba.pr.gov.br/publico/falecimentos.aspx'

    pag = requests.get(pagina)
    soup = bs(pag.text, 'html.parser')
    texto = ''

    # Faz a busca somente das TAG 'td' que estão dentro da TAG HTML TABLE/TR
    for palavra in soup.find_all('td'):
        p = palavra.get_text()  # Retira todas as TAGS HTML e retorna texto puro tratado

        # Retira acentos caracteres especias
        unicode_string = unidecode.unidecode(p)

        texto += unicode_string + '\n'  # Junto todo o texto tratado em uma variavel

    # Criar o arquivo txt dos dados colhidos
    with open('falecidos_curitiba.txt', 'w+') as file:
        file.write(str(texto))


def buscar_dados_foz():
    pagina = 'http://www3.pmfi.pr.gov.br/PSIPortal/SircofWeb/Formularios/wfrmSircObituario_Site.aspx'

    pag = requests.get(pagina)
    soup = bs(pag.text, 'html.parser')
    texto = ''

    for palavra in soup.find_all('td'):
        p = palavra.get_text()  # Retira todas as TAGS HTML e retorna texto puro tratado

        # Retira acentos caracteres especias
        unicode_string = unidecode.unidecode(p)        
        texto += unicode_string  # Junto todo o texto tratado em uma variavel

    # Criar o arquivo txt dos dados colhidos
    with open('falecidos_foz.txt', 'w+') as file:
        file.write(str(texto))


def buscar_dados_campo_largo():
    pagina = 'http://newintranet.campolargo.pr.gov.br/luto/obito/obitosdia'
    pag = requests.get(pagina)
    soup = bs(pag.text, 'html.parser')
    texto = ''


    for palavra in soup.find_all('p'):
        p = palavra.get_text()  # Retira todas as TAGS HTML e retorna texto puro tratado

        # Retira acentos caracteres especias
        unicode_string = unidecode.unidecode(p)        
        texto += unicode_string + '\n' # Junto todo o texto tratado em uma variavel

    # Criar o arquivo txt dos dados colhidos
    with open('falecidos_campo_largo.txt', 'w+') as file:
        file.write(str(texto))


if __name__=='__main__':
    buscar_dados_campo_largo()