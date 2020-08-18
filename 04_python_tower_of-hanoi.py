

# Towers of Hanoi Problem 

def tower_sort(n, stick1, stick2, stick3):
    if n == 1:
        print('from:',stick1, 'to:', stick2)
        stick1.remove(n) 
        stick2.append(n) 
        s1, s2, s3 = stick1, stick2, stick3 
    else: 
        [s1, s3, s2]  = tower_sort(n-1, stick1, stick3, stick2) 
        print('from:',s1, 'to:', s2) 
        s2 = s2 + [s1[len(s1) -1]] 
        s1.pop(len(s1)-1) 
        [s3, s2, s1] = tower_sort(n-1, s3, s2, s1) 
    return [s1, s2, s3] 


def tower_sort_input(n): 
    start_stick = list(map(lambda num: (n+1-num), list(range(1, (n+1))) )) 
    return tower_sort(n, start_stick, [], [] )

print(tower_sort_input(4)) 
# print(tower_sort_input(8)) 
# print(tower_sort_input(12)) 
