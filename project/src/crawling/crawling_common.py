import requests
import re
from urllib.parse import quote 

__author__ = 'Jee Hoon Lee'

CODE_TYPE = {'python' : 'py', 'cpp' : 'cpp'}


class Code(object):
	'''각 code의 내용, 점수 등을 가지고 있는 클래스'''

	type = None #python or cpp or else

	def __init__(self, content, added_point = 0, origin = None, *args, **kwargs):
		'''
		@DESC : 코드에 대한 컨텐츠, weight를 넣음.
		@added_point : weight를 계산할때 code가 가지고 있는 내용의 적합도와 질을
		 점수화한 결과를 넣는데, origin에 따라오는 added_point를 인수로 받음
		@origin : 어디서 들어온 코드인지 (stack or google) 확인
		'''
		self.content = content
		self.weight = self.calculate_common_weight(added_point) + self.calculate_type_bound_weight()
		self.origin = origin

		return None 

	def calculate_common_weight(self, added_point = 0):
		'''
		@DESC : 코드의 길이나 코드의 특징등을 반영하여 code의 적합도를 계산함,
			code specific
		@return : weight 반환
		'''
		return len(self.content) + added_point

	def calculate_type_bound_weight(self):
		'''
		@DESC : 코드의 언어 종류에 따른 특수한 weight들 계산
		@return : weight 반환
		'''
		return 0

class CodePython(Code):
	''' Python Specific Code'''
	type = CODE_TYPE['python']

	def __init__(self, content, added_point, origin = None, *args, **kwargs):
		Code.__init__(self, content, added_point, origin, kwargs)

	def calculate_type_bound_weight(self):
		'''
		@DESC : python만의 weight를 계산함
		'''
		weight = -self.num_imports() * 10 #import의 개수가 많으면 적합도 떨어짐

		return weight

	def num_imports(self):
		'''
		@DESC : import가 된 패키지의 갯수를 반환
		'''
		return len(re.findall(r'import \w+', self.content))




class CodeCPP(Code):
	'''CPP Specific Code'''
	type = CODE_TYPE['cpp']

	def __init__(self, content, added_point, origin = None, *args, **kwargs):
		Code.__init__(self, content, added_point, origin, kwargs)

	def calculate_type_bound_weight(self):
		'''
		@DESC : cpp만의 weight를 계산함
		'''
		weight = -self.num_includes() * 10 #import의 개수가 많으면 적합도 떨어짐

		return weight

	def num_includes(self):
		'''
		@DESC : 따옴표로 include된 헤더의 갯수를 반환
		'''
		return len(re.findall(r'include \"', self.content))


class Candidates(object):
	origin = None #stack or google or complex

	def __init__(self, codes = None):
		if codes is None:
			codes = []
		self.codes = codes #code 를 가지고 있는 list
	
	@staticmethod
	def get_request(url_target,method = '', payload=None):
		'''
		@DESC : REST API GET을 편하게 구현
		@url_target : http//.../
		@method : http//.../[method]/[payload]
		@return : raw data of get'''

		# params_encoded = urllib.parse.urlencode(params)

		
		url_target = url_target + quote(method)
		try:
			data = requests.get(url_target, params = payload, timeout = 5)
		except:
			raise BaseException

		return data

	@staticmethod
	def get_codes(contents, code_type, added_point = 0, origin = None):
		'''
		@DESC: type과 contents를 받아서 적절한 codes 뭉치를 반환시켜주는 함수
		@contents : code 내용
		@type : CODE_TYPE에 있는 code 종류
		'''
			
		if code_type == CODE_TYPE['python']:
			codes = [CodePython(i, added_point, origin) for i in contents if i is not None]
		elif code_type == CODE_TYPE['cpp']:
			codes = [CodeCPP(i, added_point, origin) for i in contents if i is not None]
		else:
			codes = [Code(i, added_point, origin) for i in contents if i is not None]

		return codes
	
	def sort_codes(self):
		'''
		@DESC: code 적합도가 높은 순으로 code를 정렬 해주는 함수
		@return: code 적합도가 가장 높은 code
		'''
		self.codes.sort(key= lambda x: x.weight, reverse = True)
		return None

	def __add__(self, other):
		'''
		@DESC : Candidates + Candidates 에 대한 정의
		'''
		new = Candidates(self.codes + other.codes)
		new.sort_codes()
		new.origin = 'COMPLEX'
		return new


