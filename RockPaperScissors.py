'''
Created on 2022/10/14

@author: t20cs021
'''
import random
'''
0->グー
1->チョキ
2->パー
'''

def ExchangeNumtoHand(n):
    if n == 0:
        return 'グー'
    elif n == 1:
        return 'チョキ'
    else:
        return 'パー'
        
n = 10
for i in range(n):

    a = random.randint(0,2)
    b = random.randint(0,2)

    print('Aの手：',ExchangeNumtoHand(a),'v.s. Bの手：',ExchangeNumtoHand(b),end= '')

    if a == b:
        print('-> 引き分け')
    
    else:
        if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
            print('-> Aの勝ち')
        else:
            print('-> Bの勝ち')
