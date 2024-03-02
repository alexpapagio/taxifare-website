import pandas as pd
import numpy as np

params = dict(pickup_datetime =1,
              pickup_longitude = 1,
              pickup_latitude = 2)

print (params['pickup_datetime'])

df = pd.DataFrame(
            np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
            columns=['lat', 'lon']
        )

print (df)
