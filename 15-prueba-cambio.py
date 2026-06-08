#VERSION V3

Monedas = ["Euros", "Reales", "Dolares"]

while True:

    print("Divisas disponibles:")
    for i in Monedas:
        print("-", i)
    datos = input("Ingrese importe en Ars y tipo de cambio: ").split()
    if len(datos) < 2:
        print("Ingrese tipo de cambio.")
        continue

#Editable: Cotizaciones 
    Dinero, Divisa = datos
    Dolar, Euro, Real = 1399, 1642, 285

    din1 = float(Dinero)

    if Divisa == "Dolares" or Divisa == "dolares":
        resultado = (din1 / Dolar)
        print("Su cambio es: $", round(resultado, 2))
    elif Divisa == "Euros" or Divisa == "euros":
        resultado = (din1 / Euro)
        print("Su cambio es: $", round(resultado, 2))
    elif Divisa == "Reales" or Divisa == "reales":
        resultado = (din1 / Real)
        print("Su cacambio es:: $", round(resultado, 2))
    else:
        print("Divisa no disponible")

    Reinicio = input("Desea realizar otra operacion?: (si/no) ")
    if Reinicio == "no" or Reinicio == "No":
        print("Gracias por utilizarnos.")
        print("Programa finalizado.")
        break
    elif Reinicio == "si" or Reinicio == "Si":
        continue



# VERSION V2

# Monedas = ["Euros", "Reales", "Dolares"]

# while True:

#     print("Divisas disponibles:")
#     for i in Monedas:
#         print("-", i)
#     Dinero, Divisa = input("Ingrese importe en Ars y tipo de cambio: ").split()
#     Dolar, Euro, Real = 1399, 1642, 285
#     datos = Dinero, Divisa

#     din1 = float(Dinero)

#     if Divisa == "Dolares":
#         resultado = (din1 / Dolar)
#         print("Su cambio es: $", round(resultado))
#     elif Divisa == "Euros":
#         resultado = (din1 / Euro)
#         print("Su cambio es: $", round(resultado))
#     elif Divisa == "Reales":
#         resultado = (din1 / Real)
#         print("Su cacambio es:: $", round(resultado))
#     else:
#         print("Divisa no disponible")

#     Reinicio = input("Desea realizar otra operacion?: (si/no) ")
#     if Reinicio == "no":
#         print("Programa finalizado")
#         break
#     elif Reinicio == "si":
#         continue




#VERSION V1

# Dinero = int(input("Cantidad a cambiar:$"))
# Monedas = ["euro", "real", "dolar"]
# Dolar, Euro, Real = 1399, 1642, 285

# print("Divisas disponibles:")

# for i in Monedas:
#     print("-", i)

# Cambio = input("Cambio que desea:")
# if Cambio == "dolar":
#     Resultado = (Dinero / Dolar)
#     print("Su vuelto seria: Usd ", round(Resultado))

# elif Cambio == "euro":
#     Resultado = (Dinero / Euro)
#     print("Su vuelto seria: Eur ", round(Resultado))

# elif Cambio == "real":
#     Resultado = (Dinero / Real)
#     print("Su vuelto seria: Brl ", round(Resultado))

# else:
#     print("Divisa no disponible")
