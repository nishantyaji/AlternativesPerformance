import datetime
import math


class TestGCD:

    def test(self):
        for fn in [TestGCD.gcd, TestGCD.math_gcd]:
            start = datetime.datetime.now()
            print("start: ", start)
            for i in range(2000, 3000):
                for j in range(3000, 4000):
                    fn(i, j)
            end = datetime.datetime.now()
            print("end: ", end)
            print("taken: ", end - start)
            # The jury is that: math.gcd is faster, way faster


    def gcd(a: int, b: int):
        small = b if a > b else a
        large = a ^ b ^ small

        r = 1
        while r > 0:
            r = large % small
            large = small
            small = r

        return large


    def math_gcd(a: int, b: int):
        return math.gcd(a, b)


if __name__ == '__main__':
    t = TestGCD()
    t.test()
