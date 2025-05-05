def main() -> None:
    list_of_tuples: list = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    out: dict = {}

    for key, value in list_of_tuples:
        if key not in out:
            out[key]: int = int(value)

    sorted_out: list = sorted(out, key=lambda x: (-int(out[x]), ord(x[0])))
    # ord('a') = 97, ord('h') = 104
    # lambda x: (int(out[x]), ord(x[0])) means int(out[x]) - primary sort, ord(x[0]) - secondary
    # -int(out[x]) int value desc, int(out[x]) int value asc
    # ord(x[0) alph asc, -ord(x[0]) alph desc

    [print(x) for x in sorted_out]

if __name__ == '__main__':
    main()
