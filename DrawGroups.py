import random

pot1 = {"Barcelona": "ESP", "Bayern Munchen": "GER", "Chelsea": "ENG", "Benfica": "POR", "PSG": "FRA", "Juventus": "ITA", "Zenit": "RUS", "PSV": "HOL"}

pot2 = {"Real Madrid": "ESP", "Atletico Madrid": "ESP", "Porto": "POR", "Arsenal": "ENG", "Manchester United": "ENG", "Valencia": "ESP", "Leverkusen": "GER", "Manchester City": "ENG"}

pot3 = {"Shakhtar Donetsk": "UKR", "Sevilla": "ESP", "Lyon": "FRA", "Dynamo Kyiv": "UKR", "Olympiacos": "GRE", "CSKA Moscow": "RUS", "Galatasaray": "TUR", "Roma": "ITA"}

pot4 = {"Bate Borisov": "RUS", "Borussia Monchengladbach": "GER", "Wolfsburg": "GER", "Dinamo Zagreb": "CRO", "Maccabi Tel Aviv": "ISR", "Gent": "BEL", "Malmo": "SWE", "Astana": "KAZ"}


group_a = []
group_b = []
group_c = []
group_d = []
group_e = []
group_f = []
group_g = []
group_h = []


def grupA():
    first_selection = random.choice(pot1.keys())
    group_a.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_a.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_a.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_a.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group A: ", group_a

def grupB():
    first_selection = random.choice(pot1.keys())
    group_b.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_b.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_b.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_b.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group B: ", group_b

def grupC():
    first_selection = random.choice(pot1.keys())
    group_c.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_c.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_c.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_c.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group C: ", group_c


def grupD():
    first_selection = random.choice(pot1.keys())
    group_d.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_d.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_d.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_d.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group D: ", group_d


def grupE():
    first_selection = random.choice(pot1.keys())
    group_e.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_e.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_e.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_e.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group E: ", group_e

def grupF():
    first_selection = random.choice(pot1.keys())
    group_f.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_f.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_f.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_f.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group F: ", group_f

def grupG():
    first_selection = random.choice(pot1.keys())
    group_g.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_g.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_g.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_g.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group G: ", group_g

def grupH():
    first_selection = random.choice(pot1.keys())
    group_h.append(first_selection)

    second_selection = random.choice(pot2.keys())
    for i in range(len(pot2)):

        if (pot1.__getitem__(first_selection) == pot2.__getitem__(second_selection)):
            second_selection = random.choice(pot2.keys())
        else:
            group_h.append(second_selection)
            break

    third_selection = random.choice(pot3.keys())
    for i in range(len(pot3)):

        if (pot1.__getitem__(first_selection) == pot3.__getitem__(third_selection) or pot2.__getitem__(
                second_selection) == pot3.__getitem__(third_selection)):
            third_selection = random.choice(pot3.keys())
        else:
            group_h.append(third_selection)
            break

    fourth_selection = random.choice(pot4.keys())
    for i in range(len(pot4)):
        if (pot1.__getitem__(first_selection) == pot4.__getitem__(fourth_selection) or pot2.__getitem__(
                second_selection) == pot4.__getitem__(fourth_selection)
            or pot3.__getitem__(third_selection) == pot4.__getitem__(fourth_selection)):
            fourth_selection = random.choice(pot4.keys())
        else:
            group_h.append(fourth_selection)
            break

    pot1.pop(first_selection)
    pot2.pop(second_selection)
    pot3.pop(third_selection)
    pot4.pop(fourth_selection)

    print "Group H: ", group_h

grupA()
grupB()
grupC()
grupD()
grupE()
grupF()
grupG()
grupH()
