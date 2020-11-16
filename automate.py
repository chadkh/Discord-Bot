
element = {'1':"Electro",
           '2':"Hydro",
           '3':"Pyro",
           '4':"Cryo",
           '5':"Geo",
           '6':"Anemo"}

weaponType = {'1':"Sword",
           '2':"Catalyst",
           '3':"Claymore",
           '4':"Bow",
           '5':"Polearm",
           }
def makeCharList():
    toRead = open('genshindata.txt',mode='r')
    fullStr = ""
    charId = 0
    for x in toRead:
        name,code = x.rstrip().split(',')
        count = 0
        string = ""
        charId += 1
        for number in code:
            if count == 0:
                string += f" rating : {number}\n id : {str(charId) + '1' + code}\n "
            elif count == 1:
                string += f"vision : {element[number]}\n "
            elif count == 2:
                string += f"weapon : {weaponType[number]}\n"
            count += 1

        name += f"\n{string}"
        fullStr += name
    
    toRead.close()
    return fullStr
    
print(makeCharList())

def makeWeaponList():
    toRead = open('genshinweapondata.txt',mode='r')
    fullStr = ""
    weaponId = 0
    currentId = ""
    
    for x in toRead:
        string = ""
        x = x.rstrip()
        
        if len(x) == 1:
            currentId = x
        else:
            name,wepType = x.split(',')
            
            string += f"name : {name}\n rating : {currentId}\n weaponType : {weaponType[wepType]}\n"
        
        fullStr += string

    return fullStr
print(makeWeaponList())
