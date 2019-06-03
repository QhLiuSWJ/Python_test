##file operator
with open('test.txt') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.rstrip())

with open('test.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

pi_String=''
with open('test.txt') as file_object:
    lines=file_object.readlines()
    for line in lines:
        pi_String+=line.rstrip()
    print(pi_String)
    ##查询莫格字符串释放包含
    if 'wi' in pi_String:
        print('this string is in pi_string')
    else:
        print('this string is not in pi_string')

with open('test.txt','a') as appendfile:
    appendfile.write('\n'+'work hard to learn python')
