import traceback
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Creating and using dictionaries in python
capitals = {'England':'London', 'Nigeria':'Abuja', 1: 'one'}
print(capitals)

# Updating dict
capitals['Japan'] = 'Tokyo' # Add new entry
print("Adding new entry: ", capitals)

capitals['Nigeria'] = 'FCT'
print("Updating dictionary: ", capitals)

del capitals['Nigeria']
logger.info("Updated dictionary: ", capitals)
# print("Updated dictionary: ", capitals)

# Trying to access invalid keys
try:
    print(capitals[111])
except Exception as e:
    print(traceback.format_exc())
    exit()