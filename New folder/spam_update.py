#!/usr/bin/python3

from csv import writer
import pandas as pd

df = pd.read_csv('spam.csv')
messages = pd.DataFrame(df, columns=['rating', 'message'])
print(messages)

def append_list_as_row(file_name, list_of_elem):
  with open(file_name, 'a+', newline='') as write_obj:

        # Create a writer object from csv module
        csv_writer = writer(write_obj)

        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def spam_update(message, analysed_rating):
  if analysed_rating[0] == 'spam':
    append_list_as_row('spam.csv', ['ham', message + ',,,'])
  else:
    append_list_as_row('spam.csv', ['spam', message + ',,,'])

def add_message(message, verdict):
  if verdict[0] == 'spam':
    append_list_as_row('spam.csv', ['spam', message + ',,,'])
  else:
    append_list_as_row('spam.csv', ['ham', message + ',,,'])
