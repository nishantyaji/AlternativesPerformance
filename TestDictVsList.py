import datetime


class TestDictVsList:

    def test(self):
        d = {x: x for x in range(0, 100000)}
        l = [i for i in range(0, 100000)]
        objs = [d, l]

        for i, fn in enumerate([TestDictVsList.test_dict, TestDictVsList.test_list]):
            start = datetime.datetime.now()
            print("start: ", start)
            fn(objs[i])

            end = datetime.datetime.now()
            print("end: ", end)
            print("taken: ", end - start)
        # Sentence: list is better than dict (but not my huge amounts)

    def test_list(l: list[int]):
        lenl = len(l)
        sm = 0
        for i in range(lenl):
            l[i] += i * i
            sm += l[i]
        return sm

    def test_dict(d: dict):
        sm = 0
        for k, v in d.items():
            d[k] += v * v
            sm += d[k]
        return sm


if __name__ == '__main__':
    t = TestDictVsList()
    t.test()
