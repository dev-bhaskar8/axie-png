import requests
import cv2
import numpy as np
from PIL import Image
from io import BytesIO

axieIds = [3333,4444,5555]
newAxieIds = [3333,1111,2222]
axie_images = []
new_axie_images = []
new_axie_stats = []
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
for i  in range(3):
    if axieIds[i] != newAxieIds[i]:
        final = cv2.arrowedLine(final, (550+1300*(i),800), (550+1300*(i),1000),(0, 0, 255), 10, tipLength = 0.5)
        url = f'https://api.axie.technology/getaxies/{newAxieIds[i]}'
        response = requests.get(url).json()
        parts=str(response['class'])+' Axie of parts - '
        for i in range(2,6):
            parts = parts+str(response['parts'][i]['name'])+',' 
        parts+=' and of stats - '+ str(response['stats']).split("\'__typename")[0][1:-2]
        print(parts[:-1])
cv2.imwrite('final.png', final)