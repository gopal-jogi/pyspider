import requests
import datetime
from bs4 import BeautifulSoup

def get_upload_date(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # YouTube video upload date is stored in a meta tag with the name "date"
    upload_date_meta = soup.find('meta', {'itemprop': 'datePublished'})

    if upload_date_meta:
        upload_date_str = upload_date_meta['content']
        # Parse the date string and format it as "Month Day, Year"
        upload_date = datetime.datetime.strptime(upload_date_str, "%Y-%m-%dT%H:%M:%SZ")
        formatted_date = upload_date.strftime(""z%Y-%m-%d")
        return formatted_date
    else:
        return None

# Example usage
video_url = 'https://www.youtube.com/watch?v=SwSbnmqk3zY'  # Replace 'VIDEO_ID' with the actual video ID
upload_date = get_upload_date(video_url)

if upload_date:
    print(f'Upload Date: {upload_date}')
else:
    print('Upload date not found.')
