import random

lista = ['π°', 'π°', 'π']
score = 0
spin = 10
a = random.choice(lista)
b = random.choice(lista)
c = random.choice(lista)


def disegno():

	print("""           /~~~~~~~~~~~~~~~~~~~\   O
          /-β’_β’-β’_β’-β’_β’-β’_β’-β’_β’-\  |
          |---------------------|  /
          |β’""", a, """β’|β’""", b, """β’|β’""", c, """β’|-/
          /---------------------\\""")

	print("""          |                     |""")
	print("""          |_____________________|""")
	print(f"          π°SCOREπ°: {score}")
	print(f"          π°SPINπ°: {spin}\n\n\n\n")


print(" \n\n\n\n\n  β­οΈβ­οΈβ­οΈβ­οΈβ­οΈWβ¨eβ¨lβ¨cβ¨oβ¨mβ¨eβ¨ Tβ¨oβ¨ Cβ¨aβ¨sβ¨iβ¨nβ¨oβ¨β­οΈβ­οΈβ­οΈβ­οΈβ­οΈ\n")

while True:
	input("             π° 1 FOR SPIN π°")

	if a == 'π°' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 300
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 300
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 300
	elif a == 'π°' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π' and c == 'π°':
		spin -= 1
		score += 500
	elif a == 'π°' and b == 'π' and c == 'π':
		spin -= 1
		score += 500
	elif a == 'π°' and b == 'π' and c == 'π':
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π°' and c == 'π':
		spin -= 1
		score += 400
	elif a == 'π' and b == 'π°' and c == 'π°':
		spin -= 1
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π°' and c == 'π°':
		spin -= 1
		score += 600
	elif a == 'π' and b == 'π' and c == 'π':
		spin -= 1
		score += 1200
	elif a == 'π°' and b == 'π°' and c == 'π°':
		spin += 6
	elif a == 'π' and b == 'π°' and c == 'π':
		spin -= 1
		score += 500
	elif a == 'π' and b == 'π°' and c == 'π':
		score += 400
	elif a == 'π°' and b == 'π' and c == 'π°':
		spin -= 1
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π' and c == 'π°':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	if spin <= 0:
		print("             β GAME OVER β")
		break

	disegno()

	a = random.choice(lista)
	b = random.choice(lista)
	c = random.choice(lista)

	import random

lista = ['π°', 'π°', 'π']
score = 0
spin = 10
a = random.choice(lista)
b = random.choice(lista)
c = random.choice(lista)


def disegno():

	print("""           /~~~~~~~~~~~~~~~~~~~\   O
          /-β’_β’-β’_β’-β’_β’-β’_β’-β’_β’-\  |
          |---------------------|  /
          |β’""", a, """β’|β’""", b, """β’|β’""", c, """β’|-/
          /---------------------\\""")

	print("""          |                     |""")
	print("""          |_____________________|""")
	print(f"          π°SCOREπ°: {score}")
	print(f"          π°SPINπ°: {spin}\n\n\n\n")


print(" \n\n\n\n\n  β­οΈβ­οΈβ­οΈβ­οΈβ­οΈWβ¨eβ¨lβ¨cβ¨oβ¨mβ¨eβ¨ Tβ¨oβ¨ Cβ¨aβ¨sβ¨iβ¨nβ¨oβ¨β­οΈβ­οΈβ­οΈβ­οΈβ­οΈ\n")

while True:
	input("             π° 1 FOR SPIN π°")

	if a == 'π°' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 300
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 300
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 300
	elif a == 'π°' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π' and c == 'π°':
		score += 300
	elif a == 'π' and b == 'π' and c == 'π°':
		spin -= 1
		score += 500
	elif a == 'π°' and b == 'π' and c == 'π':
		spin -= 1
		score += 500
	elif a == 'π°' and b == 'π' and c == 'π':
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	elif a == 'π' and b == 'π°' and c == 'π°':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π°' and c == 'π':
		spin -= 1
		score += 400
	elif a == 'π' and b == 'π°' and c == 'π°':
		spin -= 1
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π°' and c == 'π°':
		spin -= 1
		score += 600
	elif a == 'π' and b == 'π' and c == 'π':
		spin -= 1
		score += 1200
	elif a == 'π°' and b == 'π°' and c == 'π°':
		spin += 6
	elif a == 'π' and b == 'π°' and c == 'π':
		spin -= 1
		score += 500
	elif a == 'π' and b == 'π°' and c == 'π':
		score += 400
	elif a == 'π°' and b == 'π' and c == 'π°':
		spin -= 1
		score += 400
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 200
	elif a == 'π°' and b == 'π' and c == 'π°':
		score += 200
		spin += 1
	elif a == 'π°' and b == 'π°' and c == 'π°':
		score += 100
		spin += 1
	if spin <= 0:
		print("             β GAME OVER β")
		break

	disegno()

	a = random.choice(lista)
	b = random.choice(lista)
	c = random.choice(lista)
