class PokerHand:
    
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

    def check_combi(self):
        possible_hands = [self.is_flush_royal,self.is_straigth_flush,self.is_carre,self.is_full_house,
                    self.is_flush,self.is_straigth,self.is_brelan,self.is_double_pair,self.is_pair]
        trad_combi = ["Flush Royal", "Suite Couleur", "Carré", "Full House", "Couleur", "Suite", "Brelan", "Double Pair", "Paire", "Carte Haute"]
        l = [f() for f in possible_hands]
        if all(i == False for i in self.hand_color):
            print("Carte Haute")
        else:
            [print(trad_combi[i]) for i in range(len(l)) if l[i] ==  True]

    def is_flush_royal(self):
        values = [14, 13, 12, 11, 10]
        if self.hand_value == values :
            return all(i == self.hand_color[0] for i in self.hand_color)
        return False
        
    def is_straigth_flush(self):
        first_value = self.reversed_value[0]
        try_values = [i for i in range(first_value, first_value + 5)]
        if self.reversed_value == try_values:
            return all(i == self.hand_color[0] for i in self.hand_color)
        return False
    
    def is_carre(self):
        for i in range(2):
            n = self.hand_value.count(self.hand_value[i])
            if n  == 4:
                return True
        return False
    
    def is_full_house(self):
        values = self.hand_value
        if values.count(values[0]) == 3 and values.count(values[4]) == 2:
            return True
        elif values.count(values[0]) == 2 and values.count(values[4]) == 3:
            return True
        else:
            return False

    def is_flush(self):
        return all(i == self.hand_color[0] for i in self.hand_color)

    def is_straigth(self):
        first_value = self.reversed_value[0]
        return bool(self.reversed_value == [i for i in range(first_value, first_value + 5)])

    def is_brelan(self):
        for i in range(3):
            n = self.hand_value.count(self.hand_value[i])
            if n  == 3:
                return True
        return False

    def is_double_pair(self):
        c = 0
        print(self.hand_value)
        for i in range(1, 5):
            if self.hand_value[i] == self.hand_value[i-1]:
                if self.hand_value[i] != self.hand_value[i-2]:
                    c += 1
        return bool(c == 2)

    def is_pair(self):
        c = 0
        for i in range(1, 5):
            if self.hand_value[i] == self.hand_value[i-1]:
                c += 1
        return bool(c == 1)