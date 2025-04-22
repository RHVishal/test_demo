print('Welcome to the Git')
print('First Repository')
print('status -- success')

#writing a code for the voting purpose
age = int(input('Enter the age: '))

if age > 13 and age <= 17:
    print('Eligible for below teen voting')
elif age >= 18 and age <= 60:
    print('Eligible for citizen voting')
elif age >= 60 and age <= 100:
    print('Eligible for senior citizen voting')
else:
    print('Invalid age entered')
    
#additing one adition function

def add(x,y):
    return x+y

print('The sum is',add(5,6))