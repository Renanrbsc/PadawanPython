import sys
sys.path.append(r'C:\Users\900159\Documents\GitHub\PadawanPython')

from Aula51_21-02_Paradigmas_OO.Comportamentos_pessoa.pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())


