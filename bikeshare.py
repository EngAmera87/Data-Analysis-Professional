import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
print(CITY_DATA.keys())
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please enter name of city : chicago , new york city , washington:  ").lower()
    while city not in {"chicago","new york city","washington"}:
        print("invalid input please enter name of city")
        city = input ("please enter name of city : chicago , new york city , washington:  ").lower()
        if city in {"chicago","new york city","washington"}:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("please enter name of month to filter by ,or all to apply no month filter: ").lower()
    while month not in { "all", "january" , "february" , "march" , "april" , "may" , "june" }:
                        print("invalid input ")
                        month = input("please enter name of month to filter by ,or all to apply no month filter: ").lower()
                        if month in { "all", "january" , "february" , "march" , "april" , "may" , "june" }:
                                     break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("please enter name of day to filter by ,or all to apply no day filter: ").lower()
    while day not in {"all" , "monday" , "tuesday","wednesday"  , "thursday" , "friday" , "saturday" }:
         print("invalid input ")
         day = input("please enter name of day to filter by ,or all to apply no day filter: ").lower()   
         if day in {"all" , "monday" , "tuesday","wednesday"  , "thursday" , "friday" , "saturday" }:
                break
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])
    df["month"] = df["Start Time"].dt.month_name()
    df["day"] = df["Start Time"].dt.weekday_name
    df["hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        df = df[df["month"]==month.title()]
    if day != "all":
        df = df[df["day"]==day.title()]
    #print(df)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("the most common month",df["month"].mode()[0])

    # TO DO: display the most common day of week

    print("the most common day",df["day"].mode()[0])
    # TO DO: display the most common start hour
    print("the most common start hour ",df["hour"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station : ",df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station

    print("the most commonly used end station : ", df["End Station"].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    df["route"] = df["Start Station"] + "_"+ df["End Station"]
    print("the most combination trip : ",df["route"].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df["total_travel_time"] =df["End Time"] - df["Start Time"]
    
    print(df["Start Station"],df["End Station"],df["total_travel_time"])
    # TO DO: display mean travel time
    print( "total travel time: ",df["total_travel_time"].sum())
    print("mean travel time: ",df["total_travel_time"].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    

    print("count of user types :", df["User Type"].value_counts())
        
        
    

    # TO DO: Display counts of gender
    if "Gender" in df:
        print("count of gender : ",df["Gender"].value_counts())
    else:
        print("Gender data not avaliable ")
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        print("the most common year: ",df["Birth Year"].mode()[0])
        print("the earliest year of birth: ",df["Birth Year"].min())
    else:
        print("birth year data not avaliable")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def show_row(df):
    #this function for display rows
    i = 0
    w = input ("do you want display data row yes or no: ")
    while w in {"yes"}:
       print(df[i:i+5])
       w = input("do you want display more data row: ")
       if w in {"yes"}:
          i+=5
          print(df[i:i+5])
       else:
        
          break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
      
 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
