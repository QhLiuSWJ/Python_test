bicycles=['trek','cannondale','redline','specialized']
print(bicycles[-1])
print(bicycles[2].title())
##修改
bicycles[-1]='changetest'
print(bicycles[-1])
bicycles.append('addtest')
print(bicycles[-1])
print(bicycles)

#insert new item
bicycles.insert(2,'inserttest')
print(bicycles[2])

print(bicycles)
del bicycles[1]
print(bicycles)

#类似于栈的处理pop
#弹出pop中固定位置的元素,remove的使用
popedbicycles=bicycles.pop()
print(popedbicycles)
print(bicycles)
pop1_bicycles=bicycles.pop(1)
print(pop1_bicycles)



#####sort()修改后不可恢复顺序，而sorted()不会改变原始的列表，bicycle.reverse()也是永久倒转列表，len(bicycles)读取长度

bicycles.sort()
print(bicycles)
bicycles.sort(reverse=True)
print(bicycles)
bicycles.insert(1,'testsort')
print(bicycles)
