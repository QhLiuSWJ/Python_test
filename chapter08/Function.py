# ##
# def greet_user():
    # print("hello world")
# greet_user()
# def greet_user(user_name):
    # print("hello world "+user_name.title())
# greet_user('jam')
# def greet_user(user_name,other_name):
    # print("hello world "+user_name)
    # print("hello world "+other_name)
# greet_user('Liu','shen')

def greet_user(user_name,other_name ="vy"):
    print("hello world "+user_name)
    print("hello world "+other_name)
greet_user('iu','shen')
#def get_formatted_name(first_name,middle_name=' ',final_name) middle_name=' '在后面才可以进行两个参数的调用
def get_formatted_name(first_name,final_name,middle_name=''):
    if middle_name:
        full_name=first_name + ' ' + middle_name + ' ' + final_name
    else:
        full_name=first_name + ' ' + final_name
    print(full_name)
    return full_name
a=get_formatted_name('liu','shen','LS')
print(a)

unprinted_design = ['iphone case', 'robot pendant', 'dodecahedron']
completed_design = []

###pop()移除列表中的参数
##使用[:]s使得创建一个副本，而不改变实参的值
def print_design(unprinted_design,completed_design):
    while unprinted_design:
        current_design=unprinted_design.pop()
        print('current_design ' + current_design)
        completed_design.append(current_design)
        
print_design(unprinted_design[:],completed_design)

for com in completed_design:
    print(com)
print(unprinted_design)
print(str(len(unprinted_design)))
i=0

##如果unprint_design为空的话，那么for循环中的值就不会运行
for com in unprinted_design:
    i=i+1
    if com:
        print(com)
    else:
        print('unprinted_design is null')
        
print(str(i))
