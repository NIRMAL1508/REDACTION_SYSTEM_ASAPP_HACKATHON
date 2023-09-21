import requests

url = 'http://127.0.0.1:5000/submit_text'

data = {'text': 'John Smith is a 35-year-old software engineer based in 123 SanFrancisco,California. He holds a bachelors degree in computer science from Stanford University and has been working in the tech industry for over a decade. John is known for his strong problem-solving skills and his ability to work effectively in cross-functional teams.His phone number us +91 24344 23433.His email is asjdgjh@psg.com.He was born on 19/02/2000.'}

response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    print('Modified text', result['Modified text'])
    print('Maps', result['mappings'])
else:
    print('Error:', response.status_code, response.json())