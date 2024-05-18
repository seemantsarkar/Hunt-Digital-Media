#!/usr/bin/env python
# coding: utf-8

# # 1. Data Preparation and Exploration:

# In[227]:


import pandas as pd


# In[228]:


df = pd.read_csv("Data Analyst _ Sample Data _HDM - call-data-udpated.csv")


# In[229]:


# Explore the data
df


# In[230]:


df.info()


# In[231]:


# Check for missing values in each column
missing_values = df.isnull().sum(axis=0)
print("Missing Values:\n", missing_values)
  


# In[232]:


# Drop the 'From Calling Number' column
df.drop(columns=['From Calling Number'], inplace=True)


# In[233]:


# Missing values managed
missing_values = df.isnull().sum(axis=0)
print("Missing Values:\n", missing_values)


# In[234]:


# Check unique values in each column to identify inconsistencies
unique_values = df.nunique()
print("\nUnique Values:\n", unique_values)


# In[235]:


df.info()


# # 2.	Campaign Performance Report:

# In[236]:


#Total calls


# In[237]:


# Total calls (count of call_sid)
total_calls = df['Call Id'].count()
print("Total calls:", total_calls)


# In[238]:


#Unique leads


# In[239]:


# Unique leads (count of distinct lead_id)
unique_leads = df['Lead Id'].nunique()
print("Unique leads:", unique_leads)


# In[240]:


#Calls connected


# In[241]:


# Calls connected (count of call_status = "completed")
calls_completed = df[df['Call Status'] == 'completed']['Call Id'].count()
print("Calls completed:", calls_completed)


# In[242]:


#Unique calls connected 


# In[243]:


# Filter the DataFrame to include only rows where the call status is "completed"
completed_calls_df = df.where(df['Call Status'] == 'completed')

# Count the distinct lead IDs in the filtered DataFrame
unique_calls_connected = completed_calls_df['Lead Id'].dropna().nunique()

print("Unique calls connected : ", unique_calls_connected)


# In[244]:


#Leads converted 


# In[245]:


# Filter the DataFrame to include only rows where the lead status is "Interested"
interested_leads_df = df.where(df['Lead Status'] == 'Interested')

# Count the occurrences of lead IDs in the filtered DataFrame
leads_converted = interested_leads_df['Lead Id'].dropna().count()

print("Leads converted : ", leads_converted)


# In[246]:


#Qualified leads 


# In[247]:


# Get unique values in the 'Lead Status' column
unique_lead_status = df['Lead Status'].unique()

# Print unique values
print("Unique values in 'Lead Status' column:")
for status in unique_lead_status:
    print(status)


# In[248]:


# Define the advertiser criteria
advertiser_criteria = (df['Lead Status'] == 'Interested') | (df['Lead Status'] == 'Call Back')

# Filter the DataFrame based on the advertiser criteria
qualified_leads_df = df.where(advertiser_criteria)

# Count the occurrences of lead IDs in the filtered DataFrame
qualified_leads_count = qualified_leads_df['Lead Id'].dropna().count()

print("Qualified leads : ", qualified_leads_count)



# In[249]:


#Leads lost


# In[250]:


# Filter the DataFrame to include only rows where the lead status is "Not Interested"
lost_leads_df = df.where(df['Lead Status'] == 'Not Interested')

# Count the occurrences of lead IDs in the filtered DataFrame
leads_lost_count = lost_leads_df['Lead Id'].dropna().count()

print("Leads lost : ", leads_lost_count)


# In[251]:


#Average agent call duration 


# In[252]:


# Calculate the average agent call duration
average_agent_call_duration = df['Agent Duration(seconds)'].mean()

print("Average agent call duration:", average_agent_call_duration)


# In[253]:


#Average customer call duration 


# In[254]:


# Calculate the average customer call duration
average_customer_call_duration = df['Customer Duration(seconds)'].mean()

print("Average customer call duration:", average_customer_call_duration)


# # 2. Lead Disposition Report:
# 

# In[255]:


import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame containing the lead data

# Grouping and counting lead statuses
lead_status_distribution = df['Lead Status'].value_counts()

# Print the Lead Disposition Report
print("Lead Disposition Report:")
print(lead_status_distribution)

# Plotting the distribution as a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = lead_status_distribution.plot(kind='barh', color='skyblue')  # Horizontal bar plot

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height()/2, 
             f'{int(bar.get_width())}', 
             ha='left', va='center')

plt.title('Lead Disposition Report')
plt.xlabel('Count')
plt.ylabel('Lead Status')
plt.tight_layout()
plt.show()


# # 3. Agent Performance Report (per agent):

# In[256]:


#Number of calls made per agent


# In[257]:


# Grouping and counting calls made per agent
agent_performance = df.groupby('Agent Name')['Call Id'].count()

# Print the Agent Performance Report
print("Agent Performance Report - Number of Calls Made per Agent:")
print(agent_performance)

# Visualizing the results using a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = agent_performance.plot(kind='barh', color='skyblue')
plt.title('Agent Performance Report - Number of Calls Made per Agent')
plt.xlabel('Number of Calls Made')
plt.ylabel('Agent Name')

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}', 
             ha='left', va='center')

plt.tight_layout()
plt.show()


# In[258]:


#Calls connected per agent


# In[259]:


# Filter the DataFrame to include only rows where the call status is "completed"
completed_calls_df = df[df['Call Status'] == 'completed']

# Grouping and counting calls completed per agent
calls_completed_per_agent = completed_calls_df.groupby('Agent Name')['Call Id'].count()

# Print the number of calls completed per agent
print("Calls completed per agent:")
print(calls_completed_per_agent)

# Visualizing the results using a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = calls_completed_per_agent.plot(kind='barh', color='skyblue')
plt.title('Agent Performance Report - Number of Calls Completed per Agent')
plt.xlabel('Number of Calls Completed')
plt.ylabel('Agent Name')

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}', 
             ha='left', va='center')

plt.tight_layout()
plt.show()


# In[260]:


#Leads converted


# In[261]:


# Filter the DataFrame to include only rows where the lead status is "Interested"
interested_leads_df = df[df['Lead Status'] == 'Interested']

# Grouping and counting leads converted per agent
leads_converted_per_agent = interested_leads_df.groupby('Agent Name')['Lead Id'].count()

# Print the number of leads converted per agent
print("Leads converted per agent (lead_status = 'Interested'):")
print(leads_converted_per_agent)

# Visualizing the results using a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = leads_converted_per_agent.plot(kind='barh', color='skyblue')
plt.title('Agent Performance Report - Number of Leads Converted per Agent')
plt.xlabel('Number of Leads Converted')
plt.ylabel('Agent Name')

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             f'{int(bar.get_width())}', 
             ha='left', va='center')

plt.tight_layout()
plt.show()


# In[262]:


#Average agent call duration


# In[263]:


# Grouping by 'Agent Name' and calculating the mean of 'Agent Duration(seconds)' per agent
average_agent_call_duration_per_agent = df.groupby('Agent Name')['Agent Duration(seconds)'].mean()

# Print the average agent call duration per agent
print("Average agent call duration per agent (in seconds):")
print(average_agent_call_duration_per_agent)

# Visualizing the results using a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = average_agent_call_duration_per_agent.plot(kind='barh', color='skyblue')
plt.title('Agent Performance Report - Average Agent Call Duration per Agent')
plt.xlabel('Average Call Duration (seconds)')
plt.ylabel('Agent Name')

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             f'{bar.get_width():.2f}', 
             ha='left', va='center')

plt.tight_layout()
plt.show()


# In[264]:


# Assuming df is your DataFrame containing the call data

# Grouping by 'Agent Name' and calculating the mean of 'Customer Duration(seconds)' per agent
average_customer_call_duration_per_agent = df.groupby('Agent Name')['Customer Duration(seconds)'].mean()

# Print the average customer call duration per agent
print("Average customer call duration per agent (in seconds):")
print(average_customer_call_duration_per_agent)

# Visualizing the results using a horizontal bar plot
plt.figure(figsize=(10, 6))
bars = average_customer_call_duration_per_agent.plot(kind='barh', color='skyblue')
plt.title('Agent Performance Report - Average Customer Call Duration per Agent')
plt.xlabel('Average Call Duration (seconds)')
plt.ylabel('Agent Name')

# Adding annotations to the bars
for bar in bars.patches:
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
             f'{bar.get_width():.2f}', 
             ha='left', va='center')

plt.tight_layout()
plt.show()


# # 4. Additional Reports

# In[265]:


#Distribution of Call Statuses per Agent


# In[266]:


# Grouping by 'Agent Name' and 'Call Status' and counting the number of calls
call_status_distribution_per_agent = df.groupby(['Agent Name', 'Call Status'])['Call Id'].count().unstack()

# Print the call status distribution per agent
print("Call Status Distribution per Agent:")
print(call_status_distribution_per_agent)

# Visualizing the results using a stacked bar plot
call_status_distribution_per_agent.plot(kind='barh', stacked=True, figsize=(12, 8))
plt.title('Call Status Distribution per Agent')
plt.xlabel('Number of Calls')
plt.ylabel('Agent Name')
plt.tight_layout()
plt.show()


# # 5. Forecasting Objectives
# 

# # 5.1. Call Volume Forecast:

# In[269]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Convert 'Created At' column to datetime with the correct format
df['Created At'] = pd.to_datetime(df['Created At'], format='%d-%m-%Y %H:%M')

# Aggregate data: Count number of calls per day
df_daily = df.groupby(pd.Grouper(key='Created At', freq='D')).size().reset_index(name='Call Count')

# Visualize historical call volume
plt.figure(figsize=(10, 6))
plt.plot(df_daily['Created At'], df_daily['Call Count'], marker='o')
plt.title('Historical Call Volume')
plt.xlabel('Date')
plt.ylabel('Number of Calls')
plt.grid(True)
plt.show()

# Fit ARIMA model
model = ARIMA(df_daily['Call Count'], order=(1, 1, 1))  # Adjust order if needed
model_fit = model.fit()

# Forecast next 30 days
forecast = model_fit.forecast(steps=30)

# Visualize forecast
forecast_dates = pd.date_range(start=df_daily['Created At'].iloc[-1], periods=31)[1:]
plt.figure(figsize=(10, 6))
plt.plot(df_daily['Created At'], df_daily['Call Count'], label='Historical')
plt.plot(forecast_dates, forecast, label='Forecast', color='red', linestyle='--')
plt.title('Call Volume Forecast for Next 30 Days')
plt.xlabel('Date')
plt.ylabel('Number of Calls')
plt.legend()
plt.grid(True)
plt.show()

# Print forecasted call volume for next 30 days
print("Forecasted call volume for the next 30 days:")
print(forecast)


# # 5.2. Lead Conversion Forecast:

# In[270]:


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Filter data to include only interested prospects
interested_prospects = df[df['Lead Status'] == 'Interested']

# Aggregate data: Count number of leads converted into interested prospects per day
prospects_daily = interested_prospects.groupby(pd.Grouper(key='Created At', freq='D')).size().reset_index(name='Conversion Count')

# Visualize historical lead conversion
plt.figure(figsize=(10, 6))
plt.plot(prospects_daily['Created At'], prospects_daily['Conversion Count'], marker='o')
plt.title('Historical Lead Conversion')
plt.xlabel('Date')
plt.ylabel('Number of Converted Leads')
plt.grid(True)
plt.show()

# Fit ARIMA model
model = ARIMA(prospects_daily['Conversion Count'], order=(1, 1, 1))  # Adjust order if needed
model_fit = model.fit()

# Forecast next 30 days
forecast = model_fit.forecast(steps=30)

# Visualize forecast
forecast_dates = pd.date_range(start=prospects_daily['Created At'].iloc[-1], periods=31)[1:]
plt.figure(figsize=(10, 6))
plt.plot(prospects_daily['Created At'], prospects_daily['Conversion Count'], label='Historical')
plt.plot(forecast_dates, forecast, label='Forecast', color='red', linestyle='--')
plt.title('Lead Conversion Forecast for Next 30 Days')
plt.xlabel('Date')
plt.ylabel('Number of Converted Leads')
plt.legend()
plt.grid(True)
plt.show()

# Print forecasted lead conversion for next 30 days
print("Forecasted lead conversion for the next 30 days:")
print(forecast)


# In[ ]:




