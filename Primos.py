from math import isqrt


#h = quantas vezes o codigo se repitiu.
h = 0
#g = quantos primos apareceram.
g = 0
try:
	x = input("numero inicial: ")
	x = int(x)
except:
	x = 2

try:
	k = int(input("quantas vezes: "))
except:
	k = 1000


	
while True:
	h += 1
	#p = identifica se é primo.
	p = 0
	try:
		v = isqrt(x)
	except:
		x = x*(-1)
		v = math.isqrt(x)
	for c in range(1, x):
		if c > v:
			break
		if int(x/c) == x/c:
			p += 1
			if p == 2:
				break
	if p == 1:
		g += 1
		print(g,"- ",x)
		#print(x)
	x +=1
	if h == k:
		h = 0
		b = input("s/n")
		if b == "n":
			break



