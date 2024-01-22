# for i in range(5):
    # print(' '*i,'*', sep='')


# space = 4
# for i in range(1, 10):
#     if i % 2 != 0:
#         print(' '*space, end='')
#         print("*"*i)
#         space -= 1

for i in range(1, 10, 2):
    print(f'{"*"*i:^9}')
