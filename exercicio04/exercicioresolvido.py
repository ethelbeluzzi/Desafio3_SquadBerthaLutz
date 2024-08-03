import colorama
from colorama import Fore,Style

#Criando dicionario

contatos = {
    'Ethel': '91234-5678',
    'Hyngrid': '92345-6789',
    'Karine Yasmin': '93456-7890',
    'Larissa': '94567-8901',
    'Louise': '95678-9012',
    'Marina': '96789-0123',
    'Natália': '97890-1234',
    'Sofia': '98901-2345'
}

#Solicitando o nome d0 contato ao usuário
nome_procurado = str(input('Digite o nome que você procura: '))

#Verificando se o nome solicitado está no dicionário
if nome_procurado in contatos:
    print(f'Nome: {Fore.LIGHTYELLOW_EX}{nome_procurado}{Style.RESET_ALL}')
    print(f'Telefone:{Fore.LIGHTWHITE_EX} {contatos[nome_procurado]}{Style.RESET_ALL}')
else:
    print(f'{Fore.RED}Nome não encontrado!{Style.RESET_ALL}')