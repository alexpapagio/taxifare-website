import streamlit as st
import datetime
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

d = st.date_input(
    "Pick up date",
    datetime.date(2022, 5, 5))
st.write('Pick up date:', d)


t = st.time_input('Pick up time', datetime.time(8, 45))

st.write('Pick up time:', t)

pick_lon = st.number_input('Insert your pick-up longtitude',value=(-73.9798156))

st.write('Pick-up Longtitude is:', pick_lon)

pick_lat = st.number_input('Insert your pick-up Latitude',value=(40.7614327))

st.write('Your pick-up latitude is:', pick_lat)


drop_lon = st.number_input('Insert your drop-off longtitude',value=(-73.8803331))

st.write('Drop-off Longtitude is:', drop_lon)

drop_lat = st.number_input('Insert your drop_off Latitude',value=(40.6513111))

st.write('Your drop_off latitude is:', drop_lat)

count = st.text_area('Passenger count:', '''
    1
    ''')

st.write('Passenger count:', len(count))



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


'''

2. Let's build a dictionary containing the parameters for our API...



3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

params = dict(pickup_datetime =f'{d} {t}',
              pickup_longitude = pick_lon,
              pickup_latitude = pick_lat,
              dropoff_longitude = drop_lon,
              dropoff_latitude = drop_lat,
              passenger_count = count)


response = requests.get(url,params=params)
fare = response.json()
output = fare['fare']

st.markdown(f"Your fare is: {output}")


df = pd.DataFrame([[pick_lat, pick_lon],[drop_lat,drop_lon]],
            columns=['lat', 'lon']
        )

st.write(df)

st.map(df)
