#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding("utf8")
import os, time,json,traceback
import json
from math import sqrt,exp,pow
from sim_algorathm import sim_algorathm

class user_recommendation:
    def __init__(self,data_file,debug=True):
        self.debug = debug
        self.data_file = data_file
        self.algo = sim_algorathm()
        self.docs = Docs(data_file,debug=False)
        self.docs.load()

    def get_users(self, uid):
        sims = []
        for k,v in self.docs.tf_dict.items():
            if k == uid:
                continue
            #print uid,k
            (l1,l2) = self.docs.get_weight_vector(k, uid)
            if len(l1) == 0 or len(l2) == 0:
                continue
            #s =  self.algo.sim_pearson(l1,l2) 
            #s =  self.algo.sim_cos(l1,l2) 
            #s =  self.algo.sim_distance(l1,l2) 
            s =  self.algo.sim_common(l1,l2) 
            sims.append( (s,k) )
        sims.sort()
        sims = sims[0:5]
        print "uid:",uid
        print "query:", json.dumps( self.docs.tf_dict[uid],ensure_ascii=False)          
        for k,v in sims:
            print k,v
            print json.dumps(self.docs.tf_dict[v],ensure_ascii=False)
        return sims
    def get_items(self,uid):
        sims = self.get_users(uid)    
        item_sims = {}
        total_weight = {}
        have_q = self.docs.tf_dict[uid]
        for sim,uid in sims:
            items = self.docs.tf_dict[uid]
            len_nor = sqrt( len(items))
            for word,wht in items.items():
                if word in have_q:
                    continue
                if word not in item_sims:
                    item_sims[word] = sim
                else:
                    item_sims[word] += sim
                if word not in total_weight:
                    total_weight[word] = wht * self.idf_dict[word]* len_nor * sim
                else:         
                    total_weight[word] += wht * self.idf_dict[word]* len_nor * sim
        #for item,weight  in total_weight.items():
        #    total_weight[item] = total_weight[item]/ item_sims[item]
        
        r_item_list = [ (score,i) for i,score in total_weight.items()]
        r_item_list.sort()
        r_item_list.reverse()
        ret= r_item_list[0:20] 
        for s,item in ret:
            print s,item        
        return ret             
         
                  
if __name__ == '__main__':
    usage = "usage:%s data_file "
    print "welcome to use user recommendation"
    if len(sys.argv) <     2:
        print usage
    
    rem = user_recommendation(sys.argv[1])
    while True:
        uid = raw_input("please input uid:").strip()
        print "uid:",uid
        if uid == "quit":
            break
        users = rem.get_users(uid)
        
        #users = rem.get_items(uid)
        print json.dumps(users,ensure_ascii=False)          

