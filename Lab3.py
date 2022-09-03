import math

#Pedir datos por pantalla
print("-------------Ingrese Datos de los Casos 1 y 2 --------------")
W=float(input("Ingresar velocidad de operacion en rpm: "))*math.pi/30
F1= float(input("Introducir F1 en lb: "))
agl1=float(input("Introducir angulo1: "))*math.pi/180
F4= float(input("Introducir F4 en lb: "))
agl4=float(input("Introducir angulo4: "))*math.pi/180
Y=float(input("Introducir Y: "))
#Gravedad en ft/s^2
g=32.17
#Transformo la distancia de (inch a ft)
D1= -1.75/12 #Distancia del disco 2 al peso 1 [ft]
D4= 8.25/12 #Distancia del disco 2 a peso 4 [ft]
D3= 6/12 #Distancia del disco 2 al disco 3 [ft]
F1x,F1y=[F1*math.cos(agl1),F1*math.sin(agl1)]
F4x,F4y=[F4*math.cos(agl4),F4*math.sin(agl4)]
mR3X,mR3Y=[((F1x*D1)+(F4x*D4))/(D3*W**2),((F1y*D1)+(F4y*D4))/(D3*W**2)]
mR3= math.sqrt(mR3X**2+mR3Y**2)
tan3=round(math.atan2(mR3Y,mR3X)*180/math.pi,2)
mR2X,mR2Y=[((-F1x-F4x)/W**2)-mR3X,((-F1y-F4y)/W**2)-mR3Y]
mR2= math.sqrt(mR2X**2+mR2Y**2)
tan2=round(math.atan2(mR2Y,mR2X)*180/math.pi,2)
R3=round(mR3*12*g/Y,2)
R2=round(mR2*12*g/Y,2)
if (mR3X<0 and mR3Y<0):
    tan3=360+tan3
elif(mR3X>0 and mR3Y>0):
    tan3=tan3
elif(mR3X<0 and mR3Y>0):
    tan2=180+tan3
else:
    tan2=360+tan3
if (mR2X<0 and mR2Y<0):
    tan2=360+tan2
elif(mR2X>0 and mR2Y>0):
    tan2=tan2
elif(mR2X<0 and mR2Y>0):
    tan2=180+tan2
else:
    tan2=360+tan2
print("------------- Resultados del disco 3 -----------------")
print(" Ángulo del deje de giro del disco 3: "+str(tan3))
print(" Excentricidad del eje de giro con el centro del disco 3: "+str(R3)+" [in]" )
print("------------- Resultados del disco 2 -----------------")
print(" Ángulo del eje de giro del disco 2: "+str(tan2))
print(" Excentricidad del eje de giro con el centro del disco 2: "+str(R2)+" [in]")
