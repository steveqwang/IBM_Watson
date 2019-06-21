import urllib3
import requests
import json

wml_credentials={
  "password": "e368db61-e407-4f00-b387-16270b4795f4",
  "url": "https://us-south.ml.cloud.ibm.com",
  "username": "25f9726e-af0e-409b-8de3-b0a70136db50"
}

headers = urllib3.util.make_headers(basic_auth='{username}:{password}'.format(username=wml_credentials['username'],password=wml_credentials['password']))
url = '{}/v3/identity/token'.format(wml_credentials['url'])
response = requests.get(url,headers = headers)
mltoken = json.loads(response.text).get('token')

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

array_of_values_to_be_scored = [41,'Travel_Rarely',1102,'Sales',1,2,'Life Sciences',1,1,2,'Female',94,3,2,'Sales Executive',4,'Single',5993,19479,8,'Y','Yes',11,3,1,80,0,8,0,1,6,4,0,5]
another_array_of_values_to_be_scored = [49,'Travel_Frequently',279,'Research & Development',8,1,'Life Sciences',1,2,3,'Male',61,2,2,'Research Scientist',2,'Married',5130,24907,1,'Y','No',23,4,4,80,1,10,3,3,10,7,1,7]

payload_scoring = {"fields": ["Age", "BusinessTravel", "DailyRate", "Department", "DistanceFromHome", "Education", "EducationField", "EmployeeCount", "EmployeeNumber", "EnvironmentSatisfaction", "Gender", "HourlyRate", "JobInvolvement", "JobLevel", "JobRole", "JobSatisfaction", "MaritalStatus", "MonthlyIncome", "MonthlyRate", "NumCompaniesWorked", "Over18", "OverTime", "PercentSalaryHike", "PerformanceRating", "RelationshipSatisfaction", "StandardHours", "StockOptionLevel", "TotalWorkingYears", "TrainingTimesLastYear", "WorkLifeBalance", "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager"], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/fdb308b1-730c-4c98-90eb-0a5257a7cf21/deployments/e73790d2-0612-4124-b7bc-c04242eb11b7/online', json=payload_scoring, headers=header)
print("Scoring response")
#print(json.loads(response_scoring.text))

parsed = json.loads(response_scoring.text)

for value in parsed['values']:
  fields = value[:30]
  confidence = value[:32]
  prediction = value[34]
  values = value[35]
  print("\nEmployee Attrition: {}\n\tConfidence: {}\n\tFields: {}".format(prediction,zip(confidence, values), fields))