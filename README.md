# Python CLI Data Management System

CLI 환경에서 동작하는 간단한 데이터 관리 프로그램입니다.
학생 성적과 직원 정보를 관리하며, 파일 저장을 통해 데이터를 유지할 수 있습니다.

---

## Overview

이 프로젝트는 Python의 기본 개념을 활용하여 다음 기능을 구현하는 것을 목표로 합니다.

* 제어문 (while)
* 자료구조 (List, Dictionary)
* 모듈화
* 파일 입출력 (pickle)

---

## Project Structure

```
python_assignment1/
├── main.py
├── loop/
│   └── while_mission.py
└── fileio/
    └── fileio_mission.py
```

---

## Features

### 1. Student Management

* 학생 정보 추가 (학번, 이름, 점수)
* 인덱스 기반 삭제 (입력 검증 포함)
* 전체 출력 (while 반복문 사용)

```python
sungjuk_list = [
    [sno, sname, score]
]
```

---

### 2. Employee Management

* 직원 정보 추가 (사번 포함 8개 항목)
* 사번 기반 삭제 (유효성 검사 포함)
* 전체 출력
* 파일 저장 및 불러오기

```python
emp_dict = {
    emp_id: [employee_info]
}
```

```python
pickle.dump()
pickle.load()
```

---

## Key Points

* 잘못된 입력에 대해 재입력 처리
* 데이터가 없는 경우 예외 상황 처리
* 기능별 모듈 분리
* 파일 기반 데이터 저장 지원

---

## How to Run

```
python main.py
```

---

## Notes

* CLI 기반 프로그램입니다.
* 데이터는 `.dat` 파일로 저장됩니다.
