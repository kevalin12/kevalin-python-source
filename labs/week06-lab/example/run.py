def convert_currency(value, currency):
    if currency=="USD":
        print(f"{value}THB={value/33.0}USD")
    else:
        print(f"{value}USD={value*33.0}THB")

convert_currency(100, 'USD')
convert_currency(100, 'THB')