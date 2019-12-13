'''
A very simple script
'''

a = 1
b = 2
print(a)
print(b)

# ---Output---
# E:\Github\Complete-Python-3-Bootcamp>cd "00-Python Object and Data Structure Basics"

# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics>cd pylintandunittest

# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest>dir
#  Volume in drive E is Gokul
#  Volume Serial Number is F634-46BE

#  Directory of E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest

# 12-12-2019  13:46    <DIR>          .
# 12-12-2019  13:46    <DIR>          ..
# 12-12-2019  13:52                28 simpleone.py
#                1 File(s)             28 bytes
#                2 Dir(s)  544,282,832,896 bytes free

# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest>C:\Users\gokul\Anaconda3\Scripts\pylint.exe simpleone.py
# ************* Module simpleone
# simpleone.py:1:1: C0326: Exactly one space required around assignment
# a=1
#  ^ (bad-whitespace)
# simpleone.py:2:1: C0326: Exactly one space required around assignment
# b=2
#  ^ (bad-whitespace)
# simpleone.py:4:0: C0304: Final newline missing (missing-final-newline)
# simpleone.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# simpleone.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# simpleone.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# simpleone.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

# ----------------------------------------------------------------------
# Your code has been rated at -17.50/10 (previous run: -2.50/10, -15.00)


# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest>C:\Users\gokul\Anaconda3\Scripts\pylint.exe simpleone.py
# ************* Module simpleone
# simpleone.py:1:1: C0326: Exactly one space required around assignment
# a=1
#  ^ (bad-whitespace)
# simpleone.py:2:1: C0326: Exactly one space required around assignment
# b=2
#  ^ (bad-whitespace)
# simpleone.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# simpleone.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# simpleone.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# simpleone.py:4:6: E0602: Undefined variable 'B' (undefined-variable)

# ----------------------------------------------------------------------
# Your code has been rated at -15.00/10 (previous run: -2.50/10, -12.50)


# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest>C:\Users\gokul\Anaconda3\Scripts\pylint.exe simpleone.py
# ************* Module simpleone
# simpleone.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# simpleone.py:1:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# simpleone.py:2:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)

# -------------------------------------------------------------------
# Your code has been rated at 2.50/10 (previous run: 10.00/10, -7.50)


# E:\Github\Complete-Python-3-Bootcamp\00-Python Object and Data Structure Basics\pylintandunittest>


def myfun():
    '''
    A simple Function
    '''
    first = 1
    second = 2
    print(first)
    print(second)


if __name__ == "__main__":
    myfun()
