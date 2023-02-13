from pickle import FALSE
from datetime import*
#7
def date_(d:int, m:int, y:int)->bool:
    """
    """
    try:
        print(date(y,m,d))
        flag=True
    except:
        print("viga")
        flag=False 
    return flag
#6

def is_prime(n)->bool:
   
   if n < 2:

       return False

   if n == 2:

       return True

   limit = n**(1/2)

   i = 2

   while i <= limit:

       if n % i == 0:

           return False

       i += 1

   return True

   


def arithmetic(arv1:float,tehe:str,arv2:float)->any:
    """
    """
    if tehe=="+":
        vastus=arv1+arv2
    elif tehe=="-":
        vastus=arv1-arv2
    elif tehe=="*":
        vastus=arv1*arv2 
    elif tehe=="/":
        vastus=arv1-arv2 
        if arv2==0:
            vastus="DIVO"
        else:
            vastus=arv1/arv2 
    else:
        vastus="tundmatu tehe"



def is_year_leap(aasta: int)->bool:
    """
    """
    if aasta%4==0:
        t=True 
    else:
        t=FALSE 





#4

def season (m:int)->any:
    """
    """
    if m in (12,1,2):
        vas="talv"
    elif m in (3,4,5):
        vas="kevad"
    elif m in (6,7,8):
        vas="suvi"
    elif m in (9,10,11):
      print(season)

#5

def bank (b,float,aa:int)->float:
    """
    """
    for i in range (aa):
        b=b+b*0.1
    return b

