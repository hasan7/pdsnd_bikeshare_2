import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

valid_cities= {"chicago", "new york city" , "washington"}
months = [
        "january", "february", "march", "april", "may", "june"
    ]
days = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"}
choosen_city = ""



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    print("\nPlease pick a city from the list (chicago, new york city, washington)")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    #access the global virable to be updated
    global choosen_city
    while True:
        #get user input for city and do the same for month and day
        city = input("Please Enter City name: ").lower()
       
         
         #update global variable to be used later
        choosen_city = city
        if city in valid_cities:
                print("You entered:", city)
                break
        else:
            print("Wrong city, Please enter only from the list")



    # get user input for month (all, january, february, ... , june)

    
    while True:
        month = input("Please Enter Month name or all for no fliter: ").lower()
        
        if month.lower() == "all":
            print("You entered: all")
            break

        if month.lower() in months:
                print("You entered:", month)
                break
        else:
            print("Wrong month, Please enter only from the list (january, february, march, april, may, june)")

        # get user input for day of week (all, monday, tuesday, ... sunday)

    
    while True:
        day = input("Please Enter  day name or all for no fliter: ")
        #day = "sunday"

        if day.lower() == "all":
            print("You entered: all")
            break

        elif day.lower() in days:
                print("You entered:", day)
                print("user entered valid  day")
                break
        else:
            print("Wrong day, Please enter only from the list (monday, tuesday, wednesday, thursday, friday, saturday, sunday)")



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
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
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
    common_month = df['month'].mode()[0]
    print("most common start month is: "+str(common_month)+" ("+str(months[common_month-1]+")"))

    # display the most common day of week
    
    common_week = df['day_of_week'].value_counts()
    print("most common day of week is: "+str(common_week.idxmax()))

    # display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print("most common start hour is: "+str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].value_counts().idxmax()
    print("most common used start station is "+str(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].value_counts().idxmax()
    print("most common used end station is "+str(common_end_station))

    # display most frequent combination of start station and end station trip
    common_combination = (df['Start Station'] + ' - ' + df['End Station']).value_counts().idxmax()
    print("most common combination is "+str(common_combination))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = np.sum(df['Trip Duration'])
    print('total travel time is '+str(total_travel_time)+"s"+seconds_to_time(total_travel_time))

    
    # display mean travel time
    total_average_travel_time = np.mean(df['Trip Duration'])
    print('total average travel time is '+str(total_average_travel_time)+"s"+seconds_to_time(round(total_average_travel_time)))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("User types are: \n")
    for user_type, count in user_type_count.items():
        print(f"{user_type}: {count}")


    # Display counts of gender
    if(choosen_city == "washington"):
        print("sorry gender count only available for NYC and Chicago")
    else:
        
        gender_count = df['Gender'].value_counts()
        print("\ngender count is \n")
        
        for gender, count in gender_count.items():
            print(f"{gender}: {count}")


    # Display earliest, most recent, and most common year of birth
    if(choosen_city == "washington"):
        print("sorry gender count only available for NYC and Chicago")
    else:
        earliest_year = int(df['Birth Year'].min())
        print(f"Earliest year of birth: {earliest_year}")

        # Display most recent year of birth
        recent_year = int(df['Birth Year'].max())
        print(f"Most recent year of birth: {recent_year}")

        # Display most common year of birth
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Most common year of birth: {most_common_year}")
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return f" {hours}h:{minutes}m:{remaining_seconds}s"


def display_raw_data(df):
     start_raws = 0
     while True:
        print(df.iloc[start_raws:start_raws + 5])
        start_raws += 5
        
          
        while True:
            show_more = input("\nWould you like to see 5 more rows? Enter yes or no.\n").lower()
            if show_more == 'yes':
                break
            elif show_more == 'no':
                return
            else:
                print("Please enter 'yes' or 'no'.")
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while True:
            print("\nPlease choose an operation to perform:")
            print("1. Time Stats (Statistics about The Most Frequent Times of Travel)")
            print("2. Station Stats (Calculating The Most Popular Stations and Trip)")
            print("3. Trip Duration Stats (Trip Duration statistics)")
            print("4. User Stats (User base statistics)")
            print("5. Display raw data")
            print("6. Exit to Main Menu")
            
            choice = input("Enter the number corresponding to your choice: ")
            
            if choice == '1':
                time_stats(df)
            elif choice == '2':
                station_stats(df)
            elif choice == '3':
                trip_duration_stats(df)
            elif choice == '4':
                user_stats(df)
            elif choice == '5':
                display_raw_data(df)
            elif choice == '6':
                break
            else:
                print("Invalid choice. Please try again.")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
