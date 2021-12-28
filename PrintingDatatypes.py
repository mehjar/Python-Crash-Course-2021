my_name = 'Srikanth'
print("My name is {my_name}")
#The above snippet perhaps works in Python 3.6

print("My name is", my_name, "Sugavanam")
print("My name is %s." %my_name)

int1 = 25;
int2 = 26;
int3 = 27;

print("If I add %d, %d and %d, I will get %d" %(int1, int2, int3, int1 + int2 + int3))
#Note that there is no character between the end of the string and the variable list
hilarious = False
joke_evaluation = "This is a great joke! %r"

print(joke_evaluation % hilarious)

s1 = "I am adding this string..."
s2 = "...and this string."

print(s1+s2)

print("%s\n " %my_name[3]*10)
