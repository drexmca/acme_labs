"""
Sept. 9, 2015
Rex McArthur
Math 320
This is a python implmentation of the Eucledian algorithm.
"""

def find_gcd(a,b):
    '''
    This just returns lists of the remainders, divisors and gcd for 
    any two numbers. Not actually used in the final AE algorithm, but 
    a good exercise, and shows how we got where we got.
    '''
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

def Advanced_Eucledian(a,b):
    '''
    This is an incredibly consise recursive function that works perfectly.
    Collabrative credit to Devon Morris. He got it first, and helped me
    work it out.
    '''
    if a%b == 0:
        return b,0,1
    else:
        c, d, e = Advanced_Eucledian(b, a%b)
        return c,e, d - e*(a//b)

print Advanced_Eucledian(14562, 348)
# returns (6, -13, 544)
print Advanced_Eucledian(348, 14562)
# returns (6, 544, -13)





     

