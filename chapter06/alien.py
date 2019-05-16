alien_0 = {'color':'green', 'points':5 }
print(alien_0['color'])
print(alien_0['points'])
##Key and value
##add 
##python 不关心添加键值对的顺序，只关心他们的联系
print(alien_0)
alien_0['a_position']=0
alien_0['y_position']=0
print(alien_0)

##缩进时注意加上‘’
##遍历
print(alien_0['color']+
    '\n' + str(alien_0['points']))
for key,value in alien_0.items():
    print("\nKey:"+str(key))
    print("value:"+str(value))
for key in alien_0.keys():
    print(str(alien_0[key]))

##sorted 按照字母排序
for key in sorted(alien_0.keys()):
    print(str(alien_0[key]))

##sorted 按照字母排序
for value1 in alien_0.values():
    print(str(value1))
###set 输出不重复的值
for value1 in set(alien_0.values()):
    print(str(value1))
    
