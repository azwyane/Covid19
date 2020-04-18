import streamlit as st
import requests
import numpy as np
import pandas as pd


'''
# apicovid2019

**Fetch api from github**

## methods
- fetch entire data
- fetch data by country
- fetch data by continent
:sunglasses:
'''
@st.cache
def get_data():
    return requests.get("https://apicovid2019.azurewebsites.net")

get=get_data()
get_json=get.json()

if st.checkbox('Show json data'):
    st.json(get_json) #writes raw data to screen commented for now

#st.table(get_json)
first_index=list(get_json[0])
second_index=list(get_json[1])
ttile=list(second_index[0])
third_index=list(get_json[2])
#st.table(ttile)
#st.write(ttile)

st.write(first_index[0],(get_json[0])[first_index[0]])
st.write(first_index[1],(get_json[0])[first_index[1]])
st.write(first_index[2],(get_json[0])[first_index[2]])


#st.write(list(get_json[1]))
value=[]
title=[x for x in list(list(get_json[1])[0])]


#for j in list(get_json[1]):
#   data=[j[i] for i in title ]
#   value.append(data)

#value_frame=pd.DataFrame(value,columns=title)
value_frame=pd.DataFrame(list(get_json[1]))
#value_frame=value_frame.set_index("Country/other",inplace=True)
if st.checkbox('Show data in table'):
    st.dataframe(value_frame.style.highlight_max(axis=0))

if st.checkbox('show chart'):
    st.bar_chart(value_frame)


#'checking',np.histogram(value_frame['TotalCases'],bin=24,range=(0,24))[0]

#value_frame['Country/other']
'''
## VIEW INDIVIDUALLY :smile:
'''
options = st.multiselect(
        'Select',
         value_frame['Country/other']
        )

st.dataframe(value_frame[options])

