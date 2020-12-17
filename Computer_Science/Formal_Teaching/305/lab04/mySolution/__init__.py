
import turtle
import random

def tree(branchLen,t):

    if(branchLen<20):#the size to be considered a leaf and coloured green
        strinkAmount = random.randint(4, 6)#decrase for leaf lenght (4-6)
    else:
        strinkAmount = random.randint(5,15)#decrease the branch length (5-15)
    angleAmount = random.randint(int(15-branchLen/10),int(45-branchLen/3))#random angle that increase as size gets smaller
    if branchLen>5:
        setPen(branchLen,t)#sets the size can colour of the pen
        t.forward(branchLen)
        t.right(angleAmount)
        tree(branchLen-strinkAmount,t)
        t.left(angleAmount*2)
        tree(branchLen-strinkAmount,t)
        t.right(angleAmount)
        setPen(branchLen, t)#se the size and colour of the pen for backwards draw
        t.backward(branchLen)

def setPen(branchLen,t):
    if(branchLen <20):#leaf is less than 20
        t.color("green")
    else:
        t.color("brown")

    t.pensize(branchLen/5)

def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    #t.speed(0)
    turtle.tracer(10)#makes the program run faster
    t.backward(150)
    t.down()
    tree(75,t)
    myWin.exitonclick()

if __name__ == '__main__':
    main()


def power(x,n,acc=1):
    if( n ==0):
        return acc#this is the base case
    else:
        return power(x,n-1,acc*x)#subract power by one and multiple acc by x

def powerH(x,n):
    if( n==0):
        return 1
    elif(n==1):
        return x
    elif(n%2==0):
        return powerH(x,n//2) * powerH(x,n//2)#if even it splits into to even groups
    else:
        return powerH(x,n//2) * powerH(x,n//2) * x#if old it splits into to even group plus one extra

def binomialCo(n,k):#n is the column and k is the row
    if(k==0 or n ==0):
        return 1
    if(k == n):
        return 1
    return binomialCo(n,k-1) + binomialCo(n-1,k-1)#added the two value above