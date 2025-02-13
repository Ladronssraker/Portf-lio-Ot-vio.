from pathlib import Path
import ast


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


#cria um arquivo.
def criar_arquivo(nome):
	try:
		a = open(nome, "wt+")
		a.close()
	except:
		print("errro 01")
	else:
		print(f"arquivo |{nome}| criado com sucesso!")


#mostra o conteudo do arquivo.
def ver_arquivo(nome):
	try:
		a = open(nome, "rt")
	except:
		print("erro 02")
	else:
		print(a.read())
	finally:
		a.close()


#salva coisas dentro do arquivo.
def salvar(arqs, item):
	try:
		a = open(arqs, "at")
	except:
		print("erro3")
	else:
		try:
			a.write(f"{item}\n")
		except:
			print("erro 4")
		else:
			a.close()


#import Path.
#apaga um arquivo da pasta.
def apagar(nome):
	a = Path(nome)
	if a.exists():
		a.unlink()


#import ast.
#coloca o conteudo(lista) dentro do arquivo em uma variavel.
def trazer_lista(nome):
	try:
		a = open(nome, "rt")
		b = a.read()
		return ast.literal_eval(b)
	except:
		print("erro 08")
	finally:
		a.close()
	

#remove um texto do arquivo.
def remover_item_texto(arqs, item):
	try:
		with open(arqs, "r") as um:
			linhas = um.readlines()
		linhas = [linha for linha in linhas if item not in linha]
		with open(arqs, "w") as file:
			file.writelines(linhas)
	except:
		print("item não encontrado!")
		print("não ouve remoção!")


#limpa o conteudo do arquivo.
def limpar(arqs):
	with open(arqs, "w"):
		pass


#arquvo 01.
arq = "arquivo01.txt"

if not ler_arquivo(arq):
	criar_arquivo(arq)

#arquivo 02.
arq2 = "listas.txt"

if not ler_arquivo(arq2):
	criar_arquivo(arq2)
	#dados para salvar.
	dados = ["comida","01", "02", "03", 4, 5]
	salvar(arq2, dados)

#adicionando texto ao arquivo.
texto = str(input("escreva um texto: "))
salvar(arq, texto)
salvar(arq,"------")

ver_arquivo(arq)

#mostrando que se pode modificar o arquivo.
lista = trazer_lista(arq2)
print(lista)
print("_____")
print(lista[0])
print("_____")
lista.pop(1)

#salva a modificação.
limpar(arq2)
salvar(arq2, lista)
print(trazer_lista(arq2))
#si a lista for menos que dois ela é apagada.
if len(lista) < 2:
	apagar(arq2)

#remoção de item do arquivo texto.
tirar = str(input("deseja remover um item do arquivo de textos [s/n]: "))

if tirar == "s":
	qual = str(input("qual item deseja remover: "))
	remover_item_texto(arq, qual)

ver_arquivo(arq)
apagar(arq)
	
