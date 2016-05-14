import random

pot1 = {"Barcelona": "ESP", "Bayern Munchen": "GER", "Chelsea": "ENG", "Benfica": "POR", "PSG": "FRA", "Juventus": "ITA", "Zenit": "RUS", "PSV": "HOL"}

pot2 = {"Real Madrid": "ESP", "Atletico Madrid": "ESP", "Porto": "POR", "Arsenal": "ENG", "Manchester United": "ENG", "Valencia": "ESP", "Leverkusen": "GER", "Manchester City": "ENG"}

pot3 = {"Shakhtar Donetsk": "UKR", "Sevilla": "ESP", "Lyon": "FRA", "Dynamo Kyiv": "UKR", "Olympiacos": "GRE", "CSKA Moscow": "RUS", "Galatasaray": "TUR", "Roma": "ITA"}

pot4 = {"Bate Borisov": "RUS", "Borussia Monchengladbach": "GER", "Wolfsburg": "GER", "Dinamo Zagreb": "CRO", "Maccabi Tel Aviv": "ISR", "Gent": "BEL", "Malmo": "SWE", "Astana": "KAZ"}

def drawGroups(groupName):
    selections = []
    used_countries = []

    selection = random.choice(pot1.keys())
    selections.append(selection)
    used_countries.append(pot1[selection])
    pot1.pop(selection)
    selection = random.choice(pot2.keys())

    while pot2[selection] in used_countries:
        selection = random.choice(pot2.keys())
    selections.append(selection)
    used_countries.append(pot2[selection])
    pot2.pop(selection)

    selection = random.choice(pot3.keys())

    while pot3[selection] in used_countries:
        selection = random.choice(pot3.keys())
    selections.append(selection)
    used_countries.append(pot3[selection])
    pot3.pop(selection)

    selection = random.choice(pot4.keys())

    while pot4[selection] in used_countries:
        selection = random.choice(pot4.keys())
    selections.append(selection)
    used_countries.append(pot4[selection])
    pot4.pop(selection)
    print "Group", groupName, ":", selections

drawGroups("A")
drawGroups("B")
drawGroups("C")
drawGroups("D")
drawGroups("E")
drawGroups("F")
drawGroups("G")
drawGroups("H")

