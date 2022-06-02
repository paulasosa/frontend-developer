salario_base, h_extra, bon = input().split()
jorn_lab=192
h_normal=float(salario_base)/jorn_lab
h_extra=int(h_extra)* (h_normal+(h_normal*0.25))
bon=float(bon)* float(salario_base)*0.05
salario_total=float(salario_base)+h_extra+bon
salud=salario_total*0.035
pension=salario_total*0.04
compen=salario_total*0.01
salario_neto=salario_total-salud-pension-compen
print(round(salario_neto, 1))
