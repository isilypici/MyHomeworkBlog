#Mergesort Algoritması

"""
Write merge algorithm that merges 2 sorted arrays. Compute your algorithm running time as a function of n.

Example input=[1, 4, 5, 8], [2, 3, 6, 7] output=[1, 2, 3, 4, 5, 6, 7, 8]


Then integrate merge algorithm into mergesort algorithm shown in class. 
Run it on some example input, explain each step by using a debugger.
"""

def sirala(arr):
    arr_length = len(arr)
    mid_arr_point = round(arr_length/2)
    return mid_arr_point
    
def main():
    arr = [1, 4, 5, 8, 2, 3, 6, 7, 9]
    print(sirala(arr))
    
main()