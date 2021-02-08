# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

from pip._vendor.distlib.compat import raw_input

w,numero = raw_input().split()

for i in range(1,int(numero)+1):
    for j in combinations(sorted(w),i):
        print("".join(j))