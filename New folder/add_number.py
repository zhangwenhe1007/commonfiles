from csv import writer

def append_list_as_row(file_name, list_of_elem):
  with open(file_name, 'a+', newline='') as write_obj:

        # Create a writer object from csv module
        csv_writer = writer(write_obj)

        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

def add_num(number):
    append_list_as_row('unwanted_calls.csv', [number])