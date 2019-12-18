def concat_len_1(a, b):
    x = a
    if "epsilon" in a:
        x = b
        for e in a:
            if e not in x and e != "epsilon":
                x.append(e)

    return x


def concat(production, first):
    if production == "epsilon":
        return ["epsilon"]
    i = 1
    x = first.get_values_of_symbol(production[0])
    if x == []:
        return []

    while i < len(production):
        f = first.get_values_of_symbol(production[i])
        if f == []:
            return []
        y = concat_len_1(x, f)
        i += 1
        x = y

    return x

