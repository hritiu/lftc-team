from Grammar import Grammar
from read_grammar import read_grammar_from_file
from compute_first import compute_first
from compute_follow import compute_follow


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


main()