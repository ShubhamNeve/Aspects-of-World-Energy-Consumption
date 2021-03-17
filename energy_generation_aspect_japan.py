# -*- coding: utf-8 -*-
"""

**Japan**

If the analysis of the data is done closely for the country Japan then you could come to a conclusion that after 2011 their is sudden downfall in the generation of the Nuclear energy and the subsequent increase in the renewable energy.

In 2011, Natural disaster in Japan caused a massive  nuclear accident which led to the spread of radiations in the nearby areas which triggered the mass evacuation actions by the government. Later in March 2011, public sentiment shifted markedly so that there were widespread public protests calling for nuclear power to be abandoned. The balance between this populist sentiment and the continuation of reliable and affordable electricity supplies was worked out politically, and taking preventive measures to avoid such accidents and loss of life Japan thus shifted most of the energy requirements to Renewable Energy.
"""

import plotly as plotlyx
import plotly.graph_objects as go 
import plotly.express as px1
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

WEC= pd.DataFrame(pd.read_csv('World Energy Consumption.csv'))

Japan  = WEC.query('Country == "Japan"').copy()

Japan.columns

Japan['TotalEnergyConsumption'] = Japan['PrimaryEnergyConsumption']+Japan['RenewablesConsumption-EJ']

fig = px1.bar(Japan, x='year', y='TotalEnergyConsumption',
              color_discrete_sequence =['#2d6d64']*len(Japan))
fig.update_layout(plot_bgcolor="#fafafa",title = 'Japan Energy Consumption')
fig.show()

JapanNvR = Japan[['Country','year','NuclearGeneration-TWh', 'RenewablesPower-EJ','CarbonDioxideEmissions',]]

JapanNvR['RenewablesPower-EJ'] = JapanNvR['RenewablesPower-EJ']*278

JapanNvR = JapanNvR.sort_values(by='year', ascending=False)

fig = px1.bar(JapanNvR, x='year', y='NuclearGeneration-TWh',
              color_discrete_sequence =['#2d6d64']*len(JapanNvR))
fig.update_layout(plot_bgcolor="#fafafa",title = 'Japan - Nuclear Energy')
fig.show()

fig = px1.bar(JapanNvR, x='year', y='RenewablesPower-EJ',
              color_discrete_sequence =['#2d6d64']*len(JapanNvR))
fig.update_layout(plot_bgcolor="#fafafa", title= 'Japan - Renewable Energy')
fig.show()

fig = go.Figure() 

fig.add_trace(go.Scatter(x=JapanNvR['year'],
               y=JapanNvR['RenewablesPower-EJ'],
               name='Renewable Generation',
               mode='lines',
               text = JapanNvR['RenewablesPower-EJ'].astype('int'),
               hoverinfo='text',
               marker=dict(color='#FCD12A')
               ))

fig.add_trace(go.Scatter(x=JapanNvR['year'],
               y=JapanNvR['NuclearGeneration-TWh'],
               name='Nuclear Generation',
               mode='lines',
               text=JapanNvR['NuclearGeneration-TWh'].astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               ))

fig.update_layout(xaxis=go.layout.XAxis(title='Year'),plot_bgcolor="#fafafa",
                  yaxis_title="Energy generation - EJ",
                  title = 'Relation of Nuclear and Renewable Energy Generation.'
                  )

fig.show()

Japan['CarbonDioxideEmissions'] = Japan['CarbonDioxideEmissions']/Japan['CarbonDioxideEmissions'].max()
Japan['EnergyCons'] = (Japan['PrimaryEnergyConsumption']+Japan['RenewablesConsumption-EJ']) / ((Japan['PrimaryEnergyConsumption']+Japan['RenewablesConsumption-EJ']).max())

fig = go.Figure()
fig.add_trace(go.Scatter(x=Japan['year'],
               y=Japan['EnergyCons'],
               name='Primary Energy Consumption',
               mode='lines',
               text = Japan['EnergyCons'].astype('int'),
               hoverinfo='text',
               marker=dict(color='#FCD12A')
               ))

fig.add_trace(go.Scatter(x=Japan['year'],
               y=Japan['CarbonDioxideEmissions'],
               name='Carbon Emissions',
               mode='lines',
               text=JapanNvR['CarbonDioxideEmissions'].astype('int'),
               hoverinfo='text',
               marker=dict(color='seagreen')
               ))

fig.update_layout(xaxis=go.layout.XAxis(title='Year'),plot_bgcolor="#fafafa",
                  yaxis_title="Energy Consumption- EJ",
                  title = 'Energy Consumption vs Carbon Emission'
                  )

fig.show()
