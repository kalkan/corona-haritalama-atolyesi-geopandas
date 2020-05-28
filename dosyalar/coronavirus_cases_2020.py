import pandas as pd
import geopandas as gpd

data = pd.read_html('https://www.worldometers.info/coronavirus/')

for data_cases in data:
    print(data_cases)
    
data_cases = data_cases[['Country,Other', 'TotalCases' ]]

world_data = gpd.read_file(r'D:\GeoDelta\Coronavirus Cases March 2020\World_Map.shp')

for items in data_cases['Country,Other'].tolist():
    world_data_list = world_data['NAME'].tolist()
    if items in world_data_list:
        pass
    else:
        print(items + ' is not in the world_data list')
    
world_data.replace('Korea, Republic of', 'S. Korea', inplace = True)
world_data.replace('Iran (Islamic Republic of)', 'Iran', inplace = True)
world_data.replace('United States', 'USA', inplace = True)
world_data.replace('United Kingdom', 'U.K.', inplace = True)
world_data.replace('United Arab Emirates', 'U.A.E.', inplace = True)
world_data.replace('Viet Nam', 'Vietnam', inplace = True)
world_data.replace('Macau', 'Macao', inplace = True)
world_data.replace('The former Yugoslav Republic of Macedonia', 'North Macedonia', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)
world_data.replace('Czech Republic', 'Czechia', inplace = True)
world_data.replace('Palestine', 'State of Palestine', inplace = True)


data_cases.rename(columns = {'Country,Other': 'NAME'}, inplace = True)

combined = world_data.merge(data_cases, on = 'NAME')

combined.to_file(r'D:\GeoDelta\Coronavirus Cases March 2020\combined.shp')










































