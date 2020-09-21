# Pandemic-Aware Local Recommendation

## Dataset Information
**List of files**
```tex
Customer_Choice_Survey.csv
NYC_Google.csv
NYC_Yelp.csv
SF_Google.csv
SF_Yelp.csv
```
**Field Details in Each File**
* **"Customer_Choice_Survey.csv"**
Each respondent was first asked some basic details. Then 7 rounds of ranking questions were asked. In each round, they were given a list of 10 restaurants with random combinations of rating, distance and cuisine. They were asked to rank top 5 one-by-one out of those 10 provided. This becomes evident from the question titles provided the file.
* **"NYC_Google.csv" and "SF_Google.csv"**
```tex
"customer_location": location of the customer where she gets recommendation
"rank": rank of the restaurant in the recommended list
"id": restaurant's id internal to google
"latitude": latitude of restaurant's geographic coordinates
"longitude": longitude of restaurant's geographic coordinates
"name": name of the resturant
"price_level": cheap/costly level
"rating": average rating of the restaurant
"rating_count": number of ratings collected for the restaurant
"address": address of the restaurant
```
* **"NYC_Yelp.csv" and "SF_Yelp.csv"**
```tex
"customer_location": location of the customer where she gets recommendation
"rank": rank of the restaurant in the recommended list
"id": restaurant's id internal to yelp
"latitude": latitude of restaurant's geographic coordinates
"longitude": longitude of restaurant's geographic coordinates
"name": name of the resturant
"rating": average rating of the restaurant
"rating_count": number of ratings collected for the restaurant
"address": address of the restaurant
"url": link to the restaurant's yelp page
```
## Citation Information
Citation Information:
Please cite the following paper if you use this dataset.<br>

* **"Towards Sustainability and Safety: Designing Local Recommendations for Post-pandemic World"**<br>
Gourab K Patro, Abhijnan Chakraborty, Ashmi Banerjee, Niloy Ganguly.<br>
In proceedings of Fourteenth ACM Conference on Recommender Systems (RecSys-2020), Virtual Event, Brazil.<br>

Or you can also use the following bibtex.
```tex
@inproceedings{10.1145/3383313.3412251,
author = {Patro, Gourab K and Chakraborty, Abhijnan and Banerjee, Ashmi and Ganguly, Niloy},
title = {Towards Safety and Sustainability: Designing Local Recommendations for Post-Pandemic World},
year = {2020},
isbn = {9781450375832},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3383313.3412251},
doi = {10.1145/3383313.3412251},
booktitle = {Fourteenth ACM Conference on Recommender Systems},
pages = {358–367},
numpages = {10},
keywords = {COVID-19, Local Recommendation, Google Local, Yelp, Safety, Social Distancing, Sustainability, Bipartite Matching},
location = {Virtual Event, Brazil},
series = {RecSys '20}
}
```
