# This code is written in python
# The pandas library is used for data processing and to read data files

## -- IMPORT -- ##
import pandas as pd 
#The matplotlib library is used to plot histograms and scatter plots
import matplotlib.pyplot as plt
# The GWCutilities has functions to help format data printed to the console
import GWCutilities as util

# Read a comma separated values (CSV) files into a variable
# as a pandas DataFrame

## -- READING DATA -- ##
#If you wish change which data set you are working with, do that here: 
lwd=pd.read_csv("livwell135.csv")

# Add Step 1 code here:
listOfcountries = lwd["country_name"].unique()
# print(util.vformat_list(listOfcountries))

## -- DATA STORY -- ##
print()
print() # whitespace

print("Colombia is a country in Latin America with a population of over 51 million. Spanish is the main language there, but many indiginous languages are still present. \n")
print("Senegal is a country in West Africa with a population of over 18 million. With French and Wolof being major languages spoken there with many other regional ones present. \n")

print("We'll explore the well being of women in these two countries with data.\n")

input("Press enter to countinue.")

print("In Colombia and Senegal, women are both expected to deal with domestic and care work. In Senegal, this is deely rooted for as women are expected to marry in polygyny relationships, care of children, do domestic duties, farm for the house food, and dress modestly. \n")

input("Press enter to continue.")

print("In Colombia, one of women's expectations is to be beatiful. They take an active role in the workforce and the home. However, social divides can cause a women to have less financial autonomy. The workforce in Senegal, on the other hand, widely disadvantages women, but political representation by both genders is strong. \n")

input("Press enter to continue.")

print("Women in Colombia have, on average, over 8 years of education. In Senegal, women get less than 5 years of education on average. Now, with higher workforce representation in Colombia than in Senegal, there might be a correlation between years of education and women in paid work.")
print("Let's investigate the scatter plot to see this. \n")

input("Press enter to see the scatter plot.")

## -- DATA FROM KENYA -- ##
firstCountry = "Senegal"
firstCountryBooleanList = lwd["country_name"] == firstCountry
firstCountryData = lwd.loc[firstCountryBooleanList]

## -- DATA FROM COLOMBIA -- ##
secondCountry = "Colombia"
secondCountryBooleanList = lwd["country_name"] == secondCountry
secondCountryData = lwd.loc[secondCountryBooleanList]

# print(firstCountryData)

## -- PRINTING SCATTER PLOT(1) -- ##
plt.scatter(data = firstCountryData, x = "ED_educ_years_mean", y = "WK_working_paid_p", label = firstCountry) # Senegal
plt.scatter(data = secondCountryData, x = "ED_educ_years_mean", y = "WK_working_paid_p", label = secondCountry) # Colombia

# Labels, Limits, Lengend, and Show
plt.ylabel("% of Women Who Have Had Paid Work (Past 12 Months)")
plt.xlabel("Years of Education")
plt.ylim(0, 100)
plt.legend()
plt.show()

## -- ANALYZING SCATTER PLOT(1) -- ##
print("As we see, Colombia has a positive correlation between years of education and having paid work.")
print("Senegal also had this positive correlation at the start, however, there was a decrease at some point. \n")

print("We should look at this data further. \n")

input("Press enter to see the scatter plot.")

plt.cla()

## -- PRINTING SCATTER PLOT(2) -- ##
plt.scatter(data = firstCountryData, x = "year", y = "WK_working_paid_p", label = firstCountry)

plt.ylabel("% of Women Who Have Had Paid Work (Past 12 Months)")
plt.xlabel("Year")
plt.ylim(0, 100)
plt.show()

## -- ANALYZING SCATTER PLOT(2) -- ##
print("There seems to have been an event arount 2011 and 2014 that created a decrease of women having paid work.\n")

print("It is important to explore why this happened as financial autonomy decreases with a smaller presence in the workforce, and it seems that education can not guarantee higher workplace involvement for women.\n")

input("Press enter to see research questions.")

print("This bring this research question to mind:")
print("Is education not enough to bring women more job opportunites? What else can we do to promote and prepare women for the workplace? \n")

print("And to answer those questions, we need to figure out what happened in Senegal around 2011 that affect women getting a paid job?")
plt.cla()