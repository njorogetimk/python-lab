def get_dates():
    """
    Gets the two dates to do the difference
    """
    print("Enter the first date:\t")
    date_1 = input()
    print("Enter the second date:\t")
    date_2 = input()

    return date_1, date_2

def check_date_format(date):
    """
    Checks for wrong formatted date input
    """
    print("Wrong date format")

def sort_date(date1, date2):
    """
    Gets which is the earliest and latest date
    """
    split_date1 = date1.split('-')
    split_date2 = date2.split('-')
    if split_date1[2] == split_date2[2]:
        """Dates in the same year"""

        if split_date1[1] == split_date2[1]:
            """Dates in the same month"""
            if split_date1[0] == split_date2[0]:
                """Both are the same day"""
                upper_limit_date = split_date1
                lower_limit_date = split_date2
            elif split_date1[0] < split_date2[0]:
                """Date 1 earlier than date 2"""
                upper_limit_date = split_date1
                lower_limit_date = split_date2
            else:
                """Date 2 earlier than date 1"""
                upper_limit_date = split_date2
                lower_limit_date = split_date1
        elif split_date1[1] < split_date2[1]:
            """Date 1 earlier than date 2"""
            upper_limit_date = split_date1
            lower_limit_date = split_date2
        else:
            """Date 2 earlier than date 1"""
            upper_limit_date = split_date2
            lower_limit_date = split_date1
    elif split_date1[2] < split_date2[2]:
        """Date 1 earlier than date 2"""
        upper_limit_date = split_date1
        lower_limit_date = split_date2
    else:
        """Date 2 earlier than date 1"""
        upper_limit_date = split_date2
        lower_limit_date = split_date1
    
    return upper_limit_date, lower_limit_date

def years_between_no(date1, date2):
    year1 = date1.split('-')[2]
    year2 = date2.split('-')[2]
    diff = int(year1) - int(year2)
    if diff < 0:
        diff = diff * -1
    
    return diff

def days_to_end_year(splitDate):
    """Calculates the days to end the year"""
    leap_year = [31,29,31,30,31,30,31,31,30,31,30,31]
    non_leap_year = [31,28,31,30,31,30,31,31,30,31,30,31]
    if int(splitDate[2])%4 == 0:
        """It is a leap year"""
        """Get the remaining days of the month"""
        rm_days_month = leap_year[int(splitDate[1])-1] - int(splitDate[0])
        
        
        """Get the remaining month days"""
        if splitDate[1] == "12":
            rm_month_days = 0
        else:
            rm_month_days = 0 # Remaing days of the other months of the year
            month = int(splitDate[1]) # Month number from split date
            remaining_months = 12-month
            for i in range(remaining_months):
                rm_month_days = rm_month_days+leap_year[month]
                month += 1
    else:
        """It is not a leap year"""
        """Get the remaining days of the month"""
        rm_days_month = non_leap_year[int(splitDate[1])-1] - int(splitDate[0])
        
        """Get the remaining month days"""
        if splitDate[1] == "12":
            rm_month_days = 0
        else:
            rm_month_days = 0 # Remaing days of the other months of the year
            month = int(splitDate[1]) # Month number from split date
            remaining_months = 12-month
            for i in range(remaining_months):
                rm_month_days = rm_month_days+non_leap_year[month]
                month += 1
    
    remaining_days = rm_days_month + rm_month_days
    return remaining_days

def day_of_the_year(splitDate):
    """
    Gets the day of the year eg. 200th day
    """
    if int(splitDate[2])%4 == 0:
        """Its a leap year"""
        day = 366 - days_to_end_year(splitDate)
    else:
        """It's not a leap year"""
        day = 365 - days_to_end_year(splitDate)
    
    return day

def days_in_year_intervals(diff, earlierDate):
    """
    Calculates the number of leap years and no of non leap years
    """
    start_year = int(earlierDate[2])+1
    leap_years = 0
    non_leap_years = 0
    for i in range(diff-1):
        if start_year%4 == 0:
            leap_years += 1
        else:
            non_leap_years += 1
        start_year += 1
    
    total_days = 365*non_leap_years + 366*leap_years
    return total_days


def days_calc(diff, earlierDate, latterDate):
    """
    Does the days calculation based on the difference of the years in the dates (diff)
    """
    if diff == 0:
        """Dates are in the same year"""
        days = days_to_end_year(earlierDate)-days_to_end_year(latterDate)
    
    elif diff == 1:
        """Dates are in adjascent years"""
        days = days_to_end_year(earlierDate) + day_of_the_year(latterDate)
    
    else:
        """Dates are more than one year apart"""
        days = days_to_end_year(earlierDate) + day_of_the_year(latterDate) + days_in_year_intervals(diff, earlierDate)
        
    
    return days


def main():
    date1, date2 = get_dates()
    earlierDate, latterDate = sort_date(date1, date2)
    diff = years_between_no(date1, date2)
    days = days_calc(diff, earlierDate, latterDate)
    print(f"\n\nThe number of days in between are: {days}\n")

if __name__ == '__main__':
    main()
