#
#
#
import datetime

while True:
    try:
        year = int(input('Year :'))
        print(datetime.datetime.utcnow().year - year)

    except ValueError:
        print('Is not a number ')
        continue
