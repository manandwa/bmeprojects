# Mobin Anandwala
# 1/9/2017
# this code will test a theory about retrying using the url http://www.battle.net as a test
# Code updaterd on 1/11/2017 with replacing Timeout with TimeoutError (and added exceptions instead of exception on line 23)
# Also added on 1/11/2017 to show all is good with the connection
import requests

url_test = raw_input('Please enter a url starting with http:// ')
retry_flag = 0

# Main code block
try:
	r = requests.get(url_test)
except requests.exceptions.ConnectionError:
	print('Error: No internet connection')
	exit()
except requests.exceptions.Timeout:
	print('Error: request timed out')
	retry_flag += 1
	print(retry_flag)
	while retry_flag != 0 and retry_flag <= 3:
		try:
			r = requests.get(url_test)
		except requests.exceptions.Timeout:
			print('Error: request timed out')
			retry_flag +=1
			print(retry_flag)
			break
		if retry_flag > 3:
			print('Server is timing out please try again in a few minutes')
			exit()
else:
	print('Connection Good!')
	retry_flag = 0
