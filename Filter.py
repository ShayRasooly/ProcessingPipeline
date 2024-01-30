from random import randint
from collections import defaultdict
from reprlib import Repr


class Rule:
    WILDCARD = "*"
    def __init__(self, key, value, name=None):
        self.key = key
        self.value = value
        if name is None:
            repr = Repr()
            repr.Maxlong = 5
            name = repr.repr(self.key) + repr.repr(self.value) + str(randint(1000, 9999))
        self.name = name

    def result(self, entry: defaultdict):
        pass


class EqualRule(Rule):
    def result(self, entry: defaultdict):
        if  entry[self.key] == self.value or self.value == self.WILDCARD:
            return True
        return None


class NotEqualRule(Rule):
    def result(self, entry: defaultdict):
        if entry[self.key] == self.value or self.value == self.WILDCARD:
            return False
        return None


class InListRule(Rule):
    def result(self, entry: defaultdict):
        if entry[self.key] in self.value or self.value == self.WILDCARD:
            return True
        return None


class NotInListRule(Rule):
    def result(self, entry: defaultdict):
        if entry[self.key] in self.value or self.value == self.WILDCARD:
            return False
        return None


class Filter:
    def __init__(self, rules: list[Rule]):
        self.rules = rules

    def append_rule(self, rule: Rule):
        self.rules.append(rule)

    def insert_rule(self, rule_name: str, rule: Rule, index: int):
        self.rules.insert(index, rule)

    def remove_rule_by_name(self, rule_name: str):
        self.rules = list(filter(lambda rule: rule.name != rule_name, self.rules))

    def remove_rule_by_index(self, index: int):
        del self.rules[index]

    def filter(self, entries_list: list[defaultdict]):
        filter_list = len(entries_list) * [True]
        for i, entry in enumerate(entries_list):
            for rule in self.rules:
                result = rule.result(entry)
                if result is True:
                    break
                if result is False:
                    filter_list[i] = False
                    break
        entries_list[:] = [entry for i, entry in enumerate(entries_list) if filter_list[i]]
        return entries_list


