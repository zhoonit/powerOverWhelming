import sys

from . import crawling_stack
from . import crawling_google

def search(query, type = ''):
	'''
	@query : 키워드
	@type : 코드의 종류, CODE_TYPE 참조
	'''
	stack = crawling_stack.CandidatesStack(query, type)
	google = crawling_google.CandidatesGoogle(query, type)

	results = stack + google

	return [i.content for i in results.codes]

# if __name__ == '__main__':
# 	search('quick sort', 'python')