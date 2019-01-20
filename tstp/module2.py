
import module1
import csv

with open('HOF.txt', 'w') as f:
    year = input('Enter year of induction - ')
    name = input('Enter name of incuctee - ')
    f.write(year)
    f.write(name)

with open('movies.csv', 'w', newline='') as f:
    w = csv.writer(f, delimiter=',')
    w.writerow(['Top Gun', 'Risky Business', 'Minority Report'])
    w.writerow(['Titanic', 'The Revenant', 'Inception'])
    w.writerow(['Training Day', 'Man of Fire', 'Flight'])

    


