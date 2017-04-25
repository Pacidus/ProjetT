from random import randrange, seed
from PIL import Image,ImageDraw
from time import time

def gen_height_map(lissage = 0,graine = None,color=True):
    """Number*alpha*bool-> NoneType
    Hypothèse: ø
    retourne une height map (colorée ou non) génerée aléatoirement"""
    a = time()
    x = 1 + 2**11
    y = x
    size = (x,y)
    if graine == None:
        graine = time()
        print (graine)
    seed(graine)
    height = gen_height(x,y,lissage)
    M = height[0][0]
    m = height[0][0]
    for y1 in height:
        if M <= max(y1):
            M = max(y1)
        if m >= min(y1):
            m = min(y1)
    b = time()
    gen_img(height,size,M,m,color,graine,lissage)
    c = time()
    print(b-a)
    print(c-b)
    print(c-a)

def gen_List(x,y):
    """int*int -> list[list[int]
    Hypothèse: ø
    retourne une liste de longueur x composée de liste remplie de y 0 """
    return [[0 for i in range(y)]for j in range(x)]

    
def gen_img(List,size,M,m,color,graine,lissage):
    """List(number)*tuple(int,int)*number*number*bool*float*float -> NoneType
    Hypothèse: M correspond au max de List et m au minimum de List
    retourne une image en fonction des valeurs de List"""
    img = Image.new("RGB", size, "#FFFFFF")
    draw = ImageDraw.Draw(img)
    x1,y1 = size
    coordone = [(x,y) for x in range(x1) for y in range(y1)]
    name = str(graine)+" "+str(lissage)
    if color:
        name = 'carte '+name
    else:
        name = 'height map '+name
    for point in coordone:
        x,y = point
        r = (List[x][y]+abs(m))*255/(M+abs(m))
        g,b = r,r
        if color:
            if r <= 255*.7:
                r,g = 0,0
            else:
                g = r
                b,r = 255**(1-((255-g)**2)/2000),255**(1-((255-g)**2)/2000)
        draw.point(point,fill=(int(r),int(g),int(b)))
    img.show()
    img.save("/home/mahtar_nola/Bureau/Programation/Python/ProjetT/Map/"+name+".png", "PNG")

    
def gen_height(x,y,lissage):
    """int*int*Number -> list[list[Number]]
    Hypothèse: x >= 0 and y >= 0
    retourne une liste de hauteur les valeurs etant définies
    grace a la methode du diamond square"""
    height = gen_List(x,y)
    height[0][0] = randrange(0,x)
    height[x-1][0] = randrange(0,x)
    height[0][y-1] = randrange(0,y)
    height[x-1][y-1] = randrange(0,y)
    i = x-1
    while i > 1:
        di = int(i/2)
        height = Diamond(x,y,di,i,height,lissage)
        height =  Square(x,y,di,i,height,lissage)
        i = di
    return  height


def Diamond(x,y,di,i,height,lissage):
    """int^4*list(int)*float"""
    for x1 in range(di,x,i):
        for y1 in range(di,y,i):
            moyenne = (height[x1-di][y1-di] + height[x1-di][y1+di] + height[x1+di][y1+di] + height[x1-di][y1-di])/4
            height[x1][y1]= moyenne + randrange(-di,di)
    return height

def Square(x,y,di,i,height,lissage):
        """int^4*list(int)*float"""
        for x1 in range(0,x,di):
            if x1%i == 0:
                décalage = di
            else:
                décalage = 0
            for y1 in range(décalage,y,i):
                somme = 0
                n = 0
                if x1 >= di:
                    somme = somme + height[x1 - di][y1]
                    n = n+1
                if x1 + di < x:
                    somme = somme + height[x1 + di][y1]
                    n = n+1
                if y1 >= di:
                    somme = somme + height[x1][y1 - di]
                    n = n+1
                if y1 + di < y:
                    somme = somme + height[x1][y1 + di]
                    n = n+1
                height[x1][y1] = somme / n + randrange(-di,di)
        return height
                
