import world

# print(world)
# print(world.africa)
# print(world.europe)

from world import europe
# print(europe.greece)

# Because world has been imported, europe is also found in the world namespace
print(world.europe.norway)

# print(europe.spain) # Error because spain submodule has not been imported in europe/__init__.py

# Import spain explicitly
import world.europe.spain
from world.europe import norway

print(norway)

print(dir())