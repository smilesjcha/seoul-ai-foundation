# PPT Design System

## Design Direction

이 강의의 PPT는 "AI Native 업무 방식"을 다루지만, 시각적으로는 과하게 미래지향적이거나 장식적인 톤보다 신뢰감 있는 전문 강의 자료처럼 보여야 합니다. 흰색 배경, 검은색 본문, 남색에 가까운 파란색 강조색을 중심으로 구성합니다.

핵심 인상:

- 명확함
- 실무적 신뢰감
- 공공기관 강의에 어울리는 절제감
- 개발자와 PM 모두가 편하게 읽을 수 있는 구조

## Color System

### Primary Colors

| Token | Hex | Role |
| --- | --- | --- |
| `White` | `#FFFFFF` | 전체 슬라이드 배경 |
| `Black` | `#111111` | 제목, 본문, 주요 텍스트 |
| `Deep Blue` | `#123C7C` | 강조, 섹션 구분, 핵심 키워드, 도형 |

### Supporting Tints

아래 색상은 3색 원칙을 해치지 않는 범위에서만 사용합니다. 모두 `Deep Blue`의 투명도 또는 밝기 변형으로 취급합니다.

| Token | Hex | Role |
| --- | --- | --- |
| `Blue 90` | `#0D2E61` | 표지, 섹션 타이틀의 강한 강조 |
| `Blue 70` | `#2A5796` | 링크, 보조 강조 |
| `Blue 10` | `#EAF1FB` | 박스 배경, 코드 블록 배경, 다이어그램 면 |
| `Gray 80` | `#333333` | 보조 본문 |
| `Gray 20` | `#E5E7EB` | 구분선, 표 라인 |
| `Gray 5` | `#F7F8FA` | 아주 약한 영역 구분 |

### Color Rules

- 기본 배경은 항상 `White`입니다.
- 제목과 본문은 기본적으로 `Black`을 사용합니다.
- 강조는 `Deep Blue` 하나로 통일합니다.
- 중요한 숫자, 키워드, 세션 번호, 다이어그램의 핵심 노드에만 `Deep Blue`를 사용합니다.
- 한 슬라이드에서 파란색 강조 요소는 3개 이하를 권장합니다.
- 빨강, 초록, 노랑, 보라색 계열은 사용하지 않습니다.
- 그림자나 그라데이션은 사용하지 않거나 아주 약하게만 사용합니다.

## Typography

### Font

한국어 강의 자료 기준 권장 폰트:

- Primary: `Pretendard`
- Fallback: `Noto Sans KR`
- Code: `JetBrains Mono` 또는 `D2Coding`

### Type Scale

| Style | Size | Weight | Usage |
| --- | ---: | ---: | --- |
| Cover Title | 44-52pt | 700 | 표지 제목 |
| Section Title | 40-46pt | 700 | 세션 전환 슬라이드 |
| Slide Title | 28-34pt | 700 | 일반 슬라이드 제목 |
| Lead Text | 20-24pt | 500 | 핵심 문장 |
| Body | 16-18pt | 400 | 본문 |
| Caption | 11-13pt | 400 | 출처, 보조 설명 |
| Code | 12-15pt | 400 | 코드, 명령어 |

### Typography Rules

- 제목은 한 줄을 우선하되, 길면 의미 단위로 2줄까지 허용합니다.
- 본문은 문장보다 짧은 구문 중심으로 작성합니다.
- 한 슬라이드에 5개 이상의 긴 bullet을 넣지 않습니다.
- 강조 단어는 굵게 처리하거나 `Deep Blue`를 사용하되, 두 방식을 과도하게 중복하지 않습니다.
- 영어 제품명은 원문을 유지합니다: `Claude Desktop`, `Claude Code`, `GitHub`, `PRD`, `LLMOps`.

## Layout System

### Canvas

- Ratio: 16:9
- Size: Wide screen
- Safe margin: 좌우 56px, 상하 44px 이상
- Grid: 12-column grid를 가정하되, 실제 구현에서는 2-column / 3-column 중심으로 단순화합니다.

### Common Layouts

#### 1. Cover

- 흰색 배경
- 좌측 상단에 작은 강의 맥락: `서울AI재단 5시간 워크숍`
- 중앙 또는 좌측 중단에 큰 제목
- 하단에 강사 정보
- `Deep Blue`는 제목의 핵심 키워드 또는 얇은 라인에만 사용

#### 2. Section Divider

- 좌측에 큰 세션 번호
- 우측에 세션 제목과 오늘 만들 산출물
- 세션 번호는 `Deep Blue`
- 배경은 흰색 유지

#### 3. Concept Slide

- 상단 제목
- 중앙에 핵심 문장 1개
- 하단에 3개 이하의 보조 포인트

#### 4. Process Slide

- 좌에서 우로 흐르는 단계형 레이아웃
- 단계는 4-5개 이하
- 현재 강조 단계만 `Deep Blue` 사용

#### 5. Document Slide

- 좌측: 문서의 역할과 작성 기준
- 우측: PRD, 설계 문서, 프롬프트 예시 박스
- 문서 예시 박스 배경은 `Blue 10` 또는 `Gray 5`

#### 6. Code Demo Slide

- 좌측: 구현 목표
- 우측: 코드 또는 명령어 스니펫
- 코드 블록은 `Gray 5` 배경, 검은색 텍스트, 핵심 라인만 `Deep Blue`

#### 7. Review Slide

- 상단: 리뷰 질문
- 중앙: 체크리스트
- 우측 또는 하단: 개선 전/후 비교

#### 8. Wrap-up Slide

- 오늘의 핵심 메시지 3개
- 다음 실무 적용 액션 3개
- 마지막 문장은 짧고 강하게 구성

## Components

### Badge

- 배경: `Blue 10`
- 텍스트: `Deep Blue`
- 용도: `PRD`, `Design`, `Prototype`, `Prompt v2` 같은 산출물 표시

### Callout Box

- 배경: `Blue 10`
- 좌측 4px 라인: `Deep Blue`
- 용도: 핵심 원칙, 강사가 꼭 말해야 하는 문장

### Quote

- 검은색 본문
- 좌측에 `Deep Blue` 세로 라인
- 큰 따옴표 장식은 사용하지 않습니다.

### Table

- 헤더 텍스트: `Black`
- 헤더 하단 라인: `Deep Blue`
- 셀 구분선: `Gray 20`
- 배경색은 최소화합니다.

### Diagram Node

- 기본 노드: 흰색 배경, `Gray 20` 라인
- 핵심 노드: `Blue 10` 배경, `Deep Blue` 라인
- 연결선: `Gray 20`
- 방향 화살표: `Deep Blue`

## Slide Pattern For This Lecture

### Opening

1. Title
2. Instructor Intro
3. Today Outcome
4. Why AI Native Workflow

### Main Flow

1. Environment Setup
2. Problem Framing
3. PRD Writing
4. Architecture Design
5. Prototype Implementation
6. Prompt Quality Improvement
7. Code Review and Testing
8. Q&A and Expansion
9. Wrap-up

## Visual Language

### Use

- 얇은 라인
- 충분한 여백
- 명확한 제목
- 2-column 구조
- 단계형 프로세스
- 문서/코드/결과물의 실제 예시

### Avoid

- 어두운 전체 배경
- 과한 그라데이션
- 아이콘 남용
- 장식용 이미지
- 너무 많은 색상
- 긴 문단을 그대로 붙이는 방식

## Claude Code PPT Generation Rules

Claude Code로 PPT를 생성할 때는 아래 규칙을 반드시 포함합니다.

```md
PPT 디자인 시스템은 docs/09-ppt-design-system.md를 따른다.

색상은 흰색 배경, 검은색 텍스트, 남색 계열 Deep Blue 강조색을 중심으로 사용한다.
불필요한 색상, 어두운 배경, 과한 그라데이션, 장식용 이미지는 사용하지 않는다.

각 슬라이드는 하나의 메시지만 전달한다.
본문은 짧은 구문 중심으로 작성하고, 강의자가 말로 풀어낼 수 있도록 여백을 남긴다.

강의 주제는 Claude Desktop 기반 AI Native 업무 생산성 혁신이며,
문제 정의, PRD, 설계, 구현, 프롬프트 개선, 코드 리뷰의 흐름이 선명해야 한다.
```

## Sample Slide Specifications

### Cover

- Title: `개발자에서 AI Native로`
- Subtitle: `Claude Desktop으로 완성하는 업무 생산성 혁신`
- Meta: `서울AI재단 5시간 워크숍`
- Speaker: `무신사 Agentic AI PM · 서울시립대 / 아주대 AI 부문 겸임교수`

### Instructor Intro

- Title: `강사 소개`
- Main line: `AI 제품을 기획하고, 만들고, 운영해온 실무형 AI PM`
- Points:
  - `금융: AutoML Solution`
  - `의료: Computer Vision Ops`
  - `교육: LLMOps`
  - `현재: 무신사 Agent 서비스 기획`

### AI Native Workflow

- Title: `AI Native는 도구 사용법이 아니라 일의 순서입니다`
- Flow:
  - `Problem`
  - `PRD`
  - `Design`
  - `Prototype`
  - `Review`

### Final Slide

- Title: `오늘 가져갈 3가지`
- Points:
  - `AI에게 먼저 맥락을 읽힌다`
  - `문서가 구현 품질을 결정한다`
  - `자동화보다 검토 가능한 협업 구조가 먼저다`
