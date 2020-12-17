#this is a simple python script that will add my "water mark" on a piece of code
#Calvin Mozola
#September 21 2019

import random

def genRadomWaterMark():
    calvinOutline = [
    ['C','℃','ℂ','c̷̛̳̘̗̟͙̦͑̽̓͛̇͜','C̴̡̡̬͝','Ⓒ','[̲̅C]','∙∙·▫▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒC'],
    ['A','Å','A̸͚͎̫̠̫͖͘','Ⓐ','[̲̅A]'],
    ['L','ℒ','ℓ','L̵̞̀͗̓͌̍̋̏','Ⓛ','[̲̅L]'],
    ['V','℣','V̵̨̨͙̯̳̳̤̳̫̀̍̃̍̕͝','Ⓥ','۷','[̲̅V]'],
    ['I','ℹ','ⅈ','Ì̷̡͕̼̦̯̣̗͇','Ⓘ','[̲̅I]'],
    ['N','ℕ','N̸͇̗̬̑ͅ','Ⓝ','[̲̅N]','Nᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫ₒₒ▫ᵒᴼᵒ▫▫·∙∙'],
    ]
    addOnOutline = [' is my hero'," is great", " :)", " was here"]
    str="# -->  ".encode("utf-8")
    for list in calvinOutline:
        str += list[ random.randint(0,len(list)-1)].encode("utf-8")
    str+= addOnOutline[ random.randint(0,len(addOnOutline)-1)].encode("utf-8")
    return str

fileName = "test"
fileExtention = ".py"
saveName = fileName+"_waterMarked" + fileExtention
file = open(fileName+fileExtention,"r")#open with read access

content = file.readlines()
endResult = []
for line in content:
    endResult.append( line[:-1].encode("utf-8") + genRadomWaterMark() )
file.close()
saveFile = open(saveName,"wb+")
for lines in endResult:
    saveFile.write( lines + "\n".encode("utf-8") )
#saveFile.write("\n".join(endResult))
saveFile.close()
