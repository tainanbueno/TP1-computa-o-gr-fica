#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importando as bibliotecas
import requests
from tkinter import *
import math


# In[2]:


#função para traçar as linhas
#ela utiliza de um array temporário para ligar todos os pontos que foram selecionados antes de clicar no botão da função
#após desenhar as linhas, insere as coordenadas das linhas em um array 
#por último, esvazia o array temporário
def desenhar_linha():
    for i in range(0, len(temp)):
        if(i == (len(temp)-1)): #esse if é para ligar o último ponto no primeiro e assim, "fechar" o objeto
            canvas.create_line(temp[i][0]+300, temp[i][1]+300, temp[0][0]+300, temp[0][1]+300, fill="black", width=1.4)
            retas.append((temp[i][0], temp[i][1], temp[0][0], temp[0][1]))
        else:            
            canvas.create_line(temp[i][0]+300, temp[i][1]+300, temp[i+1][0]+300, temp[i+1][1]+300, fill="black", width=1.4)
            retas.append((temp[i][0], temp[i][1], temp[i+1][0], temp[i+1][1]))
    
    temp.clear()           
        
        

#função para desenhar a circunferência das transformações geométricas
#é a mesma função da circunferência de bresenham porém um pouco modificada para desenhar a circunferência depois que são 
#transformadas
def circ(xc, yc, rx, ry, cor):
    temp.clear()
    
    raio = math.sqrt((rx - xc)**2 + (ry - yc)**2)
    
    def plot_circle_points():
        canvas.create_oval((xc + x)+300, (yc + y)+300, (xc + x)+300, (yc + y)+300, outline=cor)
        canvas.create_oval((xc - x)+300, (yc + y)+300, (xc - x)+300, (yc + y)+300, outline=cor)
        canvas.create_oval((xc + x)+300, (yc - y)+300, (xc + x)+300, (yc - y)+300, outline=cor)
        canvas.create_oval((xc - x)+300, (yc - y)+300, (xc - x)+300, (yc - y)+300, outline=cor)
        canvas.create_oval((xc + y)+300, (yc + x)+300, (xc + y)+300, (yc + x)+300, outline=cor)
        canvas.create_oval((xc - y)+300, (yc + x)+300, (xc - y)+300, (yc + x)+300, outline=cor)
        canvas.create_oval((xc + y)+300, (yc - x)+300, (xc + y)+300, (yc - x)+300, outline=cor)
        canvas.create_oval((xc - y)+300, (yc - x)+300, (xc - y)+300, (yc - x)+300, outline=cor)
    
    x = 0
    y = raio
    p = 3 - 2 * raio
    plot_circle_points()
    
    while(x < y):
        if(p < 0):
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        
        x = x + 1
        plot_circle_points()     
        
        
        
#função de translação
#com o ".get()", recupera os valores que foram digitados no input da interface e utiliza eles para somar com as coordenadas
#originais dos pontos e transladar eles
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def translacao():
    cor = "#fc0b03"
    t = []
    lt = label_translacao.get().split(',')
    t.append((float(lt[0]), float(lt[1])))
      
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) + t[0][0]
            ncy = retas[i][1] + t[0][1]
            nrx = retas[i][2] + t[0][0]
            nry = retas[i][3] + t[0][1]
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) + t[0][0]
            ncy = retas[i][1] + t[0][1]
            nrx = retas[i][2] + t[0][0]
            nry = retas[i][3] + t[0][1]
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] + t[0][0]
            n1 = retas[i][1] + t[0][1]
            n2 = retas[i][2] + t[0][0]
            n3 = retas[i][3] + t[0][1]
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#fc0b03", width=1.5)

        
        
#função de rotação
#com o ".get()", recupera os valores que foram digitados no input da interface e utiliza eles para calcular com as coordenadas
#originais dos pontos e rotacionar eles. ("{:.1f}".format()) -> pegar o valor float com 1 casa decimal    
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def rotacao():
    cor = "#f01394"
    r = float(label_rotacao.get())
    seno = float("{:.1f}".format(math.sin(math.radians(r))))
    coseno = float("{:.1f}".format(math.cos(math.radians(r))))
        
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) * coseno - retas[i][1] * seno
            ncy = (retas[i][0]-300) * seno + retas[i][1] * coseno
            nrx = retas[i][2] * coseno - retas[i][3] * seno
            nry = retas[i][2] * seno + retas[i][3] * coseno 
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) * coseno - retas[i][1] * seno
            ncy = (retas[i][0]+300) * seno + retas[i][1] * coseno
            nrx = retas[i][2] * coseno - retas[i][3] * seno
            nry = retas[i][2] * seno + retas[i][3] * coseno 
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] * coseno - retas[i][1] * seno
            n1 = retas[i][0] * seno + retas[i][1] * coseno
            n2 = retas[i][2] * coseno - retas[i][3] * seno
            n3 = retas[i][2] * seno + retas[i][3] * coseno       
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#f01394", width=1.5)
        
        
        
#função de escala
#com o ".get()", recupera os valores que foram digitados no input da interface e utiliza eles para multiplcar com as coordenadas
#originais dos pontos e escalar eles
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def escala():
    cor = "#b905f0"
    s = []
    le = label_escala.get().split(',')
    s.append((float(le[0]), float(le[1])))
        
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) * s[0][0]
            ncy = retas[i][1] * s[0][1]
            nrx = retas[i][2] * s[0][0]
            nry = retas[i][3] * s[0][1]
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) * s[0][0]
            ncy = retas[i][1] * s[0][1]
            nrx = retas[i][2] * s[0][0]
            nry = retas[i][3] * s[0][1]
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] * s[0][0]
            n1 = retas[i][1] * s[0][1]
            n2 = retas[i][2] * s[0][0]
            n3 = retas[i][3] * s[0][1]    
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#b905f0", width=1.5)
        
       
    
#função de reflexãoX
#multiplica o "x" do ponto original por 1 e o "y" por -1, para assim, refletir os pontos no eixo X  
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def reflexaox():
    cor = "#1703fc"
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) * 1
            ncy = retas[i][1] * -1
            nrx = retas[i][2] * 1
            nry = retas[i][3] * -1
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) * 1
            ncy = retas[i][1] * -1
            nrx = retas[i][2] * 1
            nry = retas[i][3] * -1
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] * 1
            n1 = retas[i][1] * -1
            n2 = retas[i][2] * 1
            n3 = retas[i][3] * -1    
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#1703fc", width=1.5)
        
        
        
#função de reflexãoY
#multiplica o "x" do ponto original por -1 e o "y" por 1, para assim, refletir os pontos no eixo Y     
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def reflexaoy():
    cor = "#0394fc"
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) * -1
            ncy = retas[i][1] * 1
            nrx = retas[i][2] * -1
            nry = retas[i][3] * 1
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) * -1
            ncy = retas[i][1] * 1
            nrx = retas[i][2] * -1
            nry = retas[i][3] * 1
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] * -1
            n1 = retas[i][1] * 1
            n2 = retas[i][2] * -1
            n3 = retas[i][3] * 1    
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#0394fc", width=1.5)
            
      
    
#função de reflexãoXY
#multiplica o "x" do ponto original por -1 e o "y" por -1, para assim, refletir os pontos no eixo X e no eixo Y  
#o if é para reconhecer as circunferências e invés de traçar linhas, refazer as circunferências com os novos valores
#fiz com que as circunferências teriam os seus [0][0] somados com 300 se fosse maior que 0 e somados com -300 se fosse menor
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def reflexaoxy():
    cor = "#03e3fc"
    for i in range(0, len(retas)):
        if(retas[i][0] >= 300):
            ncx = (retas[i][0]-300) * -1
            ncy = retas[i][1] * -1
            nrx = retas[i][2] * -1
            nry = retas[i][3] * -1
            circ(ncx, ncy, nrx, nry, cor)
        elif(retas[i][0] <= -300):
            ncx = (retas[i][0]+300) * -1
            ncy = retas[i][1] * -1
            nrx = retas[i][2] * -1
            nry = retas[i][3] * -1
            circ(ncx, ncy, nrx, nry, cor)
        else:
            n0 = retas[i][0] * -1
            n1 = retas[i][1] * -1
            n2 = retas[i][2] * -1
            n3 = retas[i][3] * -1    
            canvas.create_line(n0+300, n1+300, n2+300, n3+300, fill="#03e3fc", width=1.5)               

        

#função para desenhar uma reta pelo algoritmo do Analisador Difrencial Digital
#pega os 2 últimos pontos selecionados e calcula a diferença entre os x's e os y's, vai utilizar o valor da maior diferença
#(dx ou dy) para iterar sobre ele. A cada iteração os valores de x1 e y1 serão acrescentados com um valor calculado antes 
#(x_incr ou y_incr) e um pixel (oval) será desenhado na tela
def retas_dda():
    x1 = pontos[len(pontos)-2][0] 
    y1 = pontos[len(pontos)-2][1]
    x2 = pontos[len(pontos)-1][0]
    y2 = pontos[len(pontos)-1][1]
    
    retas.append((x1, y1, x2, y2))
    temp.clear()
    
    dx = x2 - x1
    dy = y2 - y1
    
    if abs(dx) > abs(dy):
        passos = abs(dx)
    else:
        passos = abs(dy)
        
    x_incr = dx / passos
    y_incr = dy / passos
    
    x = x1
    y = y1
    
    canvas.create_oval(round(x)+300, round(y)+300, round(x)+300, round(y)+300, outline="#045c11")
    
    for i in range(1, passos):
        x = x + x_incr
        y = y + y_incr
        canvas.create_oval(round(x)+300, round(y)+300, round(x)+300, round(y)+300, outline="#045c11")

        
        
#função para desenhar uma reta pelo algoritmo de Bresenham
#pega os 2 últimos pontos selecionados e calcula a diferença entre os x's e os y's, se a dierença deles for maior que 0, 
#o incremento (ncrx) vai ser de 1, se for menor que 0, vai decrementar em 1 e a diferença fica positiva
#dependendo de qual é maior (dx ou dy), vai ser iterado sobre ele e utilizand de outros recursos vai incrementando os valores de 
#x e y até formar uma reta    
def retas_bresenham():
    x1 = pontos[len(pontos)-2][0]
    y1 = pontos[len(pontos)-2][1]
    x2 = pontos[len(pontos)-1][0]
    y2 = pontos[len(pontos)-1][1]
    
    retas.append((x1, y1, x2, y2))
    temp.clear()
    
    dx = x2 - x1
    dy = y2 - y1
    
    if(dx >= 0):
        incrx = 1
    else:
        incrx = -1
        dx = -dx
    
    if(dy >= 0):
        incry = 1
    else:
        incry = -1
        dy = -dy
    
    x = x1
    y = y1   
    
    canvas.create_oval(x+300, y+300, x+300, y+300, outline="#23e320")
    
    if(dy < dx):
        p = 2 * dy - dx
        const1 = 2 * dy
        const2 = 2 * (dy - dx)
        for i in range(0, dx):
            x = x + incrx
            if(p < 0):
                p = p + const1
            else:
                y = y + incry
                p = p + const2
                
            canvas.create_oval(x+300, y+300, x+300, y+300, outline="#23e320")
    else:
        p = 2 * dx - dy
        const1 = 2 * dx
        const2 = 2 * (dx - dy)
        for i in range(0, dy):
            y = y + incry
            if(p < 0):
                p = p + const1
            else:
                x = x + incrx
                p = p + const2
                
            canvas.create_oval(x+300, y+300, x+300, y+300, outline="#23e320")

         
        
#função para desenhar uma circunferência pelo algoritmo de Brasenham
#selecionado os 2 últimos pontos (centro e raio) e dado um cálculo de circunferência, vai colorindo os pixel (".create_oval")
#até contornar toda a circunferência
#as circunferências que têm os seus [0][0] maior que 300 são somados com 300 e os [0][0] menores que 300, são somados com -300
#isso para conseguir diferenciar as outras retas da circunferência
#como a tela quadriculada vai de 300 a -300, não tem como ter algum ponto maior que 300 ou menor que -300
def circ_bresenham():
    xc = pontos[len(pontos)-2][0]
    yc = pontos[len(pontos)-2][1]
    
    rx = pontos[len(pontos)-1][0]
    ry = pontos[len(pontos)-1][1]
    
    if(xc >= 0):
        retas.append((xc+300, yc, rx, ry))
    else:
        retas.append((xc-300, yc, rx, ry))
        
        
    temp.clear()
    
    raio = math.sqrt((rx - xc)**2 + (ry - yc)**2)
    
    def plot_circle_points():
        canvas.create_oval((xc + x)+300, (yc + y)+300, (xc + x)+300, (yc + y)+300, outline="#86db30")
        canvas.create_oval((xc - x)+300, (yc + y)+300, (xc - x)+300, (yc + y)+300, outline="#86db30")
        canvas.create_oval((xc + x)+300, (yc - y)+300, (xc + x)+300, (yc - y)+300, outline="#86db30")
        canvas.create_oval((xc - x)+300, (yc - y)+300, (xc - x)+300, (yc - y)+300, outline="#86db30")
        canvas.create_oval((xc + y)+300, (yc + x)+300, (xc + y)+300, (yc + x)+300, outline="#86db30")
        canvas.create_oval((xc - y)+300, (yc + x)+300, (xc - y)+300, (yc + x)+300, outline="#86db30")
        canvas.create_oval((xc + y)+300, (yc - x)+300, (xc + y)+300, (yc - x)+300, outline="#86db30")
        canvas.create_oval((xc - y)+300, (yc - x)+300, (xc - y)+300, (yc - x)+300, outline="#86db30")
    
    x = 0
    y = raio
    p = 3 - 2 * raio
    plot_circle_points()
    
    while(x < y):
        if(p < 0):
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y = y - 1
        
        x = x + 1
        plot_circle_points()      
    
        
        
#função para recortar uma parte da tela e mostrar apenas a parte da reta que está dentro da janela
#seleciona os  4 últimos pontos (2 para janela e 2 para a reta) e dependendo em qual parte os pontos da reta estiverem, 
#eles ganham um código em binário e utilizando esse código, sabe se a reta dos pontos está dentro da janela ou não e se tiver 
#dentro, calcula baseando nas fronteras até a reta ficar dentro da janela
def recorte_cohen():
    x1 = pontos[len(pontos)-2][0]
    y1 = pontos[len(pontos)-2][1]
    x2 = pontos[len(pontos)-1][0]
    y2 = pontos[len(pontos)-1][1]
    
    xmin = pontos[len(pontos)-4][0]
    ymin = pontos[len(pontos)-4][1]
    xmax = pontos[len(pontos)-3][0]
    ymax = pontos[len(pontos)-3][1]
    
    canvas.create_line(xmin+300, ymin+300, xmin+300, ymax+300, fill="yellow", width=1.5)
    canvas.create_line(xmin+300, ymin+300, xmin+300, ymax+300, fill="yellow", width=1.5)
    canvas.create_line(xmin+300, ymax+300, xmax+300, ymax+300, fill="yellow", width=1.5)
    canvas.create_line(xmin+300, ymax+300, xmax+300, ymax+300, fill="yellow", width=1.5)
    canvas.create_line(xmax+300, ymax+300, xmax+300, ymin+300, fill="yellow", width=1.5)
    canvas.create_line(xmax+300, ymax+300, xmax+300, ymin+300, fill="yellow", width=1.5)
    canvas.create_line(xmax+300, ymin+300, xmin+300, ymin+300, fill="yellow", width=1.5)
    canvas.create_line(xmax+300, ymin+300, xmin+300, ymin+300, fill="yellow", width=1.5)
            
    aceite = False
    feito = False
    
    
    def region_code(x, y):
        codigo = 0
        if(x < xmin):
            codigo = codigo + 1
        if(x > xmax):
            codigo = codigo + 2
        if(y < ymin):
            codigo = codigo + 4
        if(y > ymax):
            codigo = codigo + 8
            
        return codigo

    
    while(feito == False):
        c1 = region_code(x1, y1)
        c2 = region_code(x2, y2)
        
        if((c1 == 0) & (c2 == 0)):
            aceite = True
            feito = True
        elif((c1 & c2) != 0):
            feito = True
        else:
            if(c1 != 0):
                cfora = c1
            else:
                cfora = c2
            
            if((cfora & 1) == 1):
                xint = xmin 
                yint = y1 + (y2-y1) * (xmin-x1)/(x2-x1)
            elif((cfora & 2) == 2):
                xint = xmax
                yint = y1 + (y2-y1)*(xmax - x1)/(x2 - x1)
            elif((cfora & 4) == 4):
                yint = ymin 
                xint = x1 + (x2-x1) * (ymin-y1)/(y2-y1)
            elif((cfora & 8) == 8):
                yint = ymax
                xint = x1 + (x2-x1)*(ymax - y1)/(y2 - y1)

            if(c1 == cfora):
                x1 = xint
                y1 = yint
            else:
                x2 = xint
                y2 = yint
    
    if(aceite == True):
        canvas.create_line((x1+300), (y1+300), (x2+300), (y2+300), fill="black", width=1.5)
    


#função para recortar uma parte da tela e mostrar apenas a parte da reta que está dentro da janela
#seleciona os  4 últimos pontos (2 para janela e 2 para a reta) e testa em cada fronteira (esquerda, direita, inferior,
#superior) se a reta passa por ela  ou não
def recorte_liang():
    x1 = pontos[len(pontos)-2][0]
    y1 = pontos[len(pontos)-2][1]
    x2 = pontos[len(pontos)-1][0]
    y2 = pontos[len(pontos)-1][1]
    
    xjmin = pontos[len(pontos)-4][0]
    yjmin = pontos[len(pontos)-4][1]
    xjmax = pontos[len(pontos)-3][0]
    yjmax = pontos[len(pontos)-3][1]
    
    canvas.create_line(xjmin+300, yjmin+300, xjmin+300, yjmax+300, fill="#ff7803", width=1.5)
    canvas.create_line(xjmin+300, yjmin+300, xjmin+300, yjmax+300, fill="#ff7803", width=1.5)
    canvas.create_line(xjmin+300, yjmax+300, xjmax+300, yjmax+300, fill="#ff7803", width=1.5)
    canvas.create_line(xjmin+300, yjmax+300, xjmax+300, yjmax+300, fill="#ff7803", width=1.5)
    canvas.create_line(xjmax+300, yjmax+300, xjmax+300, yjmin+300, fill="#ff7803", width=1.5)
    canvas.create_line(xjmax+300, yjmin+300, xjmin+300, yjmin+300, fill="#ff7803", width=1.5)
    
    
    def cliptest(p, q, u1, u2):
        result = True
        if(p < 0.0):
            r = q / p
            if(r > u1):
                u1 = r
            elif(r > u2):
                result = False
        elif(p > 0.0):
            r = q / p
            if(r < u2):
                u2 = r
            elif(r < u1):
                result = False
        elif(q < 0.0):
            result = False
            
        return result, u1, u2
    
    u1=0.0
    u2=1.0
    
    dx = x2 - x1
    dy = y2 - y1
    
    result, u1, u2 = cliptest(-dx, (x1-xjmin), u1, u2)
    if(result == True):
        result, u1, u2 = cliptest(dx, (xjmax-x1), u1, u2)
        if(result == True):
            result, u1, u2 = cliptest(-dy, (y1-yjmin), u1, u2)
            if(result == True):
                result, u1, u2 = cliptest(dy, (yjmax-y1), u1, u2)
                if(result == True):
                    if(u2 < 1.0):
                        x2 = x1 + u2*dx
                        y2 = y1 + u2*dy
                    if(u1 > 0.0):
                        x1 = x1 + u1*dx
                        y1 = y1 + u1*dy
                                      
                    canvas.create_line(round(x1)+300, round(y1)+300, round(x2)+300, round(y2)+300, fill="black", width=1.5)
    


# In[3]:


#desenha os quadriculado 
def desenhar_grade(canvas):
    #tamano da tela=600, altura da tela=600, espaço=10
    for x in range(0, 600, 10): #desenar lina da coluna 0 até 600 (tamano da tela) dando um espaço de 10 em 10
        canvas.create_line(x, 0, x, 600, fill="gray")
        if(x == 300):
            canvas.create_line(x, 0, x, 600, fill="black")
    for y in range(0, 600, 10): #desenar lina da lina 0 até 600 (altura da tela) dando um espaço de 10 em 10
        canvas.create_line(0, y, 600, y, fill="gray")
        if(y == 300):
            canvas.create_line(0, y, 600, y, fill="black")

            
            
#mostra a coordenada do cursor do mouse na parte superior da tela       
def mostrar_coordenadas(event):
    x, y = event.x, event.y #dado o evento que mostra a posiçao do mouse, o x e o y atual está sendo salvo
    coordenadas_mouse.set(f"Coordenadas do ponto: ({x-300}, {y-300})")
    
    
    
#salva um ponto em cima de onde foi clicado na tela    
def salvar_ponto(event):
    x, y = event.x, event.y #dado o evento de clicar com o botao esquerdo do mouse, o x e o y de onde foi clicado está sendo salvo
    canvas.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black", width=2) #desena um oval na coordenada onde foi clicado
    #numero=f"({x-300}, {y-300})"
    #canvas.create_text(((x-2) + (x+2)) / 2, ((y-20) + (y)) / 2, text=numero)
    pontos.append((x-300, y-300))
    temp.append((x-300, y-300))

    
    
#remove o ultimo ponto da lista que não foi desenhado, apaga os pontos desenhando outro ponto na mesma coordenada porém de branco
#redesenha as linhas do quadriculado
def remover_ponto():
    removido = pontos.pop(-1) #fazer um try catc aqui
    temp.pop(-1)
    canvas.create_oval((removido[0]-2)+300, (removido[1]-2)+300, (removido[0]+2)+300, (removido[1]+2)+300, fill="white", outline="white", width=5)
    numero=f"({removido[0]}, {removido[1]})"
    canvas.create_text((((removido[0]-2) + (removido[0]+2)) / 2)+300, (((removido[1]-20) + (removido[1])) / 2)+300, text=numero, fill="white")
    canvas.create_text((((removido[0]-2) + (removido[0]+2)) / 2)+300, (((removido[1]-20) + (removido[1])) / 2)+300, text=numero, fill="white")
    canvas.create_text((((removido[0]-2) + (removido[0]+2)) / 2)+300, (((removido[1]-20) + (removido[1])) / 2)+300, text=numero, fill="white")
    canvas.create_text((((removido[0]-2) + (removido[0]+2)) / 2)+300, (((removido[1]-20) + (removido[1])) / 2)+300, text=numero, fill="white")
    desenhar_grade(canvas)
    desenhar_grade(canvas)
    

    
#apaga todos os elementos da tela, redesenha as linhas do quadriculado, esvazia os arrays de pontos e retas
def limpar_tela():
    canvas.delete("all")
    pontos.clear()
    retas.clear()
    temp.clear()
    desenhar_grade(canvas)
    


# In[4]:


app = Tk()
app.title("Computação Gráfica-TP1")#título

app.geometry("900x650") #tamanho da interface
app.configure(background="#ffedfb") #cor do fundo


# ------------------------------------ Botoes -----------------------------------------
#cria um frame que separa a parte dos botões "Frame"
#cria os botões de cada função e personaliza eles "Button"
#cria os labels que mostram textos na interface "Labels"
#".place()" para selecionar a posição e o tamanho dos botões
#"Entry" cria um campo de input para os valores das tranformações

frame_botoes = Frame(app, borderwidth=1, relief="solid", bg="white")
frame_botoes.place(x=10, y=10, width=200, height=630)

botao_remover = Button(frame_botoes, text="Remover último ponto", command=remover_ponto, bg="white")
botao_remover.place(x=20, y=10, width=160, height=30)

botao_limpar_tela = Button(frame_botoes, text="Limpar tela", command=limpar_tela, bg="white")
botao_limpar_tela.place(x=20, y=45, width=160, height=30)

botao_desenhar = Button(frame_botoes, text="Traçar linhas", command=desenhar_linha, bg="white")
botao_desenhar.place(x=20, y=80, width=160, height=30)

label1 = Label(frame_botoes, text="Transformações Geométricas 2D", bg="#ffedfb")
label1.place(x=1, y=130, width=180, height=15)

label2 = Label(frame_botoes, text="Digite no formato: 'x, y'", bg="#ffedfb")
label2.place(x=20, y=155, width=130, height=20)
label_translacao = Entry(frame_botoes)
label_translacao.place(x=20, y=175, width=70, height=25)
botao_translacao = Button(frame_botoes, text="Translação", command=translacao, bg="#fc0b03")
botao_translacao.place(x=95, y=175, width=85, height=25)

label3 = Label(frame_botoes, text="Digite no formato: 'x'", bg="#ffedfb")
label3.place(x=20, y=210, width=120, height=20)
label_rotacao = Entry(frame_botoes)
label_rotacao.place(x=20, y=230, width=70, height=25)
botao_rotacao = Button(frame_botoes, text="Rotação", command=rotacao, bg="#f01394")
botao_rotacao.place(x=95, y=230, width=85, height=25)

label4 = Label(frame_botoes, text="Digite no formato: (x, y)", bg="#ffedfb")
label4.place(x=20, y=265, width=130, height=20)
label_escala = Entry(frame_botoes)
label_escala.place(x=20, y=285, width=70, height=25)
botao_escala = Button(frame_botoes, text="Escala", command=escala, bg="#b905f0")
botao_escala.place(x=95, y=285, width=85, height=25)

label5 = Label(frame_botoes, text="Reflexão: escolha o tipo", bg="#ffedfb")
label5.place(x=20, y=320, width=130, height=20)
botao_reflexaox = Button(frame_botoes, text="X", command=reflexaox, bg="#1703fc")
botao_reflexaox.place(x=20, y=340, width=50, height=25)
botao_reflexaoy = Button(frame_botoes, text="Y", command=reflexaoy, bg="#0394fc")
botao_reflexaoy.place(x=75, y=340, width=50, height=25)
botao_reflexaoxy = Button(frame_botoes, text="XY", command=reflexaoxy, bg="#03e3fc")
botao_reflexaoxy.place(x=130, y=340, width=50, height=25)

label6 = Label(frame_botoes, text="Rasterização", bg="#ffedfb")
label6.place(x=1, y=385, width=80, height=15)

botao_retas_dda = Button(frame_botoes, text="Retas - DDA", command=retas_dda, bg="#045c11")
botao_retas_dda.place(x=20, y=410, width=160, height=30)

botao_retas_bresenham = Button(frame_botoes, text="Retas - Bresenham", command=retas_bresenham, bg="#23e320")
botao_retas_bresenham.place(x=20, y=445, width=160, height=30)

botao_circ_bresenham = Button(frame_botoes, text="Circunferência - Bresenham", command=circ_bresenham, bg="#86db30")
botao_circ_bresenham.place(x=20, y=480, width=160, height=30)

label7 = Label(frame_botoes, text="Recorte", bg="#ffedfb")
label7.place(x=1, y=530, width=50, height=15)

botao_recorte_cohen = Button(frame_botoes, text="Região codificada \n Cohen Sutherland", command=recorte_cohen, bg="yellow")
botao_recorte_cohen.place(x=20, y=555, width=160, height=30)

botao_retas_bresenham = Button(frame_botoes, text="Equação paramétrica \n Liang-Barsky", command=recorte_liang, bg="#ff7803")
botao_retas_bresenham.place(x=20, y=590, width=160, height=30)


# --------------------------------- quadriculado -------------------------------------------
#cria os arrays de pontos, retas e temporário
#cria um Frame para separar a parte onde vai ser desenhado (quadriculado) "Frame"
#cria um Canvas que permite desenhar pontos e retas na tela "Canvas"
#".pack()" serve para posicinar e ajustar o canvas no frame
#".bind()" salva eventos realizados pelo hardware e realiza alguns comandos

pontos = []
retas = []
temp = []

frame_quadriculado = Frame(app, borderwidth=1, relief="solid")
frame_quadriculado.place(x=220, y=40, width=600, height=600)

canvas = Canvas(frame_quadriculado, width=480, height=450, bg="white")
canvas.pack(expand=YES, fill=BOTH)
desenhar_grade(canvas)


canvas.bind("<Button-1>", salvar_ponto) #salva as informações do clicar com o botão esquerdo

canvas.bind("<Motion>", mostrar_coordenadas) #salva as informações do cursor do mouse
coordenadas_mouse = StringVar()
coordenadas_tela = Label(app, textvariable=coordenadas_mouse, bg="white", fg="black")
coordenadas_tela.place(x=220, y=13)


#permite a interface ficar em loop
app.mainloop()


# In[ ]:




