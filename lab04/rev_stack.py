stack = []
string = input("Enter a string: ")

# Push each character into the stack
for ch in string:
    stack.append(ch)

# Pop characters to reverse the string
reverse = ""

while len(stack) > 0:
    reverse = reverse + stack.pop()

print("Reversed string:", reverse)