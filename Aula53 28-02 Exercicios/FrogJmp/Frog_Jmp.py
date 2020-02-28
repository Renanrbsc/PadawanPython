
#   X = 10
#   Y = 85
#   D = 30
# a função deve retornar 3, porque o sapo será posicionado da seguinte maneira:

# após o primeiro salto, na posição 10 + 30 = 40
# após o segundo salto, na posição 10 + 30 + 30 = 70
# após o terceiro salto, na posição 10 + 30 + 30 + 30 = 100
# Escreva um algoritmo eficiente para as seguintes suposições:

def solution(X,Y,D):
    total = 10

    while True:
        total = total + 30
        if total >= 85:
            break
    return total
    
print(solution(10,85,30))