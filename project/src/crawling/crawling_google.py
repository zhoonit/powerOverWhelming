# import urllib.parse
import bs4
import re
from ..crawling.crawling_common import *

URL_GOOGLE = "https://www.google.co.kr/search?q="
GOOGLE_ADDED_POINT = 10

class CandidatesGoogle(Candidates):
	'''google용 candidtaes'''
	origin = 'GOOGLE'
	
	def __init__(self, query, type = None):
		'''
		@query : keyword
		@type : CODE_TYPE[]
		'''
		Candidates.__init__(self)

		
		results = self.get_result(query, type)
		code_set = self.get_codes_from_result(results)

		self.codes = Candidates.get_codes(code_set, type, GOOGLE_ADDED_POINT, origin = 'GOOGLE')
		self.sort_codes()

		return None


	@staticmethod
	def pack_query(query, type):
		'''query를 받아서 get parameter를 pack함
		@query: 키워드
		@type: code file type from CODE_TYPE
		'''
		params = {
			'Host':'www.google.co.kr',
			'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
			'Accept-Language':'ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3',
			'Accept-Encoding':'gzip, deflate, br',
			'Connection': 'keep-alive',
			'Upgrade-Insecure-Requests':"1"
			}

		return params



	@staticmethod
	def get_codes_from_result(soup):
		'''
		@DESC : page soup를 받아서 result가 담겨있는 주소를 반환
		@soup : get_result에서 나온 구글 서치 결과
		@return : result code content
		'''
		results = [i['href'] for i in soup.select('h3.r > a')] # get search result
		
		urls = [re.search(r'q=([^&]+)&',result).group(1) for result in results]

		codes = []
		for url in urls:
			if re.search(r'github\.com', url) is not None:
				url = re.sub(r'github\.com', 'raw.githubusercontent.com', url) #github는 raw로 바꿔줌
				url = re.sub(r'\/blob', '', url)
			try:
				target_text = Candidates.get_request(url).text
				if re.search(r'<!DOCTYPE html>', target_text) is not None:
					target_text = ""
				codes.append(target_text)

			except (requests.exceptions.ConnectTimeout, requests.exceptions.ReadTimeout):
				continue

		return codes


	@staticmethod
	def get_result(query, type):
		'''
		@query : 키워드
		@type : CODE_TYPE
		@return : page
		'''
				
		url_target = URL_GOOGLE+query+' filetype:'+type
		# print(url_target)
		page = Candidates.get_request(url_target,payload = CandidatesGoogle.pack_query(query, type)).text

		soup = bs4.BeautifulSoup(page, 'html.parser')
		return soup






#example = CandidatesGoogle('quick sort', 'cpp')

