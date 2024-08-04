#Standard Deviation

import numpy as np
alist = []

n = int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(0, n):
  ele = float(input())
  alist.append(ele)

print(alist)

mean = np.mean(alist)
var = np.mean(alist)
std = np.mean(alist)

print(f"Mean: {mean}")
print(f"Variance: {var}")
print(f"Standard Deviation: {std}")
