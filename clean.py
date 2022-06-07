# Import needed library
import pandas as pd

#Import CSV to avoid scraping again
df_url = pd.read_csv("url_animalspecies.csv")
df_prop = pd.read_csv("properties_maintenance.csv")

# Create new dataframe based on all scrapped data
df_prop = pd.concat([df_prop, df_url], axis=1)

# Rename usefull columns
df_prop.rename(columns = {'Maximale groeihoogte (in CM):':'Plant growth', 'Wintergroen?:':'Evergreen', 'Bloeimaand:':'Flowering period', 'Vochtigheid grond:':'Soil moisture', 'Positie in de tuin:':'Sun exposure', 'Bladkleur:':'Leaf color', 'Bloemkleur:':'Flower color'}, inplace = True)

# Fix scraping errors: 
# Replace 'Tuin thema's en Meer' by 'Heesters en Struiken' because this is the correct type of all the plants in question
df_prop.loc[df_prop["Type"] =="Tuin thema's en Meer", "Type"] = "Heesters en Struiken"

# Replace value by correct Type
df_prop.at[913 , 'Type'] = 'Borderplanten'
df_prop.at[517 , 'Type'] = 'Borderplanten'

# Add plant name when missing
df_prop.at[516, 'Plant name'] = 'Moeraseik'
df_prop.at[517, 'Plant name'] = 'Moerassperia'
df_prop.at[51, 'Plant name'] = 'Camelia'
df_prop.at[54, 'Plant name'] = 'Chinese Hazelaar'
df_prop.at[839, 'Plant name'] = 'Vossebes'
df_prop.at[871, 'Plant name'] = 'Witte druif'


#Drop columns that are not needed
df_prop = df_prop.drop(['Nederlandse naam:','Geslacht:','Type tuin :', 'Snoeiperiode:', 'Giftig:', 'Groeiwijze klimplant:', 'Bijvriendelijk:', 'Ondersteuning klimplant:', 'Haagplanten per strekkende meter:', 'pH waarde:', 'Stekels:', 'Planttijd:', 'Voeding / Bemesting:', 'Voeding periode:', 'Plantenfamilie:', 'Plantdichtheid Aantal planten per m2:', 'Unnamed: 0', 'Soort bodem:', 'Plantnummer:', 'winterhard:', 'Wat voor soort grond past erbij?:'], axis=1)

# Reindix column position
df_prop = df_prop.reindex(['Name','Type','Birds','Bees','Butterflies', 'Hedgehogs', 'Squirrels', 'Flowering period', 'Leaf color', 'Flower color', 'Evergreen', 'Plant growth', 'Sun exposure', 'Soil moisture', 'Maintenance', 'Maintenance description', 'Photo'], axis=1)

# Create a CSV file from the dataframe
df_prop.to_csv("properties.csv")

# Message when cleaning is finished
print("End of cleaning")

