# import urllib.parse
import requests
import json
import bs4

URL_STACK = "http://api.stackexchange.com/2.2/"

class Questions(object):
	pass

def get_request(method, payload=None):
	'''REST API GET을 편하게 구현
	method = 메소드 이름, params = dictionary 형태로 받음.'''

	# params_encoded = urllib.parse.urlencode(params)

	url_target = URL_STACK + method
	
	data = requests.get(url_target, params = payload)

	return data
	

def search_query(query,tag = None):
	'''스택오버 플로우에서 search시 이 함수를 호출
	json object 반환'''
	params = {
		'site':'stackoverflow',
		'order':'desc',
		'sort':'votes',
		'intitle':query,
		'page':1,
		'pagesize':10,
		'tagged':tag
		}

	if tag is None: del params['tag']

	return get_request('search', params).json()

def get_accepted(search_result):
	'''일정한 조건에 맞는 search_result에서 accepted id set을 반환'''

	ids = []

	for item in search_result['items']:
		try:
			ids.append(item['accepted_answer_id'])
		except KeyError as e:
			print("accepted_answer_id가 없습니다.")
			continue

	return ids

def get_code_segment(answer_id):
	'''code에 해당하는 부분만 추출하는 함수'''
	page = requests.get('http://stackoverflow.com/a/' + str(answer_id)).text

	soup = bs4.BeautifulSoup(page, 'html.parser')

	div_id = 'answer-'+str(answer_id)
	#div_id에서 code 부분을 return, 없으면 None 반환
	codes = soup.find_all(id = div_id)[0].find_all('code')
	if codes == None:
		return codes
	else:
		return max([code.text for code in codes], key=len)





# example = search_query('quicksort','python')

example = search_query('quicksort','c++')
example_set = get_accepted(example)

example_code = get_code_segment(example_set[1])