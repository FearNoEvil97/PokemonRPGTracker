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
        return self.psh.getBrawl()
    
    def addBrawl(self):
        if self.psh.getBrawl() < 5:
            if self.psh.getBrawl() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getBrawl()*6))
            
            self.psh.setBrawl(self.psh.getBrawl() + 1)
            return 0
        else:
            return -1
    
    def subtractBrawl(self):
        if self.psh.getBrawl() > 0:
            if self.psh.getBrawl() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getBrawl()*6))
            
            self.psh.setBrawl(self.psh.getBrawl() - 1)
            return 0
        else:
            return -1
        
    def getCanalyze(self):
        return self.psh.getCanalyze()
    
    def addCanalyze(self):
        if self.psh.getCanalyze() < 5:
            if self.psh.getCanalyze() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getCanalyze()*6))
            
            self.psh.setCanalyze(self.psh.getCanalyze() + 1)
            return 0
        else:
            return -1
    
    def subtractCanalyze(self):
        if self.psh.getCanalyze() > 0:
            if self.psh.getCanalyze() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getCanalyze()*6))
            
            self.psh.setCanalyze(self.psh.getCanalyze() - 1)
            return 0
        else:
            return -1        
        
    def getEvasion(self):
        return self.psh.getEvasion()
    
    def addEvasion(self):
        if self.psh.getEvasion() < 5:
            if self.psh.getEvasion() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getEvasion()*6))
            
            self.psh.setEvasion(self.psh.getEvasion() + 1)
            return 0
        else:
            return -1
    
    def subtractEvasion(self):
        if self.psh.getEvasion() > 0:
            if self.psh.getEvasion() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getEvasion()*6))
            
            self.psh.setEvasion(self.psh.getEvasion() - 1)
            return 0
        else:
            return -1        

    def getMelee(self):
        return self.psh.getMelee()
    
    def addMelee(self):
        if self.psh.getMelee() < 5:
            if self.psh.getMelee() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getMelee()*6))
            
            self.psh.setMelee(self.psh.getMelee() + 1)
            return 0
        else:
            return -1
    
    def subtractMelee(self):
        if self.psh.getMelee() > 0:
            if self.psh.getMelee() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getMelee()*6))
            
            self.psh.setMelee(self.psh.getMelee() - 1)
            return 0
        else:
            return -1        
    

#Survival Specialities
    def getAlert(self):
        return self.psh.getAlert()
    
    def addAlert(self):
        if self.psh.getAlert() < 5:
            if self.psh.getAlert() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getAlert()*6))
            
            self.psh.setAlert(self.psh.getAlert() + 1)
            return 0
        else:
            return -1
    
    def subtractAlert(self):
        if self.psh.getAlert() > 0:
            if self.psh.getAlert() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getAlert()*6))
            
            self.psh.setAlert(self.psh.getAlert() - 1)
            return 0
        else:
            return -1        

    def getAthletic(self):
        return self.psh.getAthletic()
    
    def addAthletic(self):
        if self.psh.getAthletic() < 5:
            if self.psh.getAthletic() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getAthletic()*6))
            
            self.psh.setAthletic(self.psh.getAthletic() + 1)
            return 0
        else:
            return -1
    
    def subtractAthletic(self):
        if self.psh.getAthletic() > 0:
            if self.psh.getAthletic() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getAthletic()*6))
            
            self.psh.setAthletic(self.psh.getAthletic() - 1)
            return 0
        else:
            return -1        

        
    def getNature(self):
        return self.psh.getNature()
    
    def addNature(self):
        if self.psh.getNature() < 5:
            if self.psh.getNature() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getNature()*6))
            
            self.psh.setNature(self.psh.getNature() + 1)
            return 0
        else:
            return -1
    
    def subtractNature(self):
        if self.psh.getNature() > 0:
            if self.psh.getNature() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getNature()*6))
            
            self.psh.setNature(self.psh.getNature() - 1)
            return 0
        else:
            return -1        

    def getStealth(self):
        return self.psh.getStealth()
    
    def addStealth(self):
        if self.psh.getStealth() < 5:
            if self.psh.getStealth() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getStealth()*6))
            
            self.psh.setStealth(self.psh.getStealth() + 1)
            return 0
        else:
            return -1
    
    def subtractStealth(self):
        if self.psh.getStealth() > 0:
            if self.psh.getStealth() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getStealth()*6))
            
            self.psh.setStealth(self.psh.getStealth() - 1)
            return 0
        else:
            return -1        


#ContestSpecialties
    def getAllure(self):
        return self.psh.getAllure()
    
    def addAllure(self):
        if self.psh.getAllure() < 5:
            if self.psh.getAllure() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getAllure()*6))
            
            self.psh.setAllure(self.psh.getAllure() + 1)
            return 0
        else:
            return -1
    
    def subtractAllure(self):
        if self.psh.getAllure() > 0:
            if self.psh.getAllure() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getAllure()*6))
            
            self.psh.setAllure(self.psh.getAllure() - 1)
            return 0
        else:
            return -1        

    def getEtiquette(self):
        return self.psh.getEtiquette()
    
    def addEtiquette(self):
        if self.psh.getEtiquette() < 5:
            if self.psh.getEtiquette() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getEtiquette()*6))
            
            self.psh.setEtiquette(self.psh.getEtiquette() + 1)
            return 0
        else:
            return -1
    
    def subtractEtiquette(self):
        if self.psh.getEtiquette() > 0:
            if self.psh.getEtiquette() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getEtiquette()*6))
            
            self.psh.setEtiquette(self.psh.getEtiquette() - 1)
            return 0
        else:
            return -1        

        
    def getIntimidate(self):
        return self.psh.getIntimidate()
    
    def addIntimidate(self):
        if self.psh.getIntimidate() < 5:
            if self.psh.getIntimidate() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getIntimidate()*6))
            
            self.psh.setIntimidate(self.psh.getIntimidate() + 1)
            return 0
        else:
            return -1
    
    def subtractIntimidate(self):
        if self.psh.getIntimidate() > 0:
            if self.psh.getIntimidate() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getIntimidate()*6))
            
            self.psh.setIntimidate(self.psh.getIntimidate() - 1)
            return 0
        else:
            return -1        

    
    def getPerform(self):
        return self.psh.getPerform()
    
    def addPerform(self):
        if self.psh.getPerform() < 5:
            if self.psh.getPerform() == 0:
                self.psh.setXP(self.psh.getXP() + 6)
            else:
                self.psh.setXP(self.psh.getXP() + (self.psh.getPerform()*6))
            
            self.psh.setPerform(self.psh.getPerform() + 1)
            return 0
        else:
            return -1
    
    def subtractPerform(self):
        if self.psh.getPerform() > 0:
            if self.psh.getPerform() == 1:
                self.psh.setXP(self.psh.getXP() - 6)
            else:
                self.psh.setXP(self.psh.getXP() - (self.psh.getPerform()*6))
            
            self.psh.setPerform(self.psh.getPerform() - 1)
            return 0
        else:
            return -1        
        
    def getMoves(self):
        print("todo")
    
    def addMove(self, name, types, xpCost, dmgType, dmg, description):
        moveList = self.psh.getMoves()
        tempList = [name, types, xpCost, dmgType, dmg, description]
        self.psh.addMove(tempList)
        self.psh.setXP(self.psh.getXP() - xpCost)
    
    def deleteMove(self, moveName):
        print("todo")
        