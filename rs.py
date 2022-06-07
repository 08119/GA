# Import needed library
import pandas as pd

# Import CSV with cleaned data
df_rec = pd.read_csv("properties.csv")

# Cleaning for recommender system
# Flowering period: Delete comma
df_rec['Flowering period'] = df_rec['Flowering period'].str.replace(',','')

# Plant growth, only keep the highest values
df_rec["Plant growth"] = df_rec["Plant growth"].str.split('\, ').str[-1].str.strip()
df_rec["Plant growth"] = df_rec["Plant growth"].str.split('\-').str[-1].str.strip()

# Photo URL, remove everything except URL
df_rec['Photo'] = df_rec['Photo'].map(lambda x: str(x)[2:])
df_rec['Photo'] = df_rec['Photo'].map(lambda x: str(x)[:-2])

# Create unique values: Replace animal species
df_rec['Birds'] = df_rec['Birds'].str.replace('Ja','Vogels')
df_rec['Birds'] = df_rec['Birds'].fillna('GeenVogels')
df_rec['Bees'] = df_rec['Bees'].str.replace('Ja','Bijen')
df_rec['Bees'] = df_rec['Bees'].fillna('GeenBijen')
df_rec['Butterflies'] = df_rec['Butterflies'].str.replace('Ja','Vlinders')
df_rec['Butterflies'] = df_rec['Butterflies'].fillna('GeenVlinders')
df_rec['Hedgehogs'] = df_rec['Hedgehogs'].str.replace('Ja','Egels')
df_rec['Hedgehogs'] = df_rec['Hedgehogs'].fillna('GeenEgels')
df_rec['Squirrels'] = df_rec['Squirrels'].str.replace('Ja','Eekhoorns')
df_rec['Squirrels'] = df_rec['Squirrels'].fillna('GeenEekhoorns')

# Create unique values: Indicate that it is about the colors of the leaf
df_rec['Leaf color'] = 'Blad' + df_rec['Leaf color']
# Create unique values: some plant species have leaves in different colors, also add "Blad" for the other colors
df_rec['Leaf color'] = df_rec['Leaf color'].str.replace(' ','Blad')
df_rec['Leaf color'] = df_rec['Leaf color'].str.replace(',',' ')

# Create unique values: Indicate that it is about the colors of the flower
df_rec['Flower color'] = 'Bloem' + df_rec['Flower color']
# Create unique values: some plant species have flowers in different colors, also add "Bloem" for the other colors
df_rec['Flower color'] = df_rec['Flower color'].str.replace(' ','Bloem')
df_rec['Flower color'] = df_rec['Flower color'].str.replace(',',' ')

# Create unique values: Replace evergreen
df_rec['Evergreen'] = df_rec['Evergreen'].str.replace('Ja','Wintergroen')
df_rec['Evergreen'] = df_rec['Evergreen'].str.replace('Nee','NietWintergroen')

# Soil moisture: Delete -
df_rec['Soil moisture'] = df_rec['Soil moisture'].str.replace('-',' ')

# Name: Delete -
df_rec['Name'] = df_rec['Name'].str.replace('-',' ')

# Sun exposure: standardizing the input
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace(' /',',')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Lichte, halfschaduw','Lichteschaduw Halfschaduw')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Lichte schaduw, zon','Lichteschaduw Zon')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Schaduw, Halfschaduw','Halfschaduw Schaduw')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Schaduw, Halfschaduw, Zon','Halfschaduw Schaduw Zon')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('schaduw, Halfschaduw, Zon','Halfschaduw Schaduw Zon')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Zon, Halfschaduw','Halfschaduw Zon')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Zon, Halfschaduw, Schaduw','Halfschaduw Schaduw Zon')
df_rec['Sun exposure'] = df_rec['Sun exposure'].str.replace('Halfschaduw, Zon, Schaduw','Halfschaduw Schaduw Zon')

# Rename ID column
df_rec.rename(columns = {'Unnamed: 0':'ID'}, inplace = True)

# Create a CSV file from the dataframe
df_rec.to_csv("recommender_system.csv")

# Message when cleaning is finished
print("End of cleaning for recommender system")