import time
import pandas as pd

# Create a dictionary contains the data sources for the three cities

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york.csv',
             'washington': 'washington.csv'}


# Asks user to state city, month, and day to analyze.
def data_clean():

    print('Let\'s take a tour around US bikeshare data.')
        
    # creating an empty variables to let the user set value for them
    city = ''
        
    while city not in CITY_DATA.keys():
        city = input('\nChoose your city:\n 1. Chicago\n 2. New York\n 3. washington\n\n').lower()
        if city not in CITY_DATA.keys():
            print('Invalid input. Re-Enter the city again.')

    print('Your have chosen to show {} city.'.format(city.title()))

        
    # Creating a dictionary to store all the months
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
        
    while month not in MONTH_DATA.keys():
        month = input('\nShow data of (January, February, March, April, May, June, All): ').lower()
        if month not in MONTH_DATA.keys():
            print('Invalid input. Re-Enter the month again. ')

    print("You have chosen to show {} month(s).".format(month.title()))

        
    #Creating a dictionary to store all the days
    DAY_DATA = ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'all']
    day = ''
        
    while day not in DAY_DATA:
        day = input('\nShow data of (Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, All): ').lower()
        if day not in DAY_DATA:
            print('Invalid input. Re-Enter the day again. ')

    print('You have chosen to show {} day(s).'.format(day.title()))

    print('\nYou have chosen to view data for city: {}, month/s: {} and day/s: {}. '.format(city.upper(), month.upper(), day.upper()))
    
    #Returning the city, month and day the user selected
    return city, month, day


    print('\n********************************************************************************************************************')


def load_data(city, month, day):
    print("\nwait few seconds...")
    
    # loading data from .csv files from city to filter by month and day
    df = pd.read_csv(CITY_DATA[city])

    # Converting Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extracting both month and day of week from Start Time and creating two new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filtering by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    # filtering by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df
    

    
def time_calc(df):
    print('\n--The Most Popular Times of Travel--\n')
    
    # calculating most popular times of travel
    start_time = time.time()
    
    # use mode method to find the most popular month
    common_month = df['month'].mode()[0]

    print("Most Common Month: {}\n".format(common_month))

    # use mode method to find the most popular day
    common_day = df['day_of_week'].mode()[0]
    print("Most Common Day of Week: {}\n".format(common_day))

    # Extracting hour from Start Time column and creating new hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most Common Start Hour of Day: {}\n".format(common_hour))

    # calculating the time taken to get all this calculations excuted
    print("\nThis process took {} seconds.".format(time.time() - start_time))


    print('\n********************************************************************************************************************')

    
def station_calc(df):
    print('\n--The Most Popular Stations and Trip--\n')
    
    # calculating most popular Stations and Trip
    start_time = time.time()

    # use mode method to find the common start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Common Start Station: {}\n'.format(common_start_station))

    # use mode method to find the common end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Common End Station: {}\n'.format(common_end_station))

    # Create new column with start to end using cat method and use mode to get the most frequent start to end stations
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    start_to_end = df['Start To End'].mode()[0]

    print('Most frequent combination of Start Station and End Station: {}.\n'.format(start_to_end))
    
    # calculating the time taken to get all this calculations excuted
    print("\nThis process took {} seconds.".format(time.time() - start_time))



    print('\n********************************************************************************************************************')


    
def trip_duration_calc(df):
    print('\n--Calculating Trip Duration--\n')
    
    # calculating total and average of trip duration
    start_time = time.time()

    # calculating total of travel time by using sum method
    total_travel_time = df['Trip Duration'].sum()
    
    # stating the travel time in hrs, mins and secs
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)


    print('The total travel time is {} hours, {} minutes and {} seconds.\n'.format(hour, minute, second))
    
    # calculating average of travel time by using mean method
    average_travel_time = round(df['Trip Duration'].mean())
    
    # stating the travel time in mins and secs
    mins, sec = divmod(average_travel_time, 60)

    #This filter excutes time in hours, mins, sec format if the mins exceed 60
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print('The average travel time is {} hours, {} minutes and {} seconds.\n'.format(hrs, mins, sec))
    else:
        print('The average  travel time is {} minutes and {} seconds.\n'.format(mins, sec))
        
    # calculating the time taken to get all this calculations excuted
    print("\nThis process took {} seconds.".format(time.time() - start_time))


        
    print('\n********************************************************************************************************************')

    

def user_info(df, city):
    
    print('\n--Calculating User info--\n')
    
    # calculating the users information details
    start_time = time.time()

    # count the users by value_counts method
    user_type = df['User Type'].value_counts()

    # excuting users data by their types either subscriber or customer
    print("The types of users by number are given below:\n\n{}".format(user_type))
    
    # excuting number of users by gender for both chicago and new york files but not for washington as it's file doesn't include the gender column
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print("\nThe types of users by gender are given below:\n\n{}".format(gender))
        
        
        # excuting number of users by birth year for both chicago and new york files but not for washington as it's file doesn't include the birth year column
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common = int(df['Birth Year'].mode()[0])
        
        print('------------------------------------------------\n')

        print('The earliest year of birth: {}\n'.format(earliest))
        print('The most recent year of birth: {}\n'.format(recent))
        print('The most common year of birth: {}\n'.format(common))


    
    else:
        print('\nThere is no birth year data in this file.')
    
    # calculating the time taken to get all this calculations excuted
    print("\nThis process took {} seconds.".format(time.time() - start_time))

        

    print('\n********************************************************************************************************************')
    
    

def show_data(df):
    i = 0
    user_input = input('Wanna show 5 rows of raw data?, Yes or No? ').lower()
    if user_input == 'no':
        print('\nOkay. Thank you.')
    while user_input == 'yes':
        print(df.head())
        while i + 5 < df.shape[0]:
            print(df.iloc[i: i + 5])
            i += 5
            
            # asking the user if they want to continue viewing data
            user_input = input('\nWanna show more 5 rows of raw data?, Yes or No? ').lower()
            if user_input == 'no':
                print('\nOkay. Thank you.')
                break
    if user_input not in ['yes', 'no']:
        print('Invalid input.')
        
        user_input = input('\nWanna display 5 rows of raw data?, Yes or No? ').lower()


        
#Main function to call all the previous functions

def main():
    while True:
        city, month, day = data_clean()
        df = load_data(city, month, day)
        
        
        time_calc(df)
        station_calc(df)
        trip_duration_calc(df)
        user_info(df, city)
        show_data(df)


        restart = input('\nWould you like to restart? Enter Yes or No.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
