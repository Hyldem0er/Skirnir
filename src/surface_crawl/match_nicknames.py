import os
import csv

csv_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'mapping_nicknames_names.csv'))

import csv

def match_nicknames(firstname):
    """
    Matches nicknames based on a given first name in a CSV file.
    
    Args:
        firstname (str): The first name to search for in the CSV file.
        
    Returns:
        list: A list of matching nicknames found in the CSV file.
    """
    matching_nicknames = []
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['name'] == firstname:
                matching_nicknames.append(row['nickname'])
    return matching_nicknames

def create_query_matching_nicknames(lastname, matching_nicknames_list):
    """
    Creates a query string based on matching nicknames and a last name.
    
    Args:
        firstname (str): The first name to use for nickname matching.
        lastname (str): The last name to include in the query.
        
    Returns:
        str: The constructed query string.
    """
    or_limit = len(matching_nicknames_list)
    query = "("
    for nicknames in matching_nicknames_list:
        or_limit -= 1
        query += "\"{}\"{}".format(nicknames, "+OR+" if or_limit != 0 else "")
    query += ")+AND+\"{}\"".format(lastname)
    return query


def list_nicknames():
    """
    Matches nicknames based on a given first name in a CSV file.
    
    Args:
        firstname (str): The first name to search for in the CSV file.
        
    Returns:
        list: A list of matching nicknames found in the CSV file.
    """
    data = []  # Initialize an empty list to store the data

    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        for row in csv_reader:
            data.append(row)  # Append each row as a dictionary to the 'data' list

    return data