class Rule:
    def matches(self, row1, row2):
        """
        Метод для проверки, подходит ли правило.
        """
        raise NotImplementedError

    def get_score(self):
        """
        Возвращает количество очков за совпадение.
        """
        raise NotImplementedError


class RuleManager:
    def __init__(self, rules=[], threshold=5):
        self.rules = rules
        self.threshold = threshold

    def add_rule(self, rule):
        self.rules.append(rule)

    def compare_rows(self, row1, row2):
        score = 0
        for rule in self.rules:
            if rule.matches(row1, row2):
                score += rule.get_score()

        return score >= self.threshold


"""
     Правила
"""

class NameMatchRule(Rule):
    def matches(self, row1, row2):
        return row1['name'] == row2['name']  # Проверяем совпадение имени

    def get_score(self):
        return 1


class AddressMatchRule(Rule):
    def matches(self, row1, row2):
        return row1['address'] == row2['address']  # Проверяем совпадение адресов

    def get_score(self):
        return 3

"""
    
"""

def getManager():
    return RuleManager(rules=[
        NameMatchRule,
        AddressMatchRule,
    ])
