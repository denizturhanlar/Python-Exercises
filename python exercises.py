   # Python Exercises #
###############################################
# TASK 1: Examine the types of data structures.
# Data Structres : int,float,complex,string,boolen,tuple,set

x = 8
type(x)

y = 3.2
type(y)

z = 8j + 18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

#List structure: it is inclusive, changeable and ordered
l = [1, 2, 3, 4,"String",3.2, False]
type(l)

#dictionary structure: key-values are unordered,inclusive,changeable but key value is unique
d = {"Name": "Jake",
     "Age": [27,56],
     "Adress": "Downtown"}
type(d)

#tuple structure: similar to dictionaries in terms of inclusiveness and sequencing, but cannot be changed
t = ("Machine Learning", "Data Science")
type(t)
t[0]

###############################################
#TASK 2: Convert all letters of the given string expression to uppercase. Put space("") instead of commas and periods, separate them word by word.
#Expected output: ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']

text = "The goal is to turn data into information, and information into insight."
text.upper()
text.upper().replace(","," ").replace("."," ").split()

text.lower()

###############################################
# TASK 3: Do the following tasks for the given list.
lst = ["D","A","T","A","S","C","I","E","N","C","E"]

#Step 1: Look at the number of elements of the given list.
len(lst)

# Step 2: Call the elements at index zero and ten
lst[0]
lst[10]

#Step 3: If we want the zeroth and tenth index in a single list
[lst[0], lst[10]]
[lst[0] + lst[10]]

# Step 4: Create a list ["D","A","T","A"] from the given list.
lst[0:4]

#Step 5: Delete the element in the eighth index.
lst.pop(8)
lst

#Step 6: Add a new element
lst.append("miuul")

# Step 7: Re-add element "N" to the eighth index.
lst.insert(8,"N")

###############################################
#TASK 4: Apply the following steps to the given dictionary structure. 
dict = {'Christian': ["America",18],
        'Daisy':["England",12],
        'Antonio':["Spain",22],
        'Dante':["Italy",25]}

#Step 1: Access the key values.
dict.keys()

# # Step 2: Access the values.
dict.values()

# Step 3: Update the value 12 of the Daisy key to 13.
dict.update({"Daisy": ["England",13]})

# Step 4: Add a new key, value:  key is Ahmet, value is [Turkey,24].
dict.update({"AHMET": ["TURKEY",24]})

# Step 5: Delete Antonio from dictionary.
dict.pop("Antonio")

###############################################
#  TASK 5: Write a function that takes a list as an argument, assigns the odd and even numbers in the list to separate lists and returns these lists
l = [2,13,18,93,22]
#create a function

evens=[]
odds=[]

def number(list):
    for i in list:
        if i % 2 ==0:
            even.append(i)
        else:
            odds.append(i)
    return evens,odds

 evens,odds = number(l)

#ıf we want wrıte by using list comprehension

evens_number = [i for i in l if i % 2 == 0]
odds_number = [i for i in l if i % 2 != 0]

#----------------------------------------

even_numbers=[]
odd_numbers=[]
[even_numbers.append(i) if i % 2 == 0  else odd_numbers.append(i) for i in l  ]

#want to see two of them in separate lists in a list:
all_numbers =[[],[]]
[all_numbers[0].append(i) if i % 2 == 0  else all_numbers[1].append(i) for i in l  ]

###############################################
# TASK 6: In the list given below, there are the names of the students who won degrees in engineering and medicine faculties.
# Respectively, the first three students represent the success rank of the engineering faculty, while the last three students belong to the rank of the medical faculty.
# Print student grades specific to faculty using enumarate.

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]
#by using enumnerate
#before we start:
# ogrenci refers to student,"Mühendislik Fakültesi" refers to "Engineering Faculty", "Tıp Fakültesi" refers to "Medical Faculty"

for i,name in enumerate(ogrenciler):
    if i < 3:
        i+=1
        print("Mühendislik Fakültesi", i, ". Ogrencisi:",name)

    else:
        i-=2
        print("Tıp Fakültesi", i , ". Ogrencisi:",name)

# Soluton by without using enumerate:

for i in range(len(ogrenciler)):
    if i < 3:
        print("Mühendislik Fakültesi", i+1 , ". Ogrencisi:", ogrenciler[i])

    else:
        print("Tıp Fakültesi", i-2 , ". Ogrencisi:", ogrenciler[i])


###############################################
#  TASK 7: Below are 3 lists. In the lists, there is a course code, credit and quota information, respectively. Print course information using zip
#Kredisi ...  olan ...  kodlu dersin kontenjanı ... kişidir."

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

# list(zip(kredi,ders_kodu,kontenjan))
# zip(kredi,ders_kodu,kontenjan)

for krd,kod,kont in zip(kredi,ders_kodu,kontenjan):
    print(f"Kredisi {krd}  olan {kod}  kodlu dersin kontenjanı {kont} kişidir.")

###############################################
# TASK 8: Below are 2 sets.
#You are asked to define a function; If the 1st set of cluster includes the 2nd set of cluster, print the common elements. If it does not then print the elements of the 2nd set that doesn't occure in the first set.

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

#create a function

def kumeler(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))


kumeler(kume1,kume2)
