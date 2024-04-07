def verificar_bebida(entrada):
  #se eliminan espacios vacios
  entrada = ''.join(entrada.split())
  # se divide la entrada (bebida,tamaños)
  partes = entrada.split(",")
  bebida = partes[0]
  tamaños = partes[1:]
 #se verifica que la bebida este en la primera posicion
  if bebida.isnumeric() or bebida == "":
    return "Error: el nombre de la bebida debe ir primero"

  # se verifica el nombre de la bebida 
  if not bebida.isalpha():
    return "Error: nombre de bebida debe contener únicamente caracteres alfabéticos"
  elif len(bebida) < 2 or len(bebida) > 15:
    return "Error: nombre de bebida debe ser entre 2 y 15 caracteres"

  # se validan los tamaños
  if len(tamaños) < 1 or len(tamaños) > 5:
    return "Error: ingresa de 1 a 5 números enteros separados por una coma"

  tamaños_enteros = []
  for tamaño in tamaños:
        try:
            tamaño_entero = int(tamaño)
            if tamaño_entero < 1 or tamaño_entero > 48:
                return "Error: ingresa números enteros entre 1 y 48"
            tamaños_enteros.append(tamaño_entero)
        except ValueError:
            return "Error: ingresa solo números enteros entre 1 y 48, no dejes espacios en blanco"

  # condicional para tamaños en orden ascendente
  if tamaños_enteros != sorted(tamaños_enteros):
    return "Error: los números del tamaño deben ir en orden ascendente"

  return "Entrada válida, bebida ingresada"