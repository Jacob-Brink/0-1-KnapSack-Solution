 objects = [(12, 4), (10,6), (8,5), (11,7), (14,3), (7,1),(9,6)]

weightLimit = 18

class Valuable:

  def getValue(self):
    return self.value
  
  def getWeight(self):
    return self.weight

  def __init__(self, weight, value):
    self.weight = weight
    self.value = value

valuables = []

for benefit, weight in objects:
  valuables.append(Valuable(weight, benefit))


def findBestObjects (object_list, weight):
  #base cases
  if len(object_list) == 2:
    obj1 = object_list[0]
    obj2 = object_list[1]

    if (obj1.weight + obj2.weight <= weight):
      return (object_list, obj1.value + obj2.value)
    elif (obj1.weight <= weight and obj2.weight <= weight):
      if (obj1.value > obj2.value):
        return ([obj1], obj1.value)
      else:
        return ([obj2], obj2.value)
    elif (obj1.weight <= weight):
      return ([obj1], obj1.value)
    elif (obj2.weight <= weight):
      return ([obj2], obj2.value)
    else:
      return ([], 0)

  #recursive case
  results = []

  for i in range(len(object_list)):
    obj = object_list[i]
    if (obj.weight <= weight):
      

      #result is in tuple format (array of objects, weight of objects)
      obj_list_copy = object_list[:]
      obj_list_copy.remove(obj)
      result = findBestObjects(obj_list_copy, weight - obj.weight)
      result[0]
      results.append(result)

  #find best one and return
  max = ([], 0)
  for r in results:
    if (r[1] > max[1]):
      max = r
  return max

print(findBestObjects(valuables, 18))
