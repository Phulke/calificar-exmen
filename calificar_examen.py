import pandas as pd 
print(pd.__version__)

df_estudiantes=pd.read_csv("./archivos/respuestas_estudiantes.csv")
df_correctas=pd.read_excel("./archivos/respuestas_correctas.xlsx")

preguntas=df_correctas['Pregunta'].values

clave_respuestas={}
for i in range(df_correctas.shape[0]):
    pregunta=df_correctas['Pregunta'].iloc[i]
    respuesta=df_correctas['Respuesta'].iloc[i]

    clave_respuestas[pregunta]=respuesta

df_estudiantes['Puntuacion']=0
for p in preguntas:
    respuesta_correcta=clave_respuestas[p]
    df_estudiantes['Puntuacion']=df_estudiantes['Puntuacion'].add(
        (df_estudiantes[p]==respuesta_correcta).astype(int))
    
df_detalle=df_estudiantes.copy()

for p in preguntas:
    df_detalle[p]=df_detalle[p].where(
        df_detalle[p]==clave_respuestas[p],
        df_detalle[p]+ 'X'
    )

df_detalle=df_detalle.sort_values('Puntuacion',ascending=False)
print("Leyenda:RespuestaX=Incorrecta")
print(df_detalle.to_string(index=False))

print("\n===RESULTADOS DE LOS ESTUDIANTES===")
print(df_estudiantes[['Nombre','Puntuacion']].sort_values('Puntuacion', ascending=False).to_string(index=False))

##preguntar al ususario el formato de salida 
while True:
    print("\n¿En qué formato deseas guardar los resultados?")
    print("1.CSV")
    print("2.XLSX")
    print("3.XML")

    opcion = input("Selecciona una opción (1-3): ")
    opcion = opcion.strip()

    #print(f"DEBUG → Opción capturada: '{opcion}'") esta linea fue utilizada ya que tenia un error que no podia detectar y me pidio instalar la libreria lxml

    #guardar segun la opcion elegida
    if opcion=="1":
        df_estudiantes.to_csv("resultados_examen.csv", index=False)
        print("\nResultados guardados en 'resultados_examen.csv'")
    elif opcion=="2":
        df_estudiantes.to_excel("resultados_examen.xlsx", index=False)
        print("\nResultados guardados en 'resultados_examen.xlsx'")
    elif opcion=="3":
        df_estudiantes.to_xml("resultados_examen.xml", index=False)
        print("\nResultados guardados en 'resultados_examen.xml'")
    else:
        print("\nOpción no válida. Se guardará por defecto en CSV.")
        df_estudiantes.to_csv("resultados_examen.csv", index=False)
        print("Resultados guardados en 'resultados_examen.csv'")

    while True:
        continuar = input("\n¿Deseas guardar en otro formato? (1 = Sí, 0 = Salir): ").strip()
        if continuar == "1":
            break  # vuelve al menú principal
        elif continuar == "0":
            print("Saliendo del programa...")
            exit()  # termina el programa
        else:
            print("Opción no válida. Por favor ingresa 1 o 0.")