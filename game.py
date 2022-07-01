from audioop import reverse
import random

from numpy import true_divide



class carte:
    def __init__(self, color, value):
        self.value = value
        self.color = color

    color_names = ['♣️', '♦️', '❤️', '♠️']
    value_names = [None,"1", '2', '3', '4', '5', '6', '7', 
                    '8', '9', '10', 'valet', 'dame', 'roi', "as"]
    
    def __str__(self):
        return f"{carte.value_names[self.value]} {carte.color_names[self.color]}"

    def __lt__(self, other):
        c1 = self.value
        c2 = other.value
        if self.value == 1:
            c1 = 14
        if other.value == 1:
            c2 = 14
        return c1 < c2
    
class paquet:
    def __init__(self):
        self.cartes = []
        for colors in range(4):
            for values in range(2,15):
                c = carte(colors, values)
                self.cartes.append(c)
    
    def __str__(self):
        fin = []
        for carte in self.cartes:
            fin.append(str(carte))
        return "\n ".join(fin)

    def pop_card(self):
        return self.cartes.pop()
    
    def add_card(self, card):
        self.cartes.append(card)
    
    def shuffle_deck(self):
        random.shuffle(self.cartes)

    def give_cards(self, hand, number):
        for i in range(number):
            hand.add_card(self.pop_card())
        hand.sort()

class main(paquet):
    def __init__(self, name = "", coins= 1000):
        self.cartes = []
        self.name = name
        self.coins = coins
    def __str__(self):
        fin = []
        for carte in self.cartes:
            fin.append(str(carte))
        return "\n ".join(fin)

    def get_value_list(self):
        res = []
        [res.append(i.value) for i in self.cartes]
        return res
    def get_color_list(self):
        res = []
        [res.append(i.color) for i in self.cartes]
        return res

    def sort(self):
        c = sorted(self.cartes, key=lambda card : card.value, reverse=True)
        self.cartes = c

class PokerHand:
    possible_hands = ["Royal Flush", "Straight Flush", "Carré", "Full House",
                     "Flush", "Straight", "Double Pair", "Pair", "Carte Haute"]
    
    def __init__(self, table, hand):
        self.hand_value, self.hand_color = self.creat_value_list(table, hand), self.creat_color_list(table, hand)
        self.reversed_value = self.hand_value[::-1]

    def creat_value_list(self, table, hand):
        l_value = []
        [l_value.append(i)for i in hand.get_value_list()]
        [l_value.append(i)for i in table.get_value_list()]
        l_value.sort(reverse=True)
        return l_value
    def creat_color_list(self, table, hand):
        l_color = []
        [l_color.append(i)for i in hand.get_color_list()]
        [l_color.append(i)for i in table.get_color_list()]
        l_color.sort(reverse=True)
        return l_color

    def is_flush_royal(self):
        values = [14, 13, 12, 11, 10]
        color = self.hand_color[0]
        if self.hand_value == values :
            for i in self.hand_color:
                if i != color:
                    return False
                color = i
            return True
        return False
    def is_straigth_flush(self):
        first_value = self.reversed_value[0]
        try_values = [i for i in range(first_value, first_value + 5)]
        color = self.hand_color[0]
        if self.reversed_value == try_values:
            for i in self.hand_color:
                if i != color:
                    return False
                color = i
            return True
        return False
    
    def is_carre(self):
        for i in range(2):
            n = self.hand_value.count(self.hand_value[i])
            if n  == 4:
                return True
        return False
    
    def is_full_house(self):
        values = self.hand_value
        print(values)
        if values.count(values[0]) == 3 and values.count(values[4]) == 2:
            return True
        elif values.count(values[0]) == 2 and values.count(values[4]) == 3:
            return True
        else:
            return False
            
        

            



roi = carte(0, 4)
ass = carte(3, 3)
dame = carte(2, 5)
valet = carte(1, 3)
dix = carte(0, 4)
l = [roi, ass,dame]
l2 = [valet, dix]
        

deck = paquet()
deck.shuffle_deck()
t = main(name="table")
m1 = main(name="j1")
[t.add_card(i)for i in l]
[m1.add_card(i)for i in l2]
m1_poker = PokerHand(t, m1)
print(t)
print("\n")
print(m1)

print(m1_poker.is_full_house())





