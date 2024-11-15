# -*- coding: utf-8 -*-
"""01-Kelompok I-2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19WSp7XFAKpkm-x_6BN5TyxPsQvdr9PnL

Paper Money: <br>
1. Rp 100,000    
2. Rp 50,000   
3. Rp 20,000   
4. Rp 10,000   
5. Rp 5,000   
6. Rp 2,000
<br>
<br>
Coins: <br>
1. Rp 1,000  
2. Rp 500  
3. Rp 200
4. Rp 100  
*To make it easier, we assume that all Rp. 1000 denominations are coins.

There are circumstances where the bank must liquidate all customer savings in the form of money, if the customer requests it.
And imagine this is happening right now in front of you, help the bank to calculate how many denominations of money are needed.

Here is the rule:

1. Bank must prioritize the largest denominations first to be issued.
2. If there is a balance that cannot be cashed, the bank must inform it.
3. Bank must calculate how many number of Paper Money needed and Coins needed.
4. Banks can only disburse a maximum amount of 1 billion Rupiah



Make a python code that receives an integer number of customer savings from 0 - 1 Billions.
"""

#Create command to get input from user, the input should be integer

num = int(input("Enter an integer: "))
print("You entered:", num)

#Create the code here
def tukar(uang):
    paper_money = [100000, 50000, 20000, 10000, 5000, 2000]
    coins = [1000, 500, 200, 100]
    hasil_paper = {}
    hasil_coin = {}

    for i in paper_money:
        if uang >= i:
            hasil_paper[i] = uang // i
            uang %= i

    for i in coins:
        if uang >= i:
            hasil_coin[i] = uang // i
            uang %= i

    uang_sisa = uang

    return hasil_paper, hasil_coin, uang_sisa

hasil_paper, hasil_coin, uang_sisa = tukar(num)

if num > 1000000000:
    print('Maximun Saving is 1000000000')
else:
    for paper,items in hasil_paper.items():
        print('Amount of currency Rp{} : {}'.format(paper, items))
    for coin,items in hasil_coin.items():
        print('Amount of currency Rp{} : {}'.format(coin, items))
    print('------------------------------------')
    total_paper = sum(hasil_paper.values())
    print('Total Paper Money : ', total_paper)
    total_coins = sum(hasil_coin.values())
    print('Total Paper Money : ', total_coins)
    print('------------------------------------')
    print('Cannot be cashed :', uang_sisa)

