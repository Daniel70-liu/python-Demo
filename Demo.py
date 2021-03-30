import random as rand
class Demo:
    def __init__(self):
        print(self.genRandomList())
        self.p,self.q= map(int,input().split())
        self.N=self.p*self.q
        selfN1=(self.p-1)*(self.q-1)
        print(self.genEList())
        self=int(input())
    def encrypt(self,msg):
        print("Encrypy")
    def decrypt(self,msg):
        print("Decrypt")
    def genRandomList(self):
        data = []
        while len(data)<6:
            y=rand.randint(1024,65535)
            if isPrime(y):
                data.append(y)
                return data    
    def isPrime(self,x):
        flag=True
        i=2
        while i<x//2:
            if x%i==0:
                flag=False
                break
            i=i+1
            return flag
    def fun(self, N1, e):
        maxVal = max (N1, e)
        minVal = min (N1, e)
        if maxVal %minVal==0 :
            return minVal
        else:
            return fun(minVal,maxVal%minVal)   

if __name__=='__main__':
    rsa=Demo()
    rsa.encrypt()            