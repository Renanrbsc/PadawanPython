# Aula 19 - 04-12-2019
# Lista com for e metodos

# 1 - Com a seguinte lista imprima na tela (unsado a indexação e f-string) 

cadastroHBSIS = ['nome',   ['Alex'   ,'Paulo'  ,'Pedro'  ,'Mateus' ,'Carlos' ,'João'   ,'Joaquim'],
                'telefone',['4799991','4799992','4799993','4799994','4799995','4799996','4799997'],
                'email',   ['a@a.com','b@b.com','c@c.com','d@d.com','e@e.com','f@f.com','g@g.com'],
                'idade',   ['18'     ,'25'     ,'40'     ,'16'     ,'15'     ,'19'     ,'17'     ]
                ]


# nome  Alex telefone: 4799991
# idade Carlos é 15 anos
# email de Mateus é d@d.com


print(f'{cadastroHBSIS[0]}: {cadastroHBSIS[1][0]} - {cadastroHBSIS[2].capitalize()}: {cadastroHBSIS[3][0]} ')
print(f'{cadastroHBSIS[6]} de {cadastroHBSIS[1][4]} é {cadastroHBSIS[7][4]} anos')
print(f'{cadastroHBSIS[4]} de {cadastroHBSIS[1][3]} é {cadastroHBSIS[5][3]}')


# 2 - usando o for, imprima todos nomes um abaixo do outro

for i in cadastroHBSIS[1]:
    print(i)

# 3 - Usando a indexação faça uma lista com 3 bibliotecas contendo os dados do Mateus, Paulo e João
#  contendo como chaves: nome, email, idade, telefone (nesta  sequencia)
dados_matheus = {'nome':cadastroHBSIS[1][3],'email':cadastroHBSIS[5][3],'idade':cadastroHBSIS[7][3],'telefone':cadastroHBSIS[3][3]}
dados_paulo = {'nome':cadastroHBSIS[1][1],'email':cadastroHBSIS[5][1],'idade':cadastroHBSIS[7][1],'telefone':cadastroHBSIS[3][3]}
dados_joao = {'nome':cadastroHBSIS[1][5],'email':cadastroHBSIS[5][5],'idade':cadastroHBSIS[7][5],'telefone':cadastroHBSIS[3][3]}
lista = [dados_joao,dados_matheus,dados_paulo]
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')

