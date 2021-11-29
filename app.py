import keyboard
# importing csv module
import csv

# csv file name
filename = "Donation.csv"
# initializing the titles and rows list
fields = ['Name', 'Donation']
rows = []

def CVS_reload():
    csvread = csv.reader(open(filename, 'r'))
    global fields
    fields = next(csvread)
    global rows
    for row in csvread:
        rows.append(row)

def writeCVS():
    csvwriter = csv.writer(open(filename, 'w'))
    # writing the fields
    csvwriter.writerow(fields)
    # writing the data rows
    csvwriter.writerows(rows)

def newDonation(name, amount):
    do = [name, amount]
    return do

while True:
    name = input("Name : ")
    amo = input("Donation: ")
    Dona = newDonation(name, amo)
    CVS_reload()
    rows.append(Dona)
    writeCVS()
    # get total number of rows
    print("You now have of rows: %d"%(len(rows)))
    # print("Press Q for exit! or press C for continue")
    # try:
    #     if keyboard.read_key() == 'q':  # if key 'q' is pressed 
    #        print('You Pressed q!')
    #        print('exit!')
    #        break  # finishing the loop
    #     if keyboard.read_key() == 'space':  # if key 'space' is pressed 
    #        print('You Pressed space!')
    #        print('continue!')
    #        continue  # continue the loop
    # except:
    #   print("Something wrong we have error here")



