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
     city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()
     while city not in ['chicago', 'new york city', 'washington']:
        print('We have no data for the selected city.\n')
        city = input("Would you like to see data for Chicago, New York City or Washington?\n").lower()

     # TO DO: get user input for month (all, january, february, ... , june)
     monthwillbeselected = input("Would you like to filter the data by month? Say Yes or No.\n").lower()
     while monthwillbeselected not in ['yes','no']:
         print('Please write Yes or No.\n')
         monthwillbeselected = input("Would you like to filter the data by month? Say Yes or No\n").lower()
     if monthwillbeselected == 'yes':
         month = input("Please select one month from January to June.\n").lower()
         while month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
             print('We have no data for the selected month.\n')
             month = input("Please select one month from January to June.\n").lower()
     else:
         month = 'all'
 

     # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
     daywillbeselected = input("Would you like to filter the data by day? Say Yes or No.\n").lower()
     while daywillbeselected not in ['yes','no']:
         print('Please write Yes or No.\n')
         daywillbeselected = input("Would you like to filter the data by day? Say Yes or No\n").lower()
     if daywillbeselected == 'yes':
         day = input("Please select one day from Monday to Sunday.\n").lower()
         while day not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
             print('We have no data for the selected month.\n')
             day = input("Please select one day from Monday to Sunday.\n").lower()
     else:
         day = 'all'
 
   
     print('-'*40)
     return city, month , day

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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #  extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    df['hour'] = df['Start Time'].dt.hour
    
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

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start Month:', popular_month)
    # ADDITIONAL COMMAND: this is the ey point of the work.
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Start Day:', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    print('Most commonly used start station:', df['Start Station'].value_counts().head(1))
    #print('Most commonly used start station:', df['Start Station'].mode()[0])
     # TO DO: display most commonly used end station
    print('Most commonly used end station:', df['End Station'].value_counts().head(1))
    #print('Most commonly used end station:', df['End Station'].mode()[0])
    # TO DO: display most frequent combination of start station and end station trip
    print('Most commonly combination:', ('**Start** ' + df['Start Station'] + ' **End** ' + df['End Station'] + ' ****').mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print ('Total travel time is:', df['Trip Duration'].sum())
  
    # TO DO: display mean travel time
    print('Average value for travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print ('User type counts:\n', df['User Type'].value_counts())
    
    # TO DO: Display counts of gender
    listofcities = ['chicago','new york city']
    if (city in listofcities):
        print ('Gender counts:\n', df['Gender'].value_counts())
    else:
        print ('In this city there is no gender data.')
    # TO DO: Display earliest, most recent, and most common year of birth
    if (city in listofcities):
        print('The earliest year of birth:', df['Birth Year'].min() )
        print('The latest year of birth:',df['Birth Year'].max() )
        print('The most common year of birth:',df['Birth Year'].mode()[0])
    else:
        print ('In this city there is no birth data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
            city, month, day  = get_filters()
            #print (month)
            #print (day)
            df = load_data(city, month, day)
            #print (df.columns)
            
            time_stats(df)
            
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            printing_row_data(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break

def printing_row_data(df):
    """Displays raw data."""

    print('\nRaw data...\n')
    start_time = time.time()
    
    row=0
    raw_data =input('Do you want to see 5 lines of raw data? Yes or No?\n')
    while True :
        yesOrNo = ['yes','no']
        if (raw_data.lower() in yesOrNo):
            if raw_data.lower() == 'yes':
                print(df.iloc[row : row + 5])
                row = row + 5
                raw_data = input('Do you want to see 5 more lines of raw data? Yes or No?\n')
            else:
               break
            
        else:
            print('You have to write yes or no')
            raw_data =input('Do you want to see 5 lines of raw data? Yes or No?\n')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
if __name__ == "__main__":
	main()
