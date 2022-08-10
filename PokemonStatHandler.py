import json
class PSH:
    def __init__(self, path):
        self.path = path
        f = open(self.path, "r")
        self.data = json.load(f)
        f.close()
    
    def save(self):
        f = open(self.path, "w")
        json.dump(self.data, f)
        f.close()
    
    def getName(self):
        return self.data["Name"]
    
    def setName(self, name):
        self.data["Name"] = name
        self.save()
        
    def getPokemon(self):
        return self.data["Pokemon"]
    
    def setPokemon(self, pokemon):
        self.data["Pokemon"] = pokemon
        self.save()
        
    def getType(self):
        return self.data["Type"]
    
    def setType(self, ptype):
        self.data["Type"] = ptype
        self.save()
        
    def getStarter(self):
        return self.data["Starter"]
    
    def setStarter(self, starter):
        self.data["Starter"] = starter
        self.save()
        
    def getGender(self):
        return self.data["Gender"]
    
    def setGender(self, gender):
        self.data["Gender"] = gender
        self.save()
        
    def getAbility(self):
        return self.data["Ability"]
    
    def setAbility(self, ability):
        self.data["Ability"] = ability
        self.save()
        
    def getBaseStr(self):
        return self.data["Base"]["Str"]
    
    def setBaseStr(self, basestr):
        self.data["Base"]["Str"] = basestr
        self.save()
        
    def getBaseDex(self):
        return self.data["Base"]["Dex"]
    
    def setBaseDex(self, basedex):
        self.data["Base"]["Dex"] = basedex
        self.save()
        
    def getBaseVit(self):
        return self.data["Base"]["Vit"]
    
    def setBaseVit(self, basevit):
        self.data["Base"]["Vit"] = basevit
        self.save()
        
    def getBaseSpl(self):
        return self.data["Base"]["Spl"]
    
    def setBaseSpl(self, basespl):
        self.data["Base"]["Spl"] = basespl
        self.save()
        
    def getBaseIns(self):
        return self.data["Base"]["Ins"]
    
    def setBaseIns(self, baseins):
        self.data["Base"]["Ins"] = baseins
        self.save()
        
    def getBaseHP(self):
        return self.data["Base"]["HP"]
    
    def setBaseHP(self, basehp):
        self.data["Base"]["HP"] = basehp
        self.save()

#Max Stats
    def getMaxStr(self):
        return self.data["Max"]["Str"]
    
    def setMaxStr(self, maxstr):
        self.data["Max"]["Str"] = maxstr
        self.save()
        
    def getMaxDex(self):
        return self.data["Max"]["Dex"]
    
    def setMaxDex(self, maxdex):
        self.data["Max"]["Dex"] = maxdex
        self.save()
        
    def getMaxVit(self):
        return self.data["Max"]["Vit"]
    
    def setMaxVit(self, maxvit):
        self.data["Max"]["Vit"] = maxvit
        self.save()
        
    def getMaxSpl(self):
        return self.data["Max"]["Spl"]
    
    def setMaxSpl(self, maxspl):
        self.data["Max"]["Spl"] = maxspl
        self.save()
        
    def getMaxIns(self):
        return self.data["Max"]["Ins"]
    
    def setMaxIns(self, maxins):
        self.data["Max"]["Ins"] = maxins
        self.save()
    
#Added Stats
    def getAddedStr(self):
        return self.data["Added"]["Str"]
    
    def setAddedStr(self, addedstr):
        self.data["Added"]["Str"] = addedstr
        self.save()
        
    def getAddedDex(self):
        return self.data["Added"]["Dex"]
    
    def setAddedDex(self, addeddex):
        self.data["Added"]["Dex"] = addeddex
        self.save()
        
    def getAddedVit(self):
        return self.data["Added"]["Vit"]
    
    def setAddedVit(self, addedvit):
        self.data["Added"]["Vit"] = addedvit
        self.save()
        
    def getAddedSpl(self):
        return self.data["Added"]["Spl"]
    
    def setAddedSpl(self, addedspl):
        self.data["Added"]["Spl"] = addedspl
        self.save()
        
    def getAddedIns(self):
        return self.data["Added"]["Ins"]
    
    def setAddedIns(self, addedins):
        self.data["Added"]["Ins"] = addedins
        self.save()
        
    def getAddedDef(self):
        return self.data["Added"]["Def"]
    
    def setAddedDef(self, addeddef):
        self.data["Added"]["Def"] = addeddef
        self.save()
        
#Basic Stats
    def getHP(self):
        return self.data["Basic"]["HP"]
    
    def setHP(self, hp):
        self.data["Basic"]["HP"] = hp
        self.save()
        
    def getXP(self):
        return self.data["Basic"]["XP"]
    
    def setXP(self, XP):
        self.data["Basic"]["XP"] = XP
        self.save()        
    
    def getDisobedience(self):
        return self.data["Basic"]["Disobedience"]
    
    def setDisobedience(self, Disobedience):
        self.data["Basic"]["Disobedience"] = Disobedience
        self.save()
    
    def getHeldItem(self):
        return self.data["Basic"]["HeldItem"]
    
    def setHeldItem(self, HeldItem):
        self.data["Basic"]["HeldItem"] = HeldItem
        self.save()
        
    def getHappiness(self):
        return self.data["Basic"]["Happiness"]
    
    def setHappiness(self, Happiness):
        self.data["Basic"]["Happiness"] = Happiness
        self.save()        
        
    def getLoyalty(self):
        return self.data["Basic"]["Loyalty"]
    
    def setLoyalty(self, Loyalty):
        self.data["Basic"]["Loyalty"] = Loyalty
        self.save()        
        
#Skills

    def getFight(self):
        return self.data["Skills"]["Fight"]
    
    def setFight(self, Fight):
        self.data["Skills"]["Fight"] = Fight
        self.save()
        
    def getSurvival(self):
        return self.data["Skills"]["Survival"]
    
    def setSurvival(self, Survival):
        self.data["Skills"]["Survival"] = Survival
        self.save()

    def getContest(self):
        return self.data["Skills"]["Contest"]
    
    def setContest(self, Contest):
        self.data["Skills"]["Contest"] = Contest
        self.save()
        
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
        
        