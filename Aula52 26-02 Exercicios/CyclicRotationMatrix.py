
class CyclicRotation:

    def __init__(self):
        self.list_with_values = []

    def create_list_with_values(self):
        for index in range(5):
            index = input(f"Informe o {index+1}° numero: ")
            self.list_with_values.append(index)
        return self.list_with_values

    def rotation_list(self):
        rotation_number = int(input('Digite a quantidade de rotaçôes na lista: '))
        for i in range(rotation_number):
            previous_list = self.list_with_values[:]
            self.list_with_values.insert(0, self.list_with_values[-1])
            self.list_with_values.pop()
            print(f"{previous_list}-->{self.list_with_values}")


m = CyclicRotation()
m.create_list_with_values()
m.rotation_list()