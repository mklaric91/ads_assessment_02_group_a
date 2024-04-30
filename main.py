"""
Simple Calculator
"""
# Provide your solution here
def calculate(a, b, operator):
    a=int(input("text"))
    b=int(input("text"))
    operator=str(input("text"))
    if operator("+"):
            print(a+b)
    elif operator("-"):
            print(a-b)
    elif operator ("*"):
            print(a*b)
    elif operator ("/"):
            print(a/b)
    else: print(f"invalid operator")
sum(a, b, operator)
print(f"calculate", sum)



"""
Reverse Word
"""
# Provide your solution here

#def reverse_word(word):
#    word=word.upper()
#word=str(input("Txpe in a word: "))
#print(str(word() [10:0]))

def reverse_word(word):
    reverse_word=word.upper()
word=input("Type in a word")
if input(word):
    print(reverse_word[10-0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

