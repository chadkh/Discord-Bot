#
#DEPRECATED
#
#Initial Idea
#Lots of error checking, can be split into more modules for easier clarity
#roll.py

import random
#counters for summons from event,permanent, and weapon banners
#when you get to the value it becomes a chance to be either weapon or character 
#the banners have different percentages per starred item 
class Simulator:
    def __init__(self):
        #these were counters for pity pulls
        self.EB_FOUR_STAR = 0
        self.EB_FIVE_STAR = 0
        self.SB_FOUR_STAR = 0
        self.SB_FIVE_STAR = 0
        self.WB_FOUR_STAR = 0
        self.WB_FIVE_STAR = 0

        #this can be ignored and put in the banner condition
        self.IS_GUARANTEED_FOUR_STAR_CHAR = False
        self.IS_GUARANTEED_FOUR_STAR_WEAPON = False
        self.IS_GUARANTEED_FIVE_STAR_WEAPON = False
        self.IS_GUARANTEED_FIVE_STAR_CHAR = False

    #list of 1000 numbers consisting of the chances get an item
        self.random_list = [3 for i in range(943)]
        self.random_list.extend([4 for i in range(51)])
        self.random_list.extend([5 for i in range(6)])

        random.shuffle(self.random_list)
        print(len(self.random_list))


    #char banner can give a weapon, and vice versa

    #divided into two categories 10-roll and single-roll and determine exactly which one is pulled from and add accordingly to the pity value



    

    #we can check for which banner they are rolling on 
    #etc: if w then weapon
    #elif s then standard
    #elif e then event
    def increment_standard_banner(self,value:int):
        self.SB_FIVE_STAR += 1
        self.SB_FOUR_STAR += 1
        if value == 4 or self.SB_FOUR_STAR == 10:
            self.SB_FOUR_STAR = 0 #reset back to 0 earned 4*
        elif value == 5 or self.SB_FIVE_STAR == 90:
            self.SB_FIVE_STAR = 0 #reset back to 0 earned 5*
    
    def increment_event_banner(self,value:int):
        self.EB_FIVE_STAR += 1
        self.EB_FOUR_STAR += 1
        if value == 4 or self.EB_FOUR_STAR == 10:
            #if the random item we got is not the promo then 2nd will definitely be promo
            if self.IS_GUARANTEED_FOUR_STAR_CHAR:
                #give a guaranteed promo char
                #then change variable back to false after giving promo char
                pass
            else:
                #roll normally 50% chance for promo character
                #check the roll
                #if it is not a promo character, change to variable to true
                pass
            #if is guaranteed then run guaranteed 
            #else proceed rolling as normally 
                #if they do get promo char, stay false
                #else set bool to true (means they got a weapon or non-promo char)
            self.EB_FOUR_STAR = 0 #reset back to 0 earned 4*
        elif value == 5 or self.EB_FIVE_STAR == 90:
            if self.IS_GUARANTEED_FIVE_STAR_CHAR:
                #give a guaranteed promo char
                #then change variable back to false after giving promo char
                pass
            else:
                #roll normally 50% chance for promo character
                #check the roll
                #if it is not a promo character, change to variable to true
                pass
            self.EB_FIVE_STAR = 0 #reset back to 0 earned 5*

    def increment_weapon_banner(self,value:int):
        self.WB_FIVE_STAR += 1
        self.WB_FOUR_STAR += 1
        if value == 4 or self.WB_FOUR_STAR == 10:
            if self.IS_GUARANTEED_FOUR_STAR_WEAPON:
                #give a guaranteed promo char
                #then change variable back to false after giving promo char
                pass
            else:
                #roll normally 50% chance for promo character
                #check the roll
                #if it is not a promo character, change to variable to true
                pass
            self.WB_FOUR_STAR = 0 #reset back to 0 earned 4*
        elif value == 5 or self.WB_FIVE_STAR == 90:
            if self.IS_GUARANTEED_FIVE_STAR_WEAPON:
                #give a guaranteed promo char
                #then change variable back to false after giving promo char
                pass
            else:
                #roll normally 50% chance for promo character/weapon
                #check the roll
                #if it is not a promo character, change to variable to true
                pass
            self.WB_FIVE_STAR = 0 #reset back to 0 earned 5*

    def one_roll(self,banner_type:str):
        value = self.random_list[random.randrange(0,1000)]
        #present item somewhere
        if banner_type == 'e':
            self.increment_event_banner(value)
        elif banner_type == 'w':
            self.increment_weapon_banner(value)
        elif banner_type == 's':
            self.increment_standard_banner(value)

    #then add the number of rolls to the corresponding variable
    def multi_summoning(self,banner_type:str):
            #perform wishing here 
        for i in range(10):
            self.one_roll(banner_type)
        # print(f'You Rolled on the this banner type: {banner_type}')

    def single_summoning(self,banner_type:str):
        self.one_roll(banner_type)

