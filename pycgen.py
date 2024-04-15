def _modcalc(ATR):
    return int(ATR/2) -5

class pc:
    # Basic Stuff
    PCName = ''
    PCClass = ''
    PCLevel = ''
    PCRealName = ''
    PCRace = ''
    PCAlignment = ''
    PCBackground = ''
    PCXP = 0

    #Ability Scores
    PCSTR = 0
    PCDEX = 0
    PCCON = 0
    PCINT = 0
    PCWIS = 0
    PCCHA = 0

    #Ability Modifiers, autofill
    STRMOD = 0
    DEXMOD = 0
    CONMOD = 0
    INTMOD = 0
    WISMOD = 0
    CHAMOD = 0

    #Saving throws, autofill
    STRTHR = 0
    DEXTHR = 0
    CONTHR = 0
    INTTHR = 0
    WISTHR = 0
    CHATHR = 0

    #Skill modifiers, autofill
    SMODAcrobatics = 0
    SMODAnimalHandling = 0
    SMODArcana = 0
    SMODAthletics = 0
    SMODDeception = 0
    SMODHistory = 0
    SMODInsight = 0
    SMODIntimidation = 0 #needs a special rule to intimidate by CHA or STR
    SMODInvestigation = 0
    SMODMedicine = 0
    SMODNature = 0
    SMODPerception = 0
    SMODPerformance = 0
    SMODPersuasion = 0
    SMODReligion = 0
    SMODSleightofhand = 0
    SMODStealth = 0
    SMODSurvival = 0

    #Proficiencies, attr
    PROFSTR = 0
    PROFDEX = 0
    PROFCON = 0
    PROFINT = 0
    PROFWIS = 0
    PROFCHA = 0

    #Proficiencies, skill
    PROFAcrobatics = 0
    PROFAnimalHandling = 0 
    PROFArcana = 0
    PROFAthletics = 0
    PROFDeception = 0
    PROFHistory = 0
    PROFInsight = 0
    PROFIntimidation = 0
    PROFInvestigation = 0
    PROFMedicine = 0
    PROFNature = 0
    PROFPerception = 0
    PROFPerformance = 0
    PROFPersuasion = 0
    PROFReligion = 0
    PROFSleightofhand = 0
    PROFStealth = 0
    PROFSurvival = 0

    Inspiration = 0
    PROFBonus = 0

    #Perception = WIS + mods, autofill
    Perception = 0

    #AC
    PCAC = 0

    #Initiative = Dexmod
    PCInitiative = 0

    PCSpeed = 0
    PCMaxHP = 0
    PCHP = 0
    PCMaxHitDie = '0'
    PCHitDie = '0'

    def __init__(self, PCName, PCClass, PCLevel, PCRealName, PCRace, PCAlignment,
                 PCBackground, STR, DEX, CON, INT, WIS, CHA, PROFSTR, PROFDEX, PROFCON,
                 PROFINT, PROFWIS, PROFCHA, PROFAcrobatics, PROFAnimalHandling,
                 PROFArcana, PROFAthletics, PROFDeception, PROFHistory, PROFInsight,
                 PROFIntimidation, PROFInvestigation, PROFMedicine, PROFNature,
                 PROFPerception, PROFPerformance, PROFPersuasion, PROFReligion,
                 PROFSleightofhand, PROFStealth, PROFSurvival ):
        
        self.PROFBonus = 2 #assuming level 1 generation
        self.PCName = PCName
        self.PCClass = PCClass
        self.PCLevel = PCLevel
        self.PCRealName = PCRealName
        self.PCRace = PCRace
        self.PCAlignment = PCAlignment
        self.PCBackground = PCBackground

        #Basic Attributes
        self.PCSTR = STR
        self.PCDEX = DEX
        self.PCCON = CON
        self.PCINT = INT
        self.PCWIS = WIS
        self.PCCHA = CHA

        #Attribute Proficiencies
        self.PROFSTR = PROFSTR
        self.PROFDEX = PROFDEX
        self.PROFCON = PROFCON
        self.PROFINT = PROFINT
        self.PROFWIS = PROFWIS
        self.PROFCHA = PROFCHA

        #calculate basic modifiers
        self.STRMOD = _modcalc(STR)
        self.DEXMOD = _modcalc(DEX)
        self.CONMOD = _modcalc(CON)
        self.INTMOD = _modcalc(INT)
        self.WISMOD = _modcalc(WIS)
        self.CHAMOD = _modcalc(CHA)

        #saving throws
        self.STRTHR = self.STRMOD + PROFSTR*self.PROFBonus
        self.DEXTHR = self.DEXMOD + PROFDEX*self.PROFBonus
        self.CONTHR = self.CONMOD + PROFCON*self.PROFBonus
        self.INTTHR = self.INTMOD + PROFINT*self.PROFBonus
        self.WISTHR = self.WISMOD + PROFWIS*self.PROFBonus
        self.CHATHR = self.CHAMOD + PROFCHA*self.PROFBonus

        #skill proficiencies
        self.PROFAcrobatics = PROFAcrobatics
        self.PROFAnimalHandling = PROFAnimalHandling
        self.PROFArcana = PROFArcana
        self.PROFAthletics = PROFAthletics
        self.PROFDeception = PROFDeception
        self.PROFHistory = PROFHistory
        self.PROFInsight = PROFInsight
        self.PROFIntimidation = PROFIntimidation
        self.PROFInvestigation = PROFInvestigation
        self.PROFMedicine = PROFMedicine
        self.PROFNature = PROFNature
        self.PROFPerception = PROFPerception
        self.PROFPerformance = PROFPerformance
        self.PROFPersuasion = PROFPersuasion
        self.PROFReligion = PROFReligion
        self.PROFSleightofhand = PROFSleightofhand
        self.PROFStealth = PROFStealth
        self.PROFSurvival = PROFSurvival

        #intimidation
        self.SMODIntimidation = max(self.CHAMOD, self.STRMOD) + \
                                (PROFIntimidation * self.PROFBonus)

        #STR skills
        self.SMODAthletics = self.STRMOD + (PROFAthletics * self.PROFBonus)

        #DEX Skills
        self.SMODAcrobatics = self.DEXMOD + (PROFAcrobatics * self.PROFBonus)
        self.SMODSleightofhand = self.DEXMOD + (PROFSleightofhand * self.PROFBonus)
        
        #CON skills
        #none!

        #WIS skills
        self.SMODAnimalHandling = self.WISMOD + (PROFAnimalHandling * self.PROFBonus)
        self.SMODInsight = self.WISMOD + (PROFInsight * self.PROFBonus)
        self.SMODMedicine = self.WISMOD + (PROFMedicine * self.PROFBonus)
        self.SMODPerception = self.WISMOD + (PROFPerception * self.PROFBonus)
        self.SMODSurvival = self.WISMOD + (PROFSurvival * self.PROFBonus)

        #INT Skills
        self.SMODArcana = self.INTMOD + (PROFArcana * self.PROFBonus)
        self.SMODHistory = self.INTMOD + (PROFHistory * self.PROFBonus)
        self.SMODInvestigation = self.INTMOD + (PROFInvestigation * self.PROFBonus)
        self.SMODNature = self.INTMOD + (PROFNature * self.PROFBonus)
        self.SMODReligion = self.INTMOD + (PROFReligion * self.PROFBonus)

        #CHA skills
        self.SMODDeception = self.CHAMOD + (PROFDeception * self.PROFBonus)
        self.SMODPerformance = self.CHAMOD + (PROFPerception * self.PROFBonus)
        self.SMODPersuasion = self.CHAMOD + (PROFPersuasion * self.PROFBonus)

        #passive perception
        self.Perception = WIS + self.WISMOD + (PROFWIS * self.PROFBonus)

        self.PCInitiative = self.DEXMOD
        self.PCAC = self.DEXMOD + (PROFDEX * self.PROFBonus)


def write(character:pc):
    pcfile = open('pc.tex', 'r')
    outfile = open(f'{character.PCName}.tex', 'w')

    for i in range(0, 13):
        outfile.write(pcfile.readline())
    
    #write name
    outfile.write("\n%Character name\n")
    outfile.write(f"\\CharacterName{{{character.PCName}}}\n")

    #write pc info
    outfile.write("\n%Player Character Info\n")
    outfile.write(f"\\Class{{{character.PCClass} {character.PCLevel}}}\n")
    outfile.write(f"\\Background{{{character.PCBackground}}}\n")
    outfile.write(f"\\PlayerName{{{character.PCRealName}}}\n")
    outfile.write(f"\\Race{{{character.PCRace}}}\n")
    outfile.write(f"\\Alignment{{{character.PCAlignment}}}\n")
    outfile.write(f"\\XP{{{character.PCXP}}}\n")

    #write ability scores
    outfile.write("\n%Ability scores\n")
    outfile.write(f"\\StrengthScore{{{character.PCSTR}}}\n")
    outfile.write(f"\\DexterityScore{{{character.PCDEX}}}\n")
    outfile.write(f"\\ConstitutionScore{{{character.PCCON}}}\n")
    outfile.write(f"\\IntelligenceScore{{{character.PCINT}}}\n")
    outfile.write(f"\\WisdomScore{{{character.PCWIS}}}\n")
    outfile.write(f"\\CharismaScore{{{character.PCCHA}}}\n")

    #write ability modifiers
    outfile.write("\n%Ability modifiers\n")
    outfile.write(f"\\StrengthModifier{{{character.STRMOD}}}\n")
    outfile.write(f"\\DexterityModifier{{{character.DEXMOD}}}\n")
    outfile.write(f"\\ConstitutionModifier{{{character.CONMOD}}}\n")
    outfile.write(f"\\IntelligenceModifier{{{character.INTMOD}}}\n")
    outfile.write(f"\\WisdomModifier{{{character.WISMOD}}}\n")
    outfile.write(f"\\CharismaModifier{{{character.CHAMOD}}}\n")

    #write saving throws
    outfile.write("\n%Saving throws\n")
    outfile.write(f"\\StrengthSavingThrowModifier{{{character.STRTHR}}}\n")
    outfile.write(f"\\DexteritySavingThrowModifier{{{character.DEXTHR}}}\n")
    outfile.write(f"\\ConstitutionSavingThrowModifier{{{character.CONTHR}}}\n")
    outfile.write(f"\\IntelligenceSavingThrowModifier{{{character.INTTHR}}}\n")
    outfile.write(f"\\WisdomSavingThrowModifier{{{character.WISTHR}}}\n")
    outfile.write(f"\\CharismaSavingThrowModifier{{{character.CHATHR}}}\n")

    #write skill mods
    outfile.write("\n%Skill Modifiers")
    outfile.write(f"\\AcrobaticsSkillModifier{{{character.SMODAcrobatics}}}\n")
    outfile.write(f"\\AnimalHandlingSkillModifier{{{character.SMODAnimalHandling}}}\n")
    outfile.write(f"\\ArcanaSkillModifier{{{character.SMODArcana}}}\n")
    outfile.write(f"\\AthleticsSkillModifier{{{character.SMODAthletics}}}\n")
    outfile.write(f"\\DeceptionSkillModifier{{{character.SMODDeception}}}\n")
    outfile.write(f"\\HistorySkillModifier{{{character.SMODHistory}}}\n")
    outfile.write(f"\\InsightSkillModifier{{{character.SMODInsight}}}\n")
    outfile.write(f"\\IntimidationSkillModifier{{{character.SMODIntimidation}}}\n")
    outfile.write(f"\\InvestigationSkillModifier{{{character.SMODInvestigation}}}\n")
    outfile.write(f"\\MedicineSkillModifier{{{character.SMODMedicine}}}\n")
    outfile.write(f"\\NatureSkillModifier{{{character.SMODNature}}}\n")
    outfile.write(f"\\PerceptionSkillModifier{{{character.SMODPerception}}}\n")
    outfile.write(f"\\PerformanceSkillModifier{{{character.SMODPerformance}}}\n")
    outfile.write(f"\\PersuasionSkillModifier{{{character.SMODPersuasion}}}\n")
    outfile.write(f"\\ReligionSkillModifier{{{character.SMODReligion}}}\n")
    outfile.write(f"\\SleightOfHandSkillModifier{{{character.SMODSleightofhand}}}\n")
    outfile.write(f"\\StealthSkillModifier{{{character.SMODStealth}}}\n")
    outfile.write(f"\\SurvivalSkillModifier{{{character.SMODSurvival}}}\n")

    #write ability proficiencies
    outfile.write("\n%Ability Proficiencies\n")
    outfile.write(f"\\SetStrengthProficiency{{{character.PROFSTR}}}\n")
    outfile.write(f"\\SetDexterityProficiency{{{character.PROFDEX}}}\n")
    outfile.write(f"\\SetConstitutionProficiency{{{character.PROFCON}}}\n")
    outfile.write(f"\\SetIntelligenceProficiency{{{character.PROFINT}}}\n")
    outfile.write(f"\\SetWisdomProficiency{{{character.PROFWIS}}}\n")
    outfile.write(f"\\SetCharismaProficiency{{{character.PROFCHA}}}\n")

    #write skill proficiencies
    outfile.write("\n%Skill Proficiencies\n")
    outfile.write(f"\\SetAcrobaticsProficiency{{{character.PROFAcrobatics}}}\n")
    outfile.write(f"\\SetAnimalHandlingProficiency{{{character.PROFAnimalHandling}}}\n")
    outfile.write(f"\\SetArcanaProficiency{{{character.PROFArcana}}}\n")
    outfile.write(f"\\SetAthleticsProficiency{{{character.PROFAthletics}}}\n")
    outfile.write(f"\\SetDeceptionProficiency{{{character.PROFDeception}}}\n")
    outfile.write(f"\\SetHistoryProficiency{{{character.PROFHistory}}}\n")
    outfile.write(f"\\SetInsightProficiency{{{character.PROFInsight}}}\n")
    outfile.write(f"\\SetIntimidationProficiency{{{character.PROFIntimidation}}}\n")
    outfile.write(f"\\SetInvestigationProficiency{{{character.PROFInvestigation}}}\n")
    outfile.write(f"\\SetMedicineProficiency{{{character.PROFMedicine}}}\n")
    outfile.write(f"\\SetNatureProficiency{{{character.PROFNature}}}\n")
    outfile.write(f"\\SetPerceptionProficiency{{{character.PROFPerception}}}\n")
    outfile.write(f"\\SetPerformanceProficiency{{{character.PROFPerformance}}}\n")
    outfile.write(f"\\SetPersuasionProficiency{{{character.PROFPersuasion}}}\n")
    outfile.write(f"\\SetReligionProficiency{{{character.PROFReligion}}}\n")
    outfile.write(f"\\SetSleightOfHandProficiency{{{character.PROFSleightofhand}}}\n")
    outfile.write(f"\\SetStealthProficiency{{{character.PROFStealth}}}\n")
    outfile.write(f"\\SetSurvivalProficiency{{{character.PROFSurvival}}}\n")

    #write misc things
    outfile.write("\n%misc things\n")
    outfile.write(f"\\Insipiration{{}}\n")
    outfile.write(f"\\Proficiency{{{character.PROFBonus}}}\n")
    outfile.write(f"\\Perception{{{character.Perception}}}\n")
    outfile.write(f"\\ArmorClass{{{character.PCAC}}}\n")
    outfile.write(f"\\Initiative{{{character.PCInitiative}}}\n")

    #write rest of latex template
    for line in pcfile:
        outfile.write(line)

    outfile.close()

def main():
    #lets ask a questionnaire!

    #Basic stuff
    pcname = input("Please enter character name:\t")
    pcclass = input("Please enter character class:\t")
    pclevel = input("Please enter character level:\t")
    realname = input("Please enter your player name:\t")
    pcrace = input("Please enter your character race:\t")
    pcalign = input("Please enter your character alignment:\t")
    pcbg = input("Please enter your character background:\t")
       
    STR = int(input("Please enter STR:\t"))
    DEX = int(input("Please enter DEX:\t"))
    CON = int(input("Please enter CON:\t"))
    INT = int(input("Please enter INT:\t"))
    WIS = int(input("Please enter WIS:\t"))
    CHA = int(input("Please enter CHA:\t"))

    AttrProfs = input("Please enter attribute proficiencies separated by comma:\n")
    PROFSTR = PROFDEX = PROFCON = PROFINT = PROFWIS = PROFCHA = 0
    if 'STR' in AttrProfs:
        PROFSTR = 1
    if 'DEX' in AttrProfs:
        PROFDEX = 1
    if 'CON' in AttrProfs:
        PROFCON = 1
    if 'INT' in AttrProfs:
        PROFINT = 1
    if 'WIS' in AttrProfs:
        PROFWIS = 1
    if 'CHA' in AttrProfs:
        PROFCHA = 1
    
    print("Please enter your skill attributes as numbers from the list, separated by comma")
    print("1 Acrobatics\n2 Animal Handling\n3 Arcana\n4 Athletics\n5 Deception")
    print("6 History\n7 Insight\n8 Intimidation\n9 Investigation\n10 Medicine")
    print("11 Nature\n12 Perception\n13 Performance\n14 Persuasion\n15 Religion")
    print("16 Sleight of Hand\n17 Stealth\n18 Survival\n")
    SkillProfs = [int(i) for i in input().split(',')]
    skprofs = [0]*18
    for i in SkillProfs:
        skprofs[i-1]=1

    skprofs


    character = pc(pcname, pcclass, pclevel, realname, pcrace, pcalign, pcbg, STR, DEX, CON, INT,
                   WIS, CHA, PROFSTR, PROFDEX, PROFCON, PROFINT,PROFWIS, PROFCHA, skprofs[0],
                   skprofs[1], skprofs[2],skprofs[3], skprofs[4], skprofs[5], skprofs[6],
                   skprofs[7],skprofs[8], skprofs[9], skprofs[10], skprofs[11], skprofs[12],
                   skprofs[13], skprofs[14], skprofs[15], skprofs[16], skprofs[17])
    
    write(character)

    pass

if __name__ == "__main__":
    main()