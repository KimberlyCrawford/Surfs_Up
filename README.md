# Surfs_Up

# Overview
An analysis of weather data to support investment in a surf and shake shop in Oahu, Hawaii.

## Purpose
A prospective investor, W. Avy, is concerned about the amount of precipitation in Oahu and wants to see a full year of data analyzed starting August 23, 2017. The purpose of this analysis was to provide W. Avy with insight into the weather patterns of a specific location on Oahu to build a shop. 

### Challenge: 
Additional temperature trends for the months of June and December were given to determine if the surf and ice cream shop business is sustainable year-round and would be a good investment. 

## Resources

### Data Files: 
hawaii.sqlite, climate_analysis.ipynb

### Programming Software:
- SQLite was used as a quick way to setup a database engine locally on my computer without requiring a server--used to support testing and easy prototyping. SQLite databases can be used on a mobile phone app to store certain information about you or your local users; however there are no remote users with fewer security features. Dependencies included SQLAlchemy.  
- VS Code was used to create a Flask application as Flask does not work with Jupyter Notebook. Flask was used to share the results with others via a webpage. 
- Jupyter Notebook is used to write, execute code and create graphs using Python. Dependencies included Matplotlib (fivethirtyeight style), NumPy, Pandas and DataTime.
- GitHub was used to store the code.

# Results
Precipitation Analysis - This data gives us a summary of different statistics for the amount of precipitation in a year. The count is the number of times precipitation was observed. The other statistics are the precipitation amounts for each station for each day.

Weather Station Analysis - The results show that the low (minimum) temperature is 54 degrees, the high (maximum) temperature is 85 degrees, and the average temperature is approximately 71.7 degrees. Looking at this plot, we can infer that a vast majority of the observations were over 67 degrees. If you count up the bins to the right of 67 degrees, you will get about 325 days where it was over 67 degrees when the temperature was observed.

# Challenge Summary

The following summary describes the key differences in weather between June and December and two recommendations for further analysis.

## Challenge Results: 
Summary Statistics for June
- Point 1
- Point 2
- Point 3

Summary Statistics for December
- Point 1
- Point 2
- Point 3

## Recommendations for Further Analysis: 
- Query 1 - Additional query to perform to gather more weather data for June and December.
- Query 2 - Additional query to perform to gather more weather data for June and December.