
def sort_list_two_statements(lst: list) -> list:
    lst = sorted(lst, key=lambda tup: (-tup[1], tup[0]))
    # first statement - reverse sort [1]
    # second statement - direct sorting [0]
    # print(lst) # debug
    return(lst)

    
# test_list
subject_marks = [('English', 88), ('Science', 90), ('Maths', 88),
                 ('Physics', 93), ('History', 78), ('French', 78),
                 ('Art', 78), ('Chemistry', 88), ('Programming', 91)]

# run test
for i in sort_list_two_statements(subject_marks):
    print(*i)
