import pandas as pd
import time
from datetime import datetime
import numpy as np
import plotly.express as px
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#from webdriver_manager.chrome import ChromeDriverManager


# Function to fetch data and generate treemap
def fetch_and_plot():
    # Declare browser
    chrome_driver_path = '/home/a0x0bc1/Downloads/chromedriver-linux64/chromedriver'
    service = Service(chrome_driver_path)# Create a Service object
    driver = webdriver.Chrome(service=service) # Pass the Service object to the webdriver.Chrome

    #define url of page to exract data from
    url='https://coinmarketcap.com/gainers-losers/'
    driver.get(url)
    time.sleep(5) #Sleep for few seconds so, by that time, the webpage gets loaded.
    ranking =  driver.find_elements(By.XPATH, '//*[@id="__next"]/div[2]/div/div[2]/div/div[2]/div/div[1]/div/table')# get element by XPATH from element selection in inspect mode

    """ rec =  [s.text for s in ranking] + rec #this will return ['#\nName\nPrice\n24h\nVolume(24h)
    print(rec) """

    data = []  # Extract data
    for index, rank in enumerate(ranking):
        rowData = rank.text.split('\n')
        #print(rowData) #This prints the extracted data all in a single row
        data.append(rowData)
    '''print(rowData)'''


    #Resahaping the data list to # cols, should be indented or not?
    lst1 = rowData[5:] #popping headers
    expectedRows = len(lst1) // 4 #divide the list by no of expected cols to get no of expected rows
    lst = np.array(lst1)#turning the simngle rowdata list into an array
    reshpd = lst.reshape(int(expectedRows), 4) #to get row x col
    '''print(reshpd)'''
    reshpdtrimmed = reshpd[:, :-1]#'Price' '24h%' 'Vol(24h)' were merged together so I popped them
    forth = np.array([row[3].split() for row in reshpd])#now splitting 'Price' '24h%' 'Vol(24h)' on their own
    '''print(reshpdtrimmed)'''
    merged = np.concatenate((reshpdtrimmed, forth), axis = 1)#coming together making the perfect array
    '''print(merged)'''
    first10 = np.array(merged[:10])#only need the first 10
    '''print(first10)'''

    #passing to nympy Dataframe to get tabular form
    df = pd.DataFrame(first10, columns=['CmcRank', 'Name', 'Symbol', 'Price', '24h%', 'Vol(24h)'])
    #Initially getting errors of ValueError: 5 columns passed, passed data had 125 columns
    #so needed to break the  cols down into 5
    print(df)

    df['24h%'] = df['24h%'].str.rstrip('%').astype(float)

    # Normalize the colors
    fig = px.treemap(
        df,
        path=['Name'],
        values='24h%',
        color='24h%',
        hover_data={'Symbol': True, 'Price': True, 'Vol(24h)': True, '24h%': True},
        color_continuous_scale='Greens',
    )
    timestamp = datetime.utcnow().strftime('%b %d, %Y %H:%M:%S UTC')#timestamp for the plot

    # Customize labels and hover info
    fig.update_traces(
        textinfo='label+text',
        hovertemplate='<b>%{label}</b><br>Symbol: %{customdata[0]}<br>Price: %{customdata[1]}<br>Volume(24h): %{customdata[2]}<br>24h%: %{value}%'
    )

    title= f'Top10 CMC 24h% Increase for {timestamp}'
    fig.update_layout(title=title, margin=dict(t=50, l=25, r=25, b=25))
    fig.show()

    #driver.quit


try:
    while True:
        fetch_and_plot()
        time.sleep(15)
except KeyboardInterrupt:
    print("Stopped by user")