""" ------- Update Values in Dictionaries and Lists --------- """
x = [ [5,2,3], [10,8,9] ] 

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#1
x[1].pop(0)
x[1].insert(0,15)
# print (x)

#2
# students[0]['last_name']="Bryant"
# print(students)

#3
sports_directory['soccer'][0]="Andres"
# print(sports_directory)

#4
z[0]["y"] = "20"
# print(z)

""" ------- Iterate Through a List of Dictionaries --------- """
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for i in range(0,len(students)):
        a = students[i]["first_name"]
        b= students[i]["last_name"]
        print ("first name -",a ,",","last name -", b )

# iterateDictionary(students)


""" ------- Get Values From a List of Dictionaries --------- """
def iterateDictionary2 (students):
    for i in range (0, len(students)):
        first_name = students[i].get("first_name")
        last_name = students[i].get("last_name")
        print("first", first_name)
        print("last", last_name)

# iterateDictionary2(students)


def iterateDictionary2 (students,key):

    for i in range (0, len(students)):
        value = students[i][key]
        # print(value)

iterateDictionary2(students,"last_name")

""" ------- Iterate Through a Dictionary with List Values --------- """

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo():
    for key,val in dojo.items(): 
        print ( f"{len(val)} {key}")
        for i in range(0,len(val)):
            values = val[i]
            print(values)
        
# printinfo()
