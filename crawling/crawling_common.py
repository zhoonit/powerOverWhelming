import requests

__author__ = 'Jee Hoon Lee'

CODE_TYPE = {'python' : 'py', 'cpp' : 'cpp'}


class Code(object):
	'''각 code의 내용, 점수 등을 가지고 있는 클래스'''

	type = None #python or cpp or else

	def __init__(self, content, added_point = None, origin = None, **kwargs):
		'''
		@DESC : 코드에 대한 컨텐츠, weight를 넣음.
		@added_point : weight를 계산할때 code가 가지고 있는 내용의 완성도와 질을
		 점수화한 결과를 넣는데, origin에 따라오는 added_point를 인수로 받음
		@origin : 어디서 들어온 코드인지 (stack or google) 확인
		'''
		self.content = content
		self.weight = self.calculate_weight(added_point)
		self.origin = origin

		return None 

	@classmethod
	def calculate_weight(cls, added_point = 0):
		'''
		@DESC : 코드의 길이나 코드의 특징등을 반영하여 code의 완성도를 계산함,
			code specific
		@return : weight 반환
		'''
		pass

class CodePython(object):
	type = CODE_TYPE['python']

	def __init__(self, **kwargs)
		Code.__init__(self, kwargs)


class CodeCPP(object):
	type = CODE_TYPE['cpp']


class Candidates(object):
	origin = None #stack or google

	def __init__(self):
		self.codes = [] #code 를 가지고 있는 list

	@staticmethod
	def get_request(url_target,method = None, payload=None):
		'''
		@DESC : REST API GET을 편하게 구현
		@url_target : http//.../
		@method : http//.../[method]/[payload]
		@return : raw data of get'''

		# params_encoded = urllib.parse.urlencode(params)

		url_target = url_target + method
		
		data = requests.get(url_target, params = payload)

		return data

	@staticmethod
	def get_best_code(self):
		'''
		@DESC: 
		'''
		pass
