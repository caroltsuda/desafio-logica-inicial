nome = input("Digite o nome do seu herói: ")
XP = int(input("Digite a quantidade de experiência do seu herói: "))
tabela_niveis = {1:"Ferro", 2:"Bronze", 3:"Prata", 4:"Ouro", 5:"Platina", 6:"Ascendente", 7:"Imortal", 8:"Radiante"}
nivel = 0
if XP <= 1000:
    nivel = 1
elif XP <= 2000:
    nivel = 2
elif XP <= 5000:
    nivel = 3
elif XP <= 7000:
    nivel = 4
elif XP <= 8000:
    nivel = 5
elif XP <= 9000:
    nivel = 6
elif XP <= 10000:
    nivel = 7 
else:
    nivel = 8

print(f"O Herói de nome {nome} está no nível {tabela_niveis[nivel]}")