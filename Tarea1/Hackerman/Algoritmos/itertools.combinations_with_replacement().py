# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations_with_replacement
from pip._vendor.distlib.compat import raw_input

w,numero = raw_input().split()

for i in range(1,2):
    for j in combinations_with_replacement(sorted(w),int(numero)):
        print("".join(j))