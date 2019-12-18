from Grammar import Grammar
from read_grammar import read_grammar_from_file
from compute_first import compute_first
from compute_follow import compute_follow
from compute_parse_table import compute_parse_table
from configurations_and_moves import parse_sequence


def main():
    g = Grammar()
    read_grammar_from_file(g)
    print(g.print_grammar())

    f = compute_first(g)
    print(f.get_index(), " idx")
    print(f.print_first())

    l = compute_follow(g, f)
    print(l.get_index(), " idx")
    print(l.print_follow())

    table = compute_parse_table(g, f, l)
    print(table.print_table())

    if table.check_ll1():
        print("Grammar is LL(1)")

        print("PRODUCTION STRING: ")
        w = "a*(a+a)"
        parse_sequence(w, table, g.get_start_symbol())

    else:
        print("Grammar is not LL(1)...")


main()
