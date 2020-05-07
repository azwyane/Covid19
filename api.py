import streamlit as st
import requests
#import numpy as np
import pandas as pd
import datetime

'''
# apicovid2019


**Fetch apicovid2019 from github**

*This is a usecase of the apicovid2019 from
[Azwyane](https://github.com/azwyane/apicovid2019)*

## Fetch entire data :zap:
'''

@st.cache
def get_data():
    return (requests.get("https://apicovid2019.azurewebsites.net"),datetime.datetime.now())

st.spinner('Fetching latest data')
get,time=get_data()
st.success(f"Fetched latest data at {time}, server time NP.")
get_json=get.json()

page=st.sidebar.selectbox("Navigate",["Home","View Specific Data"])

if page=="Home":
    
    '''
    # Built with streamlit with :heart:

    - To view latest data please goto the **_right side_** 
    panel and hit clear cache and re-run which would fetch
    the latest data and display the response in you desired 
    view.

    - To view the data individually either by country or continent
    please refer to the **_left side_** panel and make your choices.

    '''






    first_index=list(get_json[0])
    second_index=list(get_json[1])
    ttile=list(second_index[0])
    third_index=list(get_json[2])

    f'''
    # WORLWIDE CASES:
    ###   Total Coronavirus Cases:{((get_json[0])[first_index[0]])}
    ###   Total Worldwide Deaths :{((get_json[0])[first_index[2]])}
    ###   Total Recovered        :{((get_json[0])[first_index[4]])}
    '''

    #st.write(list(get_json[1]))
    value=[]
    title=[x for x in list(list(get_json[1])[0])]


    #value_frame=pd.DataFrame(value,columns=title)
    value_frame=pd.DataFrame(list(get_json[1]))
    value_frame=value_frame.set_index("Country/other",inplace=False)
    value_frame=value_frame.replace({"None":0,"":0})
    #if st.checkbox('View worldwide data in table'):
    #    st.dataframe(value_frame.style.highlight_max(axis=0))
    st.dataframe(value_frame,width=100000)

    drops=value_frame.drop(columns=[
        "NewCases",
        "NewDeaths",
        "ActiveCases",
        "Serious",
        "Totalcases/1Mpop",
        "Deaths/1Mpop",
        "TotalTests",
        "Tests/1Mpop"
        ])

    if st.checkbox('show cases,deaths,recoveries in same chart'):
        st.bar_chart(drops.convert_dtypes(),use_container_width=False)
else:
    value_frame=pd.DataFrame(list(get_json[1]))
    value_frame=value_frame.set_index("Country/other",inplace=False)
    value_frame=value_frame.replace({"None":0,"":0})

    pageSecond=st.sidebar.selectbox("viewing",["CountrySpecific","Continents"])
    
    if pageSecond=="CountrySpecific":
        
        '''
        ## VIEWING INDIVIDUALLY 
        '''

        options = st.sidebar.selectbox(
            'Select the country to view',
            value_frame.index)
        #options = st.multiselect(
        #        'Select',
        #         value_frame.index
        #        )

        #my_placeholder = st.empty()
        #my_placeholder.table(value_frame.loc[options])

        st.table(value_frame.loc[options])

        #this gives the transpose of the dataframe
        transpose=value_frame.T
        column=[x for x in value_frame.columns]
        #column
        first=value_frame["TotalCases"]
        first=first.T
        #first

        
    else:
        
        '''
        # view cases per continent
        '''
        v_frame=pd.DataFrame(list(get_json[2]))
        v_frame=v_frame.set_index("Country/other",inplace=False)
        v_frame=v_frame.drop(columns=[
        "Totalcases/1Mpop",
        "Deaths/1Mpop",
        "TotalTests",
        "Tests/1Mpop"
        ])

        if st.checkbox('View continent data in table'):
            st.table(v_frame.style.highlight_max(axis=0))



'''
# For Developers

Those who are willing to view the response format of the api used in this
project can view which is:
'''
if st.checkbox('Show json data'):
    st.json(get_json) #writes raw data to screen commented for now
'''
If you are interested in using the api then 
go visit *[Azwyane](https://github.com/azwyane/apicovid2019)*
for more info and documentation.
'''


