class Grammar:
    def __init__(self):
        self.nonterminals = []
        self.terminals = []
        self.productions = {}
        self.startSymbol = ""
        self.prod_idx = 0

    def set_start_symbol(self, s):
        self.startSymbol = s

    def set_nonterminals(self, nonterm_ls):
        self.nonterminals = nonterm_ls

    def set_terminals(self, term_ls):
        self.terminals = term_ls

    def get_nonterminals(self):
        return self.nonterminals

    def get_terminals(self):
        return self.terminals

    def get_productions(self):
        return self.productions

    def get_productions_of_nonterminal(self, nonterminal):
        return self.productions[nonterminal]

    def get_start_symbol(self):
        return self.startSymbol

    def add_nonterminal(self, nonterminal):
        if nonterminal not in self.nonterminals:
            self.nonterminals.append(nonterminal)

    def add_terminal(self, terminal):
        if terminal not in self.terminals:
            self.terminals.append(terminal)

    def add_production(self, nonterm, go_to_list):
        self.productions[nonterm] = go_to_list

    def add_to_productions(self, nonterm, elem):
        if nonterm not in self.productions.keys():
            self.productions[nonterm] = [elem]
            return
        self.productions[nonterm].append(elem)

    def valid_nonterminal(self, x):
        if x in self.nonterminals:
            return True
        return False

    def valid_nonterm_2(self, x):
        for i in self.nonterminals:
            if i == x:
                return True
        return False

    def valid_terminal(self, x):
        if x in self.terminals:
            return True
        return False

    def print_nonterminals(self):
        s = "N:\t{"
        for i in self.nonterminals:
            s = s + i + ", "
        s = s[:-2]
        s += "}\n"
        return s

    def print_terminals(self):
        s = "Sigma:\t{"
        for i in self.terminals:
            s = s + i + ", "
        s = s[:-2]
        s += "}\n"
        return s

    def print_production_of_nonterminal(self, nonterm):
        s = nonterm + " -> "
        for i in self.productions[nonterm]:
            self.prod_idx += 1
            s += "(" + str(self.prod_idx) + ") "
            s = s + str(i) + " | "
        s = s[:-2]
        s += "\n"
        return s

    def print_productions(self):
        s = "P:\n"
        self.prod_idx = 0
        for n in self.productions.keys():
            s += self.print_production_of_nonterminal(n)
        s += "\n"
        return s

    def print_start_symbol(self):
        return "S: {" + self.startSymbol + "}\n"

    def print_grammar(self):
        s = "Grammar:\n"
        s += self.print_nonterminals()
        s += self.print_terminals()
        s += self.print_productions()
        s += self.print_start_symbol()

        return s

    def right_linear(self):
        for k in self.productions.keys():
            for p in self.productions[k]:
                if len(p) == 2:
                    if (p[0] in self.terminals and p[1] in self.terminals) or (
                            p[0] in self.nonterminals and p[1] in self.nonterminals):
                        return False
                    if p[0] in self.nonterminals and p[1] in self.terminals:
                        return False
                elif len(p) == 1:
                    if p in self.nonterminals:
                        return False
                elif len(p) > 2 and p != "epsilon":
                    return False
        return True

    def rhs_start_symbol(self):
        for k, v in self.productions.items():
            if k != self.startSymbol:
                for s in v:
                    if self.startSymbol in s:
                        return True
        return False

    def no_epsilon_except(self):
        for k, v in self.productions.items():
            if k != self.startSymbol:
                if "epsilon" in v:
                    return False
        return True

    def no_epsilon(self):
        for v in self.productions.values():
            if "epsilon" in v:
                return False
        return True

    def regular_grammar(self):
        if self.right_linear():
            if self.no_epsilon():
                return True
            if "epsilon" in self.get_productions_of_nonterminal(self.startSymbol):
                # check S does not appear in rhs of any other production
                if not self.rhs_start_symbol():
                    if self.no_epsilon_except():
                        return True
        return False
