import json


#testa a existencia do arquivo.
def ler_arquivo(nome):
	try:
		a = open(nome, "rt")
		a.close()
	except:
		print("não existe este arquivo!")
		return False
	else:
		return True


#cria um arquivo e adiciona o conteudo.
def criar_arquivo(nome, item):
	try:
		a = open(nome, "wt+")
		#esse dados é o dicionario a ser adicionado.
		json.dump(item, a, ensure_ascii=False)
		a.close()
	except:
		print("errro 01")
	else:
		print(f"arquivo |{nome}| criado com sucesso!")


#import json
#carrega o conteudo do json para uma variavel.
def abrir_json(nome):
	try:
		a = open(nome, "rt")
		return json.load(a)
	except:
		print("erro 02")
	finally:
		a.close()



dados = {"bom": 12, "game": ["god", "mário", 10], "gol": "gàmeplay fantastica."}


arq = "games.json"


if not ler_arquivo(arq):
	criar_arquivo(arq, dados)

dici = abrir_json(arq)

print(dici["game"][1])
print("-------------")
print(dici["gol"])
