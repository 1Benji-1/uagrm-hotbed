def obtain_groups(page):
    lista_materias = []  
    
    tabla = page.ele('#gvGRUPOS')
    filas = tabla.eles('tag:tr')[1:] 

    for fila in filas:
        columnas = fila.eles('tag:td')

        if len(columnas) < 2:
            continue

        materia = columnas[0].text.strip()
        bloque_materia = f"\n📘 Materia: {materia}\n" 

        grupos = columnas[1].eles('tag:tr')

        for g in grupos:
            texto = g.text.strip()

            if not texto:
                continue

            lineas = texto.split('\n')

            grupo = docente = horario = cupo = ""

            for linea in lineas:
                if "Grupo:" in linea:
                    grupo = linea.replace("Grupo:", "").strip()
                elif "Docente:" in linea:
                    docente = linea.replace("Docente:", "").strip()
                elif "Horarios:" in linea:
                    horario = linea.replace("Horarios:", "").strip()
                elif "Cupo:" in linea:
                    cupo = linea.replace("Cupo:", "").strip()

            bloque_materia += f"  ├─ Grupo: {grupo}\n"
            bloque_materia += f"  │   Docente: {docente}\n"
            bloque_materia += f"  │   Horario: {horario}\n"
            bloque_materia += f"  │   Cupo: {cupo}\n"
            bloque_materia += "  └────────────────────\n"
            
        lista_materias.append(bloque_materia)
            
    return lista_materias 