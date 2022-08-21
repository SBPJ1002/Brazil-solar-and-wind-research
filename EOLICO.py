import pandas as pd
import math
import numpy as np
from importlib.resources import open_binary
from haversine import haversine
import matplotlib.pyplot as plt
from windrose import WindroseAxes

# 2. Entradas
LAT_in = float(input("Latitude: \n")) #3.1 Valor da latitude 
if LAT_in < -34.457466:
    print("Latitude Invalida")
    exit()
if LAT_in > 5.86878:
    print("Latitude Invalida")
    exit()
LON_in = float(input("Longitude: \n")) #3.2 Valor da longitude
if LON_in < -74.67117:
    print("Longitude Invalida")
    exit()
if LON_in > -34.131141:
    print("Longitude Invalida")
    exit()
print("\n30m\n","50m\n","80m\n","100m\n","120m\n","150m\n","200m\n")
Altura=float(input("Altura: \n"))
Temp=float(input("Temperatura(K):\n"))
Alti=float(input("Altitude(m):\n"))

coordenadas_df= pd.read_excel("D:\Iniciação cientifica - Programa\Projeto\Eolico\Coordenadas Eolico.xlsx")
fator_c = pd.read_excel(r"D:\Iniciação cientifica - Programa\Projeto\Eolico\fator c.xlsx")
fator_k = pd.read_excel(r"D:\Iniciação cientifica - Programa\Projeto\Eolico\fator k.xlsx")
rosa = pd.read_csv("D:\Iniciação cientifica - Programa\Projeto\Eolico\Rosa dos ventos.csv", sep= ";")
vel = pd.read_excel("D:\Iniciação cientifica - Programa\Projeto\Eolico\Velocidades.xlsx")
ventos = pd.read_csv("D:\Iniciação cientifica - Programa\Projeto\Eolico\Ventos Diarios.csv", sep= ";")

x = math.sqrt(math.pow(LAT_in,2)) #3.3 Modulo do valor da latitude 
y = math.sqrt(math.pow(LON_in,2)) #3.4 Modulo do valor da longitude

coordenadas_df['dif_lat'] = np.sqrt((np.sqrt(coordenadas_df['LAT'] * coordenadas_df['LAT']) - x) * (np.sqrt(coordenadas_df['LAT'] * coordenadas_df['LAT']) - x)) #3.5 Modulo da subtração da latitude digitada com o modulo de cada valor da latitude da planilha [MOD(MOD(LAT)-MOD(in_LAT))]
coordenadas_df['dif_lon'] = np.sqrt((np.sqrt(coordenadas_df['LON'] * coordenadas_df['LON']) - y) * (np.sqrt(coordenadas_df['LON'] * coordenadas_df['LON']) - y)) #3.6 Modulo da subtração da longitude digitada com o modulo de cada valor de longitude da planilha [MOD(MOD(LON)-MOD(in_LON))]
mi_lat = coordenadas_df['dif_lat'].min() #3.7 Retorna o valor minimo das subtrações da coluna da latitude
mi_lon = coordenadas_df['dif_lon'].min() #3.8 Retorna o valor minimo das subtrações da coluna da longitude
#3.9 Como essa planinha possui numeros repetidos é necessário separar os valores minimos e depois transforma-los em arrays os valores do ID de latitude e longitude para que possam ser comparados no futuro
localizar_lat = coordenadas_df.loc[coordenadas_df['dif_lat'] == mi_lat , ['ID']] #3.9.1  Separação dos valores da coluna ID da latitude
localizar_lon = coordenadas_df.loc[coordenadas_df['dif_lon'] == mi_lon , ['ID']] #3.9.2 Separação dos valores da coluna ID da longitude
lista_lat = np.array(localizar_lat) #3.9.3 Transformação em array dos valores separados da latitude
lista_lon = np.array(localizar_lon) #3.9.4 Transformação em array dos valores separados da longitude
#3.10 Metodo de comparação entre as listas
c = np.in1d(lista_lon,lista_lat).reshape(lista_lon.shape) #3.10.1 Comparação entre as arrays lista_lat e lista_lon
d = np.flatnonzero(np.in1d(lista_lon,lista_lat).reshape(lista_lon.shape).any(1)) #3.10.2 Mostra a linha está o TRUE
e = lista_lon[d] #3.10.3 Mostra o valor do ID no formato array
f = int(e) #3.10.3 Transforma o valor do ID em inteiro

if Altura == 30 or Altura == 50 or Altura ==80 or Altura ==100 or Altura ==120 or Altura ==150 or Altura ==200:
    vel_loc=vel.loc[f-1,'V_30m':'V_200m']
else:
    print("Altura Invalida")

Inicio =(LAT_in,LON_in)
Final = (float(coordenadas_df.loc[f, ['LAT']]),float(coordenadas_df.loc[f, ['LON']]))
distancia = haversine(Inicio,Final)

fator_cloc=fator_c.loc[ f-1 , 'fator_c']
fator_kloc=fator_k.loc[ f-1 , 'fator_k']
rosagraph=rosa.loc[ f-1 , 'N':'NNO'].replace({',': '.'}, regex=True).astype(float)
plt.figure(1,figsize = ((12, 10)))
plt.title("Rosa dos Ventos", fontsize= 22)
plt.ylabel("(%)")
rosagraph.plot.bar()

ventos_loc=ventos.loc[f-1,"1h ":"24h "].replace({',': '.'}, regex=True).astype(float)
plt.figure(2,figsize = ((12, 10)))
plt.title("Ventos Diarios", fontsize= 22)
plt.ylabel("(m/s)")
ventos_loc.plot.bar()

print(
    "Distancia:\n",
    round(distancia,2),"Km","\n"
    )
print(
    "\nCoordenadas:\n",
    "Latitude aproximada:\n" ,
    float(coordenadas_df.loc[f, ['LAT']]),"\n",
    "Longitude aproximada:\n",
    float(coordenadas_df.loc[f, ['LON']]),"\n"
    )
print("fator c =", fator_cloc)
print("fator k =",fator_kloc)
print("\n",
"N    ",rosagraph[0],"%","\n",
"NNE  ",rosagraph[1],"%","\n",
"NE   ",rosagraph[2],"%","\n",
"E    ",rosagraph[3],"%","\n",
"NEE  ",rosagraph[4],"%","\n",
"ESE  ",rosagraph[5],"%","\n",
"SE   ",rosagraph[6],"%","\n",
"SSE  ",rosagraph[7],"%","\n",
"S    ",rosagraph[8],"%","\n",
"SSO  ",rosagraph[9],"%","\n",
"SO   ",rosagraph[10],"%","\n",
"OSO  ",rosagraph[11],"%","\n",
"O    ",rosagraph[12],"%","\n",
"ONO  ",rosagraph[13],"%","\n",
"NO   ",rosagraph[14],"%","\n",
"NNO  ",rosagraph[15],"%","\n"
)
print("\n",
"1h  ",ventos_loc[0],"(m/s)","\n",
"2h  ",ventos_loc[1],"(m/s)","\n",
"3h  ",ventos_loc[2],"(m/s)","\n",
"4h  ",ventos_loc[3],"(m/s)","\n",
"5h  ",ventos_loc[4],"(m/s)","\n",
"6h  ",ventos_loc[5],"(m/s)","\n",
"6h  ",ventos_loc[6],"(m/s)","\n",
"8h  ",ventos_loc[7],"(m/s)","\n",
"9h  ",ventos_loc[8],"(m/s)","\n",
"10h ",ventos_loc[9],"(m/s)","\n",
"11h ",ventos_loc[10],"(m/s)","\n",
"12h ",ventos_loc[11],"(m/s)","\n",
"13h ",ventos_loc[12],"(m/s)","\n",
"14h ",ventos_loc[13],"(m/s)","\n",
"15h ",ventos_loc[14],"(m/s)","\n",
"16h ",ventos_loc[15],"(m/s)","\n",
"17h ",ventos_loc[16],"(m/s)","\n",
"18h ",ventos_loc[17],"(m/s)","\n",
"19h ",ventos_loc[18],"(m/s)","\n",
"20h ",ventos_loc[19],"(m/s)","\n",
"21h ",ventos_loc[20],"(m/s)","\n",
"22h ",ventos_loc[21],"(m/s)","\n",
"23h ",ventos_loc[22],"(m/s)","\n",
"24h ",ventos_loc[23],"(m/s)","\n")

m=(353.049/Temp)*math.pow(math.e,(-0.034*((Altura+Alti)/Temp)))

if Altura ==30:
    Dp30 = (m*math.pow(vel.loc[f-1,'V_30m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_30m'],"(m/s)")
    print("Densidade de Potência =",Dp30,"(W/m2)")



if Altura ==50:
    Dp50 = (m*math.pow(vel.loc[f-1,'V_50m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_50m'],"(m/s)")
    print("Densidade de Potência =",Dp50,"(W/m2)")



if Altura ==80:
    Dp80 = (m*math.pow(vel.loc[f-1,'V_80m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_80m'],"(m/s)")
    print("Densidade de Potência =",Dp80,"(W/m2)")



if Altura ==100:
    Dp100 = (m*math.pow(vel.loc[f-1,'V_100m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_100m'],"(m/s)")
    print("Densidade de Potência =",Dp100,"(W/m2)")



if Altura ==120:
    Dp120 = (m*math.pow(vel.loc[f-1,'V_120m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_120m'],"(m/s)")
    print("Densidade de Potência =",Dp120,"(W/m2)")

    

if Altura ==150:
    Dp150 = (m*math.pow(vel.loc[f-1,'V_150m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_150m'],"(m/s)")
    print("Densidade de Potência =",Dp150,"(W/m2)")



if Altura ==200:
    Dp200 = (m*math.pow(vel.loc[f-1,'V_200m'],3))/2
    print("Velocidade do Vento = ",vel.loc[f-1,'V_200m'],"(m/s)")
    print("Densidade de Potência =",Dp200,"(W/m2)")



plt.show()