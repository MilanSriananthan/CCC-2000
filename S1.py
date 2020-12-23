coins = int(input())
first = int(input())
second = int(input())
third = int(input())
final = 0

while True:
    if coins == 0:
        break
    first += 1
    coins -= 1
    final += 1
    if first == 35:
        first = 0
        coins += 30

    if coins == 0:
        break
    second += 1
    coins -= 1
    final += 1
    if second == 100:
        second = 0
        coins += 60

    if coins == 0:
        break
    third += 1
    coins -= 1
    final += 1
    if third == 10:
        third = 0
        coins += 9

print("Martha plays " + str(final) +  " times before going broke.")

