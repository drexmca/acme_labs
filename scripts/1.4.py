"""
Sept. 9, 2015
Rex McArthur
Math 320
This is a python implmentation of teh Eucledian algorithm.
"""

def find_gcd(a,b):
    r_list = []
    d_list = []
    if b > a:
        a, b = b, a
    r_list.append(b)
    d = a/b
    while a % (b*d) > 0:
        d = a/b
        r = a % (b * d)
        r_list.append(r)
        d_list.append(d)
        a = b
        b = r_list[-1]
    d_list.append(r_list[-2]/r_list[-1])
    print r_list
    print d_list
    return r_list, d_list


r,d = find_gcd(14562, 348)

     

