# Claude Session Commands

## 프로젝트 요약 요청

```md
이 저장소의 목적, 현재 구조, 오늘 실습에서 먼저 할 일 3가지를 정리해줘.
```

## PRD 기반 구현 요청

```md
docs/04-prd-faq-automation.md와 docs/05-architecture-faq-automation.md를 기준으로 apps/api의 MVP 기능을 먼저 구현해줘.
Mock 데이터는 data/mock을 사용하고, 작업 후 변경 파일과 이유를 요약해줘.
```

## UI 연결 요청

```md
apps/web에서 문의 목록, 상세, 추천 결과를 보여주는 운영자 화면을 만들어줘.
기존 API 계약을 유지하고, 강의용으로 읽기 쉬운 구조로 작성해줘.
```

## 품질 개선 요청

```md
응답 초안이 너무 일반적이야.
운영자 검토 포인트와 정책 확인 필요 문구를 강화하는 방향으로 개선해줘.
```

## PPT 생성 요청

```md
docs/00-course-overview.md, docs/01-instructor-intro.md, docs/02-detailed-curriculum.md, docs/06-teaching-runbook.md, docs/09-ppt-design-system.md를 기준으로 강의용 PPT를 만들어줘.

디자인은 흰색 배경, 검은색 텍스트, 남색 계열 Deep Blue 강조색 중심으로 구성해줘.
각 슬라이드는 하나의 메시지만 담고, 발표자 노트를 포함해줘.
상세 지시는 claude/prompts/06-ppt-generation.md를 따른다.
```

## 상세 원고 기반 PPT 생성 요청

```md
docs/10-ppt-lecture-outline.md와 docs/09-ppt-design-system.md를 기준으로 서울AI재단 5시간 강의용 PPT를 만들어줘.

Slide 1-77 구조를 유지하고, 각 슬라이드에는 제목, 본문, 도식 지시, 발표자 노트를 포함해줘.
강의와 실습이 자연스럽게 전환되도록 실습 슬라이드에는 사용할 파일 경로와 체크리스트를 명확히 넣어줘.
Mermaid 기반 flowchart, sequence diagram, ERD 장표는 docs/11-mermaid-diagram-guide.md를 참고해줘.
PRD 리뷰 장표에는 docs/12-prd-review-perspectives.md의 Leadership / UI/UX Designer / Engineer 관점을 반영해줘.
4명의 AI 개발자 인턴이 함께 실습하는 운영 방식은 docs/13-ai-developer-intern-lab-plan.md를 반영해줘.
상세 지시는 claude/prompts/07-ppt-from-detailed-outline.md를 따른다.
```
