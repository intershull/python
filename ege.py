# !(y->(x equil w)) and (z->x)
# полная таблица истинности для этой логической функции
def implic(a,b):
    if a==True and b==False: return False
    else: return True
        
def equival(a,b):
    if a==b: return True
    else: return False

def invers(a):
    if a==True: return False
    else: return True

def conjunct(a,b):
    if a and b: return True
    else: return False

for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                res=conjunct(invers(implic(y,equival(x,w))),implic(z,x))
                print(x,y,w,z,res)
                