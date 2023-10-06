import requests
import json
import pandas as pd



def get_data():
    # Replace 'your_api_url' with the actual API URL
       api_url = "https://dotnetces.saas.appdynamics.com/controller/rest/applications/IIB%20Hello/metric-data?metric-path=Overall%20Application%20Performance%7CIIB%20MyNode%7CCalls%20per%20Minute&time-range-type=BEFORE_NOW&duration-in-mins=4320&output=json&rollup=false"

 

# Replace 'your_api_token' with the actual API token
       api_token = "eyJraWQiOiJhNDlkNzZjZi1jMTBiLTRkYzYtOGNmYy0wYmExNTY5ODYyNDQiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJBcHBEeW5hbWljcyIsImF1ZCI6IkFwcERfQVBJcyIsImp0aSI6ImpwNUF1T3lpaEFadkJUVkhCcXVQWUEiLCJzdWIiOiJNZXRyaWNEYXRhQXBpQ2xpZW50IiwiaWRUeXBlIjoiQVBJX0NMSUVOVCIsImlkIjoiOTA5ODM4ZmItNWYyYy00ZWFhLTkzOWUtNzMwMjVhN2NjZDdlIiwiYWNjdElkIjoiYTQ5ZDc2Y2YtYzEwYi00ZGM2LThjZmMtMGJhMTU2OTg2MjQ0IiwidG50SWQiOiJhNDlkNzZjZi1jMTBiLTRkYzYtOGNmYy0wYmExNTY5ODYyNDQiLCJhY2N0TmFtZSI6ImRvdG5ldGNlcyIsInRlbmFudE5hbWUiOiIiLCJmbW1UbnRJZCI6bnVsbCwiYWNjdFBlcm0iOltdLCJyb2xlSWRzIjpbXSwiaWF0IjoxNjk1MDk5OTY4LCJuYmYiOjE2OTUwOTk4NDgsImV4cCI6MTY5NzY5MTk2OCwidG9rZW5UeXBlIjoiQUNDRVNTIn0.MIiqtowKOL4Yit4ubEHXyr1sSC2Ba4n9zb9_FQgzs9U"

 

# Define headers with the API token
       headers = {"Authorization": f"Bearer {api_token}"}


# Make API request and retrieve JSON data
       response = requests.get(api_url, headers=headers)
#xml_content = response.content

       if response.status_code == 200:
           # print("sucessfully fetched the data")
            formatted_print(response.json())
       else:
            print(
                f"Hello person, there's a {response.status_code} error with your request")

   

def formatted_print(obj):
        for item in obj:
          my_dict={}
          list1={}
          list2={}
          list3={}
          my_dict['metricValues']=item.get('metricValues')
          #print my_dict
          #text=json.dumps(my_dict,sort_keys=True, indent=4)
        #text = json.dumps(obj, sort_keys=True, indent=4)
         # print(text)
        keys = my_dict.keys()
          #values = my_dict['metricValues'].values()
         # print(my_dict['metricValues'])
        metricdata = [{dic['startTimeInMillis']: dic['sum']} for dic in my_dict['metricValues']]
        #print(metricdata)
        index = 0
        for mdata in metricdata:
          #print(mdata)
        
          
          if (index >= 0 and index <= 23):
            list1.update(mdata)
          elif (index >=24 and index <= 47):
            list2.update(mdata)
          else:
            list3.update(mdata)
          index += 1
            
        print("list1: ")
        print(list1)
        print("list2: ")
        print(list2)
        print("list3: ")
        print(list3)
        
        #self.get_user_data(api)
def main():
      get_data()
    



if __name__ == "__main__":
    main()
