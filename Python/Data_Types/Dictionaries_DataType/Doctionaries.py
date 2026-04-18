mydict1=dict();
mydict2={};
mydict2={'bihar':'patna','up':'kanpur','punjab':'amristar'};
print(mydict2.values());
print(mydict2.keys());
print(mydict2["up"]);

# del
del mydict2['up'];
print(mydict2);

# update
mydict2.update({"mp":"indore"});
print(mydict2);
mydict3={'delhi':'noida'};
mydict2.update(mydict3);
print(mydict2);


# popitem
mydict2.popitem();
print(mydict2);


# items
print(mydict2.items());


# in
print('mp' in mydict2);


# get()
print(mydict2.get('mp'));
print(mydict2['mp']);