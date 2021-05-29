import plotly as plotlyx
import plotly.graph_objects as go 
import plotly.express as px
import matplotlib.pyplot as plt
from sklearn import preprocessing 
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

WEC = pd.read_csv('World Energy Consumption.csv')

Missing_Values = WEC.isnull().sum()

Missing_Values

"""Percentage of Missing Values"""

total_cells = np.product(WEC.shape)
total_missing = Missing_Values.sum()
(total_missing/total_cells) * 100

WEC_LIST = list(WEC.select_dtypes(include=np.number).columns)

WEC_LIST.remove('year')

for i in WEC_LIST:
  fig = px.violin(WEC.query('Region != "World"'), x = "year", y=i)
  fig.show()

for i in WEC_LIST:
  WEC[i] = WEC[i].fillna(WEC.groupby('year')[i].transform('mean'))

WEC['CoalProduction-EJ'] = WEC['CoalProduction-EJ'].fillna(0)
WEC['GasProduction-EJ'] = WEC['GasProduction-EJ'].fillna(0)

for i in WEC_LIST:
  fig = px.violin(WEC.query('Region != "World"'), x = "year", y=i) 
  fig.show()

WEC.isnull().sum()

WEC1 = WEC.copy()

WEC.columns

WEC1 = WEC.query('year >= 1978')[['Region', 'year','OilConsumption-EJ','GasConsumption-EJ','CoalConsumption-EJ','NuclearConsumption-EJ','HydroConsumption-EJ','SolarConsumption-EJ','WindConsumption-EJ','RenewableConsumption-other']].melt(id_vars=['Region','year'], var_name ='Energy',value_name='values' )

WEC1.to_csv('ENERGYCONSUMPTION.csv')

ENERGY = pd.read_csv('ENERGYCONSUMPTION.csv')

PC = pd.read_csv('Power Consumption - Fuels.csv')

Colors = ['#003e3a', '#17554f', '#2d6d64', '#44867b', '#5da092', '#78b9a8', '#98d3bf']

ENERGY.columns

ENERGY['Fuels'].unique()

primary_energy = ENERGY.query('Country != "World"').groupby(['Fuels','year'])['Energy Consumption-EJ'].sum().reset_index()

primary_energy_R = ENERGY.query('Country != "World"').groupby(['Country','year'])['Energy Consumption-EJ'].sum().reset_index()

primary_energy_R

plot =  px.line(primary_energy_R, x="year", y="Energy Consumption-EJ", color='Country' )
plot.update_layout(plot_bgcolor="#fafafa",title = 'Energy Consumption by Regions')
plot.show()

plot = go.Figure() 
  
plot.add_trace(go.Scatter( 
    name = 'Wind', 
    x = primary_energy['year'], 
    y =  primary_energy.query('Fuels == "Wind"')['Energy Consumption-EJ'],
    line=dict(width=0.2, color='rgba(255, 195, 77,1)'),
    stackgroup='one'
   ))

plot.add_trace(go.Scatter( 
    name = 'Solar', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Solar"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(240, 236, 26,1)'),
    stackgroup='one'
   ) 
) 

plot.add_trace(go.Scatter( 
    name = 'Other Renewable', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Other-Renewable"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(254, 168, 119,1)'),
    stackgroup='one'
   ) 
) 
plot.add_trace(go.Scatter( 
    name = 'Hydro', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Hydro "')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(0, 59, 174,1)'),
    stackgroup='one'
   ) 
) 
plot.add_trace(go.Scatter( 
    name = 'Coal', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Coal"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgb(88, 84, 84)'),
    stackgroup='one'
   ) 
) 
plot.add_trace(go.Scatter( 
    name = 'Natural Gas', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Gas"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(25, 115, 15,1)'),
    stackgroup='one'
   ) 
) 

plot.add_trace(go.Scatter( 
    name = 'Oil', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Oil"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgb(255,105,0)'),
    stackgroup='one'
   ) 
) 
plot.add_trace(go.Scatter( 
    name = 'Nuclear', 
    x = primary_energy['year'], 
    y = primary_energy.query('Fuels == "Nuclear"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgb(163, 21, 47)'),
    stackgroup='one'
   ) 
)
plot.update_layout(plot_bgcolor="#fafafa",
                   title="Energy Consumption by Fuels",
                    xaxis_title="Year",
                    yaxis_title="Energy Consumption - EJ",
                    legend_title="Fuels ")
plot.show()

renewable = primary_energy.query('Fuels == "Wind" or Fuels == "Solar"  or Fuels == "Other-Renewable"').copy()

plot = go.Figure() 
plot.add_trace(go.Scatter( 
    name = 'Wind', 
    x = renewable['year'], 
    y =  renewable.query('Fuels == "Wind"')['Energy Consumption-EJ'],
    line=dict(width=0.2, color='rgba(255, 195, 77,1)'),
    stackgroup='one'
   ))

plot.add_trace(go.Scatter( 
    name = 'Solar', 
    x = renewable['year'], 
    y = renewable.query('Fuels == "Solar"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(240, 236, 26,1)'),
    stackgroup='one'
   ) 
) 

plot.add_trace(go.Scatter( 
    name = 'Other Renewable', 
    x = renewable['year'], 
    y = renewable.query('Fuels == "Other-Renewable"')['Energy Consumption-EJ'], 
    line=dict(width=0.2, color='rgba(254, 168, 119,1)'),
    stackgroup='one'
   ) 
) 
plot.update_layout(plot_bgcolor="#fafafa",
                   title="Renewable Energy Consumption",
                    xaxis_title="Year",
                    yaxis_title="Energy Consumption - EJ",
                    legend_title="Fuels")
plot.show()

Worldenergy = ENERGY.query('Country == "World" and year == "2019"').groupby(['Fuels','year'])['Energy Consumption-EJ'].sum().reset_index()

Worldenergy

px.pie(Worldenergy, values='Energy Consumption-EJ', names='Fuels')

Region_wisey = ENERGY.groupby(['Country','year'])['Energy Consumption-EJ'].sum().reset_index()

Region_wisey['Country'].unique()

fig = go.Figure()

fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "Africa"')['Energy Consumption-EJ'], 
        name='Africa',
        marker_color = Colors[0]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "Asia Pacific"')['Energy Consumption-EJ'], 
        name='Asia Pacific',
        marker_color = Colors[1]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "CIS"')['Energy Consumption-EJ'], 
        name='CIS',
        marker_color = Colors[2]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "Europe"')['Energy Consumption-EJ'], 
        name='Europe',
        marker_color = Colors[3]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "Middle East"')['Energy Consumption-EJ'], 
        name='Middle East',
        marker_color = Colors[4]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "North America"')['Energy Consumption-EJ'], 
        name='North America',
        marker_color = Colors[5]
        ))
fig.add_trace(
    go.Bar(
        x=Region_wisey['year'], 
        y=Region_wisey.query('Country == "South & Central America"')['Energy Consumption-EJ'], 
        name='South & Central America',
        marker_color = Colors[6]
        ))


fig.update_layout(barmode='stack',plot_bgcolor="#fafafa", xaxis={'categoryorder':'category ascending'},
                  title="Overall Energy Consumption by Regions",
                    xaxis_title="Year",
                    yaxis_title="Energy Consumption - EJ",
                    legend_title="Regions")

fig.show()

Region_wise = ENERGY.query('Country != "World"').groupby(['Country'])['Energy Consumption-EJ'].sum().reset_index()

colors = ['lightslategray',] * 7
colors[1] = 'crimson'
colors[0] = '#148199'

fig = go.Figure(data=[go.Bar(
    x=Region_wise['Country'],
    y=Region_wise['Energy Consumption-EJ'],
    marker_color=colors 
)])
fig.update_layout(title_text='Minimum and Maximum Consumption Regions',plot_bgcolor="#fafafa"
                  ,xaxis_title="Regions",
                    yaxis_title="Energy Consumption - EJ")
fig.show()

YPC = PC.groupby(['Year'])['Oil','Natural Gas','Coal','Nuclear energy','Renewables'].sum()

label = ['Oil', 'Natural Gas', 'Coal', 'Nuclear energy','Renewables']
values2018 = YPC[label].query('Year == "2018"').values.tolist()[0]
values2019 = YPC[label].query('Year == "2019"').values.tolist()[0]

Colors = ['#3a5c09', '#627200','#908700','#c59800','#ffa600']
fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]],
                    subplot_titles=['2018', '2019'])
fig.add_trace(go.Pie(labels=label, 
                     values=values2018, scalegroup='one',
                     name="Power Consumption - Fuels 2018",
                     marker_colors=Colors), 1, 1)
fig.add_trace(go.Pie(labels=label, 
                     values= values2019, scalegroup='one',
                     name="Power Consumption - Fuels 2019",
                     marker_colors=Colors), 1, 2)

fig.update_layout(title_text='Percentage of Power Consumption in 2018 & 2019',
                  legend_title="Fuels")
fig.show()

def fn_carbon_emmission( Value_in_EJ , Fueltype ):
  EJ_GJ = Value_in_EJ * 1000000000
  if Fueltype == 'Natural_Gas':
    CoE = EJ_GJ * 0.06
    CoE = CoE /1000000
    CoE = CoE - (CoE*0.08)
  elif Fueltype == 'Oil':
    CoE = EJ_GJ * 0.07
    CoE = CoE /1000000
    CoE = CoE - (CoE*0.08)
  elif Fueltype == 'Coal':
    CoE = EJ_GJ * 0.09
    CoE = CoE /1000000
    CoE = CoE - (CoE*0.08)
  elif Fueltype == 'Nuclear':
    CoE = EJ_GJ * 0.04
    CoE = CoE /1000000
    CoE = CoE - (CoE*0.08)
  elif Fueltype == 'Renewable':
    CoE = EJ_GJ * 0.06
    CoE = CoE /1000000
    CoE = CoE - (CoE*0.08)
  elif Fueltype == 'OilEq':
    CoE = EJ_GJ * 23.88458966
  return CoE

WECCE = WEC[['Region','Country','year','CarbonDioxideEmissions','OilConsumption-EJ','GasConsumption-EJ','CoalConsumption-EJ','NuclearConsumption-EJ','HydroConsumption-EJ','SolarConsumption-EJ','WindConsumption-EJ','RenewableConsumption-other']].query('Region == "World"')

WECCE['CO2_emission_tonne_NR'] = fn_carbon_emmission(WECCE['OilConsumption-EJ'],'Oil') + fn_carbon_emmission(WECCE['GasConsumption-EJ'],'Natural_Gas') + fn_carbon_emmission(WECCE['CoalConsumption-EJ'] ,'Coal') + fn_carbon_emmission(WECCE['NuclearConsumption-EJ'],'Nuclear')

WECCE['CO2_emission_tonne_R'] = fn_carbon_emmission(WECCE['HydroConsumption-EJ'] + WECCE['SolarConsumption-EJ'] + WECCE['WindConsumption-EJ'] + WECCE['RenewableConsumption-other'], 'Renewable')

WECCE['Co2_Emission_WOR'] = WECCE['CO2_emission_tonne_R'] + WECCE['CO2_emission_tonne_NR']

EMISSION = WECCE[['Region','year','CarbonDioxideEmissions','Co2_Emission_WOR']]

EMISSION.head()

fig = go.Figure() 
fig.add_trace(go.Scatter(x=EMISSION['year'],
               y=EMISSION['CarbonDioxideEmissions'],
               name='CarbonDioxideEmissions',
               mode='lines',
               text = EMISSION['CarbonDioxideEmissions'].astype('int'),
               hoverinfo='text',
               marker=dict(color='#FCD12A')
               ))

fig.add_trace(go.Scatter(x=EMISSION['year'],
               y=EMISSION['Co2_Emission_WOR'],
               name='Co2_Emission_WOR',
               mode='lines',
               text=EMISSION['Co2_Emission_WOR'].astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               ))

fig.update_layout(xaxis=go.layout.XAxis(title='Year'),
                  plot_bgcolor="#fafafa",
                  yaxis_title="Carbon dioxide Emission - Million Tonnes",
                  title = 'Carbon Dioxide Emission with respect to renewables',
                  legend_title = 'Carbon emission'
                  )

fig.show()

WECCE['Consumption_OilEQ']= fn_carbon_emmission(WECCE['OilConsumption-EJ'],'OilEq') + fn_carbon_emmission(WECCE['GasConsumption-EJ'],'OilEq') + fn_carbon_emmission(WECCE['CoalConsumption-EJ'] ,'OilEq') + fn_carbon_emmission(WECCE['NuclearConsumption-EJ'],'OilEq') + fn_carbon_emmission(WECCE['HydroConsumption-EJ'] + WECCE['SolarConsumption-EJ'] + WECCE['WindConsumption-EJ'] + WECCE['RenewableConsumption-other'], 'OilEq')

Temp = WECCE[['year','CarbonDioxideEmissions','Consumption_OilEQ']].copy()

Temp['CarbonDioxideEmissions'] = Temp['CarbonDioxideEmissions'] / Temp['CarbonDioxideEmissions'].max()

Temp['Consumption_OilEQ'] = Temp['Consumption_OilEQ'] / Temp['Consumption_OilEQ'].max()

fig = go.Figure() 
fig.add_trace(go.Scatter(x=Temp['year'],
               y=Temp['CarbonDioxideEmissions'],
               name='CarbonDioxideEmissions',
               mode='lines',
               text = Temp['CarbonDioxideEmissions'].astype('int'),
               hoverinfo='text',
               marker=dict(color='#FCD12A')
               ))

fig.add_trace(go.Scatter(x=Temp['year'],
               y=Temp['Consumption_OilEQ'],
               name='Consumption_OilEQ',
               mode='lines',
               text=Temp['Consumption_OilEQ'].astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               ))

fig.update_layout(xaxis=go.layout.XAxis(title='Year'),plot_bgcolor="#fafafa",
                  yaxis_title="values in - Million Tonnes",
                  title = 'Carbon Dioxide Emission Vs The Energy Consumption',
                  legend_title = 'Emission & Consumption')

fig.show()

WEC2019 = WEC.query('Region != "World"').copy()

WEC2019.head()

WEC2019['Region'].unique()

WEC2019['World'] = ['World',]*5060

pip install --upgrade plotly

fig = px.sunburst(WEC2019, path=['World','Region', 'Country'], values='RenewablesPower-EJ'
                    ,color_continuous_scale="darkmint",
                  color='RenewablesPower-EJ')
fig.update_layout(plot_bgcolor="#fafafa",
                  title = 'Renewable Energy Generation per Region per Country wise')
fig.show()

fig =go.Figure(go.Sunburst(
    labels=["Resources", "Renewable", "Non-Renewable", "Solar", "Wind", "Hydro", "Other", "Oil", "Natural-Gas", "Coal", "Nuclear"],
    parents=["", "Resources", "Resources", "Renewable", "Renewable", "Renewable", "Renewable", "Non-Renewable", "Non-Renewable","Non-Renewable","Non-Renewable" ],
    values=[0, 20, 20, 10,10, 10,10, 10, 10, 10, 10]
))
fig.update_layout(plot_bgcolor="#fafafa",
                  title = 'Energy Resources Types')

fig.show()

