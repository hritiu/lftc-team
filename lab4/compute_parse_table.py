from Parse_table import ParseTable
from utils import concat


def compute_parse_table(grammar, first, follow):
    table = ParseTable(grammar)

    prod_idx = 0
    for k, v in grammar.get_productions().items():
        for p in v:
            prod_idx += 1
            first_p = concat(p, first)
            for f in first_p:
                if f == "epsilon":
                    l = follow.get_values_for_symbol(k)
                    for b in l:
                        if b == "epsilon":
                            table.set_value_cell(k, "$", p, prod_idx)
                        else:
                            table.set_value_cell(k, b, p, prod_idx)
                else:
                    table.set_value_cell(k, f, p, prod_idx)

    return table
