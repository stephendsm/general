#dictionary = in real world, you have a bunch of words and they're associated with a bunch of definitons
#In python, we have names for these insted of 'words' and 'definitions'
#We call them 'keys' and 'values'
#syntex : dictionary = {'key':'value', .., ..}
#print? : print(dictionary['key'])

classmates = {'Tony':' cool but smells', 'Emma':' sits behind me', 'Lucy':' asks too many question'}

'''
#cool but tydious way
print(classmates)
print(classmates['Emma'])
'''

for k, v in classmates.items(): # 'k' = keys; 'v' = values; '.items' = gonna loops throu all the item in classmates
    print(k + v)
