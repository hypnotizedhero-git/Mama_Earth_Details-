import requests
import pandas as pd


valid=True
name='error'
data=[]
for i in range(91002200000,91002228073):
  url=f'https://mmrth-nd-api.honasa-production.net/v1/content/sankalptaru-tree/{i}'
  valid=name not in resp.keys()
  resp=requests.get(url).json()
  if(valid):
    data.append(resp)

df=pd.DataFrame(data)
df.to_csv('trial.csv')
