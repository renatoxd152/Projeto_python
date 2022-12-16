''' O boliche é um esporte praticado com uma bola pesada e tem como objetivo lançar a bola por uma pista, derrubar 10 pinos do lado oposto da pista dispostos em formação triangular.

A fórmula da contagem de pontos no boliche tem as seguintes variáveis:

Os pontos são a soma dos pinos derrubados.
Exceto quando fizer Strike (derrubar 10 pinos na 1.ª bola) ou Spare (derrubar 10 pinos nas duas bolas jogadas)
Se fizer Strike ganha bônus nas 2 bolas jogadas a seguir. Se fizer Spare ganha bônus na próxima bola jogada. O bônus é igual ao número de pinos derrubados.
O total de 1 partida pode variar de zero a 300 pontos.
A pontuação pode ir de zero (quando nenhum pino é derrubado nas dez jogadas ou “frames”) até o máximo possível de 300 pontos, ou seja, 12 “strikes” consecutivos. Supostamente, como cada partida tem 10 “frames” (jogadas), só seriam possíveis 10 “strikes”. Porém, se o jogador derrubar todos os pinos no primeiro arremesso do 10.º “frame”, tem o direito de jogar mais duas bolas, podendo completar 12 “strikes” numa mesma linha.


Faça um programa que leia a quantidade de pinos derrubados por um praticante de boliche em cada jogada e imprima:

a sequência de pinos derrubados (de acordo com os exemplos de entrada e saída e as anotações de contagem de pontos;
a pontuação final do jogador.
'''
def main(jogadas):

	total_pontos = 0
	frame = 0
	tot_jog = 0
	jog_1 = 1
	especiais = ""
	i = 0
	for jogada in jogadas:
		if jog_1 == 1:
			tot_jog += 1
			if jogada == "10":
				if tot_jog < 10:
					especiais += "X _ | "
				else:
					if int(jogadas[i + 1]) == 10:
						especiais += "X X"
					else:
						especiais += "X "+jogadas[i + 1]+" "

					if int(jogadas[i + 2]) == 10:
						especiais += " X"
					else:
						especiais += jogadas[i + 2]
					break
				frame = 0
			else:
				total_pontos += int(jogada)
				especiais += jogada + " "
				frame += int(jogada)
				jog_1 = 0
		else:
			if (frame + int(jogada)) == 10:
				if tot_jog == 10:
					especiais += "/ "+jogadas[i + 1]
					break
				else:
					especiais += "/ | "
			else:
				if tot_jog == 10:
					especiais += jogada
				else:
					especiais += jogada + " | "
			frame = 0
			jog_1 = 1
		i += 1
	print(especiais)

def pontos(points):
        
	total = 0
	jogada = 0
	prox_jogada = 1
	for i, x in enumerate(points):
		if jogada == 10:
			break
		if x == 10:
			total = total + points[i + 1]
			total = total + points[i + 2]
			jogada = jogada + 1
		elif prox_jogada == 0:
			if points[i - 1] + x == 10:
				total = total + points[i + 1]
			jogada = jogada + 1
			prox_jogada = 1
		else:
			prox_jogada = 0
		total = total + x

	return print(total)


jogadas = list(map(str, input().split()))
points = []
for i in jogadas:
	points.append(int(i))


main(jogadas)
pontos(points)
