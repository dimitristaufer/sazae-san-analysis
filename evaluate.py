# pylint: disable=W,C,R

import json

f_old = open('./Episode_1/annotated_EP_1.json')
data_old = json.load(f_old)

f_new = open('./Episode_2200/annotated_EP_2200.json')
data_new = json.load(f_new)

wo_FPlus = 0
wo_F = 0
wo_N = 0
wo_M = 0
wo_MPlus = 0

wy_FPlus = 0
wy_F = 0
wy_N = 0
wy_M = 0
wy_MPlus = 0

mo_FPlus = 0
mo_F = 0
mo_N = 0
mo_M = 0
mo_MPlus = 0

my_FPlus = 0
my_F = 0
my_N = 0
my_M = 0
my_MPlus = 0

count = 0
for spf in data_old.values():
    count += 1
    
print(count)
exit(0)

for spf in data_new.values():
    woman = spf["woman"]
    young = spf["young"]
    level = spf["level"]
    if woman == True:
        if young == True:
            if level == 'F+':
                wy_FPlus += 1
            if level == 'F':
                wy_F += 1
            if level == 'NN':
                wy_N += 1
            if level == 'M':
                wy_M += 1
            if level == 'M+':
                wy_MPlus += 1
        else:
            if level == 'F+':
                wo_FPlus += 1
            if level == 'F':
                wo_F += 1
            if level == 'NN':
                wo_N += 1
            if level == 'M':
                wo_M += 1
            if level == 'M+':
                wo_MPlus += 1
    else:
        if young == True:
            if level == 'F+':
                my_FPlus += 1
            if level == 'F':
                my_F += 1
            if level == 'NN':
                my_N += 1
            if level == 'M':
                my_M += 1
            if level == 'M+':
                my_MPlus += 1
        else:
            if level == 'F+':
                mo_FPlus += 1
            if level == 'F':
                mo_F += 1
            if level == 'NN':
                mo_N += 1
            if level == 'M':
                mo_M += 1
            if level == 'M+':
                mo_MPlus += 1
                
print("")
print("wo_FPlus: " + str(wo_FPlus))
print("wo_F: " + str(wo_F))
print("wo_N: " + str(wo_N))
print("wo_M: " + str(wo_M))
print("wo_MPlus: " + str(wo_MPlus))
print("")
print("wy_FPlus: " + str(wy_FPlus))
print("wy_F: " + str(wy_F))
print("wy_N: " + str(wy_N))
print("wy_M: " + str(wy_M))
print("wy_MPlus: " +str(wy_MPlus))
print("")
print("mo_FPlus: " + str(mo_FPlus))
print("mo_F: " + str(mo_F))
print("mo_N: " + str(mo_N))
print("mo_M: " + str(mo_M))
print("mo_MPlus: " + str(mo_MPlus))
print("")
print("my_FPlus: " + str(my_FPlus))
print("my_F: " + str(my_F))
print("my_N: " + str(my_N))
print("my_M: " + str(my_M))
print("my_MPlus: " + str(my_MPlus))
