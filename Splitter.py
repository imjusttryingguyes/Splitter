import random
print('Enter the number of friends joining (including you):')

friends_list = []
friends = {}
a = int(input())
print()
if a < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for i in range(a):
        name = input()
        friends_list.append(name)
    print()
    print('Enter the total bill value:')
    bill = int(input())
    print()

    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input()
    print()
    if answer == 'Yes':
        lucky_number = random.randint(1, a)
        print(friends_list[lucky_number], 'is the lucky one!')
        print()
        bill_person = round(bill / (a-1), 2)
        for i in range(a):
            if i == lucky_number:
                friends_name = {friends_list[i]: 0}
                friends.update(friends_name)
            else:
                friends_name = {friends_list[i]: bill_person}
                friends.update(friends_name)
        print(friends)
    else:
        print('No one is going to be lucky')
        print()
        bill_person = round(bill / a, 2)
        for i in range(a):
            friends_name = {friends_list[i]: bill_person}
            friends.update(friends_name)
        print(friends)
