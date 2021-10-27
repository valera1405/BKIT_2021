from operator import itemgetter

class Language:
    def __init__(self, id_lan, l):
        self.id_lan = id_lan
        self.l = l

class Library:
    def __init__(self, id_det, name, soft_cost, id_lan):
        self.id_lan = id_lan
        self.id_det = id_det
        self.name = name
        self.soft_cost = soft_cost

class LibLan:
    def __init__(self, id_det, id_lan):
        self.id_det = id_det
        self.id_lan = id_lan

libs = [
    Library(1, 'Emoji', 500, 1),
    Library(2, 'Pandas', 700, 1),
    Library(3, 'Console Paint', 1000, 2),
    Library(11, 'GraphABC', 1500, 3),
    Library(22, 'Math', 1200, 4),
    Library(33, 'Guava', 2000, 5),
]
langs = [
    Language(1, 'Python'),
    Language(2, 'C#'),
    Language(3, 'Pascal'),
    Language(4, 'AC++'),
    Language(5, 'Java'),
]
cross = [
    LibLan(1, 1),
    LibLan(2, 2),
    LibLan(3, 3),
    LibLan(3, 4),
    LibLan(3, 5),
    LibLan(11, 1),
    LibLan(22, 2),
    LibLan(33, 3),
    LibLan(33, 4),
    LibLan(33, 5),
]

def main():
    """Основная функция"""
    one_to_many = [(e.name, e.soft_cost, d.l)
                   for d in langs
                   for e in libs
                   if e.id_lan == d.id_lan]

    many_to_many_temp = [(d.l, ed.id_lan, ed.id_det)
                         for d in langs
                         for ed in cross
                         if d.id_lan == ed.id_lan]

    many_to_many = [(e.name, e.soft_cost, lang_name)
                    for lang_name, id_lan, id_det in many_to_many_temp
                    for e in libs if e.id_det == id_det]

    print('Задание №1')
    res1 = {}
    for d in langs:
        if d.l.lower().startswith('a'):
            d_emps = list(filter(lambda i: i[2] == d.l, one_to_many))
            d_emps_name = [x for x, _, _ in d_emps]
            res1[d.l] = d_emps_name
    print(res1)

    print('\nЗадание №2')
    res_12_unsorted = []
    for d in langs:
        d_emps = list(filter(lambda i: i[2] == d.l, many_to_many))
        if len(d_emps) > 0:
            d_sals = [sal for _, sal, _ in d_emps]
            d_sals_max = max(d_sals)
            res_12_unsorted.append((d.l, d_sals_max))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание №3')
    res_11 = sorted(many_to_many, key=itemgetter(2))
    print(res_11)
if __name__ == '__main__':
    main()
