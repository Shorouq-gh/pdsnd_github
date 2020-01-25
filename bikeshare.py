
import time
import pandas as pd
import numpy as np

#Here are the files of the data that are analyzed.
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities=['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june','july', 'august', 'september', 'october', 'november', 'december' ,'all']
days=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter city of interest ')
    while city not in cities:
        city = input('The city entered is incorrect, reenter city of interest: ')


    # get user input for month (all, january, february, ... , june)
    month = input('Enter month of interest, or (all): ')
    while month not in months:
        month = input('The month entered is incorrect, reenter month of interest: ')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter day of interest, or (all): ')
    while day not in days:
        day = input('The day entered is incorrect, reenter day of interest: ')

    print('-'*40)
    return city, month, day

#This function loads the data for the city,month, and day that the user inputs.
def load_data(city, month, day):
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = +df['month'].mode()[0]

    # display the most common day of week
    df['week'] = df['Start Time'].dt.weekday_name
    popular_day = df['week'].mode()[0]

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]

    print(' The most popular month is: '+ months[popular_month] +'\n The most popular day is: '+ str(popular_day) +'\n The most popular start hour is: '+ str(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_ss=df['Start Station'].mode()[0]

    # display most commonly used end station
    popular_es = df['End Station'].mode()[0]

    # display most frequent combination of start station and end station trip
    df['combo'] = 'Start Station- ' + df['Start Station'] + ' ' + 'End Station- ' +df['End Station']
    popular_ses= df['combo'].mode()
    print(' The most popular start station is: '+ popular_ss +'\n The most popular ending is: '+ popular_es +'\n The most popular start end station trip combination: '+ popular_ses[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    return

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['s hour'] = df['Start Time']
    df['e hour'] = df['End Time']
    df['time_for_each'] = df['e hour'] - df['s hour']
    total_time = df['time_for_each'].sum()

    # display mean travel time
    mean_time = total_time / len(df['time_for_each'])
    print('Total travel time is: '+ str(total_time)+'\n The mean time of a any given trip is: '+ str(mean_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    User_Types = df['User Type'].value_counts()
    print(User_Types)

    # Display counts of gender
    try:
        Genders = df['Gender'].value_counts()
        print(str(Genders))
    except:
        print('no gender info available')

    # Display earliest, most recent, and most common year of birth
    try:
        print('The earliest birth year is: ' + str(min(df['Birth Year'])))
        print('The most recent birth year is: ' + str(max(df['Birth Year'])))
        print('The most common birth year is: ' + str((df['Birth Year']).mode()[0]))
    except:
        print('no birth year info available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #raw data display
        answer = input('would you like to view raw data of the selected city? (yes/no) ')
        while answer not in ('yes','no'):
            answer = input('your input is invalid please choose (yes/no) ')
        i=5
        while answer =='yes':
            print(df[i-5:i])
            answer=input('would you like to view 5 more rows of data? (yes/no) ')
            while answer not in ('yes','no'):
                answer = input('your input is invalid please choose (yes/no) ')
            i+=5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
