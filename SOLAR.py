# 1. IMPORTAÇÃO DAS BIBLIOTECAS
import pandas as pd
import math
import numpy as np
from importlib.resources import open_binary
from haversine import haversine


# 2. Entradas
LAT_in = float(input("Latitude: \n")) #3.1 Valor da latitude 
if LAT_in < -33.7005:
    print("Latitude Invalida")
    exit()
if LAT_in > 5.2995:
    print("Latitude Invalida")
    exit()
LON_in = float(input("Longitude: \n")) #3.2 Valor da longitude
if LON_in < -73.949:
    print("Longitude Invalida")
    exit()
if LON_in > -34.749:
    print("Longitude Invalida")
    exit()

E =float(input("Energia Média Desejada: \n"))
Painel=float(input("Potência do Painel: \n")) 
rend = float(input("Rendimento do sistema: \n"))

# 3. PLANILHAS USADAS COMO BANCO DE DADOS
coordenadas_df= pd.read_excel("Endereço dos dados")
irradiação_global_horizontal = pd.read_csv("Endereço dos dados", sep= ";")

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

# 4. Irradiação Global Horizontal
global_horizontal = irradiação_global_horizontal.loc[ f-1 , 'JAN':'DEC'] #4.1 Mostra os valores de Janeiro até Dezembro da Irradiação Global Horizontal
global_horizontal_anu = irradiação_global_horizontal.loc[ f-1 ,'ANNUAL'] #4.2 Mostra a média anual
plt.figure(1,figsize = ((12, 10)))
plt.title("Irradiação", fontsize= 22)
plt.ylabel("Wh/m^2/dia * 30dias")
global_horizontal.plot.bar()

# 5. Irradiação Direta Normal
#direta_normal = irradiação_direta_normal.loc[ f-1 , 'JAN':'DEC'] #5.1 Mostra os valores de Janeiro até Dezembro da Irradiação Direta Normal
#direta_normal_anu = irradiação_direta_normal.loc[ f-1 ,'ANNUAL'] #5.2 Mostra a média anual

# 6. Irradiação no Plano Inclinado
#plano_inclinado = irradiação_plano_inclinado.loc[ f-1 , 'JAN':'DEC'] #6.1 Mostra os valores de Janeiro até Dezembro da Irradiação Direta Normal
#plano_inclinado_anu = irradiação_plano_inclinado.loc[ f-1 ,'ANNUAL'] #6.2 Mostra a média anual

# 7. Irradiação Difusa
#difusa = irradiação_difusa.loc[ f-1 , 'JAN':'DEC'] # 7.1 Mostra os valores de Janeiro até Dezembro da Irradiação Difusa
#difusa_anu = irradiação_difusa.loc[ f-1 ,'ANNUAL'] # 7.2 Mostra a média anual

# 8. Irradiação Fotossinteticamente Ativa
#foto_ativa = irradiação_fotossinteticamente_ativa.loc[ f-1 , 'JAN':'DEC'] #8.1 Mostra os valores de Janeiro até Dezembro da Irradiação Fotossinteticamente Ativa
#foto_ativa_anu= irradiação_fotossinteticamente_ativa.loc[ f-1 ,'ANNUAL'] #8.2 Mostra a média anual 

#9. Distancia
Inicio =(LAT_in,LON_in)
Final = (float(coordenadas_df.loc[f, ['LAT']]),float(coordenadas_df.loc[f, ['LON']]))
distancia = haversine(Inicio,Final)



Htot = np.divide([
global_horizontal_anu,
float(irradiação_global_horizontal.loc[ f-1 , 'JAN']),
float(irradiação_global_horizontal.loc[ f-1 , 'FEB']),
float(irradiação_global_horizontal.loc[ f-1 , 'MAR']),
float(irradiação_global_horizontal.loc[ f-1 , 'APR']),
float(irradiação_global_horizontal.loc[ f-1 , 'MAY']),
float(irradiação_global_horizontal.loc[ f-1 , 'JUN']),
float(irradiação_global_horizontal.loc[ f-1 , 'JUL']),
float(irradiação_global_horizontal.loc[ f-1 , 'AUG']),
float(irradiação_global_horizontal.loc[ f-1 , 'SEP']),
float(irradiação_global_horizontal.loc[ f-1 , 'OCT']),
float(irradiação_global_horizontal.loc[ f-1 , 'NOV']),
float(irradiação_global_horizontal.loc[ f-1 , 'DEC'])],1000)

potpico=E/(rend*Htot.min())

Np = potpico/Painel

Ptot = int(Np)*Painel
#Mostrar os Valores
print(
    "\nCoordenadas:\n",
    "Latitude aproximada:\n" ,
    float(coordenadas_df.loc[f, ['LAT']]),"\n",
    "Longitude aproximada:\n",
    float(coordenadas_df.loc[f, ['LON']]),"\n"
    )
print(
    "Distancia:\n",
    round(distancia,2),"Km","\n"
    )
print(
    "Irradiação","\n",
    "Media Anual:",Htot[0],"KWh/m^2/dia * 30dias","\n",
    "JAN:",Htot[1],"KWh/m^2/dia * 30dias","\n",
    "FEV:",Htot[2],"KWh/m^2/dia * 30dias","\n",
    "MAR:",Htot[3],"KWh/m^2/dia * 30dias","\n",
    "ABR:",Htot[4],"KWh/m^2/dia * 30dias","\n",
    "MAI:",Htot[5],"KWh/m^2/dia * 30dias","\n",
    "JUN:",Htot[6],"KWh/m^2/dia * 30dias","\n",
    "JUL:",Htot[7],"KWh/m^2/dia * 30dias","\n",
    "AGO:",Htot[8],"KWh/m^2/dia * 30dias","\n",
    "SET:",Htot[9],"KWh/m^2/dia * 30dias","\n",
    "OUT:",Htot[10],"KWh/m^2/dia * 30dias","\n",
    "NOV:",Htot[11],"KWh/m^2/dia * 30dias","\n",
    "DEZ:",Htot[12],"KWh/m^2/dia * 30dias","\n"
    )

print("Potência de pico:", potpico ,"Wp","\n")

print("Quantidade de paineis:", int(Np),"\n")

print("Potência Total do Sistema:", Ptot,"W")

Potinv = float(input("Potência do inversor: \n"))

Ni = int(Ptot/Potinv)

print("Quantidade de inversores:", Ni, "\n")

print("O sistema é off-grid?")
print("\n0-Sim \n 1-Não")
batyn=float(input("Resposta:"))

if batyn == 0:
    diaaut=float(input("Dias de autonomia: \n"))
    print("\n 12V \n 24V \n 36V \n 48V")
    batten=float(input("Tensão da bateria:"))
    Q=(E*diaaut)/batten	
    print("Capacidade minima da bateria:", Q ,"Ah")
    plt.show()
if batyn == 1:
    plt.show()
    exit()
if batyn < 0 or batyn > 1:
    print("Resposta invalida")
    plt.show()
    exit()
