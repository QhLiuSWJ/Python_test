##
def make_pizze(*toppings):
    """test任意参数实参"""
    for topping in toppings:
        print(topping)

def make_pizze2(size,*toppings):
    """test任意参数实参"""
    for topping in toppings:
        print(str(size)+topping)
        
make_pizze('bua','biq')

make_pizze2('bua','biq','de','fe')

def build_profile(first,last,**user_def):
    """test 字典"""
    profile={}
    profile['first name']=first
    profile['last name']=last
    for Key,value in user_def.items():
        profile[Key]=value
    print(profile)
    
build_profile('a','b',C='c',D='d')
