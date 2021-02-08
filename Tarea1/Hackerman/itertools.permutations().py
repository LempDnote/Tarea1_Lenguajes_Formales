from pip._vendor.distlib.compat import raw_input
from collections import OrderedDict

def merge_the_tools(string, k):
    # your code goes here
    l_sub_string = int(len(string)/k)
    segundo = int(len(string)/l_sub_string)
    t1 = []
    for i in range(0,len(string),k):
        t1.append(string[i:i+segundo])
    for i in t1:
        print("".join(OrderedDict.fromkeys(i)))