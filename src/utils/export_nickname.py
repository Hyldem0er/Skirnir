import csv

import csv

def export_nicknames_csv(nicknames):
    """
    Exports nicknames to a CSV file.

    Args:
        nicknames (list): List of nicknames to be exported.
    """
    with open('nicknames.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',')
        for nickname in nicknames:
            filewriter.writerow([nickname])
