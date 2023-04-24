import requests

url = "https://mail-man.p.rapidapi.com/mail"

payload = {
	"email": "technicchannel007@gmail.com",
	"password": "Olavut200399",
	"from": "Company Name <technicchannel007@gmail.com>",
	"to": "technicchannel007@gmail.com",
	"subject": "Greetings",
	"message": "<p>Hello world<p>"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "49807b3fd3msh96b96d700dc68f6p1ab4b7jsn854bae043bdd",
	"X-RapidAPI-Host": "mail-man.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())