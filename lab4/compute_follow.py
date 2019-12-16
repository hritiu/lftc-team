from Follow import Follow


def compare_follows(f1, f2):
    x = f1.get_dict()
    y = f2.get_dict()

    different_items = {k: x[k] for k in x if k in y and x[k] != y[k]}

    if len(different_items) == 0:
        return True
    return False


def get_prod_with_n_rhs(n, grammar):
    l = {}
    for k in grammar.get_nonterminals():
        l[k] = []
        for p in grammar.get_productions_of_nonterminal(k):
            if n in p:
                l[k].append(p)

    return l


def get_first(n, production, first):
    i = 0
    while i < len(production):
        if production[i] == n:
            if i == len(production) - 1:
                x = ["epsilon"]
                return x
            else:
                x = first.get_values_of_symbol(production[i+1])
                return x
        i += 1


def compute_follow(grammar, first):

    follow_list = []

    follow_0 = Follow(0)

    for n in grammar.get_nonterminals():
        if n != grammar.get_start_symbol():
            follow_0.set_value_symbol(n, [])
        else:
            follow_0.set_value_symbol(n, ["epsilon"])

    follow_list.append(follow_0)

    idx = 0
    while True:
        idx += 1
        follow = Follow(idx)

        for n in grammar.get_nonterminals():
            f_list = []
            for e in follow_list[idx-1].get_values_for_symbol(n):
                f_list.append(e)

            for lhs, rhs in get_prod_with_n_rhs(n, grammar).items():
                for p in rhs:
                    x = get_first(n, p, first)
                    for i in x:
                        if i == "epsilon":
                            for e in follow_list[idx-1].get_values_for_symbol(lhs):
                                if e not in f_list:
                                    f_list.append(e)
                        else:
                            if i not in f_list:
                                f_list.append(i)
            follow.set_value_symbol(n, f_list)

        follow_list.append(follow)

        if compare_follows(follow_list[idx-1], follow):
            break

    return follow_list[-1]
