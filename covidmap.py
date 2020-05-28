import pandas as pd
import geopandas as gpd
import requests
r = requests.get('https://www.worldometers.info/coronavirus/')
data = pd.read_html(r.text)
data = data[0]
    
data_cases = data[['Country,Other', 'TotalCases', 'TotalDeaths']]
# https://hub.arcgis.com/datasets/a21fdb46d23e4ef896f31475217cbb08_1?geometry=-80.859%2C-89.944%2C75.234%2C48.630
world_data = gpd.read_file(r'C:\Users\uzayuzal\Documents\GitHub\mapping-coronavirus\world.shp')

world_data.plot()

world_data_list = world_data['CNTRY_NAME'].tolist()
data_cases_list = data_cases['Country,Other'].tolist()

world_data_list.sort()
data_cases_list.sort()

for ulkeler in data_cases_list:
    if ulkeler in world_data_list:
        pass
    else:
        print(ulkeler + ' shape dosyasinda yok')
    
world_data.replace('Bahamas, The', 'Bahamas', inplace = True)
world_data.replace('Byelarus', 'Belarus', inplace = True)
world_data.replace('South Korea', 'S. Korea', inplace = True)
world_data.replace('United States', 'USA', inplace = True)
world_data.replace('UK.', 'UK', inplace = True)
world_data.replace('United Arab Emirates', 'UAE', inplace = True)
world_data.replace('Macau', 'Macao', inplace = True)
world_data.replace('Macedonia', 'North Macedonia', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)
world_data.replace('Myanmar (Burma)', 'Myanmar', inplace = True)


data_cases.rename(columns = {'Country,Other': 'CNTRY_NAME'}, inplace = True)

combined = world_data.merge(data_cases, on = 'CNTRY_NAME')

combined.to_file(r'C:\Users\uzayuzal\Documents\GitHub\mapping-coronavirus\combined.shp')

ax = combined.plot(figsize=(15, 15), column='TotalCases', scheme='quantiles', legend=True, legend_kwds={'loc': 'lower left'})
ax.set_title("Coronavirus Cases Worldwide")


import matplotlib.pyplot as plt
plt.savefig('covid-map.png')

# gorsellestirme 2

ax2 = combined.plot(figsize=(15, 15), column='TotalCases', scheme='fisher_jenks', k=10, legend=True, cmap='YlGn', edgecolor='black', legend_kwds={'loc': 'lower left'})
ax.set_title("Coronavirus Cases Worldwide (Classified with Fisher Jenks 10 Class")


# vaka 100000'den fazla olanlar
vaka = combined[combined['TotalCases'] > 100000]
ax3 = vaka.plot(figsize=(15, 15), column='TotalCases', scheme='fisher_jenks', k=10, legend=True, cmap='YlGn', edgecolor='black', legend_kwds={'loc': 'lower left'})
vaka['CNTRY_NAME'].size
vaka.apply(lambda x: ax3.annotate(s=x['CNTRY_NAME'], xy=x.geometry.centroid.coords[0], ha='center'),axis=1);


turkey = combined[combined['CNTRY_NAME'] == 'Turkey']
turkey.plot()
turkey


























