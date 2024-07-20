import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file & return a dataframe
    df = pd.read_csv('adult.data.csv') 

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts() #returns a series
    

    # What is the average age of men?
    df2=df[['sex','age']].groupby('sex').mean()
    average_age_men = df2['Male','age'].round(decimals=2)

    # What is the percentage of people who have a Bachelor's degree?
    total_beings= df['education'].value_count().sum()
    Bsc_deg= df['education'].value_counts()
    
    percentage_bachelors = ((Bsc_deg['Bachelors']/total_beings)*100).round(decimals=2)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  #what percentage of people with advance education make more than 50K
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
d_series=df[['education', 'salary']].groupby('education').value_counts()
#print(d_series)
total_D=d_series['Masters','>50K']+ d_series['Doctorate','>50K'] + d_series['Bachelors','>50K']
higher_education = ((total_D/total_beings)*100).round(decimals=2)
lower_education = (100-((total_D/total_beings)*100)).round(decimals=2)

    # percentage with salary >50K
salary_series=df['salary']
higher_education_rich = salary_series.value_counts()['>50K']
lower_education_rich = len(df)-higher_education_rich

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?

one_H_P_W=df[['hours-per-week', 'salary']].groupby('hours-per-week').value_counts()
value_=one_H_P_W[1,'>50K']

num_min_workers = value_
rich_percentage = (value_/len(one_H_P_W))*100

    # What country has the highest percentage of people that earn >50K?

df4=
#return the series of the column of countries
df5=df4
print(df5[0])
highest_earning_country = ((df[df['salary']=='>50K']['native-country'].value_counts())/df['native-country'].value_counts().sum())*100
    highest_earning_country_percentage = ((df[df['salary'] == '>50K']['native-country'].value_counts()) / (df['native-country'].value_counts()) * 100).sort_values(ascending=False).idxmax()

    # Identify the most popular occupation for those who earn >50K in India.
     # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['salary'] == '>50K') & (df['native-country'].isin(['India']))].groupby('occupation')['occupation'].count().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
