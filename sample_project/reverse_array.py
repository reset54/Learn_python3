our_input_string = input()
def reverse_string(string):
    for s in string[::-1]:
        print(s, end='')

# test
reverse_string(our_input_string)