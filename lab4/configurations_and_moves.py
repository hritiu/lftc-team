from Configuration import Configuration


def parse_sequence(w, table, start_symbol):
    config = Configuration(w, start_symbol)

    while True:
        head_alpha = config.head_alpha()
        head_beta = config.head_beta()

        x = table.get_value_cell(head_beta, head_alpha)

        if len(x) == 2:
            config.pop_beta()
            config.push_beta(x[0])
            config.add_pi(x[1])
        elif len(x) == 1:
            if x[0] == "pop":
                config.pop_beta()
                config.pop_alpha()
            elif x[0] == "acc":
                print("PI: ", config.get_pi())
                return True
        else:
            print("Sequence not accepted!")
            return False

