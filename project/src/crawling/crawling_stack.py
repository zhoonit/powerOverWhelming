# import urllib.parse
import json
import bs4
from crawling_common import *

URL_STACK = "http://api.stackexchange.com/2.2/"
STACK_ADDED_POINT = -1

class CandidatesStack(Candidates):
	'''
	Stackover flow에서 question을 넣으면 answer set을 반환시킴
	 '''
	origin = 'STACK'

	def __init__(self, query, code_type = None, *args, **kwargs):
		'''
		@code_type : CODE_TYPE[] 참조
		'''

		Candidates.__init__(self)

		data = CandidatesStack.search_query(query, code_type)


		question_set = CandidatesStack.get_accepted(data)
		code_set = [CandidatesStack.get_code_segment(question)
					for question in question_set if question is not None]

		self.codes = Candidates.get_codes(code_set, code_type, STACK_ADDED_POINT, 'STACK')
		
		self.sort_codes()
		
		return None

		#deprecated
		# self.question_set = CandidatesStack.get_accepted(data)
		# self.code_set = [CandidatesStack.get_code_segment(question) for question in self.question_set]
		# self.relavent_code_set = self.code_set[0]
		# self.longest_code_set = max(self.code_set, key=len)

	@staticmethod
	def search_query(query,tag = None):
		'''
		스택오버 플로우에서 search시 이 함수를 호출
		@query : 질문
		@tag : tag, 코드 타입을 반환
		@return : query를 넣으면 반환되는 json object
		'''
		if tag == 'cpp':
			tag = 'c++'

		params = {
			'site':'stackoverflow',
			'order':'desc',
			'sort':'votes',
			'intitle':query,
			'page':1,
			'pagesize':10,
			'tagged':tag
			}

		if tag is None: del params['tagged']

		return Candidates.get_request(URL_STACK,method = 'search', payload = params).json()

	@staticmethod
	def get_accepted(search_result):
		'''
		@DESC : search_result를 받아서 그중 accepted 된 answer 만 추출
		@search_result : search_query에서 넘어오는 json object
		@return : id 리스트
		'''
		ids = []

		for item in search_result['items']:
			try:
				ids.append(item['accepted_answer_id'])
			except KeyError as e:
				# print("accepted_answer_id가 없습니다.")
				continue
		if len(ids) == 0:
			raise BaseException
		return ids

	@staticmethod
	def get_code_segment(answer_id):
		'''
		@DESC : code에 해당하는 부분만 추출하는 함수
		@answer_id : stackoveflow answer_id
		@return :  code에 해당하는 블럭중 가장 긴 블럭, 없을 경우 none 반환
		'''
		page = Candidates.get_request('http://stackoverflow.com/a/' + str(answer_id) ).text

		soup = bs4.BeautifulSoup(page, 'html.parser')

		div_id = 'answer-'+str(answer_id)

		#div_id에서 code 부분을 return, 없으면 None 반환
		codes = soup.find_all(id = div_id)[0].find_all('code')
		if codes == None:
			return codes
		else:
			try:
				return max([code.text for code in codes], key=len)
			except ValueError:
				return None



# example = CandidatesStack('quick sort')
# example.Code