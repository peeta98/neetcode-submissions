from typing import List

def read_integers() -> List[int]:
    nums_str = input().split(",")
    nums_int = []
    for num_str in nums_str:
        nums_int.append(int(num_str))
    return nums_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
