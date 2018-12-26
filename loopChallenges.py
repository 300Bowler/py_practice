# Loop challenge answers

# 1.
shows = ['The Walking Dead', 'Entourage', 'The Sopranos', 'The Vampire Diaries']
for show in shows:
    print(show)

# 2.
for i in range(25, 51):
    print(i)
    
# 3.
for show in shows:
    print(show, shows.index(show))

# 4.
lst = [23, 2, 4, 6, 18, 12, 2, 64, 42]
n = 0
while True:
    print('Type q to quit - ')
    guess = input('Guess the next number - ')
    if guess == 'q':
        break
    if int(guess) == lst[n]:
        print('Your guess was correct!')
    else:
        print('Your guess was incorrect.  The number was ' + str(lst[n]))
    n = (n + 1) % 9

# 5.
lst1 = [8, 19, 148, 4]
lst2 = [9, 1, 33, 83]
final = []
for i in lst1:
    for j in lst2:
        new = i * j
        final.append(new)
print(final)

