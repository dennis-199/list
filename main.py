# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Starting with the list myList = [76, 92.3, ‘hello’, True, 4, 76], write Python statements to do the following:
#Append “apple” and 76 to the list.
#Insert the value “cat” at position 3.Insert the value 99 at the start of the list.Find the index of “hello”.
#Count the number of 76s in the list.Remove the first occurrence of 76 from the list.
#Remove True from the list using pop and index.
myList = [76, 92.3, 'hello', True, 4, 76]

myList.append("apple")         # a
myList.append(76)              # a
myList.insert(3, "cat")        # b
myList.insert(0, 99)           # c

print(myList.index("hello"))   # d
print(myList.count(76))        # e
myList.remove(76)              # f
myList.pop(myList.index(True)) # g

print (myList)
