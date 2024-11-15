import requests

def download_file(url, filename):
    """Download a file from the specified URL and save it locally."""
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f'File has been successfully downloaded and saved as {filename}')

# URL to the CSV file on GitHub
url = 'https://raw.githubusercontent.com/IBM/iot-predictive-analytics/master/data/iot_sensor_dataset.csv'

filename = 'data/iot_sensor_dataset.csv'

download_file(url, filename)
