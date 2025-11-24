from typing import Set

all:Set = {1,2,3,4,5,6,7,8,9,10}
even:Set = {2,4,6,8,10}
odd:Set = {1,3,5,7,9}

print('Even union Odd')
print(even.union(odd))

print('Even intersecion Odd')
print(even.intersection(odd))

print('All - Odd')
print(all.difference(odd))

print('C(Even)')
evens_complement = all.difference(even)
print(evens_complement)

print('C(Odd-All)')
odd_and_all_difference = odd.difference(all)
print(all.difference(odd_and_all_difference))