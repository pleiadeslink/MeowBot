import requests, json, os
from mastodon import Mastodon

# Mastodon token and domain
mastodon = Mastodon(
    access_token = 'asdf',
    api_base_url = 'https://botsin.space/'
)

# Get the image URL
URL = json.loads(requests.get('http://aws.random.cat/meow').content)["file"]

# Save image from URL
img = requests.get(URL).content
with open("cat.png", "wb") as png:
    png.write(img)

# Upload PNG file to Mastodon
media = mastodon.media_post("cat.png")
mastodon.status_post("#cats #catsofmastodon #mastocats", media_ids=media)

# Delete the image, since it is no longer needed
os.remove("cat.png")