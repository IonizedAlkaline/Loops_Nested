word = input("enter a word: ")
count = 0
char = input("enter the character to be counted: ")
for i in word:
    if i == char:
        count = count + 1
print("the number of times", char, "was in", word, "was ", count)
