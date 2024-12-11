'''import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)

print(myvar)'''


#------------------------

'''import pandas as pd
#a = [1, 7, 2]
#myvar = pd.Series(a)
#myvar = pd.Series(a, index = ["x", "y", "z"])
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)'''

#---------------------------

import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

