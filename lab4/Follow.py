class Follow:
    def __init__(self, idx):
        self.idx = idx
        self.dict = {}

    def get_index(self):
        return self.idx

    def get_dict(self):
        return self.dict

    def get_values_for_symbol(self, symbol):
        return self.dict[symbol]

    def set_value_symbol(self, symbol, value_list):
        self.dict[symbol] = value_list

    def print_follow(self):
        s = "FOLLOW:\n"
        for k, v in self.dict.items():
            s += k + " = {"
            for i in v:
                s += i + " "

            s += "}\n"

        return s
