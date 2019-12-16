
class First:
    def __init__(self, idx):
        self.idx = idx
        self.dict = {}

    def get_index(self):
        return self.idx

    def set_symbol_value(self, symbol, value_list):
        self.dict[symbol] = value_list

    def get_values_of_symbol(self, symbol):
        return self.dict[symbol]

    def get_dict(self):
        return self.dict

    def get_keys(self):
        return self.dict.keys()

    def print_first(self):
        s = "FIRST:\n"
        for k, v in self.dict.items():
            s += k + " = {"
            for e in v:
                s += e + " "
            s += "}\n"

        return s

