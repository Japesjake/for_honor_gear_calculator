import random

class Item:
    def __init__(self, type, bastion, lastStand):
        self.type = type
        self.bastion = bastion
        self.lastStand = lastStand
items = []
items.append(Item('head', 220, 0))
items.append(Item('head', 0, 110))
items.append(Item('chest', 110, 110))
items.append(Item('shoulder', 110, 110))
items.append(Item('blade', 110, 110))
items.append(Item('blade', 220, 0))
items.append(Item('hilt', 110, 110))
items.append(Item('hilt', 220, 0))
items.append(Item('shield', 110, 0))
items.append(Item('shield', 0, 110))

while True:
    bools = {'head':False, 'chest':False, 'shoulder':False, 'blade':False, 'hilt':False, 'shield':False}
    assignedItems = []
    random.shuffle(items)
    totalBastion = 0
    totalLastStand = 0
    for item in items:
        if not bools[item.type]:
            assignedItems.append(item)
            bools[item.type] = True
            totalBastion += item.bastion
            totalLastStand += item.lastStand
    if totalBastion >= 600 and totalLastStand >= 600:
        break
    

print('totals')
print('bastion: ' + str(totalBastion))
print('lastStand: ' + str(totalLastStand))
print()

for item in assignedItems:
    print(item.type)
    print('    bastion: ' + str(item.bastion))
    print('    lastStand: ' + str(item.lastStand))