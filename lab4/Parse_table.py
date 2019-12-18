
class ParseTable:
    def __init__(self, grammar):
        self.table = {}
        for n in grammar.get_nonterminals():
            self.table[n] = []
        for t in grammar.get_terminals():
            self.table[t] = [[t, ["pop"]]]
        self.table["$"] = [["$", ["acc"]]]

    def get_line(self, symbol):
        return self.table[symbol]

    def get_value_cell(self, line, col):
        for i in self.table[line]:
            if i[0] == col:
                return i[1]
        return []

    def set_value_cell(self, key, col, prod, idx):
        self.table[key].append([col, [prod, idx]])

    def print_table(self):
        s = "PARSE TABLE:\n"
        for k, v in self.table.items():
            s += k + ":\n"
            for ls in v:
                s += "\t" + ls[0] + ": "
                for i in ls[1]:
                    s += str(i)
                    s += " "
                s += "\n"

        return s

    def check_ll1(self):
        for k, v in self.table.items():
            term_list = []
            for x in v:
                term_list.append(x[0])
            if len(term_list) != len(set(term_list)):
                return False

        return True
