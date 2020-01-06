from Grammar import Grammar
from read_grammar import read_grammar_from_file, read_grammar_from_file_2
from compute_first import compute_first, compute_first2
from compute_follow import compute_follow
from compute_parse_table import compute_parse_table, compute_parse_table2
from configurations_and_moves import parse_sequence, parse_sequence2


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


# main()

def read_w():
    w = []
    x = input("Please, enter PIF (one element a time): ")
    while x != "":
        w.append(x)
        x = input("Elem: ")

    return w


def main2():
    g = Grammar()
    read_grammar_from_file_2(g)
    print(g.print_grammar())

    f = compute_first2(g)
    print(f.get_index(), " idx")
    print(f.print_first())

    l = compute_follow(g, f)
    print(l.get_index(), " idx")
    print(l.print_follow())

    table = compute_parse_table2(g, f, l)
    print(table.print_table())

    if table.check_ll1():
        print("Grammar is LL(1)")

        w = ["25", "0", "32", "0", "17", "21", "0", "16", "0", "22", "14", "26"]

        # { if x > 3 { write ( yes) ; } }
        q = ["25", "6", "0", "28", "1", "25", "10", "21", "1", "22", "14", "26", "26"]

        # { while x < y { read p ; } }
        q2 = ["25", "8", "0", "28", "0", "25", "9", "0", "14", "26", "26"]

        # { int : x ; x = 5 ; if x > 3 { write ( yes) ; } }
        q3 = ["25", "4", "33", "0", "14", "0", "32", "1", "14", "6", "0", "28", "1", "25", "10", "21", "1", "22", "14", "26", "26"]

        # ww = read_w()
        # print("WW: ", ww)
        print("PRODUCTION STRING: ")
        parse_sequence2(q3, table, g.get_start_symbol())


    else:
        print("Grammar is not LL(1)...")


main2()
