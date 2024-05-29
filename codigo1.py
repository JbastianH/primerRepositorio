notaAlta = 0.0
notaBaja = 0.0
print("Se agrega una nueva línea")
try:
    tipoPerfil = 0
    print("Bienvenido a la Escuela")
    print("1) Profesor")
    print("2) Alumno")
    tipoPerfil = int(input("Por favor ingrese una opción: "))
    while tipoPerfil > 2 or tipoPerfil <1:
        print("Opción Inválida, intente nuevamente")
        tipoPerfil = int(input("Por favor ingrese una opción: "))
except:
    print("Ha ocurrido un error")

try:
    if tipoPerfil == 1:
        rutEstudiante = int(input("Ingrese RUT del estudiante: "))
        cantNotas = int(input("Ingrese la cantidad de notas que desea ingresar: "))
        contadorNotas = 0
        print("Comience a ingresar las notas")
        while contadorNotas != cantNotas:
            contadorNotas += 1
            print("Ingrese nota", contadorNotas)
            notas = float(input())
            if notas > notaAlta: # type: ignore
                notaAlta = notas
            if contadorNotas == 1:
                notaBaja = notas
            if notas < notaBaja: # type: ignore
                notaBaja = notas
        print("Usted ha ingresado", contadorNotas, "notas")
        print("Bienvenido a la Escuela")
        print("1) Profesor")
        print("2) Alumno")
        tipoPerfil = int(input("Por favor ingrese una opción: "))
        while tipoPerfil > 2 or tipoPerfil <1:
            print("Opción Inválida, intente nuevamente")
            tipoPerfil = int(input("Por favor ingrese una opción: "))
        if tipoPerfil == 2:
            print("Ha ingresado a la opcion de estudiante")
            rutPersonal = int(input("Por favor ingrese su rut: "))
            if rutPersonal == rutEstudiante:
                print("Su nota mas alta fue: ", notaAlta)
                print("Su nota mas baja fue: ", notaBaja)






    else:
        print("Aún no tiene notas registradas")

except:
    print("Ha ocurrido un error")
