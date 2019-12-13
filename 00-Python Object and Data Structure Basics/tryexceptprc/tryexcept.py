def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number :'))
        except:
            print('''Whoops that's not number''')
            continue
        else:
            print(f"Entered value {result}")
            break
        finally:
            print('End of try/except block. I will always run')


if __name__ == "__main__":
    ask_for_int()
