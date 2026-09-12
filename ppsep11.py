'''
a = 15
b = 25
print(a+b)

#Tokens --> Keywords,Variables,Operators,Punctuators [],(),{}
#Variable should not start with number,space,symbols and also no space between words

batch = ['pfs-6','da-06']
print(batch)
print(type(batch))
#len() --> It returns the number of items in a collection

print(len(batch))
#IDLE is colour coding editor (Violet--> built in functions)

#Add 3 more student names into it.
# List --> Collection --> append(),extend(),insert()
batch.append('lahar')
print(batch)
batch.extend(['sarat','ganesh'])
print(batch)
batch.insert(0,'Sai') #insert given value at specific index
print(batch)
batch.insert(-1,'python')
print(batch)
print(len(batch))
#Indexing --> [] --> index starts at 0 ends at len(obj)-1,
#also in reverse manner it is -1 to len(obj)

print(batch[0])
print(batch[4])
 #IndexError: list index out of range

#Slicing --> Group of values [start:end]

print(batch[2:4])
# last 3 elements --> We prefer negative index values.
print(batch[-3:])
print(batch[:3])

#Striding --> [start:end:step]
print(batch[::3])
print(batch[1:5:2])#first perform batch[1:5]--> then skip 1 element
print(batch[::4])
'''
batch =['Python','Java']
print(batch)
print(type(batch))
print(len(batch))
batch.append('lahar')
print(batch)
batch.extend(['Akhil','Abi'])
print(batch)
batch.insert(0,'Suhas')
print(batch)
batch.insert(-1,'Abighna')
print(batch)
print(len(batch))
print(batch[2:4])
print(batch[1:4:2])

