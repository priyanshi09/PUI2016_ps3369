# Assignment1

In this assignment, I plotted the histogram for the age distribution. I learned various concepts from google(stackoverflow), like fitting data to Un-Normalised Gaussian distribution and plotting with histograms. Read about the one sample KS Test and Anderson-Darling Test, understood the interpretation of results.

For the other Distributions i took help from Vishwajeet, as i faced a problem while fitting data with some other distribution.


# Assignment2

I did the assignment by myself.

1) I created two dictionaries( male and female) and fetched dataframes from different Excel files to these dictionaries.

2) I tried to plot a few columns using scatter_matrix where i was unable to obtain the graphs for columns with non-real values. Hence i cleaned the data(eg. removing NaN values, converting non-real values to real values). I plotted data for males and females again to see the expected result.

3) I collected the Total Median Income for male and female and plotted it to analyse the comparison race by race. Also plotted line with equal pay of male and females.

4) I fit the data with a line on the plot, then using OLS regression model and obtained the parameters like slope, intercept etc. I used analytical solution as well to obtain the values of beta0, beta1. Again i plotted the analytical solution and regression line to scompare the results.

5) Then I worked with all types of median incomes and followed the same apprroac to obtain a graph with analytical solution, regression line, distribution of all types median incomes for males and females and 'same pay' as well.

6) Observed the data and predicted the female stipend by picking up any stipend value and using OLS regression model.

7) Lastly I analysed the total median incomes of all the races.

For Assignment 2, I helped Akshay with some minor suggestions in curve fitting and using regression.

# Assignment 3: Practice formulating the null hypothesis:

I worked individually on this and then discussed it with the group( Aaron, Vishwajeet, Achilles, Anastasia).

### 1)  - Do diets help lose more fat than the exercise?

Significance Level - 0.05 or 5%

#### Null Hypothesis: The mean weight lost of the population(test sample) that was exercising is greater than or equal to the mean weight lost of the population(control sample) that was dieting.

H0:  Mean_W(exercise) >= Mean_W(diet)

#### Alternate Hypothesis:  The mean weight lost of the population(test sample) that was exercising is less than or equal to the mean weight lost of the population(control sample) that was dieting.

H1: Mean_W(exercise) < Mean_W(diet)


### 2) - Do American trust the president?

POLL RESULTS: On May 16, 1994, Newsweek reported the results of a public opinion poll that asked: “From everything you know about Bill Clinton, does he have the honesty and integrity you expect in a president?” (p. 23).Poll surveyed 518 adults and 233, or 0.45 of them answered yes.

Significance Level - 0.05 or 5%

#### Null Hypothesis: The percentage of the American population that trusts the president is greater than or equal to the percentage of the American population that does not trust the president

H0:  Percentage(Trust) >= Percentage(Doesn'tTrust)

#### Alternate Hypothesis: The percentage of the American population that trusts the president is lesser than the percentage of the American population that does not trust the president

H1:  Percentage(Trust) < Percentage(Doesn'tTrust)


### 3) - Effectiveness of nicotine patches to quit smoking. 

Experimental setup: measure cessation rates for smokers randomly assigned to use a nicotine patch versus a placebo patch.

Significance Level - 0.05 or 5%

#### Null Hypothesis:  The Cessation rate for smokers using nicotine patch is less than or equal to the Cessation rate for smokers using the placebo patch.

H0:   Cessation Rate(Nicotine) <= Cessation Rate(Placebo)

#### Alternate Hypothesis: The Cessation rate for smokers using nicotine patch is greater than the Cessation rate for smokers using the placebo patch.

H1:  Cessation Rate(Nicotine) > Cessation Rate(Placebo)


### 4) - Quantify the danger of smoking for pregnant women. 

Experimemtal setup: measure IQ of children at ages 1, 2, 3, and 4 years of age.

Significance Level - 0.05 or 5%

#### Null Hypothesis: The mean IQ of children at ages 1,2,3 and 4 whose mother smoked during pregnancy is greater than the mean IQ of children at ages 1,2,3 and 4 whose mother did not smoke during pregnancy.

H0:  Mean(IQ at ages 1,2,3 and 4)Smoked > Mean(IQ at ages 1,2,3 and 4)NotSmoked

#### Alternate Hypothesis: The mean IQ of children at ages 1,2,3 and 4 whose mother smoked during pregnancy is greater than the mean IQ of children at ages 1,2,3 and 4 whose mother did not smoke during pregnancy.

H1:  Mean(IQ at ages 1,2,3 and 4)smoked <= Mean(IQ at ages 1,2,3 and 4)NotSmoked
