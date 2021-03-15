
def call_location(number):
    import phonenumbers
    from phonenumbers import geocoder
    import pandas as pd

    if '+' in number:
        num = number
    else:
        num = '+' + number

    try:
        x = phonenumbers.parse(num, None)
        location = geocoder.description_for_number(x, 'en')
    except phonenumbers.phonenumberutil.NumberParseException:
        return 'Invalid number'

    if '+' in number:
        number = number.replace('+', '')
    if '-' in number:
        number = number.replace('-', '')
    if ')' in number:
        number = number.replace(')', '')
    if '(' in number:
        number = number.replace('(', '')
    if ' ' in number:
        number = number.replace(' ', '')

    df = pd.read_csv('unwanted_calls.csv')
    numbs = pd.DataFrame(df)
    for ele in numbs['Number']:
        numb = str(ele).replace('-', '')
        if numb == 'nan' or numb == 'None':
            continue
        else:
            if number[1:] == numb:
                if not location:
                    return number + " has been previously marked spam."
                else:
                    return number + " is from " + location + "\n" + "This number has been previously marked spam."

    if not location:
        if list(str(number))[1:4] == ['8', '3', '3'] or list(str(number))[1:4] == ['8', '4', '4'] or list(str(number))[1:4] == ['8', '5', '5'] \
                or list(str(number))[1:4] == ['8', '8', '8'] or list(str(number))[1:4] == ['8', '6', '6'] or list(str(number))[1:4] == ['8', '0', '0']\
                or list(str(number))[1:4] == ['8', '7', '7']:
            return number + " is a toll-free scam number."
        else:
            return "Cannot find the location."

    if location == 'Quebec':
        number1 = list(str(number))
        # this means the number comes from canada or the u.s.
        if number1[1:4] == ['5', '1', '4'] or number1[1:4] == ['4', '3', '8']:
            # this means the number is from montreal
            return number + " is from Montréal."
        if number1[1:4] == ["3", "5", "4"] or number1[1:4] == ['4', '5', '0'] or number1[1:4] == ['5', '7', '9']:
            return number + " is from Banlieues de Montréal."
        if number1[1:4] == ['4', '1', '8'] or number1[1:4] == ['5', '8', '1'] or number1[1:4] == ['3', '6', '7']:
            return number + " is from Québec Est."
        if number1[1:4] == ['8', '1', '9'] or number1[1:4] == ['8', '7', '3']:
            # this means that the number is from quebec
            return number + " is from Québec Nord or Ouest."
    else:
        return number + " is from " + location