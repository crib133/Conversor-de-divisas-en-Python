Dinero = int(input("Cantidad a cambiar:$"))
Monedas = ["euro", "real", "dolar"]
Dolar = 1399
Euro = 1642
Real = 285

print("Divisas disponibles:")

for i in Monedas:
    print("-", i)

Cambio = input("Cambio que desea:")
if Cambio == "dolar":
    Resultado = (Dinero / Dolar)
    print("Su vuelto seria: Usd ", round(Resultado))

elif Cambio == "euro":
    Resultado = (Dinero / Euro)
    print("Su vuelto seria: Eur ", round(Resultado))

elif Cambio == "real":
    Resultado = (Dinero / Real)
    print("Su vuelto seria: Brl ", round(Resultado))

else:
    print("Divisa no disponible")