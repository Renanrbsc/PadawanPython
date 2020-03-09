from unittest import TestCase
from unittest.mock import patch, call

from app.api_cep import _get_somente_numeros

class TestMock(TestCase):


    def test_de_retorno_do_metodo(self):
        # Arrange

        # Action
        metodo = _get_somente_numeros('89-035-520')
        # Assertion
        self.assertEqual(metodo,'89035520',"O retorno é diferente do esperado!")
        

# py -m unittest 
# py -m unittest tests\test_no_metodo_get_somente_numeros.py


    # Teste de Cobertura
    #
    # 1- pip3 install coverage
    # 2- py -m coverage run -m unittest discover
    # 3- py -m coverage report -m
    # 4- py -m coverage html