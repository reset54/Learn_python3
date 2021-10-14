our_input_string = input().strip()
#print(our_input_string)
transform_str = our_input_string.split()
transform_str.pop(0)
transform_str.pop(len(transform_str)-1)
for s in transform_str:
    print(s, end=" " )
