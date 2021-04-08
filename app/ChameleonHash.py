import random
from hashUtil import *

def ChameleonHash(PK,g,m,r):                       #变色龙哈希
    if isinstance(m, str):
        m = str2int(m)
    return quickPower(g, m, p) * quickPower(PK, r, p) % p

def Forge(SK,m1,r1,m2):                            #求r'
    if isinstance(m1, str):
        m1 = str2int(m1)
    if isinstance(m2, str):
        m2 = str2int(m2)
    x, y, gcd = exgcd(SK, q)
    return x * (m1 - m2 + SK * r1) % q

if __name__ == "__main__":
    print('calculating...')
    SK=getSecretKey(q)
    PK=getPublicKey(SK, g, p)
    
    msg1 = 'i sent first message'                  #消息1
    msg2 = 'second message'                        #消息2
    newmsg1 = str2int(msg1)
    newmsg2 = str2int(msg2)
    rand1 = random.randint(1, q)                    # r

    print('q =', q)
    print('p =', p)
    print('g =', g)
    print('SK =', SK)
    print('PK =', PK)
    print('')

    print('msg1 =', msg1)
    print('rand1 =', rand1)
    CH=ChameleonHash(PK, g, newmsg1, rand1)
    print('CH =', CH)
    print('')
    
    print('msg2 =', msg2)
    rand2 = Forge(SK, newmsg1,rand1,newmsg2)
    print('rand2 =', rand2)
    newCH = ChameleonHash(PK, g, newmsg2, rand2)
    print('newCH =', newCH)

