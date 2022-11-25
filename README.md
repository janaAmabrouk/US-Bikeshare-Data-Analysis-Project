# **US-Bikeshare-Data-Analysis-Project**
# **Overview:**
In this project, we will make use of python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.
- According to the input the code will import the data and answer interesting questions about it by computing descriptive statistics. 
- The Source code takes in raw input to create an interactive experience in the terminal to present these statistics.


# **What Software Do I Need?**
- You should have Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like Sublime or Atom.
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).


# **Explanation of the code:**
### **How the program works:**
The program takes in raw input to create an interactive experience in the terminal that answers questions about the dataset. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.


### **The Datasets:**
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year


# **Statistics Computed**
After the user has chosen which city he wants to discover either Chicago, New York City, or Washington. In this project, the code will provide the following information:
* 1 Popular times of travel (i.e., occurs most often in the start time)
  - most common month
  - most common day of week
  - most common hour of day

* 2 Popular stations and trip
  - most common start station
  - most common end station
  - most common trip from start to end (i.e., most frequent combination of start station and end station)

* Trip duration
  - total travel time
  - average travel time

* User info
  - counts of each user type
  - counts of each gender (only available for NYC and Chicago)
  - earliest, most recent, most common year of birth (only available for NYC and Chicago)
