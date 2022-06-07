# Import needed library
import time # puts a break between each request
import requests # requests page
import pandas as pd
from bs4 import BeautifulSoup # Scrapping library

base_url = "https://www.yarinde.nl/" #the url of the website Yarinde


# PLANTS FOR ANIMAL SPECIES: scrapes pages
# Scrape name of plant species for the creation of URL
def scrape_url(url):
    page = requests.get(url, ) #use requests to get the page via HTTP
    html = BeautifulSoup(page.content, "html.parser") #page.content is the HTML file, with parser it is read as HTML
    
    descr_html = html.find_all(class_="productblock__heading") # get the name of plant species
    photo_html = html.find_all(class_='productblock__image')
    descr_list = [] # list for the name of plant species
    photo_list = [] # list for the photos of plant species
    
    #loop over HTML elements, get text and add to list   
    for i in descr_html:
        text = i.text.strip() #use .strip() string method to remove whitespace
        text = ' '.join(text.split())
        # Spaces are replaced by -
        text = text.replace(' ', '-')
        # Symboles are removed
        text = text.replace("'", '')
        text = text.replace(".", '')
        text = text.replace("(", '')
        text = text.replace(")", '')
        text = text.replace("/", '')
        text = text.replace("‘", '')
        text = text.replace("’", '')
        text = text.replace("&", '')
        text = text.replace("--", '')
        descr_list.append(text)

    for i in photo_html:
        # Get the source link of all images of the plant species
        text = [link['src'] for link in i.find_all('img')]
        photo_list.append(text)
    
    # make a dictionary with column names for data to put in DataFrame   
    data = {"Name": descr_list,
            "Photo": photo_list}
   
    df = pd.DataFrame(data)   # make a dataframe
    return df

df_url = pd.DataFrame() # create an empty dataframe

# BIRDS, there are 11 pages
for i in range(11):
    time.sleep(1)
    url_page = str(base_url+"vogelvriendelijke-tuinplanten/?page=") + str(i+1) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_url(url_page) #use scrape_page function to get df for the page
    df_page["Birds"] = "Ja" # indicates for each plant species that they are interesting for birds
    df_url = pd.concat([df_url, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index.

# BEES, there are 11 pages
for i in range(11):
    time.sleep(1)
    url_page = str(base_url+"bijvriendelijke-tuinplanten/?page=") + str(i+1) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_url(url_page) #use scrape_page function to get df for the page
    df_page["Bees"] = "Ja" # indicates for each plant species that they are interesting for bees
    df_url = pd.concat([df_url, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index.

# BUTTERFLIES,there are 12 pages
for i in range(12):
    time.sleep(1)
    url_page = str(base_url+"vlinder-lokkers/?page=") + str(i+1) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_url(url_page) #use scrape_page function to get df for the page
    df_page["Butterflies"] = "Ja" # indicates for each plant species that they are interesting for butterflies
    df_url = pd.concat([df_url, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index. 

# HEDGEHOGS, there are 2 pages
for i in range(2):
    time.sleep(1)
    url_page = str(base_url+"egelvriendelijke-tuinplanten/?page=") + str(i+1) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_url(url_page) #use scrape_page function to get df for the page
    df_page["Hedgehogs"] = "Ja" # indicates for each plant species that they are interesting for hedgehogs
    df_url = pd.concat([df_url, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index. 

# SQUIRRELS
for i in range(1):
    time.sleep(1)
    url_page = str(base_url+"eekhoorn-in-de-tuin/?page=") + str(i+1) #create the final url for the page. Note range starts at 0, so i+1
    df_page = scrape_url(url_page) #use scrape_page function to get df for the page
    df_page["Squirrels"] = "Ja" # indicates for each plant species that they are interesting for squirrels
    df_url = pd.concat([df_url, df_page], ignore_index=True) #concatenate the total df and page df. ignore_index resets index. 
    


#Groupby duplicated plants in one row
df_url = df_url.groupby("Name").first().reset_index()

#Drop Borderplan as these are not plant species
df_url = df_url[df_url["Name"].str.contains("Borderplan")==False].reset_index()
df_url = df_url.drop(['index'], axis=1)

# Change incorrect URLs by hand
df_url.at[29, 'Name'] = 'bloemwilg-itea-virginica-henry-s-garnet'
df_url.at[49, 'Name'] = 'rode-bruine-beukenhaag-fagus-sylvatica'
df_url.at[53, 'Name'] = 'cheal-treurkers-prunus-serrulata-kiku-shidare-zakura'
df_url.at[65, 'Name'] = 'daglelie-hemerocallis-chloe-s-child'
df_url.at[95, 'Name'] = 'duizendblad-achillea-filipendulina-parker-s-variety'
df_url.at[116, 'Name'] = 'duizendknoop-persicaria-filiformis-painter-s-palette'
df_url.at[137, 'Name'] = 'escallonia-c-f-ball'
df_url.at[139, 'Name'] = 'europese-larix-decidua'
df_url.at[197, 'Name'] = 'gele-dovenetel-lamiastrum-galeobdolon-herman-s-pride'
df_url.at[245, 'Name'] = 'gewoon-vingerhoedskruid-digitalis-purpurea-sutton-s-apricot'
df_url.at[276, 'Name'] = 'hemdsknoopjes-achillea-ptarmica-perry-s-white'
df_url.at[282, 'Name'] = 'aster-novae-angliae-barr-s-blue'
df_url.at[283, 'Name'] = 'aster-novae-angliae-barr-s-pink'
df_url.at[284, 'Name'] = 'aster-novae-angliae-harrington-s-pink'
df_url.at[293, 'Name'] = 'wilde-hortensia-hydrangea-arborescens-annabelle'
df_url.at[332, 'Name'] = 'japanse-sleutelbloem-primula-japonica-miller-s-crimson'
df_url.at[338, 'Name'] = 'japanse-kardinaalsmuts-euonymus-fortunei-emerald-n-gold'
df_url.at[372, 'Name'] = 'kattenkruid-nepeta-plantenmat-kant-en-klaar/'
df_url.at[408, 'Name'] = 'kogeldistel-echinops-bannaticus-taplow-blue'
df_url.at[432, 'Name'] = 'kruipend-zenegroen-ajuga-reptans-catlin-s-giant'
df_url.at[443, 'Name'] = 'kruiptijm-thymus-praecox-hall-s-variety' 
df_url.at[481, 'Name'] = 'longkruid-pulmonaria-longifolia-e-b-anderson'
df_url.at[509, 'Name'] = 'tweestijlige-meidoorn-crataegus-laevigata-paul-s-scarlet'
df_url.at[537, 'Name'] = 'oosterse-klaproos-papaver-orientale-perry-s-white'
df_url.at[568, 'Name'] = 'kant-en-klaar-pyracantha-scherm-155x120'
df_url.at[611, 'Name'] = 'rode-zonnehoed-echinacea-purpurea-kim-s-knee-high'
df_url.at[612, 'Name'] = 'echinacea-purpurea-kims-mop-head'
df_url.at[625, 'Name'] = 'rododendron-rhododendron-cunningham-s-white'
df_url.at[636, 'Name'] = 'rododendron-rhododendron-vuyk-s-rosyred'
df_url.at[842, 'Name'] = 'kniphofia-nancys-red'
df_url.at[857, 'Name'] = 'origanum-vulgare-thumble-s-variety'
df_url.at[881, 'Name'] = 'tanacetum-robinson-s-red'
df_url.at[882, 'Name'] = 'tanacetum-robinson-s-rose'
df_url.at[906, 'Name'] = 'zonnebloem-helianthus-atrorubens-gullick-s-variety'
df_url.at[909, 'Name'] = 'zonnebloem-helianthus-decapetalus-soleil-d-or'
df_url.at[922, 'Name'] = 'zonneroosje-helianthemum-lawrenson-s-pink'


#Create a CSV file from the dataframe
df_url.to_csv("url_animalspecies.csv")

#Message when scraping is finished
print("End of scraping URL")

