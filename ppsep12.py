'''
batch = ['sai','PFS-06','DA-6','saketh','akash','python','anil']
batch.insert(2,("vizag","hyd","vijayawada"))
print(batch)
print(len(batch[2]))
print(batch[2][:2])#("vizag","hyd")
print(batch[2][1])#this returns 'hyd' string
print(batch[2][::2])#returns vizag,vijayawada
print(batch[2].index('hyd'))#index seeker
#index --> First occurence
#count --> returns the count of objects
print(batch[2].count('codegnan')) #returns count as 0 
print(batch[2].index('codegnan')) #throws an error

batch = ['sai','PFS-06','DA-6','saketh','akash','python','anil']
batch.insert(3,['pfs','da','jfs'])
print(batch)
#now let's apply some of list functions in above batch list
print(batch[3])
print(batch[3][1])
#to convert only jfs as upper case --> jfs
batch[3][2] = batch[3][2].upper()
print(batch[3][2])
#now we wanted to add new course in batch[3] position-->AAA
batch[3].append('AAA')
print(batch[3])
print(len(batch))

print(batch)
batch.remove('akash')
print(batch)
#remove --> value,pop--->index
batch.pop()
print(batch)
#batch[2].remove('hyd') #raises error
#del batch[2][1] #tuple is immutable so we can't insert/remove
#We wanted to remove entire data but keep the list as it is -->clear
batch.clear()
print(batch)
'''
#lets work on Dictionaries
#dict --> {k:v}, keys must be unique
#keys can be int.float.string,list

details = {}
#print(len(details))
details['batch'] = ['PFS6']
print(details)
details['course'] = ['Python']
#print(details)
details['students'] = ['Sarat','Lahar']
#we want to update the dictionary
details.update({'branch':('hyd','vijayawada'),
                'Subjects':{'python','Aptitude','Softskills'}})
print(details)
print(len(details))
#first always check the type --> dict--> keys()
#keys(),values(),items()
print(details.keys()) #returns only keys
print(details)
details['batch'].extend(['JFS','DA'])
print(details)
print(details['batch'])
details['students'].extend(['balaji','karthik'])
print(details)
details['Subjects'].add('DSA')
print(details)
        
