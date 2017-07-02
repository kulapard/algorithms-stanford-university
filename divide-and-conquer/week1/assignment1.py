# -*- coding: utf-8 -*-

__author__ = 'Taras Drapalyuk <taras@drapalyuk.com>'
__date__ = '17.03.2017'


# x = (10^n/2)a + b
# y = (10^n/2)c + d
# xy = (10^n)ac + (10^n/2)(ad + bc) + bd
# xy = (10^n)ac + (10^n/2)( (a + b)(c + d) - ac - bd ) + bd

def split(x):
    center = len(x) / 2
    return int(x[:center]), int(x[center:])


def add(x, y):
    return int(x) + int(y)


def multiply_by_ten(x, n):
    """(x, n) -> x * 10 ^ n

    >>>multiply_by_ten(123, 0)
    123
    >>>multiply_by_ten(123, 2)
    12300

    :param x: str
    :param n: int
    :return: int
    """
    return int(str(x) + '0' * n)


def normalize(x, y):
    """12, 3456 -> 0012, 3456

    :param x: int | str
    :param y: int | str
    :return: str
    """
    x, y = str(x), str(y)
    diff = len(x) - len(y)
    if diff < 0:
        x = '0' * abs(diff) + x
    elif diff > 0:
        y = '0' * abs(diff) + y

    return x, y


def get_ad_bc(a, b, c, d):
    # 1)
    # (10^n)ac + (10^n/2)(ad + bc) + bd
    ad = multiply(a, d)  # b * d
    bc = multiply(b, c)  # b * d
    ad_bc = add(ad, bc)

    assert ad == a * d
    assert bc == b * c
    assert ad_bc == ad + bc

    # 2) Gauss’ Trick
    # ad + bc = (a + b)(c + d) - ac - bd
    a_b = add(a, b)  # a + b
    c_d = add(c, d)  # c + d

    assert a_b == a + b
    assert c_d == c + d

    print('%s + %s = %s' % (a, b, a_b))
    print('%s + %s = %s' % (c, d, c_d))

    ac = multiply(a, d)  # a * c
    bd = multiply(b, c)  # b * d

    a_b_c_d = multiply(a_b, c_d)  # (a + b)(c + d)
    a_b_c_d_2 = a_b * c_d  # (a + b)(c + d)
    ad_bc_2 = a_b_c_d - ac - bd
    assert a_b_c_d == a_b_c_d_2, (a_b_c_d, a_b_c_d_2)
    assert ad_bc_2 == ad_bc, (ad_bc_2, ad_bc)

    return ad_bc


def multiply(x, y):
    # 12, 3456 -> 0012, 3456
    x, y = normalize(x, y)

    print('x=%s' % x)
    print('y=%s' % y)

    n = len(x)

    if n == 1:
        return int(x) * int(y)

    a, b = split(x)
    c, d = split(y)

    print(a, b)
    print(c, d)

    ac = multiply(a, c)  # a * c
    bd = multiply(b, d)  # b * d

    print('%s * %s = %s' % (a, c, ac))
    print('%s * %s = %s' % (b, d, bd))

    # 1)
    # (10^n)ac + (10^n/2)(ad + bc) + bd
    ad = multiply(a, d)  # b * d
    bc = multiply(b, c)  # b * d
    ad_bc = add(ad, bc)

    assert ad == a * d
    assert bc == b * c
    assert ad_bc == ad + bc

    # TODO: результат не сходится с методом 1)
    # 2) Gauss’ Trick
    # ad + bc = (a + b)(c + d) - ac - bd
    # a_b = add(a, b)  # a + b
    # c_d = add(c, d)  # c + d
    #
    # assert a_b == a + b
    # assert c_d == c + d
    #
    # print('%s + %s = %s' % (a, b, a_b))
    # print('%s + %s = %s' % (c, d, c_d))
    #
    # a_b_c_d = multiply(a_b, c_d)  # (a + b)(c + d)
    # a_b_c_d_2 = a_b * c_d  # (a + b)(c + d)
    # ad_bc_2 = a_b_c_d - ac - bd
    # assert a_b_c_d == a_b_c_d_2, (a_b_c_d, a_b_c_d_2)
    # assert ad_bc_2 == ad_bc, (ad_bc_2, ad_bc)

    assert ad_bc == a * d + b * c

    # (10^n)ac + (10^n/2)(ad + bc) + bd
    return multiply_by_ten(ac, n) + multiply_by_ten(ad_bc, n / 2) + bd


if __name__ == '__main__':
    x = '3141592653589793238462643383279502884197169399375105820974944592'
    y = '2718281828459045235360287471352662497757247093699959574966967627'
    print(multiply(x, y))
    print(int(x) * int(y))
