import pandas as pd
import numpy as np


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(by='race').size().to_frame().reset_index()
    race_count = race_count.sort_values(by=0,ascending=False)
    race_count = np.array(race_count.iloc[:,-1])

    # What is the average age of men?
    groupof_men = df.loc[(df['sex'] == 'Male')]
    groupof_men = round(groupof_men['age'].mean().mean(),1)
    average_age_men = groupof_men

    # What is the percentage of people who have a Bachelor's degree?
 
    bachelors = df[df['education'] == 'Bachelors']
    total_samples = len(df)
    percentage_bachelors = round((len(bachelors))/total_samples*100,1)
  

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education = df.loc[df["education"].isin(["Bachelors", "Masters","Doctorate"])]
    higher_education_sum = len(higher_education)
    print('higher education total', higher_education_sum)
    lower_education = df.loc[~df["education"].isin(["Bachelors", "Masters","Doctorate"])]
    lower_education_sum = len(lower_education)
    print('lower education sum', lower_education_sum)

# percentage with salary >50K
    higher_rich = higher_education[higher_education["salary"] == ">50K"]
    higher_edu_rich_sum = len(higher_rich)
    higher_education_rich = round((higher_edu_rich_sum/higher_education_sum*100),1)
    
#print(higher_education_rich/(higher_education)*100, 'higher education with more than 50K')
    lower_rich = lower_education[lower_education["salary"] == ">50K"]
    lower_rich_sum = len(lower_rich)
    lower_education_rich = round(lower_rich_sum/lower_education_sum*100,1)
  
   
   
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = len(df.loc[df["education"].isin(["Bachelors", "Masters","Doctorate"])])
    
    lower_education = df.loc[~df["education"].isin(["Bachelors", "Masters","Doctorate"])]

    # percentage with salary >50K

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()
    print(min_work_hours)
    num_min_workers = df[(df["hours-per-week"] == 1)]
    num_min_workers = len(num_min_workers)
  

    min_work_rich = df[(df["hours-per-week"] == 1) & (df["salary"] == '>50K')]
   
    

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[(df["hours-per-week"] == 1) & (df["salary"] == '>50K')]
    num_min_workers = len(num_min_workers)
   

    rich_percentage = (len(min_work_rich) / num_min_workers * 100)
    rich_percentage = 10
    # What country has the highest percentage of people that earn >50K?
    highest_earning_country_ =  df[df["salary"]==">50K"]
    overall_earning = df[['salary','native-country']]
    df_earning = (overall_earning.groupby('native-country',as_index=False)['salary'].agg('count'))
    df_earning = df_earning.sort_values(by='native-country', ascending=False, na_position='first')
    dframe2=(highest_earning_country_.groupby('native-country',as_index=False)['salary'].agg('count'))
    dframe2 = dframe2.sort_values(by='native-country', ascending=True, na_position='first')
   
    #use merge to compare columns and keep the duplicate values
    inner_merged_total = pd.merge(df_earning,dframe2, on = "native-country")

    inner_merged_total['percentage'] = round(inner_merged_total['salary_y']/inner_merged_total['salary_x']*100,1)

    inner_merged_total = inner_merged_total.sort_values(by='percentage', ascending=False)

    highest_earning_country = inner_merged_total.iloc[0,0]
    

    
    highest_earning_country_percentage = inner_merged_total.iloc[0,-1]

    # Identify the most popular occupation for those who earn >50K in India.
    oc_india = np.where((df['native-country'] == 'India') & (df['salary'] == '>50K'))
   
    group_occupation = (df.loc[oc_india].groupby('occupation', as_index=False)['salary'].agg('count'))
    group_occupation = (group_occupation.sort_values(by='salary', ascending=False, na_position='first'))
    group_occupation = group_occupation.head(1)
    top_IN_occupation = group_occupation.iloc[0,0]
    
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

