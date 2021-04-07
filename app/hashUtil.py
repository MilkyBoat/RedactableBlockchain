import random
import math
from pyunit_prime import get_large_prime_length    #随机生成指定长度大素数
from pyunit_prime import is_prime                  #判断素数
from pyunit_prime import prime_range               #输出指定区间素数

p = 18604511303632357477261733749289932684042548414204891841229696446591
q = 2238810024504495484628367478855587567273471529988554974877219789
g = 12340

def primeFactorization():                    #分解质因数
    p=0
    q=get_large_prime_length(64)
    while True:
        d=random.randint(2,10000)
        if d%2==0:
            p=q*d+1
            if is_prime(p)==True:
                break
    primeList=prime_range(2,int(math.sqrt(d)))
    result=[[0,0] for i in range(len(primeList))]
    for i in range(len(primeList)):
        result[i][0]=primeList[i]
        while d%primeList[i]==0:
            result[i][1]+=1
            d=d//primeList[i]
    if d!=1:
        result.append([d,1])
    result.append([q,1])
    return p, q, result  

def getGenerator(result, p=p, q=q):                             #get g
    generator=random.randint(1,1000)
    while True:
        if quickPower(generator,q,p)!=1:
            generator+=1
        else:
            for i in range(len(result)):
                if quickPower(generator,int((p-1)/result[i][0]),p)==1:
                    break
            if i != len(result) - 1:
                generator += 1
            else:
                break
    return generator

def getSecretKey(q=q):                                 #get SK,x
    x=random.randint(1, q)
    return x

def getPublicKey(x, g=g, p=p):                             #get PK,h
    h=quickPower(g, x, p)
    return h

def quickPower(a,b,c):                               #快速幂
    result=1
    while b>0:
        if b%2==1:
            result=result*a%c
        a=a*a%c
        b>>=1
    return result

def exgcd(a,b):                                    #扩展欧几里得
    if b==0:
        return 1,0,a
    else:
        x,y,gcd=exgcd(b,a%b)
        x,y=y,(x-(a//b)*y)
        return x,y,gcd

def str2int(msg):                                #处理消息msg为整数
    msg_b = bytes(msg, encoding="utf8")
    return int.from_bytes(msg_b, byteorder='big', signed=False)


def int2str(msg):                                #处理整数消息msg为bytes
    return str(msg.to_bytes(length=2,byteorder='big',signed=False))

