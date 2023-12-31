#Objetivo: criar uma função que recebe como parâmetro 
#a quantidade de vitórias e derrotas de um jogador,
#depois disso retorne o resultado para uma variável, 
#o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

def calculadora_rankeadas (vitorias,derrotas):
    saldo = vitorias - derrotas
    if vitorias <= 10:
        nivel = "Ferro" 
    elif vitorias <= 20:
        nivel = "Bronze"
    elif vitorias <= 50:
        nível = "Prata"
    elif vitorias <= 80:
        nivel = "Ouro"
    elif vitorias <= 90:
        nivel = "Diamante"
    elif vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    print(f"O Herói tem saldo de {saldo} e está no nível {nivel}")

calculadora_rankeadas(91,10)