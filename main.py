import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

axieIds = [2322,3124,3224]
newAxieIds = [3331,4442,5553]
axie_images = []
new_axie_images = []

for i in range(3):
    url = f'https://assets.axieinfinity.com/axies/{str(axieIds[i])}/axie/axie-full-transparent.png'
    response = Image.open(BytesIO(requests.get(url).content))
    axie_images.append(cv2.cvtColor(np.array(response), cv2.COLOR_RGB2BGR))

for i in range(3):
    url = f'https://assets.axieinfinity.com/axies/{str(newAxieIds[i])}/axie/axie-full-transparent.png'
    response = Image.open(BytesIO(requests.get(url).content))
    new_axie_images.append(cv2.cvtColor(np.array(response), cv2.COLOR_RGB2BGR))

axie_stack1 = cv2.hconcat([axie for axie in axie_images])
axie_stack2 = cv2.hconcat([axie for axie in new_axie_images])
final = np.vstack([axie_stack1, axie_stack2])
cv2.imwrite('final.png', final)