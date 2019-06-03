# try:
    # print(5/0)
# except ZeroDivisionError:
    # print('you can not divide by zero!')

while True:
    try:
        first_number= input("\nfirst_number:")
        if first_number=='q':
            break
        second_number=input("\nsecond_number:")
        printstr=str(int(second_number)/int(first_number))
    except ZeroDivisionError:
        print('can not divise by 0!')
    else:    
        print(printstr)
