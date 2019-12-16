import re

from Grammar import Grammar


def is_char(c):
    x = re.search("^[A-Za-z]$", c)
    if x:
        return True
    return False


def check_nonterm_file(nonterm_ls):
    for i in nonterm_ls:
        if not is_char(i):
            return False
    return True


def check_terminal(c):
    x = re.search("^[a-z0-9+*()]$", c)
    if x:
        return True
    return False


def check_terminal_file(term_ls):
    for i in term_ls:
        if not check_terminal(i):
            return False
    return True


def valid_seq(s, grammar):
    if s == "epsilon":
        return True
    for c in s:
        if not grammar.valid_nonterminal(c) and not grammar.valid_terminal(c):
            return False
    return True


def read_grammar_from_file(grammar):
    with open("gr2.txt") as file:
        line = file.readline()[:-1]
        nonterminals = line.split(",")
        if check_nonterm_file(nonterminals):
            for i in nonterminals:
                grammar.add_nonterminal(i)
        else:
            print("Invalid nonterminals")
            return

        line = file.readline()[:-1]
        terminals = line.split(",")
        if check_terminal_file(terminals):
            for t in terminals:
                grammar.add_terminal(t)
        else:
            print("Invalid terminals")
            return

        start_sym_line = file.readline()[:-1]
        if grammar.valid_nonterminal(start_sym_line):
            grammar.set_start_symbol(start_sym_line)
        else:
            print("Invalid start symbol")
            return

        line = file.readline()[:-1]
        while line:
            p = line.split("->")
            p[0] = p[0].strip()
            if grammar.valid_nonterminal(p[0]):
                x = p[1].split("|")
                for idx in range(len(x)):
                    x[idx] = x[idx].replace(" ", "")
                    if not valid_seq(x[idx], grammar):
                        print("Wrong production rhs")
                        return
                # grammar.add_production(p[0], x)
                for i in x:
                    grammar.add_to_productions(p[0], i)
            else:
                print("Wrong production lhs")
                return
            line = file.readline()[:-1]
    return


