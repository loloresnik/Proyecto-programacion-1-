import random

DIAS = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
TURNOS = ("Mañana", "Tarde", "Noche")
MATERIAS = (
    "FUNDAMENTOS DE INFORMATICA",
    "ALGEBRA",
    "SISTEMA DE INFORMACION",
    "TEORIA DE SISTEMAS",
    "ARQUITECTURA DE COMPUTADORES"
)

normalizar = lambda s: str(s).strip().upper()

def buscar_maximo_en_dict(diccionario):
    if not diccionario:
        return ("", 0)

    max_clave = ""
    max_valor = -1 
    band = 0 

    for clave, valor in diccionario.items(): 
        if band == 0 or valor > max_valor:
            max_valor = valor
            max_clave = clave
            band = 1
    
    return (max_clave, max_valor)


def registrar_log_memfile(log_list, mensaje):
    linea = f"[REGISTRO] {mensaje}" 
    log_list.append(linea) 
    
    lineas_disco = []
    arch_lectura = 0
    try:
        arch_lectura = open("log.txt", "rt") 
        for l in arch_lectura:
            lineas_disco.append(l) 
    except IOError:
        print("Nota: Creando log.txt por primera vez.")
    else:
        if arch_lectura != 0:
            arch_lectura.close()
            
    lineas_disco.append(linea + "\n")

    arch_escritura = 0
    try:
        arch_escritura = open("log.txt", "wt") 
        for l in lineas_disco:
            arch_escritura.write(l) 
    except IOError:
        print("Error: No se pudo escribir en el archivo log.txt (ignorado).")
    else:
        if arch_escritura != 0:
            arch_escritura.close()

def crearArchivoUsuarios():
    pf_lectura = 0
    try:
        pf_lectura = open("usuarios.txt", "rt")
    except IOError:
        print("Archivo de usuarios no encontrado. Se creará uno nuevo con datos iniciales.")
        pf_escritura = 0
        try:
            pf_escritura = open("usuarios.txt", "wt")
            pf_escritura.write("admin;1234;admin\n")
            pf_escritura.write("profe;abcd;profesor\n")
            pf_escritura.write("alumno;1111;alumno\n")
        except IOError:
            print("Error al crear usuarios.txt")
        else:
            if pf_escritura != 0:
                pf_escritura.close()
    else:
        if pf_lectura != 0:
            pf_lectura.close()


def registrarUsuario():
    lista_usuarios = []
    arch_lectura = 0
    try:
        arch_lectura = open("usuarios.txt", "rt")
        lista_usuarios = [linea for linea in arch_lectura] 
    except IOError:
        print("No se encontró archivo de usuarios, se creará uno nuevo.")
    else:
        if arch_lectura != 0:
            arch_lectura.close()

    usuario = input("Ingrese nuevo usuario: ").strip()
    contrasena = input("Ingrese nueva contraseña: ").strip()

    usuario_existe = 0
    for linea in lista_usuarios:
        partes = linea.strip().split(";")
        if len(partes) > 0 and partes[0] == usuario:
            usuario_existe = 1
            break
    
    if usuario_existe == 1:
        print("\nError: El nombre de usuario ya existe. Intente con otro.")
        return 

    while 1:
        try:
            print("Seleccione el rol del usuario:")
            print("1. admin")
            print("2. profesor")
            print("3. alumno")
            opcion = int(input("Opción: "))
            if opcion == 1:
                rol = "admin"
                break
            elif opcion == 2:
                rol = "profesor"
                break
            elif opcion == 3:
                rol = "alumno"
                break
            else:
                print("Opción fuera de rango.")
        except ValueError:
            print("Debe ingresar un número válido (1-3).") 

    registro = usuario + ";" + contrasena + ";" + rol + "\n"
    lista_usuarios.append(registro)

    arch_escritura = 0
    try:
        arch_escritura = open("usuarios.txt", "wt")
        for linea in lista_usuarios:
            arch_escritura.write(linea) 
        print("Usuario registrado con éxito.")
    except IOError:
        print("Error al abrir usuarios.txt para escribir.")
    else:
        if arch_escritura != 0:
            arch_escritura.close()

def login():
    usuarios = []
    arch = 0
    try:
        arch = open("usuarios.txt", "rt")
        for linea in arch: 
            partes = linea.strip().split(";")
            if len(partes) >= 3:
                usuarios.append([partes[0], partes[1], partes[2]])
    except IOError:
        print("Error al abrir el archivo de usuarios.")
        return "", ""
    else:
        if arch != 0:
            arch.close()

    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()

    for u, c, r in usuarios:
        if u == usuario and c == contrasena:
            print("Inicio de sesión exitoso. Rol:", r)
            return usuario, r

    print("Usuario o contraseña incorrectos.")
    return "", ""

def generar_archivos():
    arch_check = 0
    try:
        arch_check = open("aulas.csv", "rt")
    except IOError:
        arch_aula = 0
        try:
            arch_aula = open("aulas.csv", "wt")
            for i in range(1, 4):
                arch_aula.write(f"A{i};Aula {i};{random.randint(5,10)}\n")
        except IOError:
            print("Error creando aulas.csv")
        else:
            if arch_aula != 0:
                arch_aula.close()
    else:
        if arch_check != 0:
            arch_check.close()

    arch_check = 0
    try:
        arch_check = open("alumnos.csv", "rt")
    except IOError:
        arch_alu = 0
        try:
            arch_alu = open("alumnos.csv", "wt")
            for i in range(1, 16):
                arch_alu.write(f"{i};Alumno{i};Apellido{i};\n")
        except IOError:
            print("Error creando alumnos.csv")
        else:
            if arch_alu != 0:
                arch_alu.close()
    else:
        if arch_check != 0:
            arch_check.close()
            
    arch_check = 0
    try:
        arch_check = open("profesores.csv", "rt")
    except IOError:
        arch_prof = 0
        try:
            arch_prof = open("profesores.csv", "wt")
            for i in range(1, 16):
                mat = random.choice(list(MATERIAS)) 
                arch_prof.write(f"P{i};Profesor{i};{mat}\n")
        except IOError:
            print("Error creando profesores.csv")
        else:
            if arch_prof != 0:
                arch_prof.close()
    else:
        if arch_check != 0:
            arch_check.close()

def mostrar_disponibilidad(aulas, matriz, prof_asignados):
    print("\n--- Disponibilidad de Aulas ---")
    for i in range(len(aulas)):
        print(f"{aulas[i][0]} - {aulas[i][1]} (capacidad {aulas[i][2]})")
        print("Asientos:", matriz[i]) 
        
        aula_id_actual = aulas[i][0]
        if aula_id_actual in prof_asignados: 
            lista_prof = prof_asignados[aula_id_actual] 
        else:
            lista_prof = [] 
        
        print("Profesores asignados:", lista_prof if lista_prof else "Ninguno")

def asignar(aulas, alumnos, profesores, matriz, log, prof_asignados):
    for i in range(len(aulas)):
        capacidad = int(aulas[i][2])
        for j in range(capacidad):
            if alumnos:
                alumno = alumnos.pop(0)
                matriz[i][j] = alumno[0] 
                registrar_log_memfile(log, f"Asignado alumno {alumno[0]} {alumno[1]} {alumno[2]} al aula {aulas[i][1]} en asiento {j}")

    for i in range(len(aulas)):
        aula_id = aulas[i][0]
        if aula_id not in prof_asignados:
            prof_asignados[aula_id] = [] 
        cant_prof = 1 if len(profesores) == 1 else min(2, len(profesores))
        asignados = []
        for _ in range(cant_prof):
            if profesores:
                prof = profesores.pop(0)
                asignados.append(prof[1])
        if asignados:
            prof_asignados[aula_id] = asignados[:2] 
            registrar_log_memfile(log, f"Profesores {asignados} asignados al aula {aulas[i][1]}")

def cancelar_asignacion(aulas, matriz, prof_asignados, log):
    print("\n--- Cancelar Asignación ---")
    print("1. Liberar asiento de alumno")
    print("2. Desasignar profesor")
    try:
        opcion = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if opcion == 1:
        aula_id = input("Ingrese ID de aula (ej: A1): ").strip()
        pos_in = input("Ingrese número de asiento (empezando en 0): ").strip()
        try:
            pos = int(pos_in)
        except ValueError:
            print("Debe ingresar un número válido.")
            return
        
        encontrada = 0
        for i in range(len(aulas)):
            if aulas[i][0] == aula_id:
                encontrada = 1
                if 0 <= pos < len(matriz[i]):
                    if matriz[i][pos] != 0:
                        registrar_log_memfile(log, f"Alumno {matriz[i][pos]} liberado del aula {aula_id}, asiento {pos}")
                        matriz[i][pos] = 0 
                        print("Asiento liberado.")
                    else:
                        print("Ese asiento ya estaba vacío.")
                else:
                    print("Posición fuera de rango para esa aula.")
        if encontrada == 0:
            print("ID de aula no encontrado.")
    elif opcion == 2:
        aula_id = input("Ingrese ID de aula (ej: A1): ").strip()
        if aula_id in prof_asignados and prof_asignados[aula_id]:
            profesor = prof_asignados[aula_id].pop()
            registrar_log_memfile(log, f"Profesor {profesor} desasignado del aula {aula_id}")
            print("Profesor desasignado.")
        else:
            print("No hay profesores asignados a esa aula.")
    else:
        print("Opción fuera de rango.")

def buscar(aulas, alumnos, profesores, matriz, prof_asignados):
    print("\n--- Buscar ---")
    print("1. Buscar alumno por ID")
    print("2. Buscar profesor por materia (muestra 3 aleatorios)")
    try:
        opcion = int(input("Ingrese opción: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return

    if opcion == 1:
        clave = input("Ingrese ID de alumno: ").strip()
        alumno = ""
        for alu in alumnos:
            if alu[0] == clave:
                alumno = alu
                break
        if alumno:
            asignado = 0
            for i in range(len(matriz)):
                if clave in matriz[i]:
                    print(f"Alumno {alumno[1]} {alumno[2]} está en aula {aulas[i][1]}")
                    asignado = 1
            if asignado == 0:
                print("Alumno en lista de espera o sin asignar.")
        else:
            asignado = 0
            for i in range(len(matriz)):
                if clave in matriz[i]:
                    print(f"Alumno ID {clave} está en aula {aulas[i][1]}")
                    asignado = 1
            if asignado == 0:
                print("Alumno no encontrado.")

    elif opcion == 2:
        print("\nSeleccione materia:")
        i = 1
        for mat in MATERIAS: 
            print(f"{i}. {mat}")
            i = i + 1
        try:
            op_mat = int(input("Opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return
        if op_mat < 1 or op_mat > len(MATERIAS):
            print("Opción fuera de rango.")
            return
        materia_sel = MATERIAS[op_mat-1]

        profs_materia = [p for p in profesores if p[2].upper() == materia_sel.upper()]
        if not profs_materia:
            print("No hay profesores disponibles en esa materia.")
            return

        cantidad = 3 if len(profs_materia) >= 3 else len(profs_materia)
        muestra = random.sample(profs_materia, cantidad)

        print(f"\nProfesores de {materia_sel}:")
        i = 1
        for prof in muestra:
            print(f"{i}. Legajo {prof[0]} - {prof[1]} ({prof[2]})")
            i = i + 1

        try:
            eleccion = int(input("Seleccione profesor: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            return
        if eleccion < 1 or eleccion > len(muestra):
            print("Opción fuera de rango.")
            return

        profesor = muestra[eleccion-1]
        asignado = 0
        for aula_id, lista in prof_asignados.items(): 
            if profesor[1] in lista:
                print(f"Profesor {profesor[1]} (Legajo {profesor[0]}) dicta en aula {aula_id}")
                asignado = 1
        if asignado == 0:
            print(f"Profesor {profesor[1]} (Legajo {profesor[0]}) no está asignado a ninguna aula.")
    else:
        print("Opción fuera de rango.")

def inscribir_materia(alumno_id, materias_cupos, clases_alumno, log):
    print("\n--- Inscripción a Materias ---")
    i = 1
    for mat in MATERIAS:
        print(f"{i}. {mat}")
        i = i + 1
    try:
        op = int(input("Seleccione materia: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if op < 1 or op > len(MATERIAS):
        print("Opción fuera de rango.")
        return
    materia_sel = MATERIAS[op-1]

    i = 1
    for d in DIAS: 
        print(f"{i}. {d}")
        i = i + 1
    try:
        op_d = int(input("Seleccione día: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if op_d < 1 or op_d > len(DIAS):
        print("Opción fuera de rango.")
        return
    dia_sel = DIAS[op_d-1]

    i = 1
    for t in TURNOS: 
        print(f"{i}. {t}")
        i = i + 1
    try:
        op_t = int(input("Seleccione turno: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if op_t < 1 or op_t > len(TURNOS):
        print("Opción fuera de rango.")
        return
    turno_sel = TURNOS[op_t-1]

    clave = materia_sel + " - " + turno_sel
    if clave not in materias_cupos:
        materias_cupos[clave] = random.randint(0,5) 

    cupos = materias_cupos[clave] 
    if cupos <= 0:
        print(f"No hay cupos disponibles en {materia_sel} ({turno_sel}).")
        return

    if alumno_id in clases_alumno and clases_alumno[alumno_id]:
        for clase in clases_alumno[alumno_id]:
            if "materia" in clase and clase["materia"] == materia_sel:
                print("\n Ya estás inscrito en esta materia.")
                return
            if "día" in clase and "turno" in clase and clase["día"] == dia_sel and clase["turno"] == turno_sel:
                print("\n Ya estás inscrito en otra materia en este día y turno.")
                return

    if turno_sel == "Mañana":
        horario = "07:30 a 12:30"
    elif turno_sel == "Tarde":
        horario = "13:30 a 17:30"
    else:
        horario = "18:30 a 22:30"

    aula = random.randint(1, 100)

    materias_cupos[clave] = materias_cupos[clave] - 1 

    if alumno_id not in clases_alumno:
        clases_alumno[alumno_id] = []
    clases_alumno[alumno_id].append({
        "materia": materia_sel,
        "día": dia_sel,
        "turno": turno_sel,
        "horario": horario,
        "aula": aula
    })

    linea_a_escribir = f"{alumno_id};{materia_sel};{dia_sel};{turno_sel};{horario};Aula {aula}\n"
    lineas_actuales = []
    arch_r = 0
    try:
        arch_r = open("clases_alumnos.csv", "rt") 
        for l in arch_r:
            lineas_actuales.append(l)
    except IOError:
        print("Nota: Creando clases_alumnos.csv por primera vez.")
    else:
        if arch_r != 0:
            arch_r.close()
    
    lineas_actuales.append(linea_a_escribir)
    
    arch_w = 0
    try:
        arch_w = open("clases_alumnos.csv", "wt") 
        for l in lineas_actuales:
            arch_w.write(l) 
    except IOError:
        print("Error al guardar inscripción de alumno (ignorado).")
    else:
        if arch_w != 0:
            arch_w.close()

    registrar_log_memfile(log, f"Alumno {alumno_id} se inscribió en {materia_sel} - {dia_sel} - {turno_sel} (Aula {aula})")
    print(f"\n Inscripción exitosa en {materia_sel} ({turno_sel}). Aula: {aula}. Horario: {horario}. Quedan {materias_cupos[clave]} cupos.")

def ver_clases_alumno(alumno_id, clases_alumno):
    print("\n--- Mis Clases (Alumno) ---")
    if alumno_id not in clases_alumno or not clases_alumno[alumno_id]:
        print("No tienes clases asignadas.")
        return
    i = 1
    for c in clases_alumno[alumno_id]:
        mat_str = c["materia"] if "materia" in c else "N/A"
        dia_str = c["día"] if "día" in c else "N/A"
        turno_str = c["turno"] if "turno" in c else "N/A"
        hor_str = c["horario"] if "horario" in c else "N/A"
        aula_str = c["aula"] if "aula" in c else "N/A"
        print(f"\nClase {i}: {mat_str} - {dia_str} - {turno_str} ({hor_str}) Aula {aula_str}")
        i = i + 1

def inscribir_clase_profesor(profesor_id, clases_profesor, log):
    print("\n--- Inscripción de Clase (Profesor) ---")
    i = 1
    for mat in MATERIAS:
        print(f"{i}. {mat}")
        i = i + 1
    try:
        opm = int(input("Seleccione materia: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if opm < 1 or opm > len(MATERIAS):
        print("Opción fuera de rango.")
        return
    materia_sel = MATERIAS[opm-1]

    i = 1
    for d in DIAS:
        print(f"{i}. {d}")
        i = i + 1
    try:
        opd = int(input("Seleccione día: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if opd < 1 or opd > len(DIAS):
        print("Opción fuera de rango.")
        return
    dia_sel = DIAS[opd-1]

    i = 1
    for t in TURNOS:
        print(f"{i}. {t}")
        i = i + 1
    try:
        opt = int(input("Seleccione turno: "))
    except ValueError:
        print("Debe ingresar un número válido.")
        return
    if opt < 1 or opt > len(TURNOS):
        print("Opción fuera de rango.")
        return
    turno_sel = TURNOS[opt-1]

    if profesor_id in clases_profesor and clases_profesor[profesor_id]:
        for clase in clases_profesor[profesor_id]:
            if "día" in clase and "turno" in clase and clase["día"] == dia_sel and clase["turno"] == turno_sel:
                if "materia" in clase and clase["materia"] == materia_sel:
                    print("\n Ya estás registrado en esta clase en este día y turno.")
                else:
                    print("\n Ya tienes otra clase en este día y turno.")
                return

    if turno_sel == "Mañana":
        horario = "07:30 a 12:30"
    elif turno_sel == "Tarde":
        horario = "13:30 a 17:30"
    else:
        horario = "18:30 a 22:30"

    aula = random.randint(1,100)

    if profesor_id not in clases_profesor:
        clases_profesor[profesor_id] = [] 
    clases_profesor[profesor_id].append({
        "materia": materia_sel,
        "día": dia_sel,
        "turno": turno_sel,
        "horario": horario,
        "aula": aula
    })

    linea_a_escribir = f"{profesor_id};{materia_sel};{dia_sel};{turno_sel};{horario};Aula {aula}\n"
    lineas_actuales = []
    arch_r = 0
    try:
        arch_r = open("clases_profesores.csv", "rt")
        for l in arch_r:
            lineas_actuales.append(l)
    except IOError:
        print("Nota: Creando clases_profesores.csv por primera vez.")
    else:
        if arch_r != 0:
            arch_r.close()

    lineas_actuales.append(linea_a_escribir)

    arch_w = 0
    try:
        arch_w = open("clases_profesores.csv", "wt")
        for l in lineas_actuales:
            arch_w.write(l)
    except IOError:
        print("Error al guardar inscripción de profesor (ignorado).")
    else:
        if arch_w != 0:
            arch_w.close()

    registrar_log_memfile(log, f"Profesor {profesor_id} se inscribió en {materia_sel} - {dia_sel} - {turno_sel} (Aula {aula})")
    print(f"\n Clase asignada: {materia_sel} - {dia_sel} - {turno_sel} - Aula {aula}")

def ver_clases_profesor(profesor_id, clases_profesor):
    print("\n--- Mis Clases (Profesor) ---")
    if profesor_id not in clases_profesor or not clases_profesor[profesor_id]:
        print("No tiene clases asignadas.")
        return
    i = 1
    for c in clases_profesor[profesor_id]:
        mat_str = c["materia"] if "materia" in c else "N/A"
        dia_str = c["día"] if "día" in c else "N/A"
        turno_str = c["turno"] if "turno" in c else "N/A"
        hor_str = c["horario"] if "horario" in c else "N/A"
        aula_str = c["aula"] if "aula" in c else "N/A"
        print(f"\nClase {i}: {mat_str} - {dia_str} - {turno_str} ({hor_str}) Aula {aula_str}")
        i = i + 1

def generar_reportes(aulas, matriz, log, prof_asignados):
    f_rep = 0
    f_ocu = 0
    f_prof = 0
    f_asig = 0
    f_log = 0
    
    try:
        f_rep = open("reportes.csv", "wt")
        f_ocu = open("aulas_ocupacion.csv", "wt")
        f_prof = open("prof_por_aula.csv", "wt")
        f_asig = open("asignaciones.csv", "wt")
        f_log = open("log.txt", "wt") 
        
        f_rep.write("Aula;Capacidad;Ocupados;Porcentaje\n")
        for i in range(len(aulas)):
            capacidad = int(aulas[i][2])
            ocupados = 0
            for x in matriz[i]:
                if x != 0:
                    ocupados += 1
            porcentaje = (ocupados * 100) // capacidad if capacidad > 0 else 0
            f_rep.write(f"{aulas[i][1]};{capacidad};{ocupados};{porcentaje}%\n")

        f_ocu.write("Aula;AlumnosAsignados\n")
        for i in range(len(aulas)):
            ocupados = sum(1 for x in matriz[i] if x != 0)
            f_ocu.write(f"{aulas[i][1]};{ocupados}\n")

        f_prof.write("AulaID;Profesores\n")
        for i in range(len(aulas)):
            aula_id = aulas[i][0]
            if aula_id in prof_asignados:
                nombres = prof_asignados[aula_id]
            else:
                nombres = []
            f_prof.write(f"{aula_id};{','.join(nombres)}\n")

        f_asig.write("AulaID;AulaNombre;Asiento;AlumnoID\n")
        for i in range(len(aulas)):
            aula_id = aulas[i][0]
            aula_nom = aulas[i][1]
            for asiento in range(len(matriz[i])):
                f_asig.write(f"{aula_id};{aula_nom};{asiento};{matriz[i][asiento]}\n")

        for linea in log:
            f_log.write(linea + "\n")

        print("Reportes generados correctamente.")
        
    except IOError:
        print("Error al generar reportes.")
        
    else:
        if f_rep != 0:
            f_rep.close()
        if f_ocu != 0:
            f_ocu.close()
        if f_prof != 0:
            f_prof.close()
        if f_asig != 0:
            f_asig.close()
        if f_log != 0:
            f_log.close()

def imprimir_log_recursivo(lineas, indice):
    if indice < len(lineas):
        print(lineas[indice].strip())
        imprimir_log_recursivo(lineas, indice + 1)
    else:
        print("--- Fin del log recursivo ---")

def menu_admin(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno):
    while 1: 
        print("\n--- Menú Admin ---")
        print("Usuario:", usuario, "| Rol: admin")
        print("1. Ver Archivos de Salida (estadísticas)")
        print("2. Ver LOG (registro de acciones y resumen)")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue 

        if opcion == 1:
            turnos_cont = {"Mañana":0, "Tarde":0, "Noche":0}
            solicitudes_mat = {m:0 for m in MATERIAS}
            total_inscripciones = 0
            
            for alumno_id, clases in clases_alumno.items(): 
                for c in clases:
                    if "turno" in c:
                        t = c["turno"]
                        if t in turnos_cont:
                            turnos_cont[t] += 1
                            total_inscripciones += 1
                    if "materia" in c:
                        mat = c["materia"]
                        if mat in solicitudes_mat:
                            solicitudes_mat[mat] += 1

            print("\n--- Alumnos por turno ---")
            if total_inscripciones == 0:
                print("No hay inscripciones de alumnos registradas.")
            else:
                for t in ("Mañana","Tarde","Noche"):
                    cnt = turnos_cont[t]
                    pct = (cnt * 100) / total_inscripciones if total_inscripciones > 0 else 0
                    print(f"{t}: {cnt} alumnos ({pct:.1f}%)")

            print("\n--- Inscripciones por materia (alumnos) ---")
            for m in MATERIAS:
                cnt = solicitudes_mat[m]
                pct = (cnt * 100) / total_inscripciones if total_inscripciones > 0 else 0
                print(f"{m}: {cnt} inscripciones ({pct:.1f}%)")

            prof_por_mat = {m:0 for m in MATERIAS}
            total_prof_clases = 0
            for pid, clases in clases_profesor.items():
                for c in clases:
                    if "materia" in c:
                        mat = c["materia"]
                        if mat in prof_por_mat:
                            prof_por_mat[mat] += 1
                            total_prof_clases += 1

            print("\n--- Profesores por materia (conteo de clases asignadas) ---")
            if total_prof_clases == 0:
                print("No hay inscripciones de profesores registradas.")
            else:
                for m in MATERIAS:
                    cnt = prof_por_mat[m]
                    pct = (cnt * 100) / total_prof_clases if total_prof_clases > 0 else 0
                    print(f"{m}: {cnt} ({pct:.1f}%)")

            mejor = buscar_maximo_en_dict(solicitudes_mat) 
            clave_max = mejor[0]
            val_max = mejor[1]
            if str(clave_max).strip() != "":
                pct = (val_max * 100 / total_inscripciones) if total_inscripciones > 0 else 0
                print(f"\nMateria más solicitada: {clave_max} con {val_max} inscripciones ({pct:.1f}%)")

        elif opcion == 2:
            print("\n--- REGISTRO DE ACCIONES (LOG) ---")
            
            arch = 0
            lineas = []
            try:
                arch = open("log.txt", "rt")
                for linea in arch:
                    lineas.append(linea)
            except IOError:
                print("No existe log.txt todavía.")
            else:
                if arch != 0:
                    arch.close()
            
            if not lineas:
                print("El archivo log.txt está vacío.")
            else:
                imprimir_log_recursivo(lineas, 0) 

            registros = []
            arch_log_lectura = 0
            try:
                arch_log_lectura = open("log.txt", "rt")
                for linea in arch_log_lectura:
                    registros.append(linea)
            except IOError:
                registros = []
            else:
                if arch_log_lectura != 0:
                    arch_log_lectura.close()

            def contar_recursivo(lista, idx, acc):
                if idx < len(lista):
                    linea = lista[idx]
                    if "Alumno" in linea and "inscribió en" in linea:
                        for t in TURNOS:
                            if t in linea:
                                acc["alumnos_turno"][t] += 1
                        for m in MATERIAS:
                            if m in linea:
                                acc["alumnos_mat"][m] += 1
                    if "Profesor" in linea and "inscribió en" in linea:
                        for t in TURNOS:
                            if t in linea:
                                acc["profes_turno"][t] += 1
                        for m in MATERIAS:
                            if m in linea:
                                acc["profes_mat"][m] += 1
                    return contar_recursivo(lista, idx + 1, acc) 
                else:
                    return acc

            acumulador = {
                "alumnos_turno": {t:0 for t in TURNOS},
                "profes_turno": {t:0 for t in TURNOS},
                "alumnos_mat": {m:0 for m in MATERIAS},
                "profes_mat": {m:0 for m in MATERIAS}
            }

            resumen = contar_recursivo(registros, 0, acumulador)

            print("\n--- Resumen extraído del log (recursivo) ---")
            print("\nAlumnos por turno:")
            for t in TURNOS:
                print(f"  {t}: {resumen['alumnos_turno'][t]}")
            print("\nProfesores por turno:")
            for t in TURNOS:
                print(f"  {t}: {resumen['profes_turno'][t]}")
            print("\nAlumnos por materia:")
            for m in MATERIAS:
                print(f"  {m}: {resumen['alumnos_mat'][m]}")
            print("\nProfesores por materia:")
            for m in MATERIAS:
                print(f"  {m}: {resumen['profes_mat'][m]}")

        elif opcion == 3:
            print("Saliendo del menú admin...")
            break 
        else:
            print("Opción fuera de rango.")

def menu_profesor(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno):
    while 1: 
        print("\n--- Menú Profesor ---")
        print("Usuario:", usuario, "| Rol: profesor")
        print("1. Inscribirse a clase")
        print("2. Ver mis clases asignadas")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            inscribir_clase_profesor(usuario, clases_profesor, log)
        elif opcion == 2:
            ver_clases_profesor(usuario, clases_profesor)
        elif opcion == 3:
            print("Saliendo del menú profesor...")
            break 
        else:
            print("Opción fuera de rango.")

def menu_alumno(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno):
    while 1: 
        print("\n--- Menú Alumno ---")
        print("Usuario:", usuario, "| Rol: alumno")
        print("1. Inscribirse a materias")
        print("2. Ver mis clases")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese opción: "))
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 1:
            inscribir_materia(usuario, materias_cupos, clases_alumno, log)
        elif opcion == 2:
            ver_clases_alumno(usuario, clases_alumno)
        elif opcion == 3:
            print("Saliendo del menú alumno...")
            break 
        else:
            print("Opción fuera de rango.")

def menu_principal(usuario, rol, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno):
    if rol == "alumno":
        menu_alumno(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno)
    elif rol == "profesor":
        menu_profesor(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno)
    elif rol == "admin":
        menu_admin(usuario, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno)
    else:
        print("Rol desconocido. Saliendo.")

def main():
    crearArchivoUsuarios()
    generar_archivos()
    clases_profesor = {} 
    clases_alumno = {} 

    aulas = []
    arch_aulas = 0
    try:
        arch_aulas = open("aulas.csv", "rt")
        for linea in arch_aulas:
            aulas.append(linea.strip().split(";"))
    except IOError:
        print("Error fatal: No se pudo leer aulas.csv")
        return
    else:
        if arch_aulas != 0:
            arch_aulas.close()

    alumnos = []
    arch_alumnos = 0
    try:
        arch_alumnos = open("alumnos.csv", "rt")
        for linea in arch_alumnos:
            alumnos.append(linea.strip().split(";"))
    except IOError:
        print("Error fatal: No se pudo leer alumnos.csv")
        return
    else:
        if arch_alumnos != 0:
            arch_alumnos.close()

    profesores = []
    arch_profesores = 0
    try:
        arch_profesores = open("profesores.csv", "rt")
        for linea in arch_profesores:
            profesores.append(linea.strip().split(";"))
    except IOError:
        print("Error fatal: No se pudo leer profesores.csv")
        return
    else:
        if arch_profesores != 0:
            arch_profesores.close()

    matriz = []
    for a in aulas:
        capacidad = int(a[2])
        fila = [0 for _ in range(capacidad)] 
        matriz.append(fila)

    prof_asignados = {} 
    materias_cupos = {} 
    log = [] 

    arch_cp = 0
    try:
        arch_cp = open("clases_profesores.csv", "rt")
        for linea in arch_cp:
            partes = linea.strip().split(";")
            if len(partes) >= 6:
                pid = partes[0]
                mat = partes[1]
                dia = partes[2]
                turno = partes[3]
                horario = partes[4]
                aula_text = partes[5].strip()[5:]
                try:
                    aula_num = int(aula_text)
                except ValueError:
                    aula_num = random.randint(1,100)
                if pid not in clases_profesor:
                    clases_profesor[pid] = []
                clases_profesor[pid].append({"materia": mat, "día": dia, "turno": turno, "horario": horario, "aula": aula_num})
    except IOError:
        print("Nota: No se encontró 'clases_profesores.csv' (se ignora).")
    else:
        if arch_cp != 0:
            arch_cp.close()

    arch_ca = 0
    try:
        arch_ca = open("clases_alumnos.csv", "rt")
        for linea in arch_ca:
            partes = linea.strip().split(";")
            if len(partes) >= 6:
                aid = partes[0]
                mat = partes[1]
                dia = partes[2]
                turno = partes[3]
                horario = partes[4]
                aula_text = partes[5].strip()[5:]
                try:
                    aula_num = int(aula_text)
                except ValueError:
                    aula_num = random.randint(1,100)
                if aid not in clases_alumno:
                    clases_alumno[aid] = []
                clases_alumno[aid].append({"materia": mat, "día": dia, "turno": turno, "horario": horario, "aula": aula_num})
    except IOError:
        print("Nota: No se encontró 'clases_alumnos.csv' (se ignora).")
    else:
        if arch_ca != 0:
            arch_ca.close()

    while 1: 
        print("\n--- Menú de Inicio ---")
        print("1. Registrar usuario nuevo")
        print("2. Iniciar sesión")
        print("3. Salir")
        try:
            opcion = int(input("Ingrese opción (1-3): "))
        except ValueError: 
            print("Debe ingresar un número válido (1-3).")
            continue 

        if opcion == 1:
            registrarUsuario()
        elif opcion == 2:
            usuario, rol = login()
            if usuario != "":
                menu_principal(usuario, rol, aulas, alumnos, profesores, matriz, log, prof_asignados, materias_cupos, clases_profesor, clases_alumno)
        elif opcion == 3:
            print("Programa finalizado.")
            break 
        else:
            print("Opción fuera de rango.")


if __name__ == "__main__":
    main()

