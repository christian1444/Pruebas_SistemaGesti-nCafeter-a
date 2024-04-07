import pytest
from main import verificar_bebida

#se definen las pruebas
casos_prueba = [
    ("Té,8,12,16,20,24", "Entrada válida, bebida ingresada"), #El nombre del artículo es alfabético (válido)
    ("C,8,12,16", "Error: nombre de bebida debe ser entre 2 y 15 caracteres"), #El nombre del artículo tiene menos de 2 caracteres de longitud (inválido)
    ("Cappuccino,10,12,14", "Entrada válida, bebida ingresada"), #El nombre del artículo tiene de 2 a 15 caracteres de longitud (válido)
    ("Sprite,2,11,14,48", "Entrada válida, bebida ingresada"), #El valor del tamaño está en el rango de 1 a 48 (válido)
    ("Coca Cola,2,12,16", "Entrada válida, bebida ingresada"), #El valor del tamaño es un número entero (válido)
    ("Mocha,12,16,20,24,30", "Entrada válida, bebida ingresada"), #Los valores del tamaño se ingresan en orden ascendente (válido)
    ("Fanta,12", "Entrada válida, bebida ingresada"), #Se ingresan de uno a cinco valores de tamaño (válido)
    ("Delaware,12,16,20,24,36", "Entrada válida, bebida ingresada"), #El nombre del artículo es el primero en la entrada (válido)
    ("Café,8,10,12,16", "Entrada válida, bebida ingresada"), #Una sola coma separa cada entrada en la lista (válido)
    ("Té Helado,,10,12,18,28", "Error: ingresa solo números enteros entre 1 y 48, no dejes espacios en blanco"), #La entrada contiene espacios en blanco (inválido)
    ("C@fé,8,10,12,16", "Error: nombre de bebida debe contener únicamente caracteres alfabéticos"),#El nombre del artículo NO es alfabético (inválido)
    ("Cappuccino deslactosado,10,12,14", "Error: nombre de bebida debe ser entre 2 y 15 caracteres"), #El nombre del artículo tiene más de 15 caracteres de longitud (inválido)
    ("Mundet,0,11,14,40", "Error: ingresa números enteros entre 1 y 48"), #El valor del tamaño es menor que 1 (inválido)
    ("Chilate,1,11,14,49", "Error: ingresa números enteros entre 1 y 48"), #El valor del tamaño es mayor que 48 (inválido)
    ("Agua Limón,1,11,14,-40", "Error: ingresa números enteros entre 1 y 48"), #El valor del tamaño es un negativo (inválido)
    ("Chocomilk,30,15,10,2,35", "Error: los números del tamaño deben ir en orden ascendente"), #Los valores del tamaño se ingresan en orden variado (inválido)
    ("Licuado,30,20,10,2", "Error: los números del tamaño deben ir en orden ascendente"), #Los valores del tamaño se ingresan en orden descendente (inválido)
    ("Té Chai", "Error: ingresa de 1 a 5 números enteros separados por una coma"), #Se ingresa menos de 1 tamaño (inválido)
    ("Té Limón,10,20,41,42,43,44,45", "Error: ingresa de 1 a 5 números enteros separados por una coma"), #Se ingresan más de 5 tamaños (inválido)
    ("1,Té Negro,45,32,30", "Error: el nombre de la bebida debe ir primero"), #Se ingresa menos de 1 tamaño (inválido)
]


@pytest.mark.parametrize("entrada, expected", casos_prueba)
def test_verificar_bebida(entrada, expected):
    assert verificar_bebida(entrada) == expected
