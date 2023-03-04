#Ejercicio
# Una Empresa  actualmente se encuentra  en proceso de selección de personal por lo que se necesita un programa que 
#Permita almacenar el nombre de las persona que llega a la entrevista y  la cantidad total de persona entrevistadas
# En los diferentes dìas

Persona =  [] 




def ObtenerDatos():
    Detener = True
    Conteo = 0
    while Detener == True:
        Nombre = input("Ingrese Nombre Postulante   ")
        Persona.append(Nombre)
        Pregunta = input("Desea Ingresar mas Postulantes? si/no ")
        if Pregunta == "si" or Pregunta == "Si":
            pass
        else :
            Detener = False
            for x in Persona :
                Conteo = Conteo + 1
                print(str(Conteo)+ " " + x)
            

def Salida(a):
    print(a)

ObtenerDatos()




