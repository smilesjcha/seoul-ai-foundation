# 개발자에서 AI Native로: Claude Desktop으로 완성하는 업무 생산성 혁신

서울AI재단 5시간 강의를 위한 실전형 워크숍 저장소입니다. 이 저장소는 강의 자료와 실습 코드를 분리하지 않고, 수강생이 Claude Desktop을 활용해 문제 정의부터 PRD, 설계, 프로토타입 구현, 프롬프트 개선, 리뷰까지 한 흐름으로 따라올 수 있도록 설계했습니다.

## 강의 목적

- 개발자, PM, 실무자가 Claude Desktop을 활용해 AI Native 방식으로 일하는 흐름을 익힙니다.
- 민원/FAQ 자동화 시나리오를 바탕으로 문제 정의, 문서화, 구현, 품질 개선의 전체 사이클을 경험합니다.
- "AI에게 물어보는 사람"에서 "AI와 협업해 제품을 완성하는 사람"으로 사고방식을 전환합니다.

## 강사 소개 문구

아래 문구는 강의 자료, GitHub README, 소개 슬라이드에 바로 사용할 수 있습니다.

> 무신사 Agentic AI PM으로 일하며 AI 기반 제품 기획과 실행을 함께 담당하고 있습니다.  
> 서울시립대와 아주대학교에서 AI 부문 겸임교수로 활동하며, 현업과 교육 현장을 연결하는 실전형 AI 업무 방식과 제품 개발 방법론을 강의하고 있습니다.

짧은 버전:

> 무신사 Agentic AI PM / 서울시립대·아주대 AI 부문 겸임교수

## 폴더 구조

```text
.
├── README.md
├── package.json
├── tsconfig.base.json
├── .gitignore
├── apps
│   ├── api
│   │   ├── package.json
│   │   ├── tsconfig.json
│   │   └── src
│   │       ├── index.ts
│   │       ├── lib
│   │       │   ├── ai.ts
│   │       │   └── mockData.ts
│   │       └── routes
│   │           ├── faqs.ts
│   │           └── inquiries.ts
│   └── web
│       ├── package.json
│       ├── tsconfig.json
│       ├── vite.config.ts
│       ├── index.html
│       └── src
│           ├── main.tsx
│           ├── App.tsx
│           ├── api.ts
│           ├── types.ts
│           └── styles.css
├── packages
│   └── shared
│       ├── package.json
│       ├── tsconfig.json
│       └── src
│           └── index.ts
├── docs
│   ├── 00-course-overview.md
│   ├── 01-instructor-intro.md
│   ├── 02-detailed-curriculum.md
│   ├── 03-claude-desktop-setup.md
│   ├── 04-prd-faq-automation.md
│   ├── 05-architecture-faq-automation.md
│   ├── 06-teaching-runbook.md
│   ├── 07-faq-domain-guide.md
│   ├── 08-github-publishing-guide.md
│   ├── 09-ppt-design-system.md
│   ├── session-guides
│   │   ├── 01-session-script.md
│   │   └── 02-live-demo-checklist.md
│   └── templates
│       ├── design-doc-template.md
│       ├── ppt-slide-template.md
│       └── prd-template.md
├── claude
│   ├── README.md
│   ├── PROJECT_CONTEXT.md
│   ├── CLAUDE.md
│   ├── SESSION_COMMANDS.md
│   ├── prompts
│   │   ├── 01-problem-framing.md
│   │   ├── 02-prd-writing.md
│   │   ├── 03-system-design.md
│   │   ├── 04-implementation.md
│   │   ├── 05-prompt-tuning.md
│   │   └── 06-ppt-generation.md
│   └── templates
│       ├── issue-template.md
│       └── review-checklist.md
├── data
│   └── mock
│       ├── faqs.json
│       └── inquiries.json
└── scripts
    └── bootstrap.sh
```

## 권장 진행 방식

1. `docs/00-course-overview.md`로 전체 강의 구조를 먼저 이해합니다.
2. `docs/06-teaching-runbook.md`를 기준으로 강의 흐름과 데모 포인트를 점검합니다.
3. Claude Desktop 관련 설정과 프롬프트 자산은 `claude/` 폴더에서 관리합니다.
4. 수강생 실습은 `apps/api`, `apps/web`를 단계적으로 완성하는 방식으로 진행합니다.

## 실습 시나리오

실습 주제는 "민원/FAQ 자동화 보조 서비스"입니다.

- 입력: 시민 문의/민원 텍스트
- 처리: 카테고리 분류, FAQ 매칭, 응답 초안 생성, 검토 포인트 제안
- 출력: 운영자 검토용 응답 초안과 처리 상태

이 시나리오는 공공기관, CS 조직, 교육기관 모두에 설명하기 쉽고, Claude Desktop의 문서화 역량과 코딩 협업 역량을 함께 보여주기에 적합합니다.

## 로컬 실행 예시

```bash
npm install
npm run dev:api
npm run dev:web
```

기본 주소:

- API: `http://localhost:4000`
- Web: `http://localhost:5173`

## 이 저장소를 강의 자료로 확장하는 방법

- 슬라이드가 필요하면 `docs/*.md`를 바탕으로 PPT나 Notion 자료로 옮기면 됩니다.
- PPT 디자인 기준은 `docs/09-ppt-design-system.md`를 따릅니다.
- Claude Desktop 실습 지시문은 `claude/prompts/*.md`를 복사해 바로 사용할 수 있습니다.
- GitHub 공개용 저장소 소개는 이 README와 `docs/08-github-publishing-guide.md`를 함께 활용하면 됩니다.
