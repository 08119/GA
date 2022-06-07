# Import needed library
import scrape_url # import scrape_url because it contains the df and base_url
import time # puts a break between each request
import requests # requests page
import pandas as pd
from bs4 import BeautifulSoup # Scrapping library

# /!\ Scrapping properties can take several hours /!\
def scrape_prop(url):
    page = requests.get(url, ) #use requests to get the page via HTTP
    html = BeautifulSoup(page.content, "html.parser") #page.content is the HTML file. By using the HTML parser we read it as HTML
    
    prop_html = html.find_all('td') #get all the properties
    type_html = html.find_all(class_='link dark d-inline order-sm-1') #get the type of plant
    prop_list = [] # make list for all the properties 
    type_list = [] # make list for the type of plant

    #loop over HTML table, get properties and add to list 
    for i in prop_html:
        title = i.text
        prop_list.append(title)
    
    #loop over HTML element, get type of plant and add to list 
    for i in type_html:
        title = i.text
        type_list.append(title)

    # Get only the property names (futur colomn names)
    data_columns = [v for i, v in enumerate(prop_list) if i % 2 == 0] # keeps the values of the even positions
    # Get only the property values (futur values of rows)
    data_values = prop_list[1::2] #keeps the values of the odd positions

    # Create a list of lists from 2 lists (data_columns and data_values)
    data_list=[list(a) for a in zip(data_columns, data_values)] 
    # Create a dictionary, columns name on [0], values on [1], in order to make df
    data_dict = {i[0] : i[1] for i in data_list} 
    
    # Create df with all properties
    df = pd.DataFrame([data_dict])

    # Add Type of plants to df
    df["Type"] = type_list[2]
    
    return df

df_prop = pd.DataFrame()

# Scrape for all plant species scrapped in scrape_url.py
for i in scrape_url.df_url['Name']:
    time.sleep(1)
    url_page = scrape_url.base_url + str(i) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_prop(url_page) #use scrape_page function to get df for the page
    df_prop = pd.concat([df_prop, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index.

#Create a CSV file from the dataframe
df_prop.to_csv("properties_plantspecies.csv")

#Message when scraping is finished
print("End of scraping Properties")
