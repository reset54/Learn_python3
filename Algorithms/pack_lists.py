string = "w w w o r l d g g g g r e a t t e c c h e m g g p w w"
s = string.split()
print(s)

def pack_in_lists(s: str) -> list: 
    new_lst = []
    for i in range(len(s) - 1):
        if s[i] != s[i+1]:
            n = s[i]
            n.append(s[i+1])
        else:
            pass
print(pack_in_lists)

# tests
"""

"a b c d" = [['a'], ['b'], ['c'], ['d']]
"w w w o r l d g g g g r e a t t e c c h e m g g p w w" = [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]
"g i v e t h h i i s m a a a n a g u u n" = [['g'], ['i'], ['v'], ['e'], ['t'], ['h', 'h'], ['i', 'i'], ['s'], ['m'], ['a', 'a', 'a'], ['n'], ['a'], ['g'], ['u', 'u'], ['n']]
"w w w w w w w w w w w w y y y t r t r r t r t r t w w w w w w w w" = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'], ['y', 'y', 'y'], ['t'], ['r'], ['t'], ['r', 'r'], ['t'], ['r'], ['t'], ['r'], ['t'], ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]
"w w w w w w w w w w w w w w w w w w w w" = [['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']]
"0 0 1 2 3 4 4 5 6 6 6 7 8 9 4 4" = [['0', '0'], ['1'], ['2'], ['3'], ['4', '4'], ['5'], ['6', '6', '6'], ['7'], ['8'], ['9'], ['4', '4']]
"5 1 1 g w 6 6 1 8 h e e o 5 t t 2" = [['5'], ['1', '1'], ['g'], ['w'], ['6', '6'], ['1'], ['8'], ['h'], ['e', 'e'], ['o'], ['5'], ['t', 't'], ['2']]
"r a t a t a t a t a ! ! ?" = [['r'], ['a'], ['t'], ['a'], ['t'], ['a'], ['t'], ['a'], ['t'], ['a'], ['!', '!'], ['?']]

"""