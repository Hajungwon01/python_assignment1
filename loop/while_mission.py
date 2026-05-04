# path : loop\\while_mission.py
# module : loop.while_mission

"""
함수명 : sungjuk_process()
prompt 변수를 while 문으로 반복해서 출력하면서, 입력되는 번호에 따라 sungjuk_list 의 아이템을 추가하거나 삭제하거나 출력되게 작성하시오.

sungjuk_list = [[12, '홍길동', 98], [15, '김유신', 87], [23, '황지니', 45]]
prompt = '''
            *** 원하는 메뉴 번호를 선택하세요. ***
            1. 추가
            2. 삭제
            3. 출력
            4. 끝내기
        '''
		
1 입력 : 리스트에 아이템 값들을 입력받아 추가함
  번호 : 24 (sno : int)
  이름 : 이순신 (sname : str)
  점수 : 100 (score : int)
  ==> 리스트에 추가 처리함    ==> 새로운 학생정보가 추가되었습니다.  출력함
2 입력 : 리스트의 인덱스 위치의 아이템 제거함
  현재 저장된 아이템의 갯수는 3개 입니다.  출력함
  제거할 아이템의 순번 : 3    ==> 입력받은 인덱스 위치의 아이템 제거함
  ==> 3번 위치의 아이템이 제거되었습니다.  출력함   ==> 현재 저장된 아이템의 갯수는 2개 입니다.  출력함
  ==> 잘못된 인덱스 입력시 :   '순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.' 출력함
3 입력 : 저장된 리스트 정보 아이템별로 출력함
  0 : [12, '홍길동', 98]
  1 : [15, '김유신', 87]
  2 : .......
4 입력 : while 반복 종료함
  성적관리 프로그램이 종료되었습니다.  출력함
"""

sungjuk_list = []

def sungjuk_process():
    print('\n-------------------성적관리 프로그램-------------------')
    prompt = '''
*** 원하는 메뉴 번호를 선택하세요. ***
1. 추가
2. 삭제
3. 출력
4. 끝내기
        '''
    while True:
        print(prompt)
        num = int(input('원하는 메뉴 입력 : '))
        if num == 1:
            info_add()
        if num == 2:
            info_remove()
        if num == 3:
            info_print()
        if num == 4: # while 반복 종료함
            print('\n성적관리 프로그램이 종료되었습니다.')
            break 
        if num not in [1, 2, 3, 4]:
            print('\n존재하지 않는 메뉴 번호입니다. 다시 입력해주세요!')
            continue
    return

# 리스트에 아이템 값들을 입력받아 추가함
def info_add():
    print('\n---------------------학생 정보 추가---------------------')
    sno = int(input('번호 : '))
    sname = input('이름 : ')
    score = int(input('점수 : '))
    student_info = [sno, sname, score]
    sungjuk_list.append(student_info) # 리스트에 추가 처리함

    print('\n새로운 학생 정보가 추가되었습니다.')
    return

# 리스트의 인덱스 위치의 아이템 제거함
def info_remove():
    print('\n---------------------학생 정보 삭제---------------------')    
    print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
    if len(sungjuk_list) == 0:
        print('현재 등록된 학생 정보가 없습니다. 삭제할 데이터가 존재하지 않습니다.')
        return
    if len(sungjuk_list) > 0:
        index_num = int(input('제거할 아이템의 순번 : '))

        while True:
            if 0 <= index_num < len(sungjuk_list):
                break
            print('순번이 잘못 입력되었습니다. 확인하고 다시 입력하세요.') # 잘못된 인덱스 입력 시
            index_num = int(input('제거할 아이템의 순번 : '))
        
        sungjuk_list.pop(index_num) # 입력받은 인덱스 위치의 아이템 제거함
        print(f'{index_num}번 위치의 아이템이 제거되었습니다.')
        print(f'현재 저장된 아이템의 갯수는 {len(sungjuk_list)}개 입니다.')
        return

# 저장된 리스트 정보 아이템별로 출력함
def info_print():
    print('\n---------------------학생 정보 출력---------------------')
    if len(sungjuk_list) == 0:
        print('현재 등록된 학생 정보가 없습니다. 출력할 데이터가 존재하지 않습니다.')
        return
    if len(sungjuk_list) > 0:   
        tmp = 0

        while tmp < len(sungjuk_list):
            print(f'{tmp} : {sungjuk_list[tmp]}')
            tmp += 1
        return