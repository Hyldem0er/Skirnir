import csv

def export_nicknames_csv(nicknames):
    with open('nicknames.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for nickname in nicknames:
            filewriter.writerow([nickname])
