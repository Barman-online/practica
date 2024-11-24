mensual = 30000
anual = mensual * 12
renta = anual * 0.18
seguro = anual * 0.7
pension = anual * 0.28
total =mensual + anual + renta + seguro + pension

print(f"su sueldo mensual es de {mensual}")
print(f"su sueldo anual es de {anual}")
print(f"Su impuesto a pagar anualmente de renta es de {renta}")
print(f"Su impuesto a pagar anualmente de seguro es de {seguro}")
print(f"Su impuesto a pagar anualmente de pension es de {pension}")
print(f"Su total a pagar anualmente es de {total} ")