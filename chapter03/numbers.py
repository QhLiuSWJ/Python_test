
for value in range(0,5):
    print(value)

#list将range转换为列表
numbers=list(range(1,6))
print(numbers)

squares=[]
for value in range(1,9):
    square=value**2
    squares.append(square)
    
print(squares)
print(min(squares))
print(max(squares))
print(sum(squares))

##元组的元素不可更改，但是元组可以重新赋值
dimensions=(1,2)
#dimensions[0]=2
dimensions=(2,3)
