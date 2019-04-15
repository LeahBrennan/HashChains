import hashlib
import random


seed = "c89aa2ffb9edcc6604005196b5f0e0e4"
print(seed)
#output
mapSeed = hashlib.md5(seed.encode('utf-8'))
print(mapSeed)


'''
The above is the segment of code that was not commented out from when this lab was first attempted. When run on the 15th of April, 
0x00000289F34E75D0 was the first md5 Hash Object that is outputted. It is unknown how many times it would have to be run to 
retrieve the real answer to which would be the second last hash in the chain.  
'''

mapSeed = hashlib.md5(input("c89aa2ffb9edcc6604005196b5f0e0e4").encode('utf-8'))
rnd = random.Random()
rnd.seed(mapSeed.digest())
print(mapSeed)
print(rnd.random())

#Code sourced from: https://stackoverflow.com/questions/35189234/pythons-random-seed-does-not-work-when-seeded-with-a-hash/35189437


mapSeed = 'c89aa2ffb9edcc6604005196b5f0e0e4'
r = random.Random()
r.seed = hashlib.md5('c89aa2ffb9edcc6604005196b5f0e0e4'.encode('utf-8'))
print(mapSeed)
print(random.random())
#print(r)
#print(seed)
#Code sourced from: https://stackoverflow.com/questions/35189234/pythons-random-seed-does-not-work-when-seeded-with-a-hash/35189437
#Trying a different way of applying RANDOM and a way to convert the seed to md5

'''
On the first attempt at this lab, the above should have got the user to input a seed, which would have changed every time due to RANDOM.  The first of the two eventually stopped running. 
Reviewing the whole .py file a second time, it is clear that this should have in some way included a range of values that could be mapped, to output the correct answer the first time it is run. 
As running then searching online for a converter tool and repeating this process over and over would be a tedious and time consuming process. 
In an attempt to divide the code into three separate .py files found that the first of the three parts was the only one outputting the md5 HASH object 
and that the other two were just giving the seed that had been declared previously.
'''
