def main():
    meal = input('What time is it? ')
    meal_time = convert(meal)
    
    # Breakfast
    if meal_time >= 7.0 and meal_time <= 8.0:
        print('breakfast time')
    
    # Lunch
    elif meal_time >= 12.0 and meal_time <= 13.0:
        print('lunch time')
    
    # Dinner
    elif meal_time >= 18.0 and meal_time <= 19.0:
        print('dinner time')



def convert(time):
    h, m = time.split(':')
    
    # Convert to float
    h, m = float(h), float(m)
    
    # transform minutes
    m = m/60
    
    # Return the converted
    return h + m


if __name__ == "__main__":
    main()