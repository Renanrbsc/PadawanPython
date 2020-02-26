class Pessoa:
	def __int__(self):
		self.idade = 14

	@property
	def get_nome(self):
		return self.nome

	@nome.setters
	def nome(self, nome):
		self.nome = nome
		return self.nome

p1 = Pessoa()
p1.nome()
