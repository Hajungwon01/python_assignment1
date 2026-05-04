# 🐍 Python Assignment 1

> 파이썬 기초 개념(제어문, 자료구조, 모듈화, 파일 입출력)을 활용한 실습 프로젝트

---

## 📌 Overview

본 프로젝트는 Python의 핵심 개념을 직접 구현하며 익히기 위한 과제입니다.

### ✔ 사용 개념

* 제어문 (while loop)
* 자료구조 (List, Dictionary)
* 모듈화 (패키지 구조 설계)
* 파일 입출력 (pickle)

---

## 📂 Project Structure

```
python_assignment1/
│
├─ main.py
│   └─ 프로그램 실행 및 메뉴 컨트롤러
│
├─ loop/
│   └─ while_mission.py
│       └─ 성적 관리 프로그램
│
└─ fileio/
    └─ fileio_mission.py
        └─ 직원 정보 관리 서비스
```

---

## ⚙️ Main Module (`main.py`)

* `menu()` 함수로 전체 프로그램 흐름 제어
* 사용자 입력 기반 기능 실행

| 입력 | 기능         |
| -- | ---------- |
| 1  | 성적 관리 프로그램 |
| 2  | 직원 관리 서비스  |
| 9  | 프로그램 종료    |

👉 잘못된 입력 시 예외 메시지 출력

---

## 📊 Loop Module - 성적 관리 프로그램

📄 `while_mission.py`
🔧 함수: `sungjuk_process()`

### 🗂 데이터 구조

```python
sungjuk_list = []
# [학번, 이름, 점수]
```

### ✨ 주요 기능

* **추가 (info_add)**

  * 학번, 이름, 점수 입력 → 리스트 저장

* **삭제 (info_remove)**

  * 인덱스 기반 삭제
  * 데이터 없을 경우 예외 처리
  * 잘못된 입력 시 재입력 유도

* **출력 (info_print)**

  * while문을 활용한 전체 출력

---

## 🏢 File I/O Module - 직원 관리 서비스

📄 `fileio_mission.py`
🔧 함수: `emp_process()`

### 🗂 데이터 구조

```python
emp_dict = {}
# {사번: [직원정보]}
```

### ✨ 주요 기능

* **직원 추가 (emp_add)**

  * 사번, 이름, 급여, 부서 등 8개 정보 저장

* **직원 삭제 (emp_remove)**

  * 사번 입력 → 삭제
  * 존재하지 않는 사번 → 재입력

* **전체 출력 (emp_print)**

  * while문 기반 전체 데이터 출력

* **파일 저장 (emp_file_save)**

  ```python
  pickle.dump()
  ```

* **파일 불러오기 (emp_file_read)**

  ```python
  pickle.load()
  ```

---

## 🚀 Key Features

* ✅ 데이터 유효성 검사
* ✅ 예외 처리 강화
* ✅ 무한 루프 기반 안정적인 실행

---

## ▶️ How to Run

```bash
python main.py
```

---

## 💡 Notes

* 사용자 입력 기반 CLI 프로그램입니다.
* 파일 저장 시 `.dat` 형식으로 생성됩니다.
* 잘못된 입력에도 프로그램이 종료되지 않도록 설계되었습니다.

---
