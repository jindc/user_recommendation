#coding=utf8
import sys,os,os.path
reload(sys)
sys.setdefaultencoding('utf8')
from doclib import doclib
from numpy import *
import nmf

def getarticlewords():
    dl=doclib('data/doclib/')
    dl.load()
    return dl.allwords,dl.articlewords,dl.articletitles

def makematrix(allw,articlew):
    wordvec=[]
    for w,c in allw.items():
        #if c>2 and c<len(articlew)*0.6:
        if c>1:
            wordvec.append(w)
    ll=[[(word in f and f[word] or 0) for word in wordvec ] for f in articlew ]
    return ll,wordvec

def showfeatures(w,h,titles,wordvec,out="data/features.txt"):
    outfile=file(out,'w')
    pc,wc=shape(h)
    toppatterns=[[] ] * len(titles)
    patternnames=[]
    for i in range(pc):
        slist=[]
        for j in range(wc):
            slist.append((h[i,j],wordvec[j]))
        slist.sort(reverse=True)
        n=[s[1] for s in slist[:6]]
        outfile.write( " ".join(n)+'\n')
        patternnames.append(n)

        flist=[]
        for j in range(len(titles)):
            flist.append((w[j,i],titles[j]))
            toppatterns[j].append((w[j,i],i,titles[j]))
        flist.sort(reverse=True)
        
        for f in flist[:5]:
            outfile.write("%f %s\n" % (f[0],f[1]))
        outfile.write('\n')
    return toppatterns,patternnames       

def showarticles(titles,toppatterns,patternnames,out='data/articles.txt'):
    outfile=open(out,'w')
    for j in range(len(titles)):
        outfile.write(titles[j]+'\n')
        toppatterns[j].sort(reverse=True)
        for i in range(3):
            outfile.write( "%f %s\n" % (toppatterns[j][i][0], " ".join(patternnames[toppatterns[j][i][1]])) )
    outfile.write('\n')
            


if __name__=='__main__':
    allw,artw,artt= getarticlewords()
    wordmatrix,wordvec=makematrix(allw,artw)
    print wordvec[0:10] 
    print wordmatrix[1][0:10]            
    v=matrix(wordmatrix)
    weights,feat=nmf.factorize(v,pc=5,iter=100)
    topp,pn=showfeatures(weights,feat,artt,wordvec)
    showarticles(artt,topp,pn)
