from random import sample
import json
import os


#ve se o arquivo existe!
def ler_arquivo(nome):
	try:
		a = open(nome, "rt")
		a.close()
		return True
	except:
		return False


#cria e salva o arquivo!
def salvar_arquivo(nome, item):
	try:
		a = open(nome, "w+")
		json.dump(item, a, ensure_ascii=False)
		a.close()
	except:
		print("erro 01")


#carrega os dados do arquivo para o codigo!
def abrir_arquivo(nome):
	try:
		a = open(nome, "rt")
		return json.load(a)
	except:
		print("erro 02")
	finally:
		a.close()
	


#baralho de 52 cartas!
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

#pasta onde fica o arquivo! o nome do arquivo ande fica os dados!
pasta = "dados_do_baralho"
arquivo = "cartas.json"

#ve se a pasta existe, se não cria a pasta!
if not os.path.exists(pasta):
    os.makedirs(pasta)

#carrega o arquivo dentro da pasta!
arq = os.path.join(pasta, arquivo)

#ve se o arquivo existe, se não cria!
if not ler_arquivo(arq):
	#dicionario onde fica todos os dados, incluso as cartas!
	dados = {"cartas": todas, "salves": [], "loading": [], "bol": True}
	salvar_arquivo(arq, dados)
	print("arquivo json criado!")

#onde ocorre o codigo!
while True:
	#funcão que decide o que fazer no codigo!
	num = input("quantas cartas: ").strip()
	
	#help...
	if num == "help":
		print("new  : para colocar o baralho inteiro!")
		print("save : para salvar as cartas restantes!")
		print("load : para carregar os saves!")
		print("ver   : para ver os saves salvos!")
		print("del   : para deletar os saves!")
		print("remove : para remover uma carta!")
		print("numeros para puxar mais cartas por vez!")
		print("help : para ver as funçionalidades!")
		break
	
	#carrega os dados ve se tem um save, se tiver carrega, se não carrega as cartas que sobraram!
	cartas = abrir_arquivo(arq)
	if cartas["loading"] == []:
		copia = sample(cartas["cartas"], len(cartas["cartas"]))
	else:
		if cartas["bol"]:
			cartas["bol"] = False
			cartas["cartas"] = cartas["loading"]
		copia = sample(cartas["cartas"], len(cartas["cartas"]))
		
	#apaga o save e recarrega todas as cartas!
	if num == "new":
		cartas["loading"] = []
		cartas["cartas"] = todas
		salvar_arquivo(arq, cartas)
		print("baralho compreto!")
		break
	
	#salva as cartas restantes em um save!
	if num == "save" or num == "salvar" or num == "salve" or num == "seive":
		num = str(input("nome do save: ")).strip()
		if num in cartas:
			print("ja existe um save com esse nome!")
		else:
			cartas[num] = copia
			save = cartas["salves"]
			save.append(num)
			cartas["salves"] = save
			salvar_arquivo(arq, cartas)
			print("salvo!")
		break
	
	#recarrega o save!
	if num == "load" or num == "carregar":
		num = str(input("nome do save: ")).strip()
		try:
			cartas["loading"] = cartas[num]
			cartas["bol"] = True
			salvar_arquivo(arq, cartas)
			print("carregando!")
		except:
			print("não existe nenhum save com esse nome!")
		break
	
	#ve os saves ja criados!
	if num == "salves" or num == "saves" or num == "pastas" or num == "arquivos" or num == "ver":
		print(cartas["salves"])
		break
	
	#deleta um save!
	if num == "delete" or num == "del" or num == "apagar":
			num = str(input("o que deseja deletar: ")).strip()
			if not num == "bol" and not num == "loading" and not num == "salves" and not num == "cartas":
				try:
					cartas.pop(num)
					save = cartas["salves"] 
					save.remove(num)
					cartas["salves"] = save
					salvar_arquivo(arq, cartas)
					print(f"seve: {num} deletado!")
				except:
					print("não existe esse save!")
			else:
				print("não é possivel deletar isso!")
			break
	
	#remove uma carta que ainda esta no baralho!
	if num == "remove" or num == "remover" or num == "tirar":
			num = str(input("qual carta deseja remover: ")).strip()
			if num in cartas["cartas"]:
				save = cartas["cartas"]
				save.remove(num)
				cartas["cartas"] = save
				if num in cartas["loading"]:
					save = cartas["loading"]
					save.remove(num)
					cartas["loading"] = save
				salvar_arquivo(arq, cartas)
				print("carta removida!")
			else:
				print("essa carta ja foi removida!")
			break
	
	#adiciona uma carta ao baralho se salva permanecera!
	if num == "adicionar" or num == "add" or num == "colocar":
			num = str(input("que carta deseja adicionar: "))
			if num in cartas["cartas"]:
				print("essa carta ja esta no baralho")
			else:
				save = cartas["cartas"]
				save.append(num)
				cartas["cartas"] = save
				if not cartas["bol"]:
					save = cartas["loading"]
					save.append(num)
					cartas["loading"] = save
				print("carta adicionada!")
				salvar_arquivo(arq, cartas)
			break
			
			
	#transforma 'num'' em um numero inteiro!
	try:
		num = int(num)
	except:
		num = 1
	
	#onde as cartas seram mostradas, 'num' vezes!
	print(len(copia)-1)
	for x in range(0, num):
		print(copia[len(copia)-1])
		copia.pop(len(copia)-1)
		if len(copia) == 0:
			cartas["bol"] = True
			copia = todas
			print("baralho acabou!")
			print("reembaralhado!")
			break
		
	#se ainda estiver cartas salvar os restantes no dados de cartas!
	if not len(copia) == 0:
		cartas["cartas"] = copia
	
	#o save das cartas!
	salvar_arquivo(arq, cartas)
	break



