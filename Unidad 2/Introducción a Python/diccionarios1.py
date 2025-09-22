edades = {
    "Brayan": 25,
    "Luis": 30,
    "José": 22
}
#Agregar edad de Luis
print("Edad de Luis:", edades["Luis"]) 

#Añadir un nuevo dato
edades["Pedro"] = 28
print("\nDespués de añadir a Brayan:")
print(edades)  

#Se actualizó un dato
edades["Luis"] = 26
print("\nDespués de actualizar la edad de Luis:")
print(edades)  

#Eliminando un dato del diccionario
del edades["José"]
print("\nDespués de eliminar a José:")
print(edades)                               
#El diccionario se recorrió
print("\nRecorriendo el diccionario:")
for nombre, edad in edades.items():         
     print(f"{nombre} tiene {edad} años")