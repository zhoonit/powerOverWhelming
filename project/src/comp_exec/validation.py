import subprocess
import os
import tempfile

excode = '''
#include <stdio.h>

int main(){
	printf("hello world\\n");
	return 0;
}

'''

excode_fail = '''

#include <stdio.h>

int main(){
	printf("hi")
	return 0;
}
'''

def find_util():
	'''
	@DESC: gcc path를 찾아주는 헬퍼 함수
	@return: gcc path
	'''

	try:
		finding_path = os.path.dirname(os.path.abspath(__file__))
	except NameError as e:
		finding_path = os.getcwd()


	while 'project' != os.path.basename(finding_path):
		finding_path = os.path.abspath(os.path.join(finding_path, '..'))

	try:
		gcc_path = finding_path + '\\util\\cpp\\MinGW64\\bin\\gcc'
	except NameError as e:
		raise NameError

	return gcc_path
	


def str_to_temp(code_string, code_ext):
	'''
	@DESC: code string을 받아서 temp file로 만들어주는 함수
	@code_string: code 내용
	@code_type: code_type
	'''
	file = open(next(tempfile._get_candidate_names())+'.'+code_ext, 'w+b')

	file.write(code_string.encode('mbcs'))
	file.flush()

	return file


def get_compile_result(temp_des, code_ext):
	'''
	@DESC : 컴파일해서 에러나, 결과를 스트링 형태로 반환, 사용한 파일은 모두 제거한다.
	@temp_des : temp file이 있는 descriptor
	@code_ext : code의 type 에 따른 다른 반응을 한다.
	@return : result string과 error bit 를 튜플 형태로 넘김.
	'''
	source_name = os.path.abspath(temp_des.name)

	if code_ext == 'cpp':
		exe_name = os.getcwd()+'\\'+next(tempfile._get_candidate_names())
		try:
			command = [find_util(), source_name , '-o', exe_name]

			result = subprocess.check_output(command, stderr = subprocess.STDOUT, shell=True)

			result = 'compile details: %s \nprint output: \n %s'%(
						 result.decode('mbcs') if result else 'None' , subprocess.check_output(exe_name, shell=True).decode('mbcs'))
					

			error_bit = 0

			#clean up process
			os.remove(exe_name + '.exe')

		except subprocess.CalledProcessError as e:
			result = 'error code: %d \n out: \n %s'%(e.returncode, e.output.decode('mbcs'))

			error_bit = 1
	

	#source clean up
	temp_des.close()
	os.remove(source_name)


	return result, error_bit

def test():
	pass


def validation(code_string, code_ext):
	save_file = str_to_temp(code_string, code_ext)

	return get_compile_result(save_file, code_ext)	
	
	