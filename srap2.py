
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import Counter
from datetime import datetime, timedelta

# Function to scrape video URLs from the T-Series YouTube channel within a specified date range
def scrape_video_urls(start_date, end_date):
    # Parse start_date and end_date to datetime objects
    end_date = datetime.now() - timedelta(days=int(end_date.split()[0]) * 30)  # Assuming 1 month = 30 days
    start_date = datetime.now() - timedelta(days=int(start_date.split()[0]) * 30)  # Assuming 1 month = 30 days

  # Install chromedriver if not already installed
    path = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(path)  # Initialize Chrome webdriver
    driver.get("https://www.youtube.com/@tseries/videos")  # Navigate to T-Series YouTube channel videos page
    
    video_urls = []
    
    # Scroll down the page to load all videos (you might need to adjust this based on the website's behavior)
    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        new_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    
    # Extract video URLs and upload dates
    video_elements = driver.find_elements(By.CSS_SELECTOR, "#video-title")
    for video_element in video_elements:
        video_url = video_element.get_attribute("href")
        upload_date = extract_upload_date(video_element)
        
        # Check if the upload date is within the specified range
        if start_date <= upload_date <= end_date:
            video_urls.append(video_url)

    # Count the most frequently repeated character in video IDs
    video_ids = [extract_video_id(url) for url in video_urls]
    most_common_char = find_most_common_character(video_ids)

    # Construct the output dictionary in the specified format
    output_dict = {"Most Frequently Repeated Character": most_common_char,
                   "Video URLs within Specified Date Range": video_urls}

    driver.quit()  # Close the Chrome webdriver

    return output_dict

# Function to extract upload date from video element
def extract_upload_date(video_element):
    # Extract and return upload date logic here, for example:
    # upload_date = video_element.find_element(By.CSS_SELECTOR, "span.style-scope.ytd-grid-video-renderer").text
    # Parse upload_date to a datetime object and return it
    pass

# Function to extract video ID from video URL
def extract_video_id(video_url):
    # Extract and return video ID logic here, for example:
    video_id = video_url.split("v=")[1]
    return video_id
    

# Function to find the most frequently repeated character in a list of strings (case-insensitive)
def find_most_common_character(strings):
    # Concatenate all strings and convert to lowercase
    concatenated_string = ''.join(strings).lower()
    # Use Counter to count character occurrences
    char_counts = Counter(concatenated_string)
    # Find the most common character
    most_common_char = char_counts.most_common(1)[0][0]
    return most_common_char

# Main function
if __name__ == "__main__":
    start_date = "2 months ago"
    end_date = "5 months ago"
    output_dict = scrape_video_urls(start_date, end_date)
    
    # Print output in the specified format
    for key, value in output_dict.items():
        print(f"Key: {key} Value: {value}")
