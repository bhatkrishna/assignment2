# Create a tuple with your first name, last name, and age. Create a list,
# people, and append your tuple to it. Make more tuples with the
# corresponding information from your friends and append them to the
# list. Sort the list. When you learn about sort method, you can use the
# key parameter to sort by any field in the tuple, first name, last name,
# or age.
tuple_=( 'krishan','bhat',26)
people=[]
people.append(tuple_)
print(people)
tuple1=('bikalp','Dhakal',24)
people.append(tuple1)
tuple2=('kendra','Regmi',25)
people.append(tuple2)
tuple3=('suman','Khadka',25)
people.append(tuple3)
print(people)
people.sort()
print(people)


