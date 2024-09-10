import datetime


class TestPow:
    def test(self):
        for fn in [TestPow.pow_op, TestPow.pow_rec]:
            start = datetime.datetime.now()
            print("start: ", start)
            for cnt in range(10000):
                for i in range(2, 20):
                    for j in range(3, 10):
                        fn(i, j)
            end = datetime.datetime.now()
            print("end: ", end)
            print("taken: ", end - start)

        # Jury: unsure. usually the operator wins but not always
    def pow_op(b: int, index: int):
        return b ** index

    def pow_rec(b: int, index: int):
        if index == 1:
            return b
        return TestPow.pow_rec(b, index - 1)


if __name__ == '__main__':
    t = TestPow()
    t.test()
