import requests


out_file = "./temp/client.jpg"


local = "http://localhost:5000/landmarks"


img = "C:\\Users\\alper\\Desktop\\a.jpg"
# './static/images/about/02.jpg'

with open(img, 'rb') as f:

	r = requests.post(local, files={'image': f}, stream=True)

	if r.status_code == 200:

		print("Request OK")

		print(r.text)
	else:
		print('Error')