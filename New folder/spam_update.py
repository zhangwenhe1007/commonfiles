#!/usr/bin/python3

from csv import writer
import pandas as pd

#i used the complete path, because if I don't use it, maybe VScode gets confused with all the files and can't find spam.csv?... pain
df = pd.read_csv(r'C:\Users\pc\Documents\CODES_EXPOSCIENCES\CODE KIVY_APP\New folder\spam.csv')
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
    append_list_as_row(r'C:\Users\pc\Documents\CODES_EXPOSCIENCES\CODE KIVY_APP\New folder\spam.csv', ['ham', message + ',,,'])
  else:
    append_list_as_row(r'C:\Users\pc\Documents\CODES_EXPOSCIENCES\CODE KIVY_APP\New folder\spam.csv', ['spam', message + ',,,'])

def add_message(message, verdict):
  if verdict[0] == 'spam':
    append_list_as_row(r'C:\Users\pc\Documents\CODES_EXPOSCIENCES\CODE KIVY_APP\New folder\spam.csv', ['spam', message + ',,,'])
  else:
    append_list_as_row(r'C:\Users\pc\Documents\CODES_EXPOSCIENCES\CODE KIVY_APP\New folder\spam.csv', ['ham', message + ',,,'])
