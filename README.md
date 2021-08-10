# Surfs_Up

# Overview
An analysis of weather data to support investing in a surf and shake shop in Oahu, Hawaii.

## Purpose
A prospective investor, W. Avy, is concerned about the amount of precipitation in Oahu and wants to see a full year of data analyzed starting August 23, 2017. The purpose of this analysis is to provide W. Avy with insight into the weather patterns of a specific location on Oahu where you would like to build your shop. 

## Resources

## Data Files
hawaii.sqlite
climate_analysis.ipynb

## Programming Software
- SQLite was used as a quick way to setup a database engine locally on my computer without requiring a server--used to support testing and easy prototyping. SQLite databases can be used on a mobile phone app to store certain information about you or your local users; however there are no remote users with fewer security features. Dependencies included SQLAlchemy.  
- VS Code was used to create a Flask application. 
- Jupyter Notebook is used to write, execute code and create graphs using Python. Dependencies included Matplotlib (fivethirtyeight style), NumPy, Pandas and DataTime.
- GitHub was used to store the code.

# Results
Precipitation Analysis - This data gives us a summary of different statistics for the amount of precipitation in a year. The count is the number of times precipitation was observed. The other statistics are the precipitation amounts for each station for each day.

Weather Station Analysis - The results show that the low (minimum) temperature is 54 degrees, the high (maximum) temperature is 85 degrees, and the average temperature is approximately 71.7 degrees. Looking at this plot, we can infer that a vast majority of the observations were over 67 degrees. If you count up the bins to the right of 67 degrees, you will get about 325 days where it was over 67 degrees when the temperature was observed.

# Summary