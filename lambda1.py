def testfunc(num):
    return lambda x: x * num 
        # x is the number we don't know yet
        #lambda expressions return function objects

result10 = testfunc(10)
result100 = testfunc(100)

print(result10(9)) # = 90
print(result100(9)) # = 900

result10 = lambda x: x*10  #same thing
result100 = lambda x: x*100 #same thing 



numbers_list = [2,6,8,10,4,12,7,13,17,0,3,21]

filtered_list = list(filter(lambda num: (num > 7), numbers_list)) #object is lambda function or reg function
print(filtered_list)



mapped_list = list(map(lambda num: num % 2, numbers_list)) #getting the remainder when dividing the numbers by 2


print(mapped_list)

