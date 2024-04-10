# CMSE202-Final-Project
Spring Semester 2024, Sectoin 001, Dr. Yang
Group 7: Infrastructure & Urban Planning 2

Group Members:
Matt Gagea, Tiffany Rennells, Marco Abat, Brendan Hunt

Abstract:

Public transportation is typically a staple part of a quality-of-life assessment of a major city. Detroit is unique in this sense due to the fact that much of its economy and function revolves around automobiles. This reliance perservered, even when the automobile industry slowly started to leave the city, resulting in the gradual loss of over 150,000 industry jobs. This came to a peak in 2013 when Detroit became the largest city ever to declare bankruptcy in the United States (1). Fortunately, since then, the Detroit economy has been on a steady incline. Transportation-related infrastructure for the metro-detroit area, however, has been consistently mediocre. Outside of the bus systems, there is a single elevated rail system that makes rounds within the downtown area, however, it is plauged by an innefficient route and low-ridership. The consequences of this lacking transportation system have been felt; In 2016, there were 24.7% of households in the metro Detroit area that lacked a car. This is much higher than the national average of 8.7% per city (2). Our project aims to offer a solution to the current shortcomings of the Detroit public transportation network: By calculating population densities across designated census tracts (3), plotting nodes in communities that are in need of transportation, and connecting these nodes using different algorithms, we have designed a subway system that is accessible to both Detroit and its surrounding suburbs.

Sources:

(1) "Detroit bankruptcy officially over, finances handed back to the city". WXYZ. December 10, 2014. Archived from the original on March 4, 2016.

(2) Maciag, Mike (December 9, 2014). "Vehicle Ownership in U.S. Cities Data and Map". Governing. Archived from the original on January 15, 2024.

(3) https://app-simplyanalytics-com.proxy2.cl.msu.edu/index.html

How to Run the Code: 

Older versions of our code can be accessed in the "legacy" folder.

the text file, variable_names.txt, contains the names of the variables and what they represent. Its contents are as follows:

VALUE0	% Transportation to Work | Public transportation, 2023
VALUE1	% Transportation to Work | Bicycle, 2023
VALUE2	% Transportation to Work | Walked, 2023
VALUE3	% Transportation to Work | Car, truck, or van, 2023
VALUE4	# Housing Units, 2023
VALUE5	# Vehicles Available | Occupied housing units, 2023
VALUE6	# Vehicles Available | No vehicle available, 2023
VALUE7	# Housing Occupancy Status | Occupied, 2023
VALUE8	Median Household Income, 2023
VALUE9	# Total Population, 2023

The code for all of the objects is in the file titled Public_Transit_System.ipynb. Our objects are as follows: Block_Group, City, Superblock, and Train.

The City object simply defines the boundaries of the city & the confines in which we are designing our system. The Block_Group object is used to separate areas of the city into block groups based off of population, and the Superblock object takes a certain amount of block groups and creates a "Superblock" out of them, which is simply a a grouping of block groups that we can then place a node either in or around. Our Train object is used to connect the superblocks using the nodes we placed. All of this code is gathered and used in our Main_Project file.

Designated tasks for each group member:

Tiffany - Used elements of the Folium package to edit our City map and object, and placed the nodes on the map using both Geopandas and Folium

Brendan - Working with folium to create the block groups and superblocks. The code was adjusted multiple times to account for area of superblocks, populations in each superblocks, and optimal locations for a subway station.

Matt - Creating algorithms to optimize train routes between nodes. Referenced the Washington, DC subway system in order to design the most sensible and convenient subway system in terms of number of stops and distance between nodes. 

Marco - Creating a Geopandas map + Alternative mapping, utilizing Latitude and Longitude in order to create the simplest and most flexible map. Wrote the README file as well.

The presentation was designed and created by all group members.
