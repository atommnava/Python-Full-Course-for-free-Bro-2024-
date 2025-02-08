# Match case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case'
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            return "It's sunday"
        case 2:
            return "It's Monday"
        case 3:
            return "It's Tuesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case _: # default
            return "Not a valid day"


print("The day: ", day_of_week(1))