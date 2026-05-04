# path : fileio\\fileio_mission.py
# module : fileio.fileio_misson

# 파일입출력, 반복문, 리스트, 딕셔너리 사용 실습문제 요구사항
"""
while 문을 사용해서 prompt 가 반복해서 출력되도록 함
입력된 번호에 따라서 emp_list 에 아이템 추가, 삭제, 출력 처리하도록 함
emp_list는 딕셔너리

prompt = '''
        *** 직원 정보 관리 서비스 ***
        1. 새 직원정보 추가
        2. 직원정보 삭제
        3. 전체 출력
        4. 파일에 저장
        5. 파일로 부터 직원정보 읽어오기
        9. 서비스 끝내기
        '''
		
1 이 입력되면 리스트에 추가할 아이템 정보를 키보드로 입력받아서 추가함
  사번 : 200 (empid : str)
  이름 : 홍길순 (empname : str)
  주민번호 : 851225-1234567 (empno : str)
  이메일 : hong77@test.com (email : str)
  전화번호 : 010-1234-5678 (phone : str)
  급여 : 3800000 (salary : int)
  직급 : 대리 (job : str)
  부서 : 개발부 (dept : str)
  => 사번은 키로 해서 딕셔너리에 직원정보를 리스트로 저장함
     사번 : [사번, 이름, 주민번호, 이메일, 전화번호, 급여, 직급, 부서]
2 입력 시 :
    삭제할 사번 : 200
    => 딕셔너리에서 해당 사번의 아이템 제거함
    => '200 번 사번의 직원 정보가 삭제되었습니다.' 출력함
3 입력 시 :
    딕셔너리의 각 아이템의 정보를 한줄씩 출력되게 함
    사번 : [리스트 정보]
    사번 : [리스트 정보]
    ....
4 입력 시 :
    딕셔너리 상태 그대로 파일에 저장되도록 함
    저장할 파일명 : employees.dat
    ==> 'employees.dat 파일에 성공적으로 저장되었습니다.' 출력됨
5 입력 시 :
    읽을 파일명 : employees.dat
    => 파일의 내용을 읽어서 딕셔너리(emp_dict)에 저장하고 출력되게 함
9 입력 시 :
    while 문 끝내면서 프로그램 종료되게 함
    => 종료시 '직원 관리 프로그램을 종료합니다.' 출력함

함수명 : emp_process()
"""

import os
import pickle

emp_dict = {}

def emp_process():
    print('\n-------------------직원관리 프로그램-------------------')
    prompt = '''
*** 직원 정보 관리 서비스 ***
1. 새 직원정보 추가
2. 직원정보 삭제
3. 전체 출력
4. 파일에 저장
5. 파일로 부터 직원정보 읽어오기
9. 서비스 끝내기
    '''
    while True:
        print(prompt)
        num = int(input('원하는 메뉴 입력 : '))
        if num == 1:
            emp_add()
        if num == 2:
            emp_remove()
        if num == 3:
            emp_print()
        if num == 4:
            emp_file_save()
        if num == 5:
            emp_file_read()
        if num == 9: # while 반복 종료함
            print('\n직원 관리 프로그램을 종료합니다.')
            break 
        if num not in [1, 2, 3, 4, 5, 9]:
            print('\n존재하지 않는 메뉴 번호입니다. 다시 입력해주세요!')
            continue
    return

# 새 직원정보 추가
def emp_add():
    print('\n---------------------직원 정보 추가---------------------')

    empid = input('사번 : ')
    empname = input('이름 : ')
    empno = input('주민번호 : ')
    email = input('이메일 : ')
    phone = input('전화번호 : ')
    salary = int(input('급여 : '))
    job = input('직급 : ')
    dept = input('부서 : ')
    emp_list = [empid, empname, empno, email, phone, salary, job, dept] 

    # 사번은 키로 해서 딕셔너리에 직원정보를 리스트로 저장함
    emp_dict[empid] = emp_list # 사번 : [사번, 이름, 주민번호, 이메일, 전화번호, 급여, 직급, 부서]
    print('\n새로운 직원 정보가 추가되었습니다.')
    return

# 직원정보 삭제
def emp_remove():
    print('\n---------------------직원 정보 삭제---------------------')
    if len(emp_dict) == 0:
        print('현재 등록된 직원 정보가 없습니다. 삭제할 데이터가 존재하지 않습니다.')
        return
    if len(emp_dict) > 0:
        remove_key = input('삭제할 사번 : ')

        while True:
            if remove_key in emp_dict:
                break
            print('\n사번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.') # 잘못된 사번 입력 시
            remove_key = input('삭제할 사번 : ')
        
        emp_dict.pop(remove_key) # 딕셔너리에서 해당 사번의 아이템 제거함
        print(f'\n{remove_key}번 사번의 직원 정보가 삭제되었습니다.')
        return

# 전체 출력
def emp_print():
    print('\n---------------------직원 정보 출력---------------------')
    if len(emp_dict) == 0:
        print('현재 등록된 학생 정보가 없습니다. 출력할 데이터가 존재하지 않습니다.')
        return
    if len(emp_dict) > 0:
        tmp = 0

        empid_list = list(emp_dict.keys())

        while tmp < len(empid_list):
            print(f'{empid_list[tmp]} : {emp_dict[empid_list[tmp]]}') # 딕셔너리의 각 아이템의 정보를 한줄씩 출력되게 함
            tmp += 1
        return

# 파일에 저장
def emp_file_save():
    print('\n----------------------파일에 저장----------------------')
    str_path = input('저장할 파일명 : ')
    f = open(str_path, 'wb')
    pickle.dump(emp_dict, f) # 딕셔너리 상태 그대로 파일에 저장되도록 함
    f.close()

    print(f'\n{str_path} 파일에 성공적으로 저장되었습니다.')
    return

# 파일로부터 직원정보 읽어오기
def emp_file_read():
    print('\n---------------------직원 정보 로드---------------------')
    str_path = input('읽을 파일명 : ')
    f = open(str_path, 'rb')
    read_data = pickle.load(f) 
    f.close()

    # 파일의 내용을 읽어서 딕셔너리(emp_dict)에 저장하고 출력되게 함
    emp_dict = read_data 
    print(emp_dict)
    return