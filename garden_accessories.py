# Import needed library
import pandas as pd

# Create an empty dataframe with column names
df_garden_ac = pd.DataFrame(columns = ['Naam', 'Diersoort', 'Omschrijving', 'Foto'])
print(df_garden_ac)

# Fill in dataframe with new rows
# Hedgehog house
df_garden_ac = df_garden_ac.append({'Naam' : 'Egelhuis', 'Diersoort' : 'Egel', 'Omschrijving' : "Dit mooie natuurlijke egelhuis is een veilige thuisbasis voor de egel. Het beschermt de egel tegen het tuingereedschap (maaien, vorken)  maar ook tegen vossen en dassen. Het stevige stalen frame heeft een waterdicht dak wat is afgewerkt met geborsteld hout. De smalle ingang is speciaal ontworpen om roofdieren zoals dassen maar ook honden af te schrikken. Het huis is meer gemaakt als schuilplaats dan voor de winterslaap. Indien er extra takken en kreupelhout worden neergelegd kan het zo zijn dat de egel er zijn winterslaap houdt. Zet het egelhuis niet in de wind, stapel bladeren of bladeren rond het huis om het verder te camoufleren. Plaats gesneden korte stukken droog gras en leg dit binnen in het huis als nestmateriaal. Het huisje kan worden schoongemaakt, doe dit het liefst in april.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/0/6/0679505019130_0.jpg'}, ignore_index = True)

# Squirrel feeder
df_garden_ac = df_garden_ac.append({'Naam' : 'Eekhoorn voederhuis', 'Diersoort' : 'Eekhoorn', 'Omschrijving' : "Eekhoorns eten graag pinda's, zonnebloempitten en hazelnoten. Doormiddel van een voederhuis zult u, zeker in bosrijke gebieden, eekhoorns aantrekken naar de tuin.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/8/7/8714982093425.jpg'}, ignore_index = True)

# Squirrel house
df_garden_ac = df_garden_ac.append({'Naam' : 'Eekhoorn woonhuis', 'Diersoort' : 'Eekhoorn', 'Omschrijving' : "Door de verstedelijking van ons landschap zoeken eekhoorns steeds vaker voedsel en onderdak in onze tuinen. Een eekhoorn woonhuis is voorzien van twee in- en uitgangen. Dit biedt de eekhoorn een snelle ontsnappingsmogelijkheid bij gevaar. Hang het eekhoorn woonhuis in een boom op een hoogte van 3-5 meter en de openingen niet naar het zuidwesten gericht.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/5/0/5051054197609.jpg'},ignore_index = True)

# Pile of twigs
df_garden_ac = df_garden_ac.append({'Naam' : 'Stapel takken', 'Diersoort' : 'Vogel, Amfibie, Egel', 'Omschrijving' : "Heeft u de ruimte, leg dan een stapel takken of takkenril aan. Veel kleinere vogels, zoals heggenmus, winterkoning en roodborst vinden hier voedsel, schuilgelegenheid en een nestplaats. Een takkenril of takkenwal is een opstapeling van takken. Een takkenril is goedkoop en eenvoudig te realiseren. Een goed aangelegde ril is een compleet ecosysteem op zich. Ook voor veel andere dieren zijn takkenwallen van betekenis, zoals amfibieën, insecten, kleine zoogdieren.", 'Foto': 'https://www.shutterstock.com/fr/image-photo/pile-dry-twigs-tree-fire-on-1945951579'},ignore_index = True)

# Pile of leaves
df_garden_ac = df_garden_ac.append({'Naam' : 'Stapel bladeren', 'Diersoort' : 'Vogel, Egel', 'Omschrijving' : "Laat afgevallen bladeren zoveel mogelijk tussen de beplanting liggen; insecten en slakken houden zich hier schuil en vogels als merel, heggenmus en roodborst weten dit beslist te vinden.", 'Foto': 'https://static.turbosquid.com/Preview/2014/05/20__21_28_41/011.jpg71e72016-b764-44aa-b485-3a2d206543e7Zoom.jpg'},ignore_index = True)

# Amphibian house
df_garden_ac = df_garden_ac.append({'Naam' : 'Amfibieënhuis', 'Diersoort' : 'Amfibie', 'Omschrijving' : "Een amfibieënhuis is gemaakt om amfibieën te beschermen tegen roofdieren of om te overwinteren. Het huisje kan het beste in de buurt van een vijver of vochtige plek staan. Het liefst in een schaduwrijke omgeving, het dient er rustig en koel te zijn. Het amfibieënhuis kan bedekt worden met extra vegetatie om extra warmte te bieden. Verder is er geen enkel onderhoud nodig. Voor in de zomer kan er een gedeelte uit de onderkant gehaald worden zodat er contact gemaakt kan worden met de (verkoelende) bodem.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/0/6/0679505017396.jpg'},ignore_index = True)

# Insect hotel
df_garden_ac = df_garden_ac.append({'Naam' : 'Insectenhotel', 'Diersoort' : 'Bij', 'Omschrijving' : "Maak je tuin extra insectenvriendelijk met een insectenhuis! Kies een rustige, windstille plek uit om je insectenhuis op te hangen. Zorg er ook voor dat het een plek is waar de insecten een vrije aanvliegroute hebben. Bevestig het insectenhuis stevig zodat het bij harde wind niet gaat slingeren. Dit insectenhuis is met name geschikt voor bijen.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/5/0/5051054218311.jpg'},ignore_index = True)

# Butterfly house
df_garden_ac = df_garden_ac.append({'Naam' : 'Vlinderkast', 'Diersoort' : 'Vlinder', 'Omschrijving' : "Een vlinderkast biedt een schuilplaats voor vlinders. In de zon hangen, bij voorkeur in de luwte (niet in de volle wind), hoogte maakt niet zoveel uit", 'Foto': 'https://www.intratuin.nl/media/catalog/product/5/0/5051054184333.jpg'},ignore_index = True)

# Bird house
df_garden_ac = df_garden_ac.append({'Naam' : 'Vogelkast', 'Diersoort' : 'Vogel', 'Omschrijving' : "Natuurlijke nestplaatsen zijn helaas niet overal ruim voorhanden. Vooral in stedelijk gebied zijn nestkasten een dankbaar alternatief. Een nestkast in de tuin is een waar genoegen, voor jou én de vogels. Het is leuk om de bedrijvigheid te volgen, vanaf de eerste aarzelende inspectie, de nestbouw, het aanvliegen met voedsel tot het uitvliegen van de jongen. De vogelkast is geschikt voor de koolmees, kuifmees, boomklever, bonte vliegenvanger, huismus, ringmus en gekraagde roodstaart.", 'Foto': 'https://www.intratuin.nl/media/catalog/product/8/7/8714335900363.jpg'},ignore_index = True)

# Pond
df_garden_ac = df_garden_ac.append({'Naam' : 'Vijver', 'Diersoort' : 'Vogel, Amfibie', 'Omschrijving' : "Maak rondom een geleidelijk aflopende grindoever (variatie in waterdiepten). Vogels kunnen zo altijd op hun ‘eigen niveau’ bij het water. Leg de vijver zo aan dat het ondiepste deel in de zon ligt. Hier kunnen allerlei waterdiertjes zich al vroeg in het voorjaar opwarmen.In het ondiepe deel kunnen vogels makkelijk bij het water komen om te drinken en te badderen. En kikkers en padden zetten hier hun eieren af.", 'Foto': 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/027beebf-13e0-4cf9-8b4d-9fc58de4b879/d9o647n-8ce6b189-1d61-41f6-88f8-5d1d58ab9040.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzAyN2JlZWJmLTEzZTAtNGNmOS04YjRkLTlmYzU4ZGU0Yjg3OVwvZDlvNjQ3bi04Y2U2YjE4OS0xZDYxLTQxZjYtODhmOC01ZDFkNThhYjkwNDAucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.blRPYyM_VfQS-Ub0vEc8ITV5o7rfqQti5_S19n52zSg'},ignore_index = True)

# Dead wood
df_garden_ac = df_garden_ac.append({'Naam' : 'Dood hout', 'Diersoort' : 'Vogel, Bij, Vlinder', 'Omschrijving' : "Dood hout, of het nu op de grond ligt of nog in levende bomen en struiken hangt, is waardevol voor insecten en insectenetende vogels.", 'Foto': 'https://image.pngaaa.com/199/311199-middle.png'},ignore_index = True)

# Bird bath
df_garden_ac = df_garden_ac.append({'Naam' : 'Vogelbad', 'Diersoort' : 'Vogel', 'Omschrijving' : "Vogels hebben dagelijks behoefte aan drinkwater en moeten een bad kunnen nemen om hun veren in conditie te houden. Als de tuin geen ruimte laat aan een,vijver is een ondiepe waterschaal een prima alternatief. Plaats de schaal op een voor vogels veilige plaats op een open plek, maar wel met een boom of struik in de buurt. Bij gevaar kunnen de vogels dan wegduiken. Ververs dagelijks het water", 'Foto': 'https://www.intratuin.nl/media/catalog/product/8/7/8714982098710_2.jpg'},ignore_index = True)


#Create a CSV file from the dataframe
df_garden_ac.to_csv("garden_accessories.csv")

# Print dataframe in terminal
print(df_garden_ac)