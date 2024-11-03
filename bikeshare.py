import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
     
    while True:
        city = input("Enter the city name: ").lower()
        if city in CITY_DATA:
                break
        else:
                print("Invalid input. Please choose from chicago, new york city, or washington.")
                            
       
    
    print(city)
        
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = ''
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in months:
        month = input("Please enter a month (january to june) or 'all': ").lower()
        if month not in months:
            print("Invalid month name. Please try again.")
    print(month)
    
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in days:
        day = input("Please enter a day or 'all': ").lower()
        if day not in days:
            print("Invalid day name. Please try again.")
    print(day)

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
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    
    df['month'] = df['Start Time'].dt.month
    print(df.head())
    df['day_of_week'] = df['Start Time'].dt.day_name()
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    mode_value = df['month'].mode()
    
    print("most common month", mode_value)

    
    # TO DO: display the most common day of week
    
    df['day_of_week'] = df['Start Time'].dt.day_name()

    mode_value = df['day_of_week'].mode()
    
    print("most common day", mode_value)

    # TO DO: display the most common start hour
    
    df['hour_of_day'] = df['Start Time'].dt.hour

    common_sh = df['hour_of_day'].mode()
    
    print("most common hour", common_sh)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    counts = df['Start Station'].value_counts()
    count_ss = counts.index[0]
    print ("most commonly used start station:",count_ss)

    # TO DO: display most commonly used end station

    counts = df['End Station'].value_counts()
    count_es = counts.index[0]
    print ("most commonly used end station:",count_es)

    # TO DO: display most frequent combination of start station and end station trip
    
    combined_colmn = df.groupby(['Start Station', 'End Station']).size()
    combined_comn = combined_colmn.idxmax()
    combined_comn_num = combined_colmn.max()
    print("most common combination",combined_comn)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_tt = df['Trip Duration'].sum()
    print("total travel time:",total_tt)
    
    # TO DO: display mean travel time
    
    total_mt = df['Trip Duration'].mean()
    print("mean travel time:", total_mt)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    count_ut = df['User Type'].value_counts()
    #df['User Type'].count()#
    
    print("counts of user types",count_ut)


    # TO DO: Display counts of gender
    
    try:
     count_gndr = df['Gender'].value_counts()
     print("counts of gender",count_gndr)
    except:
     print("gender info column dosent exists in this city ")
    
   

    # TO DO: Display earliest, most recent, and most common year of birth
    
    
    try:
     print("earliest birth:",df['Birth Year'].min())
     print("most recent birth:",df['Birth Year'].max())
     print("most common year of birth:",df['Birth Year'].mode())
    except:
     print("birth info column dosent exists in this city")
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    
    f_index = 0
    user_choice = ""

    while user_choice.lower() != "no":
        user_choice = input("Would you like to view more raw data for the city selected? \nPrint yes or no\n")
        
        if user_choice.lower() == "yes":
            l_index = f_index + 5
            print(df.iloc[f_index:l_index])
            f_index = l_index



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
