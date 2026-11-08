# ==========================================
# ORIGINAL API TESTING EXAMPLE
# ==========================================
import requests

def retrieve_epic_photos(api_key, date):
    endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
    params = {"api_key": api_key}

    response = requests.get(endpoint_url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Data not received. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    photos = retrieve_epic_photos("DEMO_KEY", "2016-03-08")

    if photos:
        print(f"Photos on this date: {len(photos)}")
        print()
        for key, value in photos[0].items():
            print(f"{key}: {value}")
    else:
        print("No photos for this date.")
# ==========================================
# COMPLETED BIRTHDAY EARTH PROGRAM
# ==========================================
# Birthday Earth: NASA EPIC PROJECT
# Name: Zy'on Reynolds
# Description: This program will use NASA's EPIC API key to retrieve photographs of earth taken on a user's birhtday.
# It will randomly select a photograph and display its image link with infomation provided.
import requests
import random
# Function 1 - wWll be retrieveing NASA EPIC photos from the birthday the user enters.
def get_epic_photos(api_key, date):
  endpoint_url = f"https://api.nasa.gov/EPIC/api/natural/date/{date}"
  params = {"api_key": api_key}

  response = requests.get(endpoint_url, params=params)

  if response.status_code == 200:
                  return response.json()
  else:
    print(f"Data not received. Status code: {response.status_code}")
    return None
# Testing for Function 1
photos = get_epic_photos("DEMO_KEY", "2016-03-08")

if photos:
    print("Photos found:", len(photos))
else:
    print("No photos available.")
# Function 2 - The program will be selecting a random photo from the list.

def select_random_photo(photos):
    if photos:
        selected_photo = random.choice(photos)
        return selected_photo
    else:
        return None
