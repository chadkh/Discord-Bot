#BaseBanner.py
#Implements the Base Banner Gacha attributes
import random
import json
class BaseBanner:
    def __init__(self):
        #have a list of drops according to banner
        self.drops = []
    #what will be the same is generating probability

    # #create a chance method for the 50/50
    # def getChance(self):
    #     pass

    # #maintain a list of possible drops in a banner
    # def getPossibleDrops(self):
    #     pass

    #generates the probability range for a banner
    def genProbabilityRange(self,b:int,p:int,o:int):
        
        return [3 for x in range(b)] + [4 for x in range(p)] + [5 for x in range(o)]
        


    #generates a random number from 0 to length of list (getting the index)
    def genRandomNumber(self,arr:list):
        
        return random.randrange(0,len(arr))


    #rearrange the array in a random order
    def scramble(self,arr:list):
        random.shuffle(arr)

    #returns an iterable with filtered condition
    def refine(self,iterable,rating):
        # print(iterable)
        filtered = filter(lambda x: x['rating'] == str(rating),iterable)
        # for x in filtered:
        #     print(x)
        return filtered
        

    def retrieveDropList(self,path:str):
        data = open(path,'r')
        jsonData = json.load(data)
        data.close()
        return jsonData