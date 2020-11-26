from .BaseBanner import BaseBanner

FOUR_STAR_PITY_CAP = 10
FIVE_STAR_PITY_CAP = 90
DROPSFILE_PATH = ".\\data\\wanderLustInvocationDrops.json"

class wanderLustInvocationBanner(BaseBanner):
    def __init__(self):
        self.fourStarPity = 0
        self.fiveStarPity = 0
        self.chanceList = self.genProbabilityRange(943,51,6) #according to standard banner rates
        self.drops = self.retrieveDropList(DROPSFILE_PATH) #probably use a json file to store the data for the banner
        # print("printed drops!" ,self.drops)
        #could maintain a list of the different starred items instead of having to filter constantly

    #executed when command happens
    #pass number of rolls as argument
    def roll(self,numRolls:int):
        itemList = []
        for x in range(numRolls):
            #getRandomValue from the chanceList
            #could change to either scramble list once per roll or shuffle once and base it off seed (more ideal for 10-pulls?)
            self.scramble(self.chanceList)
            randomValue = self.chanceList[self.genRandomNumber(self.chanceList)] #get a random element in this list (getting the rating)
            self.addToPity()
            #corrected value if a pity is reached
            randomValue = self.checkPity(randomValue)

            #filter the drops with the random value as key for the rating
            tempDrops = list(self.refine(self.drops,randomValue))
            # print(tempDrops)
            #item is a dict
            item = tempDrops[self.genRandomNumber(tempDrops)]
            itemList.append(item)
        
        return self.message(itemList)

    def checkPity(self,rating:int):
        print(f"Four Star Pity Count: {self.fourStarPity}")
        print(f"Five Star Pity Count: {self.fiveStarPity}")
        if self.fourStarPity % FOUR_STAR_PITY_CAP == 0 or rating == 4:
            self.resetFourStarPity()
            return 4
        elif self.fiveStarPity % FIVE_STAR_PITY_CAP == 0 or rating == 5:
            self.resetFiveStarPity()
            return 5

        return rating
    
    #if the roll happens to hit a 4/5 star then we can filter to those specific sets

    
    def message(self,iterable:list):
        return "".join([ f"You got the {dictionary['rating']}-star item {dictionary['name']}!\n" for dictionary in iterable ])

    def resetFourStarPity(self):
        self.fourStarPity = 0

    def resetFiveStarPity(self):
        self.fiveStarPity = 0

    def addToPity(self):
        self.fourStarPity += 1
        self.fiveStarPity += 1


    