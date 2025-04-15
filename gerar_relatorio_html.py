#Kauan Sarzi da Rocha 10427235 Turma: 01J


#função para carregar os dados
def carregar_dados():
    dataset = []                    #lista que irá receber todos os dados do arquivo
    with open('emack.csv', 'r') as file: 
        linhas = file.readlines()
        cabecalho = linhas[0].strip().split(',')
        for linha in linhas[1:]:
            valores = linha.strip().split(',')
            produto = {}
            for i in range(len(cabecalho)):
                produto[cabecalho[i]] = valores[i]  #dicionário com a chave id e conteúdo c os outros valores
            dataset.append(produto)
    print (dataset)
    return dataset

#função para listar categorias
def listarCategorias(dados): #recebe como parametro dados, que é o dataset retornado pela função anterior
    categorias = []
    for produto in dados:
        if produto["categoryName"] not in categorias:
            categorias.append(produto["categoryName"])
    return categorias

#função que lista produtos por categoria
def listarProdutosCategoria(dados, categoria):
    produtos = []
    for produto in dados:
        if produto["categoryName"] == categoria:
            produtos.append(produto)
    return produtos

#
def ultVendaMes(produto):
    return int(produto["boughtInLastMonth"])



def cont_produtos_categoria(dados):
    contL = 0
    contC = 0
    contE = 0
    contEL = 0
    contM = 0
    contagem_categorias = []
    for produto in dados:
        categoria = produto["categoryName"]
        if categoria == "Livros":
            contL += 1
        elif categoria == "Casa":
            contC += 1
        elif categoria == "Esportes":
            contE += 1
        elif categoria == "EletrÃ´nicos":
            contEL += 1
        elif categoria == "Moda":
            contM += 1
    contagem_categorias.append(contL)
    contagem_categorias.append(contC)
    contagem_categorias.append(contE)
    contagem_categorias.append(contEL)
    contagem_categorias.append(contM)
    return contagem_categorias

def percentCategoria(dados,cont_produtos_categoria):
    porcentL = 0
    porcentC = 0
    porcentE = 0
    porcentEL = 0
    porcentM = 0
    contagem_categorias = cont_produtos_categoria(dados)
    produtosTotais = len(dados)
    porcentL = (contagem_categorias[0] / produtosTotais) * 100
    porcentC = (contagem_categorias[1] / produtosTotais) * 100
    porcentE = (contagem_categorias[2] / produtosTotais) * 100
    porcentEL = (contagem_categorias[3] / produtosTotais) * 100
    porcentM = (contagem_categorias[4] / produtosTotais) * 100
    return porcentL, porcentC, porcentE, porcentEL, porcentM


def best_sallers_categoria(dados):
    
     _ = cont_produtos_categoria(dados) 
     contL = 0
     contC = 0
     contE = 0
     contEL = 0
     contM = 0
     cont_bestSallers = []
     for produto in dados:
         
        if produto["isBestSeller"] == "true": 
            categoria = produto["categoryName"]
            if categoria == "Livros":
                 contL += 1
            elif categoria == "Casa":
                 contC += 1
            elif categoria == "Esportes":
                contE += 1
            elif categoria == "EletrÃ´nicos":
                contEL += 1
            elif categoria == "Moda":
                contM += 1
     cont_bestSallers.append(contL)
     cont_bestSallers.append(contC)
     cont_bestSallers.append(contE)
     cont_bestSallers.append(contEL)
     cont_bestSallers.append(contM)
     proporcao_bestSellers = [cont_bestSallers[i] / _[i] * 100 for i in range(len(_))]
     return proporcao_bestSellers
                
                    




def preco_produto(produto):
    return float(produto["price"])
    
def top10_caros(dados):
    produtos_ordenados = sorted(dados, key = preco_produto)
    mais_caros = produtos_ordenados[-10:]  #10 primeiros   mesma ideia de contador
    return mais_caros

def top10_baratos(dados):
    produtos_ordenados = sorted(dados, key = preco_produto)
    mais_baratos = produtos_ordenados[:10] #10 ultimos(fatiamento)
    return mais_baratos

def listar_produtos_por_categoria(dados, categoria_escolhida): 
    item = listarProdutosCategoria(dados, categoria_escolhida)
    for item in dados:
        if item["categoryName"] == categoria_escolhida:
            return item 





def gerarHtml_BestSellers(dados):
    relatorio = "<html><head><title>Relatório Top 10 Best Sellers por Categoria</title></head><body>"
    categorias = listarCategorias(dados)
    for categoria in categorias:
        relatorio += f"<h1>{categoria}</h1>"
        produtos = listarProdutosCategoria(dados, categoria)
        produtos_ordenados = sorted(produtos, key=ultVendaMes)
        relatorio += "<ol>"
        for produto in produtos_ordenados[:10]:
            relatorio += f"<li>{produto['title']} - Quantidade Vendida: {produto['boughtInLastMonth']}</li>"
        relatorio += "</ol>"
    relatorio += "</body></html>"
    with open("relatorio_top_10_best_sellers.html", "w") as file:
        file.write(relatorio)


def gerarHtml_ProdutosPorCategoriaEscolhida(dados):
    css = """
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { color: #333; border-bottom: 2px solid #333; padding-bottom: 5px; }
        ul { padding-left: 20px; }
        li { margin-bottom: 5px; }
    </style>
    """
    categorias = listarCategorias(dados)
    print("Categorias disponíveis:")
    for i, categoria in enumerate(categorias, 1):
        print(f"{i} - {categoria}")
    escolha = int(input("Escolha o número da categoria que deseja listar os produtos: "))
    if 1 <= escolha <= len(categorias):
        categoria_escolhida = categorias[escolha - 1]
        produtos = listarProdutosCategoria(dados, categoria_escolhida)
        relatorio = f"<html><head><title>Relatório de Produtos - {categoria_escolhida}</title>"
        relatorio += css
        relatorio += "</head><body>"
        relatorio += f"<h1>{categoria_escolhida}</h1>"
        relatorio += "<ul>"
        for produto in produtos:
            relatorio += f"<li>ID: {produto['id']}, Título: {produto['title']}, Preço: {produto['price']}, Vendidos no Último Mês: {produto['boughtInLastMonth']}</li>"
        relatorio += "</ul>"
        relatorio += "</body></html>"
        filename = f"relatorio_produtos_{categoria_escolhida.lower().replace(' ', '_')}.html"
        with open(filename, "w") as file:
            file.write(relatorio)
        print(f"Relatório de produtos da categoria '{categoria_escolhida}' gerado: {filename}")
    else:
        print("Escolha inválida.")




#apresenta o menu
def menu():
    print ("1- contagem de produtos por categoria")
    print("2- percentual de produtos por categoria")
    print("3- Avaliar a proporção de produtos best-sellers em cada categoria")
    print("4- Identificar os 10 produtos mais caros e mais baratos no geral")
    print("5- Listar os produtos por categoria escolhida ")
    print("6- Gerar um relatório em HTML demonstrando os Top 10 bestsellers por categoria")
    op = int(input())
    return op

#programa principal
dados = carregar_dados() # carregar dados/ dataset que é retornado nessa função é atribuido a DADOS, que tem acesso global
while True:
    opcao = menu()
    if opcao == 7:
        break
    if opcao == 1:
        resposta = cont_produtos_categoria(dados)
        print("Livros:", resposta[0])
        print("Casa:", resposta[1])
        print("Esporte:", resposta[2])
        print("EletrÃ´nicos:", resposta[3])
        
        print("Moda:",resposta[4])

    elif opcao == 2:
       percentual = percentCategoria(dados, cont_produtos_categoria)
       print("Livros:", percentual[0])
       print("Casa:", percentual[1])
       print("Esporte:", percentual[2])
       print("EletrÃ´nicos:", percentual[3])
       print("Moda:", percentual[4])


    elif opcao == 3:
        best_sellers = best_sallers_categoria(dados)
        print("Livros:", best_sellers[0],"%")
        print("Casa:", best_sellers[1],"%")
        print("Esporte:", best_sellers[2],"%")
        print("EletrÃ´nicos:", best_sellers[3],"%")
        print("Moda:", best_sellers[4],"%")
        


    elif opcao == 4:
        resp = top10_caros(dados)
        print("TOP 10 PRODUTOS MAIS CAROS")
        for item in resp:
            for chave,valor in item.items():
                print(chave,":",valor)
                print("-" * 60)
        resp = top10_baratos(dados)
        print("TOP 10 PRODUTOS MAIS BARATOS")
        for item in resp:
            for chave,valor in item.items():
                print(chave,":",valor)
                print("-" * 60)
        
                
    elif opcao == 5:
         gerarHtml_ProdutosPorCategoriaEscolhida(dados)
         print("-="*30)  
  

    elif opcao == 6:
      gerarHtml_BestSellers(dados)
      print("Relatório gerado")
