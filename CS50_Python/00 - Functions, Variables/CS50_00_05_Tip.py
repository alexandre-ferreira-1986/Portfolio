#https://www.w3schools.com/python/ref_string_replace.asp

def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dol_float = float(d.replace("$", ""))
    return dol_float


def percent_to_float(p):
    perc = float(p.replace("%", ""))
    return perc/100


main()