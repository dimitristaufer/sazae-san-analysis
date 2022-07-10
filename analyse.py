# pylint: disable=W,C,R

import json

f_old = open('./Episode_1/transcript_95.json')
f_new = open('./Episode_2200/transcript_95.json')

data_old = json.load(f_old)
data_new = json.load(f_new)

toAnalyze_EP_1 = {
    "data" : []
}

toAnalyze_EP_2200 = {
    "data" : []
}

def wordOfInterest(word):
    # F+
    if word.endswith("わ"):
        return "F+"
    if word.endswith("わよ"):
        return "F+"
    if word.endswith("わね"):
        return "F+"
    if word.endswith("だわ"):
        return "F+"
    if word.endswith("かしら"):
        return "F+"
    # F
    if word.endswith("の"):
        return "F"
    if word.endswith("のよ"):
        return "F"
    if word.endswith("のね"):
        return "F"
    if word.endswith("てね"):
        return "F"
    if word.endswith("でしょう"):
        return "F"
    # NN
    if word.endswith("ね"):
        return "NN"
    if word.endswith("よ"):
        return "NN"
    if word.endswith("もん"):
        return "NN"
    if word.endswith("さ"):
        return "NN"
    if word.endswith("かな"):
        return "NN"
    # M
    if word.endswith("だろう"):
        return "M"
    # M+
    if word.endswith("ぜ"):
        return "M+"
    if word.endswith("ぞ"):
        return "M+"
    if word.endswith("な"):
        return "M+"
    if word.endswith("かよ"):
        return "M+"
    return ""

for part in data_old["parts"]:
    for word in part["words"]:
        level = wordOfInterest(str(word["word"].partition('|')[0]))
        if level != "":
            toAnalyze_EP_1["data"].append({"sfp" : str(word["word"].partition('|')[0]), "level" : level, "start_time" : word["start_time"][:-7]})
            
for part in data_new["parts"]:
    for word in part["words"]:
        level = wordOfInterest(str(word["word"].partition('|')[0]))
        if level != "":
            toAnalyze_EP_2200["data"].append({"sfp" : str(word["word"].partition('|')[0]), "level" : level, "start_time" : word["start_time"][:-7]})
            
#print(toAnalyze_old)
#print("")
#print(toAnalyze_new)

with open("./Episode_1/toAnalyze_EP_1.json", "w") as j:
	json.dump(toAnalyze_EP_1, j, ensure_ascii=False)
 
with open("./Episode_2200/toAnalyze_EP_2200.json", "w") as j:
	json.dump(toAnalyze_EP_2200, j, ensure_ascii=False)