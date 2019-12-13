# one.py

# print('Name :',__name__)#,'\nMain print : ',__main__)
# print('hello')

def func():
    print("FUNC() in one.py")

print("Top level in one.py")

if __name__ == "__main__":
    print("one.py is ran directly!")
else:
    print('one.py is imported')




