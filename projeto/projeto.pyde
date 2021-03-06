participantes = ["ana","marco","bia","julia","pedro"]
num = len(participantes)
angulo = 360/num
giro = 0
velocidade = 0
freio = -0.1

def setup():
    global garrafa,cor
    size(400,400)
    garrafa = loadImage("garrafa.png")
    cor = color(random(255),random(255),random(255))
    imageMode(CENTER)
def draw():
    
    background(cor)
    global botao1
    botao1 = criaBtn("play",50,50,50,50)
    
    translate(width/2,height/2) 
    x = 0
    y = 0
    w = 50
    h = 50
    
    
    for p in participantes:
        line(x,y,x,y-100)
        rotate(radians(angulo/2))
        text(p, x, y - 50)
        rotate(radians(angulo/2))      
        
    giraGarrafa()    
        
def giraGarrafa():
    global giro, velocidade,freio       
    rotate(radians(giro))   
    image(garrafa, 0, 0, 50, 50)  
    giro += velocidade
    velocidade += freio
     
    
    if giro > 360:
        #modulo % e o resto da divisao
        giro = giro % 360
        
    if velocidade <= 0:
      velocidade = 0
freio = 0

def criaBtn(texto,y,x,w,h):
    fill(0,200,0)
    ellipse(x,y,w,h)
    fill(0)
    textAlign(CENTER,CENTER)
    text(texto,x,y)
    
    d = sqrt(pow(mouseX-x, 2) + pow(mouseY-y, 2))
    
    
    if d < w\2:
        return True
    else:
        return False
    
def mouseClicked():
    if botao1:
        global velocidade
        velocidade += random(5,10)