import json

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
    #create a list of dicts
    #to convert to json 
def makeCharList():
    toRead = open('.\\data\\characterdata',mode='r')
    # fullStr = ""
    charId = 0
    char_list = []
    for x in toRead:
        name,code = x.rstrip().split(',')
        count = 0
        char_info = {} #dict to hold character information
        charId += 1
        char_info["name"] = name
        for number in code:
            if count == 0:
                # string += f" rating : {number}\n id : {str(charId) + '1' + code}\n "
                char_info["rating"] = number
                char_info["id"] = str(charId) + "1" + code
            elif count == 1:
                # string += f"vision : {element[number]}\n "
                char_info["vision"] = element[number]
            elif count == 2:
                # string += f"weapon : {weaponType[number]}\n"
                char_info["weapon"] = weaponType[number]
            count += 1

        # name += f"\n{string}"
        # fullStr += name
        char_list.append(char_info) #add the chardict into the list
    # print(char_list)
    with open(".\\data\\wanderLustInvocationDrops.json",'w') as outfile:
        json.dump(char_list,outfile)
    
    toRead.close()
    # return fullStr
    


def makeWeaponList():
    toRead = open('.\\data\\weapondata',mode='r')
    # fullStr = ""
    currentId = ""
    weapon_list = []
    for x in toRead:
        # string = ""
        x = x.rstrip()
        weapon_data = {}
        if len(x) == 1:
            currentId = x
        else:
            name,wepType = x.split(',')
            weapon_data["name"] = name
            weapon_data["rating"] = currentId
            weapon_data["weaponType"] = weaponType[wepType]
            # string += f"name : {name}\n rating : {currentId}\n weaponType : {weaponType[wepType]}\n"
            weapon_list.append(weapon_data)
        # fullStr += string
    with open(".\\data\\wanderLustInvocationDrops.json","a") as outfile:
        json.dump(weapon_list,outfile)
    # return fullStr

def makeBannerList():

    banner_list = {'childe':'childe', 'farewell':'childe', 'fos':'childe',
        'klee':'klee', 'sparkling':'klee', 'ss':'klee',
        'venti':'venti', 'ballad':'venti', 'big':'venti',
        'wanderlust':'standard', 'wli':'standard', 'standard':'standard', 'perm':'standard',
        'epitome':'epitome','ei':'epitome'}

    with open(".\\data\\bannerList.json","w") as outfile:
        json.dump(banner_list,outfile)


if __name__ == "__main__":
    # # makeCharList()
    # # makeWeaponList()
    makeBannerList()
    #data = open(".\\data\\wanderLustInvocationDrops.json",'r')
    #jsonData = json.load(data)
    #list of dictionaries
    #jsonData = [dict{}]
    # for x in jsonData:
    #     if x['rating'] == "5":
    #         print(x)
    #filtered = filter(lambda x: x['rating'] == str(5),jsonData)
    #for x in filtered:
    #    print(x)
    # print('5' == str(5))

