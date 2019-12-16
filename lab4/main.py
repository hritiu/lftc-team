from Grammar import Grammar
from read_grammar import read_grammar_from_file
from compute_first import compute_first


def main():
    g = Grammar()
    read_grammar_from_file(g)
    print(g.print_grammar())

    f = compute_first(g)
    print(f.get_index(), " idx")
    print(f.print_first())


main()