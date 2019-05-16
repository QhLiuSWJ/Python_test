alien_0 = {'color': 'green',
    'point': 5}
alien_1 = {'color': 'yellow',
    'point': 3}
alien_2 = {'color': 'red',
    'point': 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
###嵌套的使用，将字典存储在列表中，或者将列表中的值存储在字典中

aliens_=[]
for alien_number in range(1,30):
    new_alien={'color': 'red',
        'point': 15}
    aliens_.append(new_alien)
##print(aliens)
for alien in aliens_[:30]:
    print(alien)
print("....")
print("\n\ntotal number of aliens is"+str(len(aliens_)))
