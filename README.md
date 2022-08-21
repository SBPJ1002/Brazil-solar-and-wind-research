# SISTEMA DE RECOMENDAÇÃO DE VIABILIDADE DE CAPACIDADE E CUSTEIO PARA AGILIZAR ESTUDOS DE GERAÇÃO DE ENERGIA SOLAR-EÓLICA  

A base de dados que foi utilizada para montar o código está no link vinculado ao arquivo txt

O código denominado SOLAR funciona da seguinte forma:

  Latitude: Coordenadas no local em decimal

  Longitude: Coordenadas no local em decimal

  Energia Média Desejada: valor do consumo energetico do local onde será realizada a instalação do sistema, o valor é dado em Watts

  Potência do Painel: Potência do painel que foi escolhido para o projeto, o valor é dado em Watts
  
  Potência do inversor:Potência do inversor que será utilizada no projeto

Rendimento do sistema: Este rendimento é dado referente as perdas do sistema, o valor é admensional sendo no intervalo de 0.0 a 1.0, este valor é obtido a partir da seguinte formula (1-perdas)
  
  Aparecerá uma opção para caso o sistema for off-grid, caso a opção seja marcada será necessário informar a quantidade de dias de autonomia e a tensão da bateria que será utilizada
  
A partir dos dados fornecidos as seguintes informações irão aparecer em tela:

  Latitude e Longitude aproximada que foi encontrada no banco de dados
  
  Distancia entre o ponto geografico inserido e o ponto geografico encontrado no banco de dados 

  Irradiação para cada mês do ano

  Potência de pico

  Quantidade de paineis

  Potência Total do Sistema
  
  Quantidade de inversores
  
  Capacidade minima da bateria

Um grafico da irradiação solar para o local informado será mostrado em tela 

  
O código denominado EOLICO funciona da seguinte forma:

  Latitude: Coordenadas no local em decimal

  Longitude: Coordenadas no local em decimal
  
  Altura: Altura da torre escolhida, podendo ser os seguintes valores (30m, 50m, 80m, 100m, 120m, 150m, 200m)
  
  Temperatura(K): Temperatura do local informado em Kelvin
  
  Altitude(m): Altitude do local informado em Kelvin
  
A partir dos dados fornecidos as seguintes informações irão aparecer em tela:

  Distancia entre o ponto geografico inserido e o ponto geografico encontrado no banco de dados 
  
  Latitude e Longitude aproximada que foi encontrada no banco de dados
  
  fator c : É uma medida para a velocidade característica do vento da distribuição sendo proporcional a velocidade média do vento
  
  fator k : Um valor baixo de k simboliza ventos variáveis e ventos constantes são caracterizados por um grande valor de k.
  
  A rosa dos ventos para cada direcão
  
  A variaçãos dos ventos para cada hora do dia
  
  A velocidade do vento para a altura escolhida
  
  A densidade de potência para a altura escolhida
