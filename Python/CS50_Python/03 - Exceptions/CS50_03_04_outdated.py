months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Start the Loop
while True:

    # Ask the date
    date = input('Date: ').strip()

    try:

        # Check (MM/DD/YYYY)
        month, day, year = date.split('/')

        if (int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31):
            break

    except:
        try:
            # Check (MM DD, YYYY)
            o_month, o_day, year = date.split(" ")

            for i in range(len(months)):
                if o_month == months[i]:
                    month = i + 1


            day = o_day.replace(',', '')

            # Wait for the error
            if not o_day.endswith(","):
                continue

            
            if (int(month) >= 1 and int(month) <= 12 and int(day) >= 1 and int(day) <= 31):
                break

        except:
            pass

print(f'{year}-{int(month):02}-{int(day):02}')
