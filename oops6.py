#act1
# Python program to overload equality
# and less than operators

class A:
	def __init__(self, a):
		self.a = a
	def __lt__(self, other):
		if(self.a<other.a):
			return "ob1 is less than ob2"
		else:
			return "ob2 is less than ob1"
	def __eq__(self, other):
		if(self.a == other.a):
			return "Both are equal"
		else:
			return "Not equal"
				
ob1 = A(2)
ob2 = A(3)
print("Passed Values :", ob1.a, ob2.a)
print(ob1 < ob2)

ob3 = A(4)
ob4 = A(4)
print("Passed Values :", ob3.a, ob4.a)
print(ob3 == ob4)


#act2
class flashcard:
	def __init__(self, word, meaning):
		self.word = word
		self.meaning = meaning
	def __str__(self):
		
		#we will return a string
		return self.word+' ( '+self.meaning+' )'
		
flash = []
print("welcome to flashcard application")

#the following loop will be repeated until
#user stops to add the flashcards
while(True):
	word = input("enter the name you want to add to flashcard : ")
	meaning = input("enter the meaning of the word : ")
	
	flash.append(flashcard(word, meaning))
	option = int(input("enter 0 , if you want to add another flashcard otherwise enter 1 : "))
	
	if(option):
		break
		
# printing all the flashcards
print("\nYour flashcards")
for i in flash:
	print(">", i)

#act3
import random

class FruitQuiz:

	# Create a constructor
	def __init__(self):
		
		# Create a dictionary of fruits as keys and color as value
		self.fruits={'apple':'red',
					'orange':'orange',
					'watermelon':'green',
					'banana':'yellow'}

	# Function for the quiz, here a fruit will be chosen randomly	
	def quiz(self):
		while (True):
			
			fruit, color = random.choice(list(self.fruits.items()))
			
			print("What is the color of {}".format(fruit))
			user_answer = input()
			
			if(user_answer.lower() == color):
				print("Correct answer")
			else:
				print("Wrong answer")
				
			option = int(input("enter 0 , if you want to play again otherwise enter 1: "))
			if (option):
				break

print("welcome to fruit quiz ")
fq = FruitQuiz()
fq.quiz()

#act4
class Animal:
 
    def __init__(self, age):
        self.__age = age
 
    def setage(self, age):
        self.__age = age
  
    def getage(self):
        return self.__age
 
 
    def __add__(self, predict):
        return Animal( self.__age + predict.__age )
 
    def __gt__(self, predict):
        return self.__age > predict.__age
 
    def __lt__(self, predict):
        return self.__age < predict.__age
 
    def __str__(self):
        return "Combined age of the two animals " + str(self.__age)
 
c1 = Animal(5)
print(c1.getage())
 
c2 = Animal(6)
print(c2.getage())
 
c3 = c1 + c2
print(c3.getage())
 
print( c3 > c2) 
 
print( c1 < c2) 
 
print(c3) 

#acp
class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(1))
print(py_solution().int_to_Roman(35))

