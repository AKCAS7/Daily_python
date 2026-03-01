'''Dictionary comprehension'''
'''new_dict = {new_key:new_value for item in list}'''
'''new_dict = {new_key:new_value for (key, value) in dict.items()}'''

import random
names = ['Alex', 'Dave', 'James', 'Gabriel']
student_scores = { name: random.randint(1,100) for name in names }

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = { word:len(word) for word in sentence.split()}
print(result)
