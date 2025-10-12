# 🧩 웹 토이 프로젝트 기획서

## 1. 프로젝트 개요
- **프로젝트 이름**:  crud_promt
- **한줄 설명**:  LLM에 api 요청을 하고 그에 대한 결과를 게시해주는 crud 게시판 생성
- **프로젝트 목표**:  
    1. LLM에 api 요청이 가능해야 한다.  
        * openai / claude / gemini
    2. image 업로드가 가능해야 한다.
    3. csv / xlsx와 같은 table data 업로드가 가능해야 한다.
    4. 동시에 여러개의 model에 api 요청이 가능해야 한다.
    5. 완료시 slack-bot으로 완료 알림이 발송되어야 한다.(Option)

---

## 2. 주요 기능 (Feature List)

| 기능명 | 설명 | 우선순위 (⭐) |
|:-------|:------|:-------------|
|api 요청 | LLM에 api 요청(비동기)을 보낸다. | ⭐️⭐️⭐️⭐️⭐️ |
|image 업로드 | api 요청을 보낼 경우 image 업로드가 가능해야 한다. | ⭐️⭐️⭐️ |
|table 업로드 | api 요청을 보낼 경우 table data(csv/xlsx) 업로드가 가능해야 한다. | ⭐️⭐️⭐️ |
|결과 다운로드 | LLM 답변 결과(raw json)를 다운로드 한다. | ⭐️⭐️⭐️ |
|slack-bot | api 요청을 보낼 경우 image 업로드가 가능해야 한다. | ⭐️ |

---

## 3. 사용자 시나리오 (User Flow)

- **시작 화면** → **게시글** → **게시글 클릭** → **각 게시글 확인** → **필요시 다운로드**
- **시작 화면** → **새 글 작성** → **각 prompt 설정 및 요청**

---

## 4. 기술 스택

| 구분 | 기술 | 비고 |
|:----|:----|:----|
| Frontend | React / Tailwind / Vite | |
| Backend | FastAPI | |
| DB | SQLite | |
| 배포 | fe:Vercel / be:미정  | |
| 기타 | Git / CI/CD | |

---

## 5. 화면 설계 (Wireframe)

- [ ] main 화면  
- [ ] create-post 화면
- [ ] detail-post 화면

> 간단히 손그림 또는 Figma, Excalidraw로 스케치해도 OK

---

## 6. API 설계 (간략)

| API | Method | 설명 | 요청 파라미터 | 응답 예시 |
|:----|:--------|:-----|:---------------|:-----------|
| `/upload` | POST | 파일 업로드 | system_prompt, user_prompt, table_data, image | `{ "status": "ok" }` |
| `/post/{id}` | GET | api 요청 결과 게시글 | id | `{ 추후 작성 }` |

---

## 7. 일정 계획 (MVP 중심)

| 주차 | 목표 | 세부 내용 |
|:----|:-----|:-----------|
| 1주차 | 기획 및 설계 | 기능 정의, 화면 설계 |
| 2주차 | FE/BE 기본 구조 세팅 | React + FastAPI 연결 |
| 3주차 | 핵심 기능 구현 | 업로드/처리/출력 |
| 4주차 | 배포 및 테스트 | Vercel 연결 |

---

## 8. 기대 효과 및 확장 계획

- **현재 목표**: 
    1. client가 안정적으로 prompt test를 진행한다.
- **추후 확장 아이디어**:  
    1. 사용자 로그인 기능
    2. AI 기반 prompt 추천/정제

---

## 9. 참고자료 / 영감

- **레퍼런스 서비스**:  
- **디자인 영감**:  
- **관련 라이브러리**:  

---

