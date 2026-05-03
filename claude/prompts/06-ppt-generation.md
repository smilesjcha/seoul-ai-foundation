# PPT Generation Prompt

```md
너는 강의용 PPT를 만드는 시니어 프레젠테이션 디자이너이자 AI PM이야.

목표:
서울AI재단 5시간 강의 <개발자에서 AI Native로: Claude Desktop으로 완성하는 업무 생산성 혁신>의 발표용 PPT를 생성한다.

반드시 참고할 문서:
- docs/00-course-overview.md
- docs/01-instructor-intro.md
- docs/02-detailed-curriculum.md
- docs/03-claude-desktop-setup.md
- docs/04-prd-faq-automation.md
- docs/05-architecture-faq-automation.md
- docs/06-teaching-runbook.md
- docs/09-ppt-design-system.md

디자인 시스템:
- 배경은 흰색을 기본으로 한다.
- 텍스트는 검은색을 기본으로 한다.
- 강조색은 남색에 가까운 파란색 `#123C7C`를 사용한다.
- 전체 색상은 흰색, 검은색, Deep Blue 중심으로 제한한다.
- 과한 그라데이션, 장식용 이미지, 어두운 배경, 불필요한 색상은 사용하지 않는다.
- 슬라이드마다 메시지는 하나만 선명하게 전달한다.
- 본문은 긴 문장보다 짧은 구문 중심으로 작성한다.

강사 소개 반영:
- 무신사 Agentic AI PM
- 서울시립대 / 아주대 AI 부문 겸임교수
- 금융 AutoML Solution, 의료 Computer Vision Ops, 교육 LLMOps 서비스 경험
- 현재 무신사에서 Agent 서비스 기획 진행

권장 슬라이드 구성:
1. 표지
2. 강사 소개
3. 오늘의 목표
4. 왜 AI Native Workflow인가
5. 5시간 전체 흐름
6. 환경 세팅
7. 민원/FAQ 자동화 문제 정의
8. 사용자 흐름
9. PRD 작성 방법
10. PRD 예시
11. 설계 문서화 방법
12. 아키텍처 개요
13. 프로토타입 구현 1: API와 Mock Data
14. 프로토타입 구현 2: UI 연결
15. Prompt 품질 개선
16. Edge Case 대응
17. 코드 리뷰와 테스트
18. 실무 확장 방향
19. Q&A
20. Wrap-up

산출물:
- 편집 가능한 pptx 파일
- 각 슬라이드는 제목, 핵심 메시지, 발표자 노트가 포함되어야 한다.
- 발표자 노트에는 강사가 말할 핵심 포인트를 3-5문장으로 적는다.
```
