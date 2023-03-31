cantidad = int(input("cantidad de boletas: "))

print('Que tipo de sala quieres')
print('1: Dimamica ')
print('2: 3D')
print('3: 2D')

tipo_sala=int(input("Digite su opcion: "))

if tipo_sala == 1:
    precio_boleta = 18800
elif tipo_sala == 2:
    precio_boleta = 15500
else :
    precio_boleta = 11300

print("entre las 17 y 23 es hora pico")
print("indique horario entre las 0 y 23 horas")

horario = int(input("hora de la pelicula: "))

if horario < 17 and horario > 23:
    descuento = (precio_boleta * 10)/100
    descuento_inicial = descuento*cantidad
    aunmento_horario_final=0
    if cantidad >= 3:
        descuento_extra = 500 *cantidad
elif tipo_sala == 1:
    aunmento_horario = (precio_boleta*50)/100
    aunmento_horario_final = aunmento_horario*cantidad
    descuento_inicial=0
    descuento_extra=0
else:
    aunmento_horario = (precio_boleta*25)/100
    aunmento_horario_final = aunmento_horario*cantidad
print("tipo de pago")
print("1: tarjeta de cinemax")
print("2: sin tarjeta de cinemax")

tipo_pago=int(input("digite su opcion: "))

if tipo_pago == 1:
    descuento_tipo_pago = (precio_boleta*5)/100
    descuento_tipo_pago_final= descuento_tipo_pago*cantidad
else:
    descuento_tipo_pago_final=0

print("quiere una reserva")
print("1: si ")
print("2: no ")
reserva = int(input("Digite su opcion: "))

if reserva == 1:
    aumento_reserva = cantidad*2000
else:
    aumento_reserva=0
    


precio_total= (precio_boleta * cantidad)-(descuento_inicial + descuento_extra + descuento_tipo_pago_final)+aunmento_horario_final+aumento_reserva
print("total")
print(precio_total)