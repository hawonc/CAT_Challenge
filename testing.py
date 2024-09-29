import requests
import matplotlib.pyplot as plt


base_url = 'http://127.0.0.1:3030'

example_string = '001 010 000 010 001 010 011 011 100'
body = {'string' : example_string}

response = requests.post(f'{base_url}/respond', json=body)


print(response.json())

# create a bar chart
plt.bar(["Faulty", "Not Faulty"], [response.json()['f'], response.json()['nf']])

# add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart')

# show the plot
plt.show()