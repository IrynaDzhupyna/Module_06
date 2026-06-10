import sys

print("Before:", end='')
if 'alchemy' in sys.modules:
    print(" alchemy is already imported")
else:    print(" alchemy is not imported yet")
print()
import alchemy

print("After:", end='')
if 'alchemy' in sys.modules:
    print(" alchemy is now imported")
else:    print(" alchemy is still not imported")
if 'alchemy.elements' in sys.modules:
    print("alchemy.elements is imported")
else:    print("alchemy.elements is not imported")
# to see what is imported in alchemy
print(alchemy.__dict__.keys())

print()
import alchemy.elements

if 'alchemy.elements' in sys.modules:
    print("alchemy.elements is imported")
else:    print("alchemy.elements is not imported")
# to see what is imported in alchemy
print(alchemy.__dict__.keys())

# to see myown namespaces
print()
print(dir())
