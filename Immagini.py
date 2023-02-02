import os
import openai
import urllib.request
from PIL import Image
openai.api_key = "API-KEY"
print("immagine:")
immagine=input()
response = openai.Image.create(
  prompt=immagine,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
urllib.request.urlretrieve(image_url, "nomeimmagine.png")
img = Image.open("nomeimmagine.png")
img.show()
os.remove("nomeimmagine.png")

