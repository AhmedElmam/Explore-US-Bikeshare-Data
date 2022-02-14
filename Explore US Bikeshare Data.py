import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
   
    
   
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city=input("please choose a city from chicago , new york city or washington : ").lower()
    while city not in CITY_DATA.keys():
        print("enter vaild city name")
        city=input("please choose a city from chicago , new york city or washington : ").lower()
        
     

    # TO DO: get user input for month (all, january, february, ... , june)
    months=["january" ,"february" ,"march" ,"april", "may" ,'june', 'all' ]
    while True:
      month=input('filter data by month, please type a month or all for not filtering by month : january ,february ,march ,april , may ,june or all :').lower()
      if month in months:
        break
      else:
           print("enter a vaild month") 
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=["all" , "monday", "tuesday" , 'wednesday', "thursday","friday" ,"saturday", "sunday" ]
    while True:
           day=input("filter data by day, please enter a valid day or all for not filtering by date : monday ,tuesday , wednesday , thursday , friday , saturday , sunday or all :").lower()
           if day in days:
               break
           else:
               print("enter a vaild day")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day_of_week']=df['Start Time'].dt.day_name()
    
    if month != 'all':
        months=["january" ,"february" ,"march" ,"april", "may" ,'june']
        month=months.index(month)+1
        
        df=df[df['month']==month]
        
    if day != "all" :
        df=df[df['day_of_week']==day.title()]


    return df


def time_stats(df):
  


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_popular_month=df['month'].mode()[0]
    print('the most common month is:' ,most_popular_month)

    # TO DO: display the most common day of week
    most_popular_day=df['day_of_week'].mode()[0]
    print('the most common day is:' ,most_popular_day)

    # TO DO: display the most common start hour
    df['hours']=df['Start Time'].dt.hour
    most_popular_hour=df["hours"].mode()[0]
    print('the most common hour is:' ,most_popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_popular_startstation=df["Start Station"].mode()[0]
    print('the most popular start station is:' ,most_popular_startstation)

    # TO DO: display most commonly used end station
    most_popular_endstation=df['End Station'].mode()[0]
    print('the most common end station is:' ,most_popular_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df["start and end station"]=df['Start Station']+" to "+df["End Station"]
    most_popular_startendstation=df["start and end station"].mode()[0]
    print("the most popular start and end staion is:" ,most_popular_startendstation)
  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time is :' ,total_travel_time )

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('avrage travel time is : ' ,mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_of_users=df['User Type'].value_counts()
    print('number of users types is : ' , count_of_users)

    # TO DO: Display counts of gender
    if "gender" in df.columns:
      print('count of gender type is :' ,df['Gender'].valuecounts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns: 
     earliest_year= df['Birth Year'].min()
     print('the most early birth year is:' ,earliest_year)   
     
     most_recent_year=df["Birth Year"].max()
     print("the most recent birth year is :" ,most_recent_year)
    
     most_common_year=df["Birth Year"].mode()[0]
     print("the most common birth year is :" ,most_common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def  display_raw_data(df):
    
       display_Raw_datas=input("would you like to display 5 rows data ? 'yes' or 'no' ").lower()

       i=0
       
       while True:
        if display_Raw_datas == "no" :
         break
        print(df[i:i+5])
        display_Raw_datas=input("would you like to display 5 rows data ? 'yes' or 'no' ").lower()
        i += 5 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	 main()



