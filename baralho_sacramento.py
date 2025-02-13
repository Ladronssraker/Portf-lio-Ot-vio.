import random
from pathlib import Path
import ast

#ve se o arquivo existe!
def ler_arquivo(nome):
	try:
		a = open(nome, "rt")
		a.close()
	except:
		print("não existe este arquivo!")
		return False
	else:
		return True

#cria arquivo!
def criar_arquivo(nome):
	try:
		a = open(nome, "wt+")
		a.close()
	except:
		print("errro 01")
	else:
		print(f"arquivo |{nome}| criado com sucesso!")

#ver os itens ou carregar os item para o codigo!
def ver_arquivo(nome):
	try:
		a = open(nome, "rt")
	except:
		print("erro 02")
	else:
		print(a.read())
	finally:
		a.close()

#salvar dados no arquivo!
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

#deletar arquivo!
def apagar(arqh):
	nome = Path(arqh)
	if nome.exists():
		nome.unlink()

#recarregar arquivos.
def organizar():
	try:
		antes = open("dados.txt", "rt")
		coisa = antes.read()
		cartas = ast.literal_eval(coisa)
		antes.close()
		if num == "new" or num == "New":
			cartas = todas.copy()
			
			apagar("loading.txt")
		else:
			if len(cartas) < 1:
				if ler_arquivo("loading.txt"):
					bol = open("loading.txt", "rt")
					loa = f"{bol.read()}"
					bol.close()
					pin = open(loa, "rt")
					lin = pin.read()
					pin.close()
					cartas = ast.literal_eval(lin)
				else:
					cartas = todas.copy()
				
	except:
		cartas = todas.copy()
	finally:
		return cartas


#limpa todo o conteudo do arquivo.
def limpar(arqs):
	with open(arqs, "w"):
		pass



#verifica e cria arquivos!
	
arq = "salves.txt"

if not ler_arquivo(arq):
	criar_arquivo(arq)

arq = "loading.txt"

if not ler_arquivo(arq):
	criar_arquivo(arq)

arq = "dados.txt"

if not ler_arquivo(arq):
	criar_arquivo(arq)

dados = "dados.txt"



# deck de cartas!
todas = [
"A de espada",
"A de paus",
"A de copas",
"A de ouro",
"2 de espada",
"2 de paus",
"2 de copas",
"2 de ouro",
"3 de espada",
"3 de paus",
"3 de copas",
"3 de ouro",
"4 de espada",
"4 de paus",
"4 de copas",
"4 de ouro",
"5 de espada",
"5 de paus",
"5 de copas",
"5 de ouro",
"6 de espada",
"6 de paus",
"6 de copas",
"6 de ouro",
"7 de espada",
"7 de paus",
"7 de copas",
"7 de ouro",
"8 de espada",
"8 de paus",
"8 de copas",
"8 de ouro",
"9 de espada",
"9 de paus",
"9 de copas",
"9 de ouro",
"10 de espada",
"10 de paus",
"10 de copas",
"10 de ouro",
"J de espada",
"J de paus",
"J de copas",
"J de ouro",
"Q de espada",
"Q de paus",
"Q de copas",
"Q de ouro",
"K de espada",
"K de paus",
"K de copas",
"K de ouro"
]


#manter as cartas quando sai e
#retornar as cartas quando acabam!
fim = 0
#codigo de funcionamento!
while True:
	if fim == 1:
		break
		
	#pergunta inicial de funcionamento.
	num = input("puxar quantas cartas: ").strip()
	if num == "sair":
		print("saindo...")
		break
	
	#organiza quais e como serão as cartas.
	cartas = organizar()
	
	if num == "remove" or num == "remover" or num == "tirar":
		num = str(input("nome da carta que deseja remover: ")).strip()
		um = True
		for k in cartas:
			if k == num:
				cartas.remove(num)
				limpar(dados)
				salvar(dados, cartas)
				print("carta removida!")
				um = False
				break
		if um:
			print("esta carta não esta no baralho no momento!")
		break
	
	if num == "save" or num == "salvar" or num == "salve":
		while True:
			num = input("nome do salve: ").strip()
			if num == "sair":
				print("saindo...")
				break
			item = num
			num = num+".txt"
			if ler_arquivo(num):
				print("ja existe um save com esse nome!")
				print("por favor escreva outro nome!")
			else:
				criar_arquivo(num)
				salvar(num, cartas)
				try:
					salvar("salves.txt", item)
					print("salvando...")
				except:
					print("erro 09")
				break
		break
		
	if num == "load" or num == "carregar":
		while True:
			num = input("nome do selve: ").strip()
			if num == "sair":
				print("saindo...")
				break
			num = num+".txt"
			if ler_arquivo(num):
				with open(dados, "w"):
					pass
				apagar("loading.txt")
				co = open(num, "rt")
				salvar(dados, co.read())
				ko = open("loading.txt", "wt+")
				ko.write(f"{num}")
				ko.close()
				co.close()
				print("carregado!")
				break
			else:
				print("para sair escreva 'sair'")
		break
		
	if num == "delete" or num == "del" or num == "apagar":
		while True:
			num = input("nome do salve: ").strip()
			num2 = num
			if num == "sair":
				print("saindo...")
				break
			num = num+".txt"
			arquivo = Path(num)
			if arquivo.exists():
				arquivo.unlink()
				try:
					with open("salves.txt", "r") as um:
						linhas = um.readlines()
					linhas = [linha for linha in linhas if num2 not in linha]
					with open("salves.txt", "w") as file:
						file.writelines(linhas)
				except:
					print("erro 10")
				print("save deletado!")
				break
			else:
				print("arquivo não existe!")
		break
		
	if num == "salves" or num == "saves" or num == "pastas" or num == "arquivos" or num == "ver":
		ver_arquivo("salves.txt")
		break
				
	
	print("faltam",len(cartas)-1, "cartas")
#transforma o input em numero!
	try:
		num = int(num)
		if num == 0:
			print("vc parou de puxar cartas!")
			break
	except:
		num = 1
	if num > 100:
		print("escolha numeros menores que 100!")
		break
	#repete quantos vezes quiser < 100!
	#e remove as cartas escolhidas.
	for b in range(0, num):
		x = random.randint(0, len(cartas)-1)
		print(cartas[x])
		cartas.pop(x)
		if len(cartas) == 0:
			print("nao tem mais cartas")
			recolocar = input("deseja outro baralho: [S/N] ").strip()
			if recolocar == "s" or recolocar == "S" or recolocar == "":
				cartas = 0
				#mantem o load carregado.
				#quando acaba as cartas.
				try:
					if cartas == 0:
						if ler_arquivo("loading.txt"):
							bol = open("loading.txt", "rt")
							loa = f"{bol.read()}"
							bol.close()
							print(loa)
							pin = open(loa, "rt")
							lin = pin.read()
							pin.close()
							cartas = ast.literal_eval(lin)
						else:
							cartas = todas.copy()
				except:
					cartas = todas.copy()
					print("carregando todas as cartas!")
				
			else:
				fim = 1
				#deleta o arquivo quando esta vazia!
				apagar(dados)
				print("finalisando programa...")
				break
			#break
	#apaga o que estiver no arquivo.
	limpar(dados)
	#substitue pelas cartas que sobraram!
	salvar(dados, cartas)
	break




