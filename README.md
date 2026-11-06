# birthday-earth-nasa-epic

This program uses NASA's EPIC API to retrieve photographs of Earth taken on a specific date. It will display the total number of available photos and information about the first photograph returned by NASA.

## How it works
- retrieve_epic_photos(api_key, date): Connects to Nasa's EPIC API and retrieves photos for a selected date.
- select_random_photo(photos): Randomly select one photo from the avaiable photos.
- create_photo_url(photo, date): Creates a link to view the selected NASA photograph.

## How to run
1. Install requests: pip install requests
2. Run: python birthday_earth.py
3. Uses "DEMO_KEY" by default. Swap in your own key
   from api.nasa.gov for higher rate limits.

## Built with
Python, requests and the NASA EPIC API
