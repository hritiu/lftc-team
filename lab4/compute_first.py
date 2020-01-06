from First import First
from utils import *


def starts_with_terminal(prod, terminals):
    if prod[0] in terminals:
        return True
    return False


def compare_firsts(f1, f2):
    x = f1.get_dict()
    y = f2.get_dict()

    different_items = {k: x[k] for k in x if k in y and x[k] != y[k]}

    if len(different_items) == 0:
        return True
    return False


def set_terminals(grammar, first):
    for t in grammar.get_terminals():
        first.set_symbol_value(t, [t])


def compute_first(grammar):
    firsts_list = []

    first_0 = First(0)

    firsts_list.append(first_0)

    set_terminals(grammar, first_0)

    for n in grammar.get_nonterminals():
        f_list = []
        for p in grammar.get_productions_of_nonterminal(n):
            if starts_with_terminal(p, grammar.get_terminals()):
                f_list.append(p[0])
            elif p == "epsilon":
                f_list.append("epsilon")
        first_0.set_symbol_value(n, f_list)

    idx = 0
    while True:
        prev_f = firsts_list[idx]
        idx += 1
        first = First(idx)
        firsts_list.append(first)

        set_terminals(grammar, first)

        for n in grammar.get_nonterminals():
            f_list = []
            t = prev_f.get_values_of_symbol(n)
            for i in t:
                f_list.append(i)

            for p in grammar.get_productions_of_nonterminal(n):
                x = concat(p, firsts_list[idx - 1])
                for i in x:
                    if i not in f_list:
                        f_list.append(i)

            first.set_symbol_value(n, f_list)

        if compare_firsts(firsts_list[idx-1], first):
            break

    return firsts_list[-1]


def compute_first2(grammar):
    firsts_list = []

    first_0 = First(0)

    firsts_list.append(first_0)

    set_terminals(grammar, first_0)

    for n in grammar.get_nonterminals():
        f_list = []
        for p in grammar.get_productions_of_nonterminal(n):
            if starts_with_terminal(p, grammar.get_terminals()):
                f_list.append(p[0])
            elif p == "epsilon":
                f_list.append("epsilon")
        first_0.set_symbol_value(n, f_list)

    idx = 0
    while True:
        prev_f = firsts_list[idx]
        idx += 1
        first = First(idx)
        firsts_list.append(first)

        set_terminals(grammar, first)

        for n in grammar.get_nonterminals():
            f_list = []
            t = prev_f.get_values_of_symbol(n)
            for i in t:
                f_list.append(i)

            for p in grammar.get_productions_of_nonterminal(n):
                x = concat2(p, firsts_list[idx - 1])
                for i in x:
                    if i not in f_list:
                        f_list.append(i)

            first.set_symbol_value(n, f_list)

        if compare_firsts(firsts_list[idx-1], first):
            break

    return firsts_list[-1]
