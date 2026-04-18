#set data Structure in python(Properties of set is : 1. sets are mutable , 2. duplicacy is not allowed , 3. indexing is not possible )

myset1=set(); #this is a first way for creating of set using set constructor method
print(type(myset1))

myset2={} ; #it create dict
print(type(myset2))

myset3={1,2,2,3,4,5,5};
print(type(myset3))

myset3.add(10);
print(myset3);

myset3.remove(10);
print(myset3)


myset3.add("coding");
print(myset3);


myset3.discard("coding");
print(myset3);
myset3.add("pw");
print(myset3);


# difference between discard and remove in set
myset3.discard(7);
print(myset3);
# myset3.remove(7);
print(myset3);


myset3.update({11,12,13});
print(myset3);

# union
my_set1={1,2,3};
my_set2={3,4,5};
# my_set1=my_set1.union(my_set2);
print(my_set1);
print(my_set2);

# intersection
# my_set1=my_set1.intersection(my_set2);
print(my_set1);

# difference
print(my_set1.difference(my_set2));
print(my_set2.difference(my_set1));

# symmetric_difference
print(my_set1.symmetric_difference(my_set2));


# clear()
my_set1.clear();
print(my_set1);

# del
# del my_set1;
print(my_set1)


# difference between assignment operator and copy method
myset_1={1,2,3};
myset_2=myset_1;
myset_3=myset_1.copy();
myset_1.add(6);
print("myset 1 value is : ", myset_1, " my set 2 value is : ", myset_2 , "and my set 3 value is : ", myset_3);
