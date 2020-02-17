import pandas as pd
us_cities = pd.read_csv("/home/kyleasti/Documents/ASTI/plotly/P-Poteka Installation Info 2.csv", encoding='iso-8859-1')

import plotly.express as px

fig = px.scatter_mapbox(us_cities, lat="Lat", lon="Lon", hover_name="Location", hover_data=["City", "Serial Number"],
                        color_discrete_sequence=["fuchsia"], zoom=10)
fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()