# Oracle Solutions Engineer Project

## Collaborators

* [Daniel Brett](https://github.com/dbrett90)

## Project Scope and Goal

Using "anonymized" [Yelp data](https://www.kaggle.com/yelp-dataset/yelp-dataset/data) from Kaggle, I create an application that allows a user to input some auxiliary information to see if they can find a reviewer in the database. Please note that **due to github's restraint on file sizes, the file containing the actual yelp reviews could not be uploaded.** However, I have uploaded a smaller version of the file so that this code can be executed. However, please note that the following sections are based on the original file size. This project was derived from work I had done for my senior thesis on Linkage Attacks and Modern Privacy Techniques and adapted to fit an oracle cloud container and to utilize some of Oracle's cloud analytics tools. 

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

## Challenges

Having never deployed a cloud application, there was definitely a learning curve when it came to integrating some of oracle's cloud projects with this small application. However, the nice thing about this dataset was that its inherent sparseness allowed for easy scoring using a scoring algorithm derived from a research paper about the [Netflix Prize](https://www.cs.utexas.edu/~shmat/shmat_oak08netflix.pdf). This is what allowed for proper scoring of each search query and to determine if a match was present in the database. 

## Applications

This brief application was intended to demonstrate my technical skillset and to showcase my background in security. It also provides insight into the how our current definition of "privacy" and "anonymity" is flawed. Using information that is not uniquely identifying information, I am able to de-anonymize a given reviewer. 


