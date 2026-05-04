# main.py
# 파이썬 과제 1
# 과제 실행 테스트용 스크립트

import loop.while_mission as lw
import fileio.fileio_mission as ff

def menu():
    prompt = '''
*** 파이썬 과제 1 ***
1. while 실습문제
2. fileio 실습문제
9. 과제 실행 테스트 끝내기
'''
    while True:
        print(prompt)
        num = int(input('원하는 메뉴 입력 : '))
        if num == 1:
            lw.sungjuk_process()
        if num == 2:
            ff.emp_process()
        if num == 9:
            break
        if num not in [1, 2, 9]:
            print('\n존재하지 않는 메뉴 번호입니다. 다시 입력해주세요!')
            continue
    return


if __name__ == '__main__':
    menu()