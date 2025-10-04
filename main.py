# Import necessary libraries
import requests
import os
from datetime import datetime

# --- CONFIGURATION ---
# It's better practice to use environment variables for sensitive data
# rather than hardcoding them directly in the script.
# On Windows, you can set them with: set USERNAME="your_username"
# On macOS/Linux, use: export USERNAME="your_username"
USERNAME = os.getenv("PIXELA_USERNAME", "YOUR_USERNAME") # Fallback for if env var isn't set
TOKEN = os.getenv("PIXELA_TOKEN", "YOUR_TOKEN") # Fallback for if env var isn't set
GRAPH_ID = "graph1" # It's okay to hardcode this if it's not sensitive

# --- API ENDPOINTS ---
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
pixel_creation_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

# --- HEADERS FOR AUTHENTICATION ---
# The API token is sent in the request header for security
headers = {
    "X-USER-TOKEN": TOKEN
}

# ------------------------------------------------------------------------------------
# The following sections are commented out.
# You only need to run them once to set up your user and graph.
# ------------------------------------------------------------------------------------

# ## STEP 1: Create a new Pixela user (only needs to be run once)
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
# try:
#     response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
#     response.raise_for_status() # This will raise an exception for HTTP errors (e.g., 4xx or 5xx)
#     print("User created successfully.")
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred during user creation: {e}")


# ## STEP 2: Create a new graph definition (only needs to be run once)
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai" # A nice purple color
# }
# try:
#     response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#     response.raise_for_status()
#     print("Graph created successfully.")
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred during graph creation: {e}")

# ------------------------------------------------------------------------------------
# --- DAILY OPERATIONS ---
# ------------------------------------------------------------------------------------

## STEP 3: Post a new pixel to the graph
# Get today's date in the required format YYYYMMDD
date_today = datetime.now().strftime("%Y%m%d")

# Get user input for the quantity and validate it
while True:
    quantity_input = input("How many kilometers did you cycle today? ")
    try:
        # Ensure the input can be converted to a float. The API expects a string.
        float(quantity_input)
        break # Exit the loop if input is a valid number
    except ValueError:
        print("Invalid input. Please enter a number (e.g., 5.5 or 10).")


# Prepare the data for the API POST request
pixel_data = {
    "date": date_today,
    "quantity": quantity_input,
}

# Make the POST request to add a pixel
try:
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    response.raise_for_status() # Check for errors
    print("Pixel posted successfully!")
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"An error occurred while posting the pixel: {e}")


## (Optional) STEP 4: Update an existing pixel using PUT
# This is useful if you made a mistake and need to correct a value.
# update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_today}"
#
# new_pixel_data = {
#     "quantity": "7.5"
# }
#
# try:
#     response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#     response.raise_for_status()
#     print("Pixel updated successfully.")
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred while updating the pixel: {e}")


## (Optional) STEP 5: Delete a pixel using DELETE
# delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date_today}"
#
# try:
#     response = requests.delete(url=delete_endpoint, headers=headers)
#     response.raise_for_status()
#     print("Pixel deleted successfully.")
#     print(response.text)
# except requests.exceptions.RequestException as e:
#     print(f"An error occurred while deleting the pixel: {e}")