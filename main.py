import requests
import numpy as np

# my first project
response = requests.get("https://api.github.com")
print("GitHub API status:", response.status_code)
print("You're set up correctly!")


