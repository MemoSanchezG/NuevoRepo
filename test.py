import re
 
ventas = ["12/10/2026 ; $1,250.00", "13/10/2026;$980",
          "ayer ; $300", "14/10/2026 ; gratis"]
total, errores = 0, []
 
for venta in ventas:
    fecha, monto = re.split(r"\s*;\s*", venta)
    monto = re.sub(r"[$,]", "", monto)          # limpiar
    if not re.fullmatch(r"\d{2}/\d{2}/\d{4}", fecha):
        fecha = re.sub(r"ayer", "18/10/2026", fecha)          # limpiar
        errores.append(f"{venta}: fecha inválida, cambiada a {fecha}")
    elif not re.fullmatch(r"\d+(\.\d{2})?", monto):
        monto = re.sub(r"gratis", "0", monto)          # limpiar
        errores.append(f"{venta}: monto inválido, cambia a {monto}")
        total = total + float(monto)
    else:
        total = total + float(monto)
 
print("Total:", total)
print("Errores:", errores)
