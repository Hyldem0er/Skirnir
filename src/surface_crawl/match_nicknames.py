import os
import csv

# filename = os.path.abspath("../../data/mapping_nicknames_names.csv")
# print(filename)

filename = 'D:\Epita\Skirnir\data\mapping_nicknames_names.csv'

def match_nicknames(firstanme):
    matching_nicknames = []
    with open(filename, mode='r') as csv_file:
        print("passe par la")
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['name'] == firstanme:
                matching_nicknames.append(row['nickname'])
    return matching_nicknames


def create_query_matching_nicknames(firstname, lastname):
    matching_nicknames_list = match_nicknames(firstname)
    # (("Jean"+OR+"John")+AND+"+Deriaux")+
    or_limit = len(matching_nicknames_list)
    query = "(("
    for nicknames in matching_nicknames_list:
        or_limit -= 1
        query += "\"{}\"{}".format(nicknames, "+OR+" if or_limit != 0 else "")
    query += ")+AND+\"+{}\"".format(lastname)

    print(query)

    return query
