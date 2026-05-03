# 설계 문서: 민원/FAQ 자동화 보조 서비스

## 1. 시스템 개요

이 시스템은 운영자가 문의를 처리할 때 필요한 정보와 응답 초안을 빠르게 제공하는 내부 도구입니다. 학습 목적상 실제 LLM API 대신 Mock 분류 및 응답 생성 모듈로 시작하되, 추후 Claude API나 기타 LLM과 연결할 수 있도록 설계합니다.

## 2. 구성 요소

- Web App: 운영자 UI
- API Server: 문의 목록 조회, 상세 조회, 응답 초안 생성
- Mock Data Layer: FAQ와 문의 데이터 저장
- AI Layer: 카테고리 분류, FAQ 매칭, 응답 초안 생성

## 3. 데이터 흐름

1. Web App이 문의 목록을 요청한다.
2. API Server가 Mock Data에서 문의 목록을 반환한다.
3. 운영자가 특정 문의를 선택한다.
4. Web App이 상세 정보와 추천 결과를 요청한다.
5. AI Layer가 카테고리, FAQ, 초안을 조합해 결과를 반환한다.

## 4. 아키텍처 원칙

- 데이터와 AI 로직을 분리한다.
- 문서 기반 개발을 우선한다.
- LLM 연결 전에도 데모가 가능해야 한다.
- 운영자 승인 단계를 전제로 설계한다.

## 5. API 초안

### `GET /health`

- 서버 상태 확인

### `GET /api/faqs`

- FAQ 목록 조회

### `GET /api/inquiries`

- 문의 목록 조회

### `GET /api/inquiries/:id`

- 문의 상세 조회

### `POST /api/inquiries/:id/recommendation`

- 카테고리, 추천 FAQ, 응답 초안, 검토 포인트 생성

## 6. 데이터 모델

### FAQ

- `id`
- `category`
- `question`
- `answer`
- `tags`

### Inquiry

- `id`
- `channel`
- `status`
- `citizenName`
- `subject`
- `message`
- `receivedAt`
- `priority`

### Recommendation

- `inquiryId`
- `category`
- `matchedFaqIds`
- `draftReply`
- `reviewNotes`

## 7. 프롬프트 레이어 설계

실제 LLM 연동 시에는 아래 세 단계로 나누는 것이 좋습니다.

- 분류 프롬프트: 어떤 유형의 문의인지 식별
- 응답 프롬프트: FAQ와 정책을 반영한 초안 작성
- 검토 프롬프트: 운영자 확인 포인트 제안

## 8. 확장 방향

- 실제 DB 연동
- 상태 변경 API
- 승인 이력 관리
- FAQ 관리 화면
- 기관별 정책 템플릿 관리
- LLM 호출 로그와 평가 데이터 축적
