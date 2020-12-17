import timeit

def recMC(coinValueList,change):
   minCoins = change
   if change in coinValueList:
     return 1
   else:
      for i in [c for c in coinValueList if c <= change]:
         numCoins = 1 + recMC(coinValueList,change-i)
         if numCoins < minCoins:
            minCoins = numCoins
   return minCoins

print("hi")
#time = 5
#time = timeit.timeit(recMC([1,5,10,25],63) )
#print("finished recMC in:{time}".format(time=6) )
#print(recMC([1,5,10,25],63))
