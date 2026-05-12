Monedas = ["Euros", "Reales", "Dolares"]
print("Divisas disponibles:")
for i in Monedas:
    print("-", i)
Dinero, Divisa = input("Ingrese importe en Ars y tipo de cambio: ").split()
Dolar, Euro, Real = 1399, 1642, 285

din1 = float(Dinero)
operador = Divisa

if operador == "Dolares":
    resultado = (din1 / Dolar)
    print("Su cambio es: $", round(resultado))
elif operador == "Euros":
    resultado = (din1 / Euro)
    print("Su cambio es: $", round(resultado))
elif operador == "Reales":
    resultado = (din1 / Real)
    print("Su cacambio es:: $", round(resultado))

else:
    print("Divisa no disponible")

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
