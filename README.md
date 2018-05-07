# Oracle Solutions Engineer Project

## Collaborators

* [Daniel Brett](https://github.com/dbrett90)

## Project Scope and Goal

Using "anonymized" [Yelp data](https://www.kaggle.com/yelp-dataset/yelp-dataset/data) from Kaggle, I create an application that allows a user to input some auxiliary information to see if they can find a reviewer in the database. Please note that **due to github's restraint on file sizes, the file containing the actual yelp reviews could not be uploaded, please reference URL.**  This project was derived from work I had done for my senior thesis on Linkage Attacks and Modern Privacy Techniques and adapted to fit an oracle cloud container. I had initially hoped to utilize Oracle's analytics tools, but was unsuccessful. 

## Context
With the recent Cambridge Analytica scandal, users want to know how their information is being stored, released, and who has access to it. With my background in cybersecurity, I thought it would be an interesting exercise to see if I could de-anonymize a restaurant reviewer based on a small amount of auxiliary information. If successful, I would then write out the rest of that reviewers restaurant reviews to numbered text files. This exercise hopes to prove that the way potentially sensitive data is released online is flawed as potentially compromising information (i.e. a harsh review, revierer's location/habits) can be revealed.  

## Metadata and Associated Information 
Outlined below is some relevant information regarding the dataset(s). The information below was crucial in constructing quasi-identifier for the search algorithms.

**Figure 1. Dataset Column and Associated Attribute**

| Column Number     | Attribute      | 
| ------------- |:-------------:| 
| 0  | Review ID| 
| 1 | User ID   |  
| 2 | Business ID| 
|3 | Stars | 
|4 | Date|
|5 | Review Text|
|6 | Useful|
|7 | Funny|
|8 | Cool |

The table below outlines the difference in reviews after looking at all reviews versus just those about restaurants. It provides insight into the size of the dataset and how large the dataset is after preprocessing.


**Figure 2. Review Statistics**

| | Total Reviews | Number of Businesses | Unique Reviewers|
| ------------- |:-------------: | :-------------: | ------------- |
|**Entire Dataset**| 5200000|174000| 2500000|
|**After Filtering** |1804242|115242|902121|

## Scoring Algoritm

This program utilizes a scoring algorithm derived from a research paper about the [Netflix Prize](https://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pdf). In essence the scoring mechanism is predicated on two things, a similarity function and a weight vector. The weight vector was necessary in the creation of my thesis as we were considering mutliple reviews at the same time, but for this simple application it was relatively irrelevant. Therefore we only used the sim function, which was based on compatability between the auxiliary information and selected record. The attributes compared were restaurant name (must be direct match), rating (within 2 stars), and date (within a week). Using just these three fields as a quasi-identifier, I was able to successfully de-anonymize a given reviewer. 

## Challenges

Having never deployed a cloud application, there was definitely a learning curve when it came to integrating some of oracle's cloud projects with this small application. I ultimately settled on using one of Oracle's cloud containers to deploy the results of one of the experiments after tinkering with some of the data visualization tools and failing to get a working product. 

## Applications

This brief application was intended to demonstrate my technical skillset and to showcase my background in security. It also provides insight into the how our current definition of "privacy" and "anonymity" is flawed. Using information that is not uniquely identifying information, I am able to de-anonymize a given reviewer. This code is meant to showcase privacy flaws in lieu service.


