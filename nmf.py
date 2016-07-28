from numpy import *

def difcost(a,b):
    dif=0
    for i in range(shape(a)[0]):
        for j in range(shape(a)[1]):
            dif+=pow(a[i,j]-b[i,j],2)
    return dif
def factorize(v,pc=10,iter=50):
    ic=shape(v)[0]
    fc=shape(v)[1]
    
    #random weight matrix and feature matrix
    w=matrix([[random.random() for j in range(pc)] for i in range(ic)]) 
    h=matrix([[ random.random()  for j in range(fc)] for i in range(pc)])
    for i in range(iter):
        wh=w*h
        cost=difcost(v,wh)
        if i%10==0:print cost
        if cost==0:break
        
        #update feature matrix
        hn=transpose(w)*v
        hd=transpose(w)*w*h
        h=matrix(array(h)*array(hn)/array(hd))

        #update weight matrix
        wn=v*transpose(h)
        wd=(w*h*transpose(h))
        w=matrix(array(w)*array(wn)/array(wd))
    return w,h    
if __name__=='__main__':
    ll=[[1,2,3],[4,5,6]]
    m1=matrix(ll)
    m2=matrix([[1,2],[3,4],[5,6]])
    w,h=factorize(m1*m2) 
    print w*h 
    print m1*m2 
