READ ME - Recommender system of plant species that contribute to biodiversity

#1. 
The programming language used is Python3. 
There are 8 files. 6 files are for collecting and cleaning the data. These are the .py files. These files can be read in an intergrated development environment like Visual Studio Code.

2 files are different iterations of the recommender system. These are the .ipynb files. These files are Jupyter Notebook and can be read under Jupyter.

The .py files related to the recommender system are:
- scrape_url.py
- properties.py
- maintenance.py
- clean.py
- rs.py

The .py file containing the garden accessories is:
- garden_accessories.py


#2. Libraries that need to be installed:
- import time
- import requests
- import pandas
- from bs4 import BeautifulSoup
- from sklearn.feature_extraction.text import TfidfVectorizer
- from sklearn.metrics.pairwise import cosine_similarity
- from IPython.display import Image

#3. How to run the code?
#3.1 .py files 
To run the recommender system properly, please run first the .py files in the following order:
1. scrape_url.py
2. properties.py
3. maintenance.py
4. clean.py
5. rs.py

#3.2 .ipynb files 
You do not need to run the file to view the outcomes. If you do want to run the file please keep the following in mind. Both .ipynb files ask for input to run the code. This is similar to the input requested from the user, that is, the plant species the user already has in their garden, the characteristics of their garden, and the user's criteria. The input MUST match collected data (values) that are in the database (CSV file). For support in entering correct input, examples are printed out at the same time. The inputs that can be entered are repeated below.

#3.2.1 Iteration 1 - Garden plants Recommender system.ipynb
You will be asked for input at 1.3 Create user profile.
First, it asks for a number that indicates how many plants the user has in their garden. For example, enter 3.
Then you will be asked to enter a plant species name as many times as the digit you entered before this.
For example: 
First, enter "Pontische Rododendron Rhododendron ponticum Roseum"
Then "Blauwe regen Wisteria sinensis Boskoop"
Finally "Franse lavendel Lavandula stoechas subsp pedunculata".

#3.2.2 Iteration 2 - Garden plants Recommender system.ipynb
You will be asked for input at 2.1 Create user profile, 2.2 Create garden profile, and 2.3 Collect user criteria.

# CREATE USER PROFILE
First, it asks for a number that indicates how many plants the user has in their garden. For example, enter "3".
Then you will be asked to enter a plant species name as many times as the digit you entered before this.
For example: 
First, enter "Pontische Rododendron Rhododendron ponticum Roseum"
Then "Blauwe regen Wisteria sinensis Boskoop"
Finally "Franse lavendel Lavandula stoechas subsp pedunculata".

# CREATE GARDEN PROFILE
First, you will be asked about the sun exposure of the user's garden.
For example, enter "Halfschaduw"

Second, you will be asked about the soil moisture of the user's garden.
For example, enter "Vochthoudend"

# COLLECT USER CRITERIA
First, it asks for a number that indicates how many criteria the user finds important. For example, enter "2".
You will then be asked to enter the criteria name (column name) and the desired value of these criteria (value) as many times as the number you entered for this purpose. This means that if you have indicated that the user finds n criteria important, you will have to enter n*2 an input.
For example: 
First, enter "Type"
Then "Borderplanten"
Then "Bees"
Finally "Bijen".

