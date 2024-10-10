from persona import Alumno

registro_alumnos = {}

#Diccionario para almacenar los 50 alumnos

#Capturar 3 registros
for i in range(3):
    alumno = Alumno()
    alumno.set_nombre (input("Introduce el nombre:"))
    alumno.set_apellido_paterno (input("Introduce el apellido paterno:"))
    alumno.set_apellido_materno (input("Introduce el apellido materno:"))
    alumno.set_no_control (input("Introduce el numero de control:"))
    alumno.set_semestre (int(input("Introduce el semestre:")))

    registro_alumnos[i] = alumno

#Mostrar los 3 nombres de los registros
for i in range(3):
    print(f"Nombre del alumno{i+1}: {registro_alumnos[i].get_nombre_completo()}")