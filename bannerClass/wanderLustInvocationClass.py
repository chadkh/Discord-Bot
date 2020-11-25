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

    #executed when command happens
    #pass number of rolls as argument
    def roll(self,numRolls:int):
        for x in range(numRolls):
            #getRandomValue from the chanceList
            randomValue = self.genRandomNumber(self.chanceList) #get a random element in this list (getting the rating)
            self.addToPity()
            randomValue = self.checkPity(randomValue)
            #corrected value if a pity is reached
            #filter the drops with the random value as key for the rating
            # and select from corresponding list
            

            #
        #

    def checkPity(self,rating:int):
        if self.fourStarPity % FOUR_STAR_PITY_CAP == 0 or rating == 4:
            self.resetFourStarPity()
            return 4
        elif self.fiveStarPity % FIVE_STAR_PITY_CAP == 0 or rating == 5:
            self.resetFiveStarPity()
            return 5

        return rating
    
    #if the roll happens to hit a 4/5 star then we can filter to those specific sets?
    def filter(self):
        pass

    
    def message(self):
        pass

    def resetFourStarPity(self):
        self.fourStarPity = 0

    def resetFiveStarPity(self):
        self.fiveStarPity = 0

    def addToPity(self):
        self.fourStarPity += 1
        self.fiveStarPity += 1


    