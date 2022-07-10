# pylint: disable=W,C,R

import json
from re import X
import readchar
import io
import os
 
f_old = open('./Episode_2200/toAnalyze_EP_2200.json')
data_old = json.load(f_old)["data"]

annotated = {}

if os.path.isfile('./Episode_2200/annotated_EP_2200.json') and os.access('./Episode_1/annotated_EP_1.json', os.R_OK):
    annotated = open('./Episode_2200/annotated_EP_2200.json')
    annotated = json.load(annotated)

for occurence in data_old:
    if occurence["start_time"] in annotated:
        continue
    print(occurence)
    print("")
    print("woman? (y/n) ")
    occurence["woman"] = str(repr(readchar.readchar()))
    if occurence["woman"] == "'q'":
        exit(0)
    if occurence["woman"] == "'s'":
        continue
    if occurence["woman"] == "'y'":
        occurence["woman"] = True
    else:
        occurence["woman"] = False
    print("young? (y/n) ")
    occurence["young"] = str(repr(readchar.readchar()))
    if occurence["young"] == "'q'":
        exit(0)
    if occurence["young"] == "'s'":
        continue
    if occurence["young"] == "'y'":
        occurence["young"] = True
    else:
        occurence["young"] = False
    annotated[occurence["start_time"]] = occurence
    with open("./Episode_2200/annotated_EP_2200.json", "w") as j:
	    json.dump(annotated, j, ensure_ascii=False)
    
    
    
    

