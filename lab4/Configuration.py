
class Configuration:
    def __init__(self, w, symbol):
        self.input_stack = []
        for i in w:
            self.input_stack.append(i)
        self.input_stack.append("$")

        self.working_stack = [symbol, "$"]
        self.pi = ""

    def head_alpha(self):
        return self.input_stack[0]

    def head_beta(self):
        return self.working_stack[0]

    def pop_alpha(self):
        self.input_stack.pop(0)

    def pop_beta(self):
        self.working_stack.pop(0)

    def push_beta(self, prod):
        if prod != "epsilon":
            i = len(prod) - 1
            while i >= 0:
                self.working_stack.insert(0, prod[i])
                i -= 1

    def push_beta2(self, prod):
        if prod != ["epsilon"]:
            i = len(prod) - 1
            while i >= 0:
                self.working_stack.insert(0, prod[i])
                i -= 1

    def add_pi(self, prod_idx):
        self.pi += " " + str(prod_idx)

    def get_pi(self):
        return self.pi

    def is_final_config(self):
        if self.input_stack == ["$"] and self.working_stack == ["$"]:
            return True
        return False
