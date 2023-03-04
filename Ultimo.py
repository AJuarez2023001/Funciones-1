#Ejercicio
# Una Empresa  actualmente se encuentra  en proceso de selección de personal por lo que se necesita un programa que 
#Permita almacenar el nombre de las persona que llega a la entrevista y  la cantidad total de persona entrevistadas
# En los diferentes dìas

Postulantes = []

Pregunta = False

def obtenerDatos():
    Nombre = input("Ingrese Nombre Postulantes  ")
    Postulantes.append(Nombre)
    print(Nombre+ "Ha sido añadido correctamente  ")
    PreguntaIngreso()


def PreguntaIngreso() : 
    print("¿Hay nuevos postulantes?  ")
    Respuesta = input("S/N ")
    if Respuesta == "S" or Respuesta == "s":
        obtenerDatos()
    else :
        Salida() 
       

def Salida() :
        conteo = 0
        for x in Postulantes :
            Conteo = Conteo + 1
            print((Conteo)+ " " + x)
   

PreguntaIngreso()
