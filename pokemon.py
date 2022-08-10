import os.path
import PSH

class Pokemon:
    def __init__(self, name):
        path = "pokemon/" + name + ".json"
        if not os.path.exists(path):
            f = open(path, "x")
            f.close()
        self.psh = PSH(path)
    
    def initialize(self, stats):
        print("Do Something")
    
    def getLevel(self):
        print("Do Something")
    
    def getName(self):
        return self.psh.getName()
    
    def setName(self, name):
        self.psh.setName(name)
        
    def getPokemon(self):
        return self.psh.getPokemon()
    
    def setPokemon(self, pokemon):
        self.psh.setPokemon(pokemon)
        
    def getType(self):
        return self.psh.getType()
    
    def setType(self, ptype):
        self.psh.setType(ptype)
        
    def getStarter(self):
        return self.psh.getStarter()
    
    def setStarter(self, starter):
        self.psh.setStarter(starter)
        
    def getGender(self):
        return self.psh.getGender()
    
    def setGender(self, gender):
        self.psh.setGender(gender)
        
    def getAbility(self):
        return self.psh.getAbility()
    
    def setAbility(self, ability):
        self.psh.setAbility(ability)

#Base Stats        
    def getStr(self):
        return self.psh.getBaseStr() + self.psh.getAddedStr()
    
    def addStr(self):
        if self.psh.getAddedStr() < self.psh.getMaxStr():
            self.psh.setAddedStr(self.psh.getAddedStr() + 1)
            self.psh.setXP(self.psh.getXP() + (self.psh.getAddedStr() + self.psh.getBaseStr())*10)
            return 0
        else:
            return -1
    
    def subtractStr(self):
        if self.psh.getAddedStr() > 0:
            self.psh.setAddedStr(self.psh.getAddedStr() - 1)
            self.psh.setXP(self.psh.getXP() - (self.psh.getAddedStr() + self.psh.getBaseStr())*10)
            return 0
        else:
            return -1

    def getDex(self):
        return self.psh.getBaseDex() + self.psh.getAddedDex()
    
    def addDex(self):
        if self.psh.getAddedDex() < self.psh.getMaxDex():
            self.psh.setAddedDex(self.psh.getAddedDex() + 1)
            self.psh.setXP(self.psh.getXP() + (self.psh.getAddedDex() + self.psh.getBaseDex())*10)
            return 0
        else:
            return -1
    
    def subtractDex(self):
        if self.psh.getAddedDex() > 0:
            self.psh.setAddedDex(self.psh.getAddedDex() - 1)
            self.psh.setXP(self.psh.getXP() - (self.psh.getAddedDex() + self.psh.getBaseDex())*10)
            return 0
        else:
            return -1
            
    def getVit(self):
        return self.psh.getBaseVit() + self.psh.getAddedVit()
    
    def addVit(self):
        if self.psh.getAddedVit() < self.psh.getMaxVit():
            self.psh.setAddedVit(self.psh.getAddedVit() + 1)
            self.psh.setXP(self.psh.getXP() + (self.psh.getAddedVit() + self.psh.getBaseVit())*10)
            return 0
        else:
            return -1
    
    def subtractVit(self):
        if self.psh.getAddedVit() > 0:
            self.psh.setAddedVit(self.psh.getAddedVit() - 1)
            self.psh.setXP(self.psh.getXP() - (self.psh.getAddedVit() + self.psh.getBaseVit())*10)
            return 0
        else:
            return -1   
        
    def getSpl(self):
        return self.psh.getBaseSpl() + self.psh.getAddedSpl()
    
    def addSpl(self):
        if self.psh.getAddedSpl() < self.psh.getMaxSpl():
            self.psh.setAddedSpl(self.psh.getAddedSpl() + 1)
            self.psh.setXP(self.psh.getXP() + (self.psh.getAddedSpl() + self.psh.getBaseSpl())*10)
            return 0
        else:
            return -1
    
    def subtractSpl(self):
        if self.psh.getAddedSpl() > 0:
            self.psh.setAddedSpl(self.psh.getAddedSpl() - 1)
            self.psh.setXP(self.psh.getXP() - (self.psh.getAddedSpl() + self.psh.getBaseSpl())*10)
            return 0
        else:
            return -1
            
    def getIns(self):
        return self.psh.getBaseIns() + self.psh.getAddedIns()
    
    def addIns(self):
        if self.psh.getAddedIns() < self.psh.getMaxIns():
            self.psh.setAddedIns(self.psh.getAddedIns() + 1)
            self.psh.setXP(self.psh.getXP() + (self.psh.getAddedIns() + self.psh.getBaseIns())*10)
            return 0
        else:
            return -1
    
    def subtractIns(self):
        if self.psh.getAddedIns() > 0:
            self.psh.setAddedIns(self.psh.getAddedIns() - 1)
            self.psh.setXP(self.psh.getXP() - (self.psh.getAddedIns() + self.psh.getBaseIns())*10)
            return 0
        else:
            return -1
        
#Basic Stats
    def getHP(self):
        return self.psh.getHP()
    
    def setHP(self, hp):
        self.psh.setHP(hp)
        
    def addHP(self):
        if self.psh.getHP() < self.psh.getMaxHP():
            self.psh.setHP(self.psh.getHP() + 1)
            return 0
        else:
            return -1
    
    def subtractHP(self):
        if self.psh.getHP() > 0:
            self.psh.setHP(self.psh.getHP() - 1)
            return 0
        else:
            return -1
            
    def getXP(self):
        return self.psh.getXP()
    
    def setXP(self, XP):
        self.psh.setXP(XP)
        
    def addXP(self):
        self.psh.setXP(self.psh.getXP() + 1)
        return 0
     
    def subtractXP(self):
        self.psh.setXP(self.psh.getXP() - 1)
     
    def getDisobedience(self):
        return self.psh.getDisobedience()
        
    def addDisobedience(self):
        if self.psh.getDisobedience() < 5:
            self.psh.setDisobedience(self.psh.getDisobedience() + 1)
            return 0
        else:
            return -1
    
    def subtractDisobedience(self):
        if self.psh.getDisobedience() > 0:
            self.psh.setDisobedience(self.psh.getDisobedience() - 1)
            return 0
        else:
            return -1  
    
    def getHeldItem(self):
        return self.psh.getHeldItem()
    
    def setHeldItem(self, HeldItem):
        self.psh.setHeldItem(HeldItem)
        
    def getHappiness(self):
        return self.psh.getHappiness()
        
    def addHappiness(self):
        if self.psh.getHappiness() < 5:
            self.psh.setHappiness(self.psh.getHappiness() + 1)
            return 0
        else:
            return -1
    
    def subtractHappiness(self):
        if self.psh.getHappiness() > 0:
            self.psh.setHappiness(self.psh.getHappiness() - 1)
            return 0
        else:
            return -1         
        
    def getLoyalty(self):
        return self.psh.getLoyalty()
        
    def addLoyalty(self):
        if self.psh.getLoyalty() < 5:
            self.psh.setLoyalty(self.psh.getLoyalty() + 1)
            return 0
        else:
            return -1
    
    def subtractLoyalty(self):
        if self.psh.getLoyalty() > 0:
            self.psh.setLoyalty(self.psh.getLoyalty() - 1)
            return 0
        else:
            return -1        
        
#Skills
    def getFight(self):
        return self.psh.getFight()
    
    def addFight(self):
        if self.psh.getFight() < 5:
            if self.psh.getFight() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getFight()*8))
            
            self.psh.setFight(self.psh.getFight() + 1)
            return 0
        else:
            return -1
    
    def subtractFight(self):
        if self.psh.getFight() > 0:
            if self.psh.getFight() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getFight()*8))
            
            self.psh.setFight(self.psh.getFight() - 1)
            return 0
        else:
            return -1
        
    def getSurvival(self):
        return self.psh.getSurvival()
    
    def addSurvival(self):
        if self.psh.getSurvival() < 5:
            if self.psh.getSurvival() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getSurvival()*8))
            
            self.psh.setSurvival(self.psh.getSurvival() + 1)
            return 0
        else:
            return -1
    
    def subtractSurvival(self):
        if self.psh.getSurvival() > 0:
            if self.psh.getSurvival() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getSurvival()*8))
            
            self.psh.setSurvival(self.psh.getSurvival() - 1)
            return 0
        else:
            return -1

    def getContest(self):
        return self.psh.getContest()
    
    def addContest(self):
        if self.psh.getContest() < 5:
            if self.psh.getContest() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getContest()*8))
            
            self.psh.setContest(self.psh.getContest() + 1)
            return 0
        else:
            return -1
    
    def subtractContest(self):
        if self.psh.getContest() > 0:
            if self.psh.getContest() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getContest()*8))
            
            self.psh.setContest(self.psh.getContest() - 1)
            return 0
        else:
            return -1

#6 for new, then 6x current score for specialties        
#Fight Specialties
    def getBrawl(self):
        return self.data["FightSpecialties"]["Brawl"]
    
    def setBrawl(self, Brawl):
        self.data["FightSpecialties"]["Brawl"] = Brawl
        self.save()
        
    def getCanalyze(self):
        return self.data["FightSpecialties"]["Canalyze"]
    
    def setCanalyze(self, Canalyze):
        self.data["FightSpecialties"]["Canalyze"] = Canalyze
        self.save()        
        
    def getEvasion(self):
        return self.data["FightSpecialties"]["Evasion"]
    
    def setEvasion(self, Evasion):
        self.data["FightSpecialties"]["Evasion"] = Evasion
        self.save()   
    
    def getMelee(self):
        return self.data["FightSpecialties"]["Melee"]
    
    def setMelee(self, Melee):
        self.data["FightSpecialties"]["Melee"] = Melee
        self.save()     

#Survival Specialities
    def getAlert(self):
        return self.data["SurvivalSpecialties"]["Alert"]
    
    def setAlert(self, Alert):
        self.data["SurvivalSpecialties"]["Alert"] = Alert
        self.save() 
        
    def getAthletic(self):
        return self.data["SurvivalSpecialties"]["Athletic"]
    
    def setAthletic(self, Athletic):
        self.data["SurvivalSpecialties"]["Athletic"] = Athletic
        self.save() 
        
    def getNature(self):
        return self.data["SurvivalSpecialties"]["Nature"]
    
    def setNature(self, Nature):
        self.data["SurvivalSpecialties"]["Nature"] = Nature
        self.save() 
        
    def getStealth(self):
        return self.data["SurvivalSpecialties"]["Stealth"]
    
    def setStealth(self, Stealth):
        self.data["SurvivalSpecialties"]["Stealth"] = Stealth
        self.save()

#ContestSpecialties
    def getAllure(self):
        return self.data["ContestSpecialties"]["Allure"]
    
    def setAllure(self, Allure):
        self.data["ContestSpecialties"]["Allure"] = Allure
        self.save() 
        
    def getEtiquette(self):
        return self.data["ContestSpecialties"]["Etiquette"]
    
    def setEtiquette(self, Etiquette):
        self.data["ContestSpecialties"]["Etiquette"] = Etiquette
        self.save() 
        
    def getIntimidate(self):
        return self.data["ContestSpecialties"]["Intimidate"]
    
    def setIntimidate(self, Intimidate):
        self.data["ContestSpecialties"]["Intimidate"] = Intimidate
        self.save()
        
    def getPerform(self):
        return self.data["ContestSpecialties"]["Perform"]
    
    def setPerform(self, Perform):
        self.data["ContestSpecialties"]["Perform"] = Perform
        self.save()
        
    def getMoves(self):
        return self.data["Moves"]
    
    def setMoves(self, Moves):
        self.data["Moves"] = Moves
        self.save()
        