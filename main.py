edad = int(input('proporciona la edad de vida(1-30): '))
etapadevida = None
if edad == 1 or edad == 2 or edad == 3 or edad == 4 or edad == 5 or edad == 6 or edad == 7 or edad == 8 or edad == 9 or edad == 10:
    etapadevida = 'Niñes'
elif edad == 11  or  edad == 12 or edad == 13 or edad == 14 or edad == 15 or edad == 16 or edad == 17 or edad == 18 or edad == 19 or edad == 20:
    etapadevida = 'adolesencia'
elif edad == 20 or edad == 21 or edad == 22 or edad == 23 or edad == 24 or edad == 25 or edad == 26 or edad == 27 or edad == 28 or edad == 29 or edad == 30:
    etapadevida = 'adultes'
else:
    etapadevida = 'edad no reconocida '
print(f'le edad es {edad} y la etapa de vida es {etapadevida}')