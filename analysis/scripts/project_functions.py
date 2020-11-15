import pandas as pd
import numpy as np

def load_and_process(file):
    """
    Load and clean a dataframe
    
    Parameters
    ----------
    An Url or a path to a file
    
    Returns
    -------
    A dataframe
    
    """  
    
   #Method chain 1 (Load data, drop columns, rename columns, change dataType)
    
    df1 = (pd.read_csv(file)
      .drop(columns = ['Unnamed: 0','DateType','ResidenceCity','ResidenceCounty', 'ResidenceState',
                       'DeathCity','DeathCounty','Location','LocationifOther','DescriptionofInjury','InjuryPlace',
                       'InjuryCity','InjuryCounty','InjuryState','OtherSignifican', 'Other','DeathCityGeo',
                       'ResidenceCityGeo','InjuryCityGeo' ], axis = 1)
      .rename(columns={"Amphet": "Amphetamine", "Tramad": "Tramadol"}))
    
    
    #Method chain 2(cleaning, change datatype)
    
    df2 = (df1.dropna()
           .drop_duplicates(['ID'])
           .assign(Date = pd.to_datetime(df1["Date"]))
           .astype({'Age': 'int64', 'Fentanyl_Analogue': 'int64'})
           .drop(index =[507,2808,3741,3801,62,583,4199,4384,263,456,3213,3499,4794])
           .astype({'Fentanyl': 'int64', 'Morphine_NotHeroin': 'int64', 'AnyOpioid': 'int64'}))
    return df2