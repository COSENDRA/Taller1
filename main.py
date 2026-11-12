import json
import csv

with open('data.json', 'r') as file:
    data = json.load(file)


# 1. GASTO TOTAL POR USUARIO
print("1. GASTO TOTAL POR USUARIO")
gastos_usuario = {}

for usuario in data.keys():
    total = 0

    for compra in data[usuario]:
        total += compra["precio"]

    gastos_usuario[usuario] = total

for usuario in gastos_usuario.keys():
    print(usuario, ":", round(gastos_usuario[usuario], 2), "€")


# 2. CLIENTE VIP (MAYOR GASTO)
print("2. CLIENTE VIP (MAYOR GASTO)")
mayor_gasto = max(gastos_usuario.values())


for usuario in gastos_usuario.keys():
    if gastos_usuario[usuario] == mayor_gasto:
        print(usuario, ":", round(gastos_usuario[usuario], 2), "€")


# 3. CLIENTE CON MAS ARTICULOS
print("3. CLIENTE CON MAS ARTICULOS")
mayor_cantidad = 0

for usuario in data.keys():
    if len(data[usuario]) > mayor_cantidad:
        mayor_cantidad = len(data[usuario])

for usuario in data.keys():
    if len(data[usuario]) == mayor_cantidad:
        print(usuario, ":", mayor_cantidad, "articulos")


# 4. PRODUCTO MAS CARO Y MAS BARATO
print("4. PRODUCTO MAS CARO Y MAS BARATO")
productos = []

for usuario in data.keys():
    for compra in data[usuario]:
        productos.append(compra)

producto_caro = productos[0]
producto_barato = productos[0]

for producto in productos:

    if producto["precio"] > producto_caro["precio"]:
        producto_caro = producto

    if producto["precio"] < producto_barato["precio"]:
        producto_barato = producto

print("Mas caro:", producto_caro["producto"], producto_caro["precio"], "€")
print("Mas barato:", producto_barato["producto"], producto_barato["precio"], "€")


# 5. RESUMEN POR CATEGORIAS
print("5. RESUMEN POR CATEGORIAS")
gastos_categoria = {}

for usuario in data.keys():
    for compra in data[usuario]:
        categoria = compra["categoria"]

        if categoria not in gastos_categoria:
            gastos_categoria[categoria] = 0

        gastos_categoria[categoria] += compra["precio"]

for categoria in gastos_categoria.keys():
    print(categoria, ":", round(gastos_categoria[categoria], 2), "€")


# 6. PRODUCTOS CON IVA
print("6. PRODUCTOS CON IVA")
for usuario in data.keys():
    for compra in data[usuario]:
        compra["precioIVA"] = round(compra["precio"] * 1.21, 2)

for usuario in data.keys():
    for compra in data[usuario]:
        print(compra["producto"], ":", compra["precioIVA"], "€")


# 7. CREAR FICHERO CSV
print("7. CREAR FICHERO CSV")
with open("contabilidad_a.csv", "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile, delimiter=";")

    writer.writerow(["producto", "precioIVA"])

    for usuario in data.keys():
        for compra in data[usuario]:
            writer.writerow([
                compra["producto"],
                compra["precioIVA"]
            ])

