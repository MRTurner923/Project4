# Project4
TripleTen Project 4: Software Development Tools

https://project4-oyq4.onrender.com

For this project I'll be analyzing the vehicles_us dataset. I'll be looking to answer 4 questions from this dataset:

1: Do 4WD vehicles sell faster than non-4WD vehicles?

2: What color cars sell for the most on average?

3: Do sedans/coupes with high mileage sell for more than SUV's/trucks with high mileage?

4: How does a vehicle's manufacturer affect it's resale price?

Assumptions made for this analysis is that the price is in USD, "high mileage" is any odometer reading over 100,000 miles, and that every car was sold on the last day it was listed (highest possible days_listed value), and that the alpha for all statistical tests is 0.05.

1. Comparison of 4WD vs Non-4WD Vehicle Sale Time

Null hypothesis: 4WD and Non-4WD vehicles have the same average vehicle sale time

Alternative hypothesis: 4WD and Non-4WD vehicles do not have the same average vehicle sale time

Based on the t-test of this data set, the p-value is 0.649, greater than our alpha of 0.05, therefore, we cannot reject the null hypothesis for this test.

2. Comparison of Average Sale Prices of Vehicles Based on Paint Color

Null hypothesis: Car paint color does not affect average vehicle sale price

Alternative hypothesis: Car paint color does affect average vehicle sale price

Based on the ANOVA of this data set, the p-value is << 0.001, therefore, the null hypothesis is rejected.

3. Comparison of Average Sale Prices of High Mileage Sedans/Coupes vs Pickup Trucks/SUVs

Null hypothesis: High mileage sedans and coupes have the same average sale price as high mileage pickup trucks and SUVs

Alternative hypothesis: High mileage sedans and coupes do not have the same average sale price as high mileage pickup trucks and SUVs

Based on the t-test for this dat set, the p-value is <<0.001, therefore, this null hypothesis is also rejected.

4. Comparing Resale Price by Vehicle Manufacturer

Null hypothesis: The manufacturer of a vehicle has no impact on the resale price of that vehicle

Alternative hypothesis: The manufacturer of a vehicle does have an impact on the resale price of that vehicle

Based on the ANOVA of this data set, the p-value is <<0.001, and this null hypothesis is also rejected.

# Conclusions
After analyzing and performing different comparisons on this data set, I would conclude, almost obviously, that there are a large number of factors that would affect the resale price of a vehicle. Most are listed in the data and give a very comprehensive coverage of what could be the reason a vehicle was sold for the price it was. Some factors I'd be interested in looking at is owner history, smoker/non-smoker vehicle, number of accidents, if the vehicle had a rebuilt title or not, and what state the vehicle was sold in. I think all of these would paint an even clearer picture of the resale value of each vehicle, and comparing them all would be a lengthy, but probably worthwhile, process. From the specific tests I performed, I was surprised at only one of the results; analysis 1. From my own car buying experiences, I would always prefer a 4WD vehicle and found it difficult to find the make/model of a vehicle I wanted in the 4WD option, so I thought that 4WD vehicles must be sold faster than non-4WD vehicles. At least from this data set, that doesn't appear to be the case, but again, I have been shopping for cars in Chicago where we get 6 months of winter and 4WD is almost a necessity to get through the snow and ice safely, so that could be a personal bias. It's no secret that a majority of cars on the road today are black, gray, white, and silver, but I didn't suspect that cars of a different color necessarily sold for a higher/lower price than others. Analysis 3 was also not a surprise, as someone who has purchased 2 vehicles, a sedan and an SUV (black and white, respectively, to reiterate my earlier point), I knew that SUV's and pickup trucks generally come with a larger price tag than their sedan/coupe counterparts. Evening the playing field for high mileage instances of each type of interest here, I was again expecting the SUV's and trucks to continue to hold their resale value higher than sedans and coupes, and yet again, the data presented here supported my thought process. Finally, comparing resale price by manufacturer. It again, should come as no surprise that the manufacturer of a vehicle plays a part in how much that vehicle initially sells and even resells for. There were not a ton of instances of the luxury car brands in this dataset, but those that were seemed to typically be higher on average. It is worth noting, however, there were a few American brands with very high sale values in the dataset, and further investigation into those revealed they were some American classic cars that are much rarer now than when they were originally produced, so it makes sense that in good condition, these vehicles would sell for large amounts of money.
