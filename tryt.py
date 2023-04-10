import requests

url = "https://jspell-checker.p.rapidapi.com/check"

payload = {
	"language": "enUS",
	"fieldvalues": "thiss is intresting",
	"config": {
		"forceUpperCase": False,
		"ignoreIrregularCaps": False,
		"ignoreFirstCaps": True,
		"ignoreNumbers": True,
		"ignoreUpper": False,
		"ignoreDouble": False,
		"ignoreWordsWithNumbers": True
	}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "49807b3fd3msh96b96d700dc68f6p1ab4b7jsn854bae043bdd",
	"X-RapidAPI-Host": "jspell-checker.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)