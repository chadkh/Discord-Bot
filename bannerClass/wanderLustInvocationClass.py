from .BaseBanner import BaseBanner

class wanderLustInvocationBanner(BaseBanner):
    def __init__(self):
        self.fourStarPity = 0
        self.fiveStarPity = 0
        self.chanceList = self.genProbabilityRange(943,51,6) #according to standard banner rates
        self.drops = [] #probably use a json file to store the data for the banner

    #executed when command happens
    def roll(self):
        pass

    #if the roll happens to hit a 4/5 star then we can filter to those specific sets?
    def filter(self):
        pass

    
    def message(self):
        pass