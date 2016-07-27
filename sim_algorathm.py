#coding=utf-8
import sys,os
reload(sys)
sys.setdefaultencoding("utf8")
import json
import time
import math
from math import exp,pow,sqrt
import traceback

class sim_algorathm:
    def __init__(self,debug = False):
        self.debug = debug

    def sim_std(self,c1,c2):
        sum1 = sqrt(sum([ pow(x,2) for x in c1]))
        sum2 = sqrt(sum([pow(x,2) for x in c2] ))
        #sum1 = sum(c1)
        #sum2 = sum(c2)
        rate = float(sum1)/float(sum2)
        if abs(rate) < 1:
            rate = abs(1/rate)
        if self.debug:
            print "sum rate:"
            print "c1:",c1
            print "c2:",c2
            print "distance info:", sum1,sum2 ,rate
        return rate
         
    def sim_cos(self,c1,c2):
        c_diff = sum( [ c1[i] * c2[i] for i in range(len(c1)) ])
        c1_d = sum([ pow( c1[i],2) for i in range(len(c1))  ] )
        c2_d = sum([ pow( c2[i],2) for i in range(len(c1))  ] )
        rrate = c_diff / ( float( sqrt(c1_d)) * float( sqrt(c2_d))) 
        r_distance = float( "%0.3f" % (1 - rrate)) 
        if self.debug:
            print "cos:"
            print "c1:",c1
            print "c2:",c2
            print "distance info:", c_diff,c1_d , c2_d,rrate,r_distance
        return r_distance 
    def sim_distance(self,c1,c2):
        dis = sqrt(sum([ pow(c1[i]-c2[i],2) for i in range(len(c1))  ] )  ) 
        return dis
    def sim_common_rate(self,c1,c2):
        diff = sum( [c1[i] + c2[i] for i in range(len(c1)) if c1[i] != 0 and c2[i] != 0])
        dis = 1 - float(diff)/sqrt( sum(c1 + c2)   )
        return dis
    def sim_common(self,c1,c2):
        diff = sum( [c1[i] + c2[i] for i in range(len(c1)) if c1[i] != 0 and c2[i] != 0])
        dis =  1/float(diff)
        return dis
    def sim_pearson(self,c1,c2):
        n = len(c1)
        s1 = sum(c1)
        s2 = sum(c2)
        vsum = sum( [c1[i] * c2[i]  for i in range(n)])
        c_diff = vsum - s1*s2/n
        c1_d = sum ([pow(x,2) for x in c1  ]) - pow(s1,2)/n
        c2_d = sum ([pow(x,2) for x in c2  ]) - pow(s2,2)/n

        if c1_d == 0 or c2_d == 0:
            if self.debug :print "data all is zero" 
            return -1
        c_base = ( float( sqrt(c1_d)) * float( sqrt(c2_d))) 
        rrate = c_diff / c_base
        r_distance = float( "%0.3f" % (1 - rrate)) 
        if self.debug:
            print "pearson2"
            print "distance info:",c1_d , c2_d,c_diff,c_base,rrate,r_distance
        return r_distance 
