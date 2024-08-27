import os

class CloudDatabase:
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def search_by_url(self, url):
        results = []
        for file_name in os.listdir(self.dir_name):
            if file_name.endswith('.txt'):
                with open(os.path.join(self.dir_name, file_name), 'r') as f:
                    for line in f.readlines():
                        if url in line:
                            results.append(line.strip())
        return results

    def search_by_keyword(self, keyword):
        results = []
        for file_name in os.listdir(self.dir_name):
            if file_name.endswith('.txt'):
                with open(os.path.join(self.dir_name, file_name), 'r') as f:
                    for line in f.readlines():
                        if keyword in line:
                            results.append(line.strip())
        return results

def main():
    dir_name = 'db'
    if os.path.exists(dir_name):
        cloud_db = CloudDatabase(dir_name)
    else:
        print("Erro: Diretório não encontrado.")
        return

    print("Bem-vindo ao Cloud Database!")
    painel_login = """
____ ____ __   ____ ____ ____   ____ __   ____ _    ___  
|  _\|___\| |  |_ _\| __\| . \  | __\| |  |   ||| \ |  \ 
| _\ | /  | |__  || |  ]_|  <_  | \__| |__| . |||_|\| . \
|/   |/   |___/  |/ |___/|/\_/  |___/|___/|___/|___/|___/
"""
    print(painel_login)

    while True:
        print("\nOpções:")
        print("[1] Buscar por URL")
        print("[2] Buscar por Palavra Chave")
        print("[3] Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            url = input("Digite a URL: ")
            results = cloud_db.search_by_url(url)
            if results:
                print(f'Resultados encontrados para "{url}":')
                for result in results:
                    print(result)
            else:
                print(f'Nenhum resultado encontrado para "{url}"')
        elif opcao == "2":
            keyword = input("Digite a palavra-chave: ")
            results = cloud_db.search_by_keyword(keyword)
            if results:
                print(f'Resultados encontrados para "{keyword}":')
                for result in results:
                    print(result)
            else:
                print(f'Nenhum resultado encontrado para "{keyword}"')
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()