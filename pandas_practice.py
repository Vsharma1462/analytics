"""import pandas as pd
mydataset={
    'car' :["bmw",'volvo','ford'],
    'passings' : [2,3,4],
    'engine' : ['petrol','diesel','cng']
}

myvar=pd.DataFrame(mydataset)
print(myvar)

print(pd.__version__)
---------------------------------------------------------------------------------------
import pandas as pd

a=[1,7,2]

myvar=pd.Series(a)
print(myvar)
-------------------------------------------------------------------------------------
import pandas as pd 

cal={"day1":23,"day2":34,"day3":45}

myvar=pd.Series(cal,index=["day1","day2"])

print(myvar)
---------------------------------------------------------------------------------------
import pandas as pd
mydataset={
    'car' :["bmw",'volvo','ford'],
    'passings' : [2,3,4],
    'engine' : ['petrol','diesel','cng']
}

myvar=pd.DataFrame(mydataset,index=['a','b','c'])
print(myvar.loc['a'])

----------------------------------------------------------------------------------------

import pandas as pd 

df =pd.read_csv("csv1.csv")

print(df)
-------------------------------------------------------------------------------------

import pandas as pd 

df =pd.read_csv("csv1.csv")

print(df.to_string())

-------------------------------------------------------------------------------------


import pandas as pd 

print(pd.options.display.max_rows)

--------------------------------------------------------------------------------------


import pandas as pd 

pd.options.display.max_rows=999


print(pd.options.display.max_rows)

----------------------------------------------------------------------------------

import pandas as pd 

df =pd.read_json("json1.json")

print(df.to_string())
------------------------------------------------------------------------------------

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df =pd.DataFrame(data)


print(df)
-----------------------------------------------------------------------------


import pandas as pd 

df =pd.read_csv("csv1.csv")

print(df.head(4))

------------------------------------------------------------------------

import pandas as pd 

df =pd.read_csv("csv1.csv")

print(df.tail(4))
print(df.info())
-----------------------------------------------------------

import pandas as pd

df=pd .read_csv("csv1.csv")


df.fillna(python,inplace=True)

print(df)
--------------------------------------------------------------------"""


import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("data.csv")
df.corr()
print(df.corr())
#df.plot(kind="hist" , x="Duration" )

#plt.show()
