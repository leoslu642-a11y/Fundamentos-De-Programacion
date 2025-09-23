#Crear una lista vacía con mi nombre y agregar 5 elementos con input:(Nombre, preparatoria, lugar de residencias, edad, carrera)

#Se crea una lista llamada lista de datos
lista_datos = []

print("Lista de Datos")

#Agrega dato1 a la lista
dato1 = input("Nombre: ")
lista_datos.append(dato1)

#Agrega dato2 a la lista
dato2 = input("Preparatoria: ")
lista_datos.append(dato2)

#Agrega dato3 a la lista
dato3 = input("Lugar de residencias: ")
lista_datos.append(dato3)

#Agrega dato4 a la lista
dato4 = input("Edad: ")
lista_datos.append(dato4)

#Agrega dato5 a la lista
dato5 = input("Carrera: ")
lista_datos.append(dato5)


#Se imprime la lista
print("\n📌 Tu lista de datos es:")
for dato in lista_datos:
    print(f"- {dato}")

    print("\n✅ ¡Lista creada con éxito!")