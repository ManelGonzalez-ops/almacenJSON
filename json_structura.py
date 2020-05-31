import json
import pathlib

def creadorInfo(num_socio, nombre_socio):
    contenido = [
        {"num_socio": num_socio},
        {"nombre": nombre_socio},
        {"compras": [

        ]}
    ]
    return contenido


def crearStrucutra():
    file = pathlib.Path("json_socios.json")
    if file.exists() == False:
        mi_json = {}
        mi_json.setdefault("socios", [])
        contenido = [
            {"num_socio": "0000"},
            {"nombre": "Primer socio"},
            {"compras": [
                {
                    "codigo": "000",
                    "compras": 0
                 }
            ]}
        ]
        mi_json["socios"].append(contenido)

        archivo = open("json_socios.json", "w")
        json.dump(mi_json, archivo, ensure_ascii=False, indent=3)
        archivo.close()

def comprobarSocio():
    num_socio = input("indique su numero de socio")
    archivo = open("json_socios.json", "r")
    mijson = json.load(archivo)
    estabaSocio = False
    for socio in mijson["socios"]:

        if socio[0]["num_socio"] == str(num_socio):
            estabaSocio = True

    if estabaSocio == False:
        nuevo_nombre = input("socio no registrado, indiquenos que nombre desea ser guardado en nuestra bbdd")
        nuevo_socio = creadorInfo(num_socio, nuevo_nombre)
        mijson["socios"].append(nuevo_socio)

    añadirCompras(num_socio, mijson, archivo)


def añadirCompras(num_socio, archivoJson, archivo):
    codigo=""
    while codigo != "salir":
        codigo = input("añade el codigo del item, escribe salir para salir")
        if codigo != "salir":
            cantidad = input("añade la cantidad")
            for socio in archivoJson["socios"]:
                if socio[0]["num_socio"] == num_socio:
                    if len(socio[2]) == 0:
                        nuevaCompra = {
                            "codigo": codigo,
                            "compras": cantidad
                        }
                        socio[2]["compras"].append(nuevaCompra)
                    else:
                        estabaObjeto = False
                        for compri in socio[2]["compras"]:
                            if compri["codigo"] == codigo:
                                copiaCantidad = compri["compras"]
                                compri["compras"] = int(copiaCantidad) + int(cantidad)
                                estabaObjeto = True
                        if estabaObjeto == False:
                            nuevaCompra = {
                                "codigo": codigo,
                                "compras": cantidad
                            }
                            socio[2]["compras"].append(nuevaCompra)


    archivo.close()
    fichero = open("json_socios.json", "w")
    json.dump(archivoJson, fichero, ensure_ascii="False", indent=3)


def muestraResultados():
    archivo = open("json_socios.json", "r")
    mijson = json.load(archivo)
    agregado = ""
    for registro in mijson["socios"]:
        header = ":::::::: %s, codigo de socio %s" % (registro[1]["nombre"], registro[0]["num_socio"])
        print(header)
        for reg in registro[2]["compras"]:
            agregado = "%s codigo compra: %s, cantidad: %d \n" % (agregado, reg["codigo"], int(reg["compras"]))
        print(agregado, "\n\n")

def init():
    crearStrucutra()
    print("Bienvenido!")
    accion = ""
    while accion != "0":
        accion = input("porfavor elija una acción: \nAgregar datos ---- Tecla: 1\nMostrar datos ---- Tecla: 2\n" +
                   "Salir ---- tecla 0 ")
        if accion == "1":
            comprobarSocio()
        elif accion == "2":
            muestraResultados()
    print("Hasta la próxima")



init()



