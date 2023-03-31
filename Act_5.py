clase_mas_accidente = {'volcamiento': 130,'colision':100, 'caidas_del_vehiculo':25, 'atropellos':10}

cla_acc=0 # almacencenar el valor del set : clase_mas_accidente
tipo_cla_acc= None #alamacenar la clave del set : clase_mas_accidente

heridos_fecha= {'20,02,2018':2, '10,02,2018': 1, '15,02,2018' : 1}
fecha=None  #almacenar la clave del set : heridos_fecha
heridos=0   #almacenar el valor del set : heridos_fecha

calle_30 = {}

for clave, valor in clase_mas_accidente.items():
    if valor > cla_acc:
        cla_acc= valor
        tipo_cla_acc = clave
calle_30['clase_mas_accidente']=(tipo_cla_acc,cla_acc) #agregando clave y valor al set : calle_30

for clave, valor in heridos_fecha.items():
    if valor > heridos:
        heridos=valor
        fecha=clave


calle_30['accidentes_gravedad']={'cantidad_max_heridos':(heridos,fecha)} #agregando clave y valor al set : calle_30




print(calle_30)