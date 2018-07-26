from functools import reduce


# lowest common multiple-LCM 最小公倍
def lcm_seq(seq):  # 求多个数的最小公倍
    def gcd(a, b):  # 求两个数的最大公约数
        r = a % b
        if r:
            return gcd(b, r)
        else:
            return b

    def lcm(a, b):  # 求两个数的最小公倍数
        return a * b / gcd(a, b)
    return reduce(lcm, seq)


lis = [9, 3, 6]
print(int(lcm_seq(lis)))
