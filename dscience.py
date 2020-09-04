'''
def square(num):
    return num**2
output = square(5)
print(output)
'''

'''
def time2(num):
    return num*3
output = time2(5)
print(output)
seq = [1,2,3,4,5] #created a list

chelsea = list(map(time2,seq)) #map is a built in function, that allows me to save steps istead of me usig a for loop
print(chelsea) #it prints out the sequece multiplied by 3

#lamda expressions
t = lambda num: num * 2
print(t(9)) #the  valur inside the () arguement is multiplied by 2 which is declared

p = list(map(lambda num: num*3,seq)) #write lambda what you want to pass in : calling what you want to return out
print(p)



seq = [2,4,6,8,10,12,14,16]

p = list(map(lambda num: num*4,seq))
print(p)

#in writing lambda expression you will not have to start writing a function, you just have to write is as done in lie 29
'''

'''
seq = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,1718]
r = list(filter(lambda num: num%2 == 0, seq))
print(r)

#filter function doesn't map element to a sequence rather it filters element from a sequence like the example on line 37 returns all even number in the sequence
#filter and lambda takes in a value that returns a value either true or false 
'''
# All about methods mehn
'''
e = "my name is Adediran Eniayooo"
tein = e.lower()
print(tein)

azeem = e.split() #splits a text to a string and remove the whitespace
print(azeem)

'''
#what is 7 to the power of 4
#value =  7**4
#print(value)
'''
#A function tha extracts domain name from a website or a function tat rabs the email website domain from a string in the form
txt = "user@domain.com"
def domainGet(txt):
    return txt
output =  domainGet(txt.split('@') [1])
print(output)
'''

'''
#A Basic function that returns True if the word 'dog is contained in the input string 
txt = "Is there a dog here?"
def findDog(txt):
    return True
vell = "dog" in txt
print(vell)

def findDog(txt):
    if 'dog' in st.lower():
        print("True")
    else:
        print("False")
        
'''

#A function that counts the number of times the word "dog occurs in a string

#n = "The dog runs faster than the other dog dude!"
#word = "dog"
#count = n.count(word)
#print(count)

# lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'
seq = ['soup','dog','salad','cat','great']
a = list(filter(lambda letters: letters[:][0]== "s", seq))
print(a)



