"""All 77 slides — mapped 1:1 from docs/10-ppt-lecture-outline.md."""

# Section dividers (PART 2~10) reuse slide numbers 8/15/22/30/40/49/56/63/68.
# Slide 1 is the cover.

SLIDES = [
    # ====================================================== PART 1. Intro
    {
        "no": 1,
        "type": "cover",
        "title": "개발자에서 AI Native로",
        "body": [
            "서울AI재단 5시간 실습형 워크숍",
            "문제 정의부터 PRD, 설계, 구현, 리뷰까지 한 번에 경험한다",
        ],
        "note": (
            "오늘은 Claude Desktop을 단순히 질문에 답하는 도구로 쓰는 시간이 아닙니다. "
            "문제를 정의하고, 문서를 만들고, 코드를 구현하고, 품질을 검토하는 전체 업무 흐름을 "
            "AI와 함께 끝까지 경험해보겠습니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 2,
        "type": "two_column",
        "title": "강사 소개",
        "body": [
            "무신사 Agentic AI PM",
            "서울시립대 / 아주대 AI 부문 겸임교수",
            "금융 AutoML Solution / 의료 Computer Vision Ops / 교육 LLMOps 경험",
            "현재 무신사에서 Agent 서비스 기획 진행",
        ],
        "right_kind": "cards",
        "right_cards": [
            {"title": "ML", "body": ["AutoML Solution", "금융 도메인"]},
            {"title": "DL", "body": ["Computer Vision Ops",
                                       "의료 도메인"]},
            {"title": "LLM", "body": ["LLMOps Service", "교육 도메인"]},
            {"title": "Agent", "body": ["Agentic AI PM",
                                          "무신사 (현재)"], "accent": True},
        ],
        "note": (
            "저는 금융, 의료, 교육 도메인에서 각각 AutoML, Computer Vision Ops, "
            "LLMOps 서비스를 만들어왔고, 현재는 무신사에서 Agent 서비스 기획을 진행하고 "
            "있습니다. 오늘 강의는 이론 소개보다 실제 업무를 AI Native하게 바꾸는 과정에 "
            "초점을 두겠습니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 3,
        "type": "card_grid",
        "title": "오늘의 큰 질문",
        "card_cols": 2,
        "cards": [
            {"title": "AI에게 일을 맡긴다는 것",
             "body": ["사람이 무엇을 정의해야 하나"]},
            {"title": "문서와 코드의 연결",
             "body": ["문서는 어떻게 구현 기준이 되나"]},
            {"title": "Claude Desktop의 역할",
             "body": ["어떤 업무 파트너가 될 수 있나"]},
            {"title": "사람의 판단 영역",
             "body": ["사람은 어디서 검토해야 하나"], "accent": True},
        ],
        "note": (
            "오늘의 질문은 'Claude를 어떻게 쓰나요?'보다 조금 더 큽니다. "
            "AI와 함께 일할 때 사람이 무엇을 정의하고, AI에게 무엇을 맡기고, 다시 사람이 어디서 "
            "검토해야 하는지를 보는 것이 핵심입니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 4,
        "type": "concept",
        "title": "오늘 만들 결과물",
        "lead": "5시간이 끝나면 작은 제품 개발 패키지가 남는다",
        "body": [
            "Problem Statement",
            "PRD v1",
            "설계 문서 (Flowchart, Sequence, ERD)",
            "민원/FAQ 자동화 프로토타입",
            "Prompt v2 + 리뷰 노트와 확장 아이디어",
        ],
        "note": (
            "5시간이 끝났을 때 남는 것은 단순한 데모 화면 하나가 아닙니다. "
            "문제 정의 문서, PRD, 설계 문서, 코드, 프롬프트 개선안, 리뷰 노트까지 하나의 "
            "작은 제품 개발 패키지를 갖게 됩니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 5,
        "type": "schedule",
        "title": "5시간 전체 시간표",
        "schedule_rows": [
            ("13:00–13:30", "환경 세팅 & OT", "Claude Desktop, GitHub clone, 실습 환경 구성", "실행 환경"),
            ("13:30–14:00", "문제 정의 & 서비스 이해", "FAQ/민원 자동화 시나리오, 사용자 흐름 정의", "Problem Statement"),
            ("14:00–14:30", "PRD 작성", "기능 정의, 사용자 플로우, 성공 기준", "PRD v1"),
            ("14:30–14:40", "Break", "휴식", "—"),
            ("14:40–15:10", "설계 문서화", "아키텍처, Flow, Sequence, 테이블", "설계 문서"),
            ("15:10–15:50", "프로토타입 구현 1", "Mock data, API 연결", "기능 v1"),
            ("15:50–16:00", "Break", "휴식", "—"),
            ("16:00–16:40", "프로토타입 구현 2", "응답 생성, UI 연결", "기능 v2"),
            ("16:40–17:10", "AI 품질 개선", "Prompt 튜닝, Edge case", "Prompt v2"),
            ("17:10–17:30", "코드 리뷰 & 테스트", "Claude/Codex 리뷰, 리팩토링", "리뷰 노트"),
            ("17:30–17:50", "Q&A / 확장 논의", "실무 적용, 확장 방향", "인사이트"),
            ("17:50–18:00", "Wrap-up", "핵심 정리, Best Practice", "최종 결과"),
        ],
        "body": ["슬라이드는 설명 자료이자 다음 작업으로 넘어가는 안내판"],
        "note": (
            "오늘은 문서만 만들다가 끝나지도 않고, 코드만 치다가 끝나지도 않습니다. "
            "13시부터 18시까지 문제 정의, PRD, 설계, 구현, 품질 개선, 리뷰를 한 번의 흐름으로 "
            "경험합니다. 중간중간 실습 시간이 들어가므로, 슬라이드는 설명 자료이면서 동시에 "
            "다음 작업으로 넘어가는 안내판 역할을 합니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 6,
        "type": "process",
        "title": "오늘의 실습 시나리오",
        "flow_items": ["시민 문의", "FAQ 매칭", "응답 초안", "운영자 검토"],
        "body": [
            "민원/FAQ 자동화 보조 서비스",
            "반복 문의를 분류하고 FAQ와 연결",
            "응답 초안을 생성한다",
            "운영자가 검토하고 확정한다",
        ],
        "note": (
            "오늘 다룰 예제는 민원/FAQ 자동화입니다. 공공기관, 고객지원, 교육기관 어디에나 "
            "설명하기 쉬운 문제이고, AI가 사람을 대체하기보다 운영자의 반복 업무를 줄이는 "
            "방향으로 설계하기 좋습니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 7,
        "type": "concept",
        "title": "오늘의 핵심 메시지",
        "lead": "AI Native는 도구 목록이 아니라 일의 순서다",
        "body": [
            "좋은 결과는 좋은 질문보다 좋은 맥락에서 나온다",
            "문서가 구현 품질을 결정한다",
            "자동화보다 검토 가능한 협업 구조가 먼저다",
            "빠른 개발의 핵심은 작게 나누고 자주 검토하기",
        ],
        "note": (
            "오늘 계속 반복될 메시지는 이것입니다. AI를 잘 쓰는 개발자는 프롬프트를 길게 쓰는 "
            "사람이 아니라, 일을 잘게 나누고 맥락을 잘 제공하고 검토 기준을 명확히 주는 "
            "사람입니다. 그래서 AI Native 개발은 속도와 검토를 함께 설계하는 일입니다."
        ),
        "speak_seconds": "80초",
    },
    # ====================================================== PART 2.
    {
        "no": 8,
        "type": "section_divider",
        "title": "AI Native Workflow란 무엇인가",
        "part_no": "02",
        "section_title": "AI Native Workflow와\nClaude Desktop",
        "section_sub": "AI를 흐름 안에 배치한다",
        "section_outcomes": [
            "AI Native의 정의와 기존 방식과의 차이",
            "Claude Desktop에 일을 잘 맡기는 공식",
            "프로젝트 폴더 기반 협업 감각",
        ],
        "body": [
            "AI를 별도 도구가 아니라 업무 흐름 안에 배치하는 방식",
            "문제 정의, 문서화, 구현, 검토를 연결한다",
            "사람이 방향과 기준을 잡고, AI가 반복과 초안을 담당한다",
            "AI와 함께 빠르게 가설을 검증하는 개발 방식",
        ],
        "note": (
            "AI Native는 AI를 마지막에 붙이는 자동화가 아닙니다. 처음 문제를 정의하는 순간부터 "
            "AI와 함께 일하고, 중간 산출물을 다음 단계의 입력으로 계속 연결하는 방식입니다."
        ),
        "speak_seconds": "90초",
    },
    {
        "no": 9,
        "type": "comparison",
        "title": "기존 업무 방식과의 차이",
        "columns": [
            {"title": "Question-based",
             "body": ["필요한 순간마다 AI에게 질문",
                       "산출물은 사람이 다시 정리",
                       "맥락이 매번 끊김"]},
            {"title": "Workflow-based",
             "body": ["산출물이 다음 단계의 입력",
                       "문서와 코드가 이어짐",
                       "사람은 기준과 검토 담당"],
             "accent": True},
        ],
        "body": ["산출물이 다음 산출물의 재료가 되는 구조를 만든다"],
        "note": (
            "초기 AI 활용은 대개 질문 단위입니다. 하지만 실제 업무 생산성이 올라가는 지점은 "
            "질문 하나의 답이 아니라, 산출물들이 다음 산출물의 재료가 되는 구조를 만들 때입니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 10,
        "type": "cycle",
        "title": "Claude Desktop의 역할",
        "cycle_items": [
            "Project Context",
            "Docs",
            "Code",
            "Review",
        ],
        "body": [
            "프로젝트 폴더 맥락을 읽고, 문서와 코드를 함께 다루며, 검토 기준을 반영해 개선한다",
        ],
        "note": (
            "Claude Desktop의 강점은 대화창 하나에서 끝나는 것이 아니라, 프로젝트 폴더의 "
            "문서와 코드를 함께 보며 작업할 수 있다는 점입니다. 그래서 오늘은 Claude를 "
            "문서 작성 도구가 아니라 프로젝트 파트너처럼 써보겠습니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 11,
        "type": "badge_row",
        "title": "Claude에게 일을 잘 맡기는 기본 공식",
        "badges": ["역할", "맥락", "산출물", "제약", "검토 기준"],
        "body": [
            "역할 — 어떤 관점으로 일할지",
            "맥락 — 어떤 문서와 파일을 기준으로 볼지",
            "산출물 — 무엇을 만들어야 하는지",
            "제약 — 무엇은 하지 말아야 하는지",
            "검토 기준 — 성공 여부를 어떻게 판단할지",
        ],
        "note": (
            "프롬프트를 잘 쓴다는 것은 멋진 문장을 쓰는 것이 아닙니다. 역할, 맥락, 산출물, "
            "제약, 검토 기준을 빠뜨리지 않는 것이 훨씬 중요합니다."
        ),
        "speak_seconds": "90초",
    },
    {
        "no": 12,
        "type": "two_column",
        "title": "나쁜 요청과 좋은 요청",
        "body": [
            "나쁜 요청 — '앱 만들어줘'",
            "좋은 요청 — 'PRD와 설계 문서를 기준으로 문의 목록 API부터 구현해줘'",
            "차이는 구체성보다 작업 단위와 기준",
        ],
        "right_kind": "cards",
        "right_cards": [
            {"title": "Before", "body": [
                "앱 만들어줘",
                "쉽게 빠르게",
                "기준 문서 없음",
            ]},
            {"title": "After", "body": [
                "PRD와 설계 문서를 기준으로",
                "문의 목록 API부터",
                "변경 파일과 이유 요약",
            ], "accent": True},
        ],
        "note": (
            "좋은 요청은 길기만 한 요청이 아닙니다. AI가 바로 작업할 수 있을 만큼 기준 "
            "문서와 작업 범위를 정확히 지정한 요청입니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 13,
        "type": "tree",
        "title": "실습 저장소 구조 읽기",
        "body": [
            "docs — 강의 문서와 설계 문서",
            "claude — Claude Desktop용 맥락과 프롬프트",
            "apps/api — 백엔드 API",
            "apps/web — 운영자 UI",
            "data/mock — FAQ와 문의 Mock 데이터",
        ],
        "tree_lines": [
            "/",
            "├─ docs/",
            "│   ├─ 00-course-overview.md",
            "│   ├─ 04-prd-faq-automation.md",
            "│   └─ 05-architecture-faq-automation.md",
            "├─ claude/",
            "│   ├─ CLAUDE.md",
            "│   ├─ PROJECT_CONTEXT.md",
            "│   └─ prompts/",
            "├─ apps/",
            "│   ├─ api/   (Express + TS)",
            "│   └─ web/   (React)",
            "└─ data/",
            "    └─ mock/",
            "        ├─ faqs.json",
            "        └─ inquiries.json",
        ],
        "note": (
            "오늘의 저장소는 강의 자료와 실습 코드가 분리되어 있지 않습니다. "
            "Claude가 문서를 읽고 코드를 고치고, 다시 문서 기준으로 리뷰할 수 있도록 "
            "일부러 한 폴더 안에 구성했습니다."
        ),
        "speak_seconds": "90초",
    },
    {
        "no": 14,
        "type": "card_grid",
        "title": "데모 1 · 프로젝트 요약과 4인 역할 분담",
        "card_cols": 2,
        "cards": [
            {"title": "AI PM",
             "body": ["문제 정의, PRD",
                       "비목표/리스크 관리"], "accent": True},
            {"title": "UX Builder",
             "body": ["사용자 흐름, UI",
                       "Flowchart 담당"]},
            {"title": "Backend Engineer",
             "body": ["API, 데이터 모델",
                       "Sequence/ERD 담당"]},
            {"title": "Quality Engineer",
             "body": ["테스트, Edge case",
                       "리뷰 노트 담당"]},
        ],
        "body": [
            "Claude Desktop에 프로젝트 폴더를 열고 claude/PROJECT_CONTEXT.md를 먼저 읽힌다",
            "참고 — docs/13-ai-developer-intern-lab-plan.md",
        ],
        "note": (
            "첫 데모는 구현이 아닙니다. 먼저 Claude에게 이 프로젝트가 무엇인지 요약하게 "
            "하겠습니다. 그리고 네 명의 인턴이 있다면 역할을 나눕니다. 한 명은 문제와 PRD, "
            "한 명은 사용자 흐름과 UI, 한 명은 API와 데이터, 한 명은 품질과 테스트를 맡으면 "
            "실습이 훨씬 유기적으로 진행됩니다."
        ),
        "speak_seconds": "실연 포함 5분",
    },
    # ====================================================== PART 3.
    {
        "no": 15,
        "type": "section_divider",
        "title": "왜 민원/FAQ 자동화인가",
        "part_no": "03",
        "section_title": "문제 정의 &\n서비스 이해",
        "section_sub": "기능 목록 이전에 문제와 사용자",
        "section_outcomes": [
            "Problem Statement",
            "사용자별 불편 분리",
            "자동화 가능/제외 범위",
        ],
        "body": [
            "반복 문의가 많다",
            "기준 문서와 FAQ가 존재한다",
            "완전 자동화보다 운영자 보조가 적합하다",
            "공공기관과 CS 조직 모두 이해하기 쉽다",
        ],
        "note": (
            "민원/FAQ 자동화는 AI 교육 예제로 매우 좋습니다. 반복성과 기준이 있고, 동시에 "
            "사람이 검토해야 하는 지점도 분명하기 때문입니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 16,
        "type": "comparison",
        "title": "자동화할 수 있는 일과 하면 안 되는 일",
        "columns": [
            {"title": "할 수 있는 일",
             "body": ["분류", "FAQ 매칭", "응답 초안", "검토 포인트 제안"],
             "accent": True},
            {"title": "조심할 일",
             "body": ["정책 판단", "민감 민원 처리",
                       "개인정보 포함 문의"]},
            {"title": "하지 말아야 할 일",
             "body": ["운영자 승인 없는 자동 발송"]},
        ],
        "body": ["자동화 가능성만 보지 말고, 자동화 위험 영역도 함께 정한다"],
        "note": (
            "실무에서 중요한 것은 자동화 가능성만 보는 것이 아닙니다. 무엇을 자동화하면 "
            "위험한지도 함께 정해야 합니다. 이 경계가 있어야 조직에서 신뢰를 얻을 수 있습니다."
        ),
        "speak_seconds": "90초",
    },
    {
        "no": 17,
        "type": "card_grid",
        "title": "사용자 관점으로 문제 보기",
        "card_cols": 3,
        "cards": [
            {"title": "시민",
             "body": ["빠르고 정확한 답변"]},
            {"title": "운영자",
             "body": ["반복 답변 시간 단축",
                       "검토 가능한 초안"], "accent": True},
            {"title": "관리자",
             "body": ["처리량과 품질 편차",
                       "리스크 모니터링"]},
        ],
        "body": ["문제 정의는 기능 목록이 아니라, 누가 어떤 불편을 겪는지 분리해서 보는 일"],
        "note": (
            "문제 정의는 기능 목록이 아닙니다. 누가 어떤 불편을 겪고 있는지를 분리해서 보는 "
            "일입니다. 오늘은 시민, 운영자, 관리자 관점으로 나눠보겠습니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 18,
        "type": "process",
        "title": "Problem Statement의 역할",
        "flow_items": ["Problem", "PRD", "Design", "Implementation"],
        "emphasize_index": 0,
        "body": [
            "무엇이 문제인지 한 문단으로 정리한다",
            "왜 지금 해결해야 하는지 설명한다",
            "해결 범위와 비범위를 구분한다",
            "이후 PRD와 설계의 기준이 된다",
        ],
        "note": (
            "Problem Statement는 문서 작성 과제가 아닙니다. 이후 PRD와 설계, 구현이 "
            "흔들리지 않게 만드는 기준점입니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 19,
        "type": "document",
        "title": "문제 정의 프롬프트 예시",
        "badge": "Prompt",
        "body": [
            "역할 — AI PM",
            "맥락 — 민원/FAQ 자동화",
            "산출물 — Problem Statement",
            "제약 — 완전 자동 발송은 제외",
            "기준 — 공공기관 실무에 맞는 표현",
        ],
        "box_title": "claude/prompts/01-problem-framing.md",
        "box_lines": [
            "너는 공공기관 민원 운영을 이해하는 AI PM이야.",
            "",
            "민원/FAQ 자동화 보조 서비스를 위한",
            "Problem Statement 초안을 만들어줘.",
            "",
            "포함:",
            "- 시민/운영자/관리자별 불편",
            "- 자동화 가능 범위",
            "- 자동화 제외 범위",
            "- 성공의 정의",
            "",
            "제약: 완전 자동 발송은 제외한다.",
        ],
        "note": (
            "Claude에게 문제 정의를 맡길 때도 기준을 함께 줘야 합니다. 특히 이번 예제에서는 "
            "운영자 승인과 정책 확인이 중요한 제약입니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 20,
        "type": "review",
        "title": "실습 1 · Problem Statement 만들기",
        "lead": "AI PM이 초안 → 나머지 3명이 누락 관점 리뷰",
        "body": [
            "claude/prompts/01-problem-framing.md를 사용한다",
            "운영자, 시민, 관리자 문제를 분리한다",
            "자동화 가능 범위와 제외 범위를 함께 적는다",
            "결과를 docs 문서와 비교한다",
        ],
        "note": (
            "이제 첫 번째 실습입니다. Claude에게 문제 정의를 만들어보게 하고, 나온 문서를 "
            "그대로 믿기보다 범위와 위험 요소가 충분히 들어갔는지 함께 확인하겠습니다. "
            "네 명이 함께한다면 한 명이 초안을 만들고, 나머지는 사용자, 기술, 품질 관점에서 "
            "빠르게 리뷰합니다."
        ),
        "speak_seconds": "실습 포함 9분",
    },
    {
        "no": 21,
        "type": "review",
        "title": "문제 정의 결과 리뷰",
        "lead": "지금은 멋진지보다 다음 단계로 넘길 수 있는지를 본다",
        "body": [
            "문제가 기능으로만 쓰이지 않았는가",
            "사용자별 불편이 분리되었는가",
            "자동화 제외 범위가 있는가",
            "이후 PRD로 이어질 만큼 명확한가",
        ],
        "note": (
            "AI가 만든 문서에서 가장 자주 생기는 문제는 그럴듯하지만 기준이 약하다는 점입니다. "
            "지금은 내용이 멋진지보다 다음 단계로 넘길 수 있을 만큼 명확한지를 봅니다."
        ),
        "speak_seconds": "4분",
    },
    # ====================================================== PART 4. PRD
    {
        "no": 22,
        "type": "section_divider",
        "title": "PRD는 AI와 팀이 공유하는 기준 문서다",
        "part_no": "04",
        "section_title": "PRD 작성",
        "section_sub": "구현 기준이자 의사결정 기준",
        "section_outcomes": [
            "MVP PRD v1",
            "비목표와 성공 지표",
            "Leadership / Designer / Engineer 리뷰",
        ],
        "body": [
            "기능을 나열하는 문서가 아니다",
            "사용자, 범위, 성공 기준을 합의하는 문서다",
            "AI에게 구현 기준을 제공한다",
            "팀에게 의사결정 기준을 제공한다",
        ],
        "note": (
            "AI 시대에도 PRD가 사라지는 것이 아니라 오히려 더 중요해집니다. AI가 빠르게 "
            "구현할수록 무엇을 구현해야 하는지에 대한 기준이 더 필요합니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 23,
        "type": "card_grid",
        "title": "좋은 PRD의 최소 구성",
        "card_cols": 3,
        "cards": [
            {"title": "문제 정의", "body": ["왜 만드는가"]},
            {"title": "사용자", "body": ["누가 쓰는가"]},
            {"title": "핵심 기능", "body": ["MVP 범위"], "accent": True},
            {"title": "비목표", "body": ["하지 않는 것"]},
            {"title": "성공 지표", "body": ["어떻게 판단하나"]},
            {"title": "리스크", "body": ["오픈 질문"]},
        ],
        "body": ["오늘은 1일 내 프로토타입 가능한 최소 PRD를 만든다"],
        "note": (
            "오늘은 거대한 PRD를 만들지 않습니다. 대신 AI와 개발자가 바로 다음 단계로 넘어갈 "
            "수 있는 최소한의 PRD를 만듭니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 24,
        "type": "concept",
        "title": "MVP 범위 제한이 중요한 이유",
        "lead": "AI는 범위를 넓히는 데 능하다 — 좁히는 것이 PM의 역할",
        "body": [
            "실습 시간은 제한되어 있다",
            "MVP는 작아야 완성된다",
            "완성된 작은 기능이 확장 논의의 출발점이다",
        ],
        "note": (
            "Claude에게 그냥 서비스를 만들어달라고 하면 기능이 쉽게 커집니다. 오늘은 오히려 "
            "범위를 줄이는 것이 좋은 PM의 역할입니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 25,
        "type": "review",
        "title": "민원/FAQ 자동화 MVP",
        "lead": "운영자가 문의를 보고 AI 초안을 검토하는 흐름까지",
        "body": [
            "Mock 데이터 기반 문의 목록",
            "문의 상세 보기",
            "FAQ 매칭",
            "응답 초안 생성",
            "운영자 검토 포인트 표시",
        ],
        "note": (
            "오늘의 MVP는 매우 명확합니다. 실제 발송이나 관리자 기능까지 만들지 않고, "
            "운영자가 문의를 보고 AI 초안을 검토할 수 있는 흐름까지만 만듭니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 26,
        "type": "comparison",
        "title": "성공 기준은 어떻게 잡을까",
        "columns": [
            {"title": "Metric",
             "body": ["응답 초안 작성 시간 단축",
                       "반복 문의 처리 속도"]},
            {"title": "Quality",
             "body": ["운영자 검토 가능성",
                       "톤과 정확성"], "accent": True},
            {"title": "Safety",
             "body": ["FAQ 미매칭 처리",
                       "확정 표현 제한"]},
        ],
        "body": ["AI 기능의 성공 기준은 정확도 하나로 끝나지 않는다"],
        "note": (
            "AI 기능의 성공 기준은 정확도 하나로 끝나지 않습니다. 운영자가 검토하기 쉬운지, "
            "위험한 문의를 무리하게 답하지 않는지도 함께 봐야 합니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 27,
        "type": "document",
        "title": "PRD 작성 프롬프트 예시",
        "badge": "Prompt",
        "body": [
            "참고 문서 — Problem Statement",
            "목표 — MVP PRD",
            "포함 항목 — 사용자, 기능, 비목표, 성공 지표",
            "제약 — 1일 내 프로토타입 가능한 수준",
        ],
        "box_title": "claude/prompts/02-prd-writing.md",
        "box_lines": [
            "Problem Statement를 입력으로 사용해",
            "민원/FAQ 자동화의 MVP PRD를 작성해줘.",
            "",
            "포함:",
            "- 사용자 (시민/운영자/관리자)",
            "- 핵심 기능 (분류/매칭/초안/검토)",
            "- 비목표 (자동 발송, 관리자 콘솔)",
            "- 성공 지표 (Metric/Quality/Safety)",
            "- 리스크 / 오픈 질문",
            "",
            "범위: 1일 내 프로토타입 가능한 수준",
        ],
        "note": (
            "PRD 작성에서는 Claude에게 무엇을 포함할지뿐 아니라 어느 수준까지 쓰면 되는지도 "
            "알려줘야 합니다. 오늘 기준은 1일 내 프로토타입 가능한 수준입니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 28,
        "type": "review",
        "title": "실습 2 · PRD v1 만들기",
        "lead": "Problem Statement → PRD → 3관점 리뷰 준비",
        "body": [
            "Problem Statement를 입력으로 사용한다",
            "docs/templates/prd-template.md 구조를 따른다",
            "MVP 범위를 작게 유지한다",
            "비목표와 리스크를 반드시 포함한다",
            "Leadership / Designer / Engineer 관점으로 1차 리뷰",
        ],
        "note": (
            "이제 문제 정의를 PRD로 바꾸겠습니다. 여기서 중요한 것은 기능을 많이 넣는 것이 "
            "아니라, 오늘 끝까지 만들 수 있는 범위를 정하는 것입니다."
        ),
        "speak_seconds": "실습 포함 11분",
    },
    {
        "no": 29,
        "type": "card_grid",
        "title": "PRD는 세 관점으로 리뷰한다",
        "card_cols": 3,
        "cards": [
            {"title": "Leadership",
             "body": ["회사에 왜 필요한가",
                       "Business Value"], "accent": True},
            {"title": "UI/UX Designer",
             "body": ["사용자가 잘 쓸 수 있는가",
                       "User Experience"]},
            {"title": "Engineer",
             "body": ["구현 가능한가",
                       "Technical Feasibility"]},
        ],
        "body": ["참고 — docs/12-prd-review-perspectives.md"],
        "note": (
            "PRD는 기획자 혼자 만족하는 문서가 아닙니다. 임원 관점에서는 회사가 투자할 가치가 "
            "있는지, 디자이너 관점에서는 실제 화면으로 옮겼을 때 사용자가 헷갈리지 않는지, "
            "엔지니어 관점에서는 API와 데이터 구조로 구현 가능한지를 봐야 합니다."
        ),
        "speak_seconds": "6분",
    },
    # ====================================================== PART 5.
    {
        "no": 30,
        "type": "section_divider",
        "title": "설계 문서는 왜 필요한가",
        "part_no": "05",
        "section_title": "설계 문서화",
        "section_sub": "PRD를 구현 가능한 구조로 옮긴다",
        "section_outcomes": [
            "Flowchart / Sequence / ERD",
            "API 계약과 데이터 모델",
            "AI Layer 분리 구조",
        ],
        "body": [
            "PRD를 구현 가능한 구조로 바꾼다",
            "데이터 흐름과 API 경계를 정한다",
            "프론트엔드, 백엔드, AI 로직의 책임을 나눈다",
            "Mermaid 다이어그램으로 사람과 AI가 같은 구조를 본다",
        ],
        "note": (
            "설계 문서는 개발자만을 위한 문서가 아닙니다. Claude에게도 어떤 파일을 어떻게 "
            "만들지 판단하게 해주는 중간 번역 문서입니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 31,
        "type": "card_grid",
        "title": "Mermaid로 먼저 그릴 3가지",
        "card_cols": 3,
        "cards": [
            {"title": "Flowchart",
             "body": ["사용자 흐름",
                       "어떤 순서로 쓰는가"]},
            {"title": "Sequence Diagram",
             "body": ["호출 순서",
                       "Web/API/AI Layer"], "accent": True},
            {"title": "ERD",
             "body": ["데이터 구조",
                       "Inquiry/FAQ/Recommendation"]},
        ],
        "body": ["참고 — docs/11-mermaid-diagram-guide.md"],
        "note": (
            "설계 단계에서는 그림을 많이 그리는 것이 목적이 아닙니다. Flowchart로 사용자 "
            "흐름을 보고, Sequence Diagram으로 호출 순서를 보고, ERD로 데이터 구조를 보면 "
            "Claude가 코드를 만들 때 기준이 훨씬 명확해집니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 32,
        "type": "process",
        "title": "Flowchart · 사용자 흐름 먼저 보기",
        "flow_items": [
            "시민 문의 접수",
            "운영자 목록 확인",
            "문의 상세 선택",
            "FAQ 매칭",
            "응답 초안 생성",
            "운영자 검토",
            "응답 확정",
        ],
        "emphasize_index": 5,
        "body": [
            "자동 발송이 아니라 사람 검토를 반드시 거친다",
        ],
        "note": (
            "Flowchart는 사용자의 큰 이동 경로를 보여줍니다. 여기서 꼭 봐야 할 것은 AI가 "
            "답변을 만든 뒤 바로 발송하지 않고, 운영자 검토 단계를 지난다는 점입니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 33,
        "type": "sequence",
        "title": "Sequence Diagram · API 호출 순서 보기",
        "actors": ["Operator", "Web", "API Server", "AI Layer", "Mock Data"],
        "messages": [
            "Operator → Web : 문의 상세 선택",
            "Web → API : GET /api/inquiries/:id",
            "API → Data : 문의와 FAQ 조회",
            "API → AI : 추천 결과 생성 요청",
            "AI → API : category, draftReply, reviewNotes",
            "API → Web : InquiryDetailResponse",
            "Web → Operator : 상세 화면 표시",
        ],
        "note": (
            "Sequence Diagram은 개발자가 특히 좋아해야 하는 다이어그램입니다. 어떤 컴포넌트가 "
            "어떤 순서로 호출되는지 보이면 API 구현과 프론트엔드 연결이 훨씬 쉬워집니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 34,
        "type": "erd",
        "title": "ERD · 데이터 구조 보기",
        "entities": [
            {"name": "INQUIRY",
             "fields": [
                 "id  PK",
                 "status",
                 "subject",
                 "message",
                 "priority",
             ]},
            {"name": "RECOMMENDATION",
             "fields": [
                 "id  PK",
                 "inquiryId  FK",
                 "category",
                 "draftReply",
                 "reviewNotes",
             ]},
            {"name": "FAQ",
             "fields": [
                 "id  PK",
                 "category",
                 "question",
                 "answer",
             ]},
        ],
        "relations": [(0, 1, "1 : 1"), (1, 2, "n : m")],
        "note": (
            "오늘은 JSON으로 실습하지만, ERD를 그려보면 나중에 실제 DB로 바꾸는 상상을 할 수 "
            "있습니다. 특히 AI 결과물인 Recommendation을 따로 보는 것이 중요합니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 35,
        "type": "api_table",
        "title": "API 설계 초안",
        "headers": ["Method", "Path", "역할"],
        "col_widths": [None, None, None],
        "rows": [
            ("GET", "/health", "서버 상태 확인"),
            ("GET", "/api/faqs", "FAQ 전체 조회"),
            ("GET", "/api/inquiries", "문의 목록"),
            ("GET", "/api/inquiries/:id", "문의 상세 + 추천 결과"),
            ("POST", "/api/inquiries/:id/recommendation",
             "분류·매칭·초안·검토 포인트 생성"),
        ],
        "body": ["오늘 데모는 목록 / 상세 / 추천 생성 정도면 충분"],
        "note": (
            "API는 많을 필요가 없습니다. 오늘의 목표는 문의를 보고 추천 결과를 확인하는 것이"
            "므로, 목록, 상세, 추천 생성 정도면 충분합니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 36,
        "type": "two_column",
        "title": "AI Layer를 분리하는 이유",
        "body": [
            "Mock 규칙 기반으로도 데모 가능",
            "나중에 LLM API로 교체 가능",
            "분류, 매칭, 응답 생성을 따로 개선 가능",
            "품질 평가 지점을 분리할 수 있음",
        ],
        "right_kind": "cards",
        "right_cards": [
            {"title": "Now", "body": [
                "Rule-based AI Layer",
                "data/mock 활용",
                "강의 중 안정 동작",
            ]},
            {"title": "Later", "body": [
                "Claude API / 다른 LLM 교체",
                "RAG / 정책 검색 추가",
                "평가 데이터 축적",
            ], "accent": True},
        ],
        "note": (
            "오늘은 실제 LLM API 없이도 데모가 가능해야 합니다. 그래서 AI Layer를 별도 함수로 "
            "빼두고, 나중에 Claude API나 다른 모델로 교체할 수 있게 설계합니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 37,
        "type": "document",
        "title": "설계 문서 작성 프롬프트",
        "badge": "Prompt",
        "body": [
            "역할 — Tech Lead",
            "기준 문서 — PRD",
            "산출물 — architecture, API, data model, AI flow",
            "제약 — 강의용으로 이해하기 쉬운 구조",
        ],
        "box_title": "claude/prompts/03-system-design.md",
        "box_lines": [
            "PRD를 입력으로 사용해 설계 문서를 작성해줘.",
            "",
            "포함:",
            "- Mermaid Flowchart (사용자 흐름)",
            "- Mermaid Sequence (Web/API/AI 호출 순서)",
            "- Mermaid ERD (Inquiry/FAQ/Recommendation)",
            "- API Contract (Method, Path, Body)",
            "- AI Layer 입출력 명세",
            "",
            "구조: 강의용으로 이해하기 쉽게.",
        ],
        "note": (
            "설계 문서에서는 너무 복잡한 인프라 설계를 피하고, 오늘 만들 기능을 설명할 수 있는 "
            "구조에 집중합니다."
        ),
        "speak_seconds": "65초",
    },
    {
        "no": 38,
        "type": "review",
        "title": "실습 3 · 설계 문서 만들기",
        "lead": "PRD → Mermaid → 설계 → 구현 순서",
        "body": [
            "PRD를 입력으로 사용한다",
            "Flowchart, Sequence, ERD를 작성한다",
            "API, 데이터 모델, AI Layer를 정리한다",
            "구현 순서를 함께 뽑는다",
            "UX Builder는 Flow, Backend는 Sequence/ERD, Quality는 상태/테스트 흐름",
        ],
        "note": (
            "이제 PRD를 설계 문서로 바꾸겠습니다. 이번에는 글만 쓰지 않고 Mermaid로 flow, "
            "sequence, ERD까지 함께 만들겠습니다. AI 개발자 입장에서는 이 다이어그램들이 "
            "바로 구현 지시서 역할을 합니다."
        ),
        "speak_seconds": "실습 포함 14분",
    },
    {
        "no": 39,
        "type": "review",
        "title": "구현 전 최종 확인",
        "lead": "이 네 가지가 분명해야 Claude가 어긋나지 않는다",
        "body": [
            "무엇을 먼저 만들 것인가",
            "어떤 Mock 데이터를 쓸 것인가",
            "API 응답 형태는 무엇인가",
            "UI는 어떤 정보를 보여줄 것인가",
        ],
        "note": (
            "구현 전에 이 네 가지가 분명해야 합니다. 그렇지 않으면 Claude가 열심히 코드를 "
            "만들더라도 우리가 원하는 데모 흐름과 어긋날 수 있습니다."
        ),
        "speak_seconds": "5분",
    },
    # ====================================================== PART 6.
    {
        "no": 40,
        "type": "section_divider",
        "title": "프로토타입 구현의 원칙",
        "part_no": "06",
        "section_title": "프로토타입 구현 1\nAPI와 Mock Data",
        "section_sub": "작은 단위로 자주 실행 확인",
        "section_outcomes": [
            "MVP API 5개",
            "Mock 데이터 연결",
            "기능 v1 (서버 실행 가능)",
        ],
        "body": [
            "작은 단위로 요청한다",
            "API부터 완성한다",
            "Mock 데이터로 먼저 동작시킨다",
            "실행 가능한 상태를 자주 확인한다",
        ],
        "note": (
            "AI와 코딩할 때 가장 위험한 것은 한 번에 큰 덩어리를 맡기는 것입니다. 오늘은 API, "
            "데이터, UI, 품질 개선을 작은 단위로 나누겠습니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 41,
        "type": "code_demo",
        "title": "Mock Data의 역할",
        "body": [
            "네트워크나 DB 없이 데모 가능",
            "입력과 출력 예시를 고정",
            "AI 결과 품질 비교가 쉬움",
            "강의 중 실패 리스크 감소",
        ],
        "code_lines": [
            "// data/mock/faqs.json",
            "[",
            "  {",
            "    \"id\": \"faq-001\",",
            "    \"category\": \"민원처리\",",
            "    \"question\": \"민원 처리 기간은 얼마인가요?\",",
            "    \"answer\": \"일반 민원은 7일 이내…\"",
            "  }",
            "]",
            "",
            "// data/mock/inquiries.json",
            "[",
            "  {",
            "    \"id\": \"inq-001\",",
            "    \"subject\": \"민원 처리 기간 문의\",",
            "    \"status\": \"open\"",
            "  }",
            "]",
        ],
        "code_highlight": {0, 10},
        "note": (
            "Mock 데이터는 대충 넣는 임시 데이터가 아닙니다. 강의와 데모에서는 시스템의 "
            "입력과 출력을 안정적으로 보여주는 핵심 장치입니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 42,
        "type": "document",
        "title": "API 구현 요청 예시",
        "badge": "Prompt",
        "body": [
            "기준 문서 — docs/04-prd-faq-automation.md",
            "기준 문서 — docs/05-architecture-faq-automation.md",
            "범위 — apps/api MVP API",
            "데이터 — data/mock 사용",
            "산출물 — 변경 파일과 이유 요약",
        ],
        "box_title": "claude/prompts/04-implementation.md",
        "box_lines": [
            "docs/04-prd-faq-automation.md 와",
            "docs/05-architecture-faq-automation.md 를 기준으로",
            "apps/api 의 MVP API를 구현해줘.",
            "",
            "Mock 데이터는 data/mock/ 을 사용한다.",
            "",
            "구현 후 변경된 파일 목록과",
            "각 파일의 변경 이유를 요약해줘.",
        ],
        "note": (
            "구현 요청에서도 기준 문서를 반드시 지정합니다. Claude가 어떤 설계를 따라야 "
            "하는지 알고 있어야 코드가 문서와 맞게 나옵니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 43,
        "type": "code_demo",
        "title": "문의 목록 API",
        "body": [
            "GET /api/inquiries",
            "id, status, subject, channel, priority",
            "운영자 화면의 첫 데이터 소스",
        ],
        "code_lines": [
            "GET /api/inquiries",
            "",
            "[",
            "  {",
            "    \"id\": \"inq-001\",",
            "    \"status\": \"open\",",
            "    \"subject\": \"민원 처리 기간 문의\",",
            "    \"channel\": \"web\",",
            "    \"priority\": \"normal\"",
            "  },",
            "  {",
            "    \"id\": \"inq-002\",",
            "    \"status\": \"in_review\",",
            "    \"subject\": \"개인정보 정정 요청\",",
            "    \"channel\": \"phone\",",
            "    \"priority\": \"high\"",
            "  }",
            "]",
        ],
        "code_highlight": {0},
        "note": (
            "첫 API는 문의 목록입니다. 이 API가 있어야 운영자가 어떤 문의들이 들어왔는지 보고, "
            "이후 상세 화면으로 넘어갈 수 있습니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 44,
        "type": "code_demo",
        "title": "문의 상세 API",
        "body": [
            "GET /api/inquiries/:id",
            "원문 + 추천 결과를 함께 반환",
            "UI 상세 패널의 데이터 소스",
        ],
        "code_lines": [
            "GET /api/inquiries/inq-001",
            "",
            "{",
            "  \"inquiry\": {",
            "    \"id\": \"inq-001\",",
            "    \"subject\": \"민원 처리 기간 문의\",",
            "    \"message\": \"제가 5월 1일에 신청한…\"",
            "  },",
            "  \"recommendation\": {",
            "    \"category\": \"민원처리\",",
            "    \"matchedFaqs\": [\"faq-001\"],",
            "    \"draftReply\": \"안녕하세요, 시민님…\",",
            "    \"reviewNotes\": [",
            "      \"실제 접수일 확인이 필요\"",
            "    ]",
            "  }",
            "}",
        ],
        "code_highlight": {0},
        "note": (
            "상세 API에서는 원문 문의뿐 아니라 추천 결과까지 함께 내려줍니다. 강의용 데모에서는 "
            "이 편이 흐름을 보여주기 쉽습니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 45,
        "type": "process",
        "title": "추천 생성 API",
        "flow_items": ["Inquiry", "Category", "FAQ Match",
                          "Draft Reply", "Review Notes"],
        "body": [
            "POST /api/inquiries/:id/recommendation",
            "카테고리 분류 / FAQ 매칭 / 응답 초안 / 검토 포인트",
            "오늘 데모의 핵심 기능",
        ],
        "note": (
            "추천 생성 API는 오늘 데모의 핵심입니다. 여기서 AI 기능처럼 보이는 분류, 매칭, "
            "초안 생성, 검토 포인트가 한 번에 만들어집니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 46,
        "type": "code_demo",
        "title": "데모 2 · API 서버 실행",
        "body": [
            "의존성 설치",
            "API 개발 서버 실행",
            "/health 확인",
            "문의 목록 API 확인",
        ],
        "code_lines": [
            "$ npm install",
            "",
            "$ npm run dev:api",
            "  ▶ api server listening on :4000",
            "",
            "$ curl http://localhost:4000/health",
            "  { \"status\": \"ok\" }",
            "",
            "$ curl http://localhost:4000/api/inquiries",
            "  [ ... ]",
        ],
        "code_highlight": {0, 2},
        "note": (
            "이제 실제 API 서버를 실행해보겠습니다. 강의 중에는 화면이 예쁘게 뜨는 것보다 "
            "먼저 API가 안정적으로 응답하는지를 확인하는 것이 중요합니다."
        ),
        "speak_seconds": "실연 포함 6분",
    },
    {
        "no": 47,
        "type": "review",
        "title": "실습 4 · API 응답 확인하기",
        "lead": "추천 결과의 reviewNotes가 함께 오는지 본다",
        "body": [
            "/health",
            "/api/faqs",
            "/api/inquiries",
            "/api/inquiries/:id",
            "추천 결과의 reviewNotes 확인",
        ],
        "note": (
            "수강생들은 지금 각자 API 응답을 확인합니다. 특히 추천 결과에 단순 답변만 있는지, "
            "운영자 검토 포인트까지 있는지를 봐주세요."
        ),
        "speak_seconds": "실습 포함 10분",
    },
    {
        "no": 48,
        "type": "review",
        "title": "API 구현 리뷰 포인트",
        "lead": "데이터 / 라우트 / AI 로직이 분리되어 있는가",
        "body": [
            "Mock 데이터가 분리되어 있는가",
            "AI 로직이 별도 함수로 분리되어 있는가",
            "없는 문의 id에 404를 반환하는가",
            "응답 형태가 UI에서 쓰기 쉬운가",
        ],
        "note": (
            "여기서는 코드 품질을 깊게 리뷰하기보다 데모와 확장에 필요한 최소 기준을 봅니다. "
            "데이터, 라우트, AI 로직이 분리되어 있으면 다음 단계가 편해집니다."
        ),
        "speak_seconds": "5분",
    },
    # ====================================================== PART 7.
    {
        "no": 49,
        "type": "section_divider",
        "title": "운영자 UI의 목표",
        "part_no": "07",
        "section_title": "프로토타입 구현 2\nUI와 응답 생성",
        "section_sub": "운영자 콘솔로서의 화면",
        "section_outcomes": [
            "목록 / 상세 2단 레이아웃",
            "추천 결과 + 검토 포인트",
            "기능 v2 (E2E 데모 완성)",
        ],
        "body": [
            "문의 목록을 빠르게 훑는다",
            "문의 상세를 확인한다",
            "AI 추천 결과를 검토한다",
            "응답 초안과 주의점을 함께 본다",
        ],
        "note": (
            "오늘 UI는 예쁘게 포장된 랜딩 페이지가 아니라 운영자 콘솔입니다. 반복 업무를 하는 "
            "사람이 빠르게 읽고 판단할 수 있어야 합니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 50,
        "type": "two_column",
        "title": "UI 구성 요소",
        "body": [
            "상단 — 서비스 제목과 목적",
            "좌측 — 문의 목록",
            "우측 — 상세 문의",
            "우측 내부 — 응답 초안, 검토 포인트",
        ],
        "right_kind": "placeholder",
        "right_caption": (
            "wireframe placeholder\n"
            "\n"
            "┌─ Header ──────────────┐\n"
            "│ 좌측 목록 │ 우측 상세 │\n"
            "│           │ 추천 결과 │\n"
            "│           │ 검토 포인트│\n"
            "└───────────────────────┘"
        ),
        "note": (
            "운영자 도구에서는 정보 배치가 중요합니다. 목록에서 선택하고, 상세를 보고, "
            "추천 결과를 바로 검토하는 흐름이 자연스러워야 합니다."
        ),
        "speak_seconds": "65초",
    },
    {
        "no": 51,
        "type": "document",
        "title": "UI 구현 요청 예시",
        "badge": "Prompt",
        "body": [
            "범위 — apps/web 운영자 화면",
            "API 계약 유지",
            "목록/상세 2단 레이아웃",
            "강의용 가독성 우선",
        ],
        "box_title": "claude/prompts/04-implementation.md (UI)",
        "box_lines": [
            "apps/web 에서 운영자 화면을 만들어줘.",
            "",
            "API 계약은 apps/api 와 정확히 맞추고,",
            "목록 / 상세 2단 레이아웃을 사용한다.",
            "",
            "상세 패널에는",
            "- 문의 원문",
            "- 카테고리 / FAQ 매칭",
            "- 응답 초안",
            "- 검토 포인트",
            "를 함께 표시한다.",
            "",
            "코드는 강의에서 읽기 쉽게 작성해줘.",
        ],
        "note": (
            "프론트엔드 요청에서도 디자인보다 먼저 정보 구조를 지정합니다. 목록과 상세가 어떻게 "
            "연결되는지만 분명해도 Claude가 훨씬 안정적으로 구현합니다."
        ),
        "speak_seconds": "65초",
    },
    {
        "no": 52,
        "type": "code_demo",
        "title": "데모 3 · Web 앱 실행",
        "body": [
            "Web 개발 서버 실행",
            "문의 목록 → 선택 → 상세",
            "응답 초안과 검토 포인트 확인",
        ],
        "code_lines": [
            "$ npm run dev:web",
            "  ▶ web running on http://localhost:5173",
            "",
            "  → 브라우저 열기",
            "  → 좌측 목록에서 문의 선택",
            "  → 우측 상세 패널 확인",
            "  → 추천 결과의 reviewNotes 확인",
        ],
        "code_highlight": {0},
        "note": (
            "이제 운영자 화면을 띄우겠습니다. 여기서 핵심은 AI 답변이 자동 발송되는 것이 "
            "아니라, 운영자가 검토할 수 있는 형태로 제시된다는 점입니다."
        ),
        "speak_seconds": "실연 포함 7분",
    },
    {
        "no": 53,
        "type": "review",
        "title": "실습 5 · UI에서 문의 흐름 확인",
        "lead": "이때부터는 품질 판단의 눈을 함께 가져간다",
        "body": [
            "각 문의를 선택한다",
            "카테고리가 어떻게 바뀌는지 본다",
            "FAQ 매칭 수를 확인한다",
            "응답 초안의 톤을 확인한다",
            "검토 포인트가 적절한지 본다",
        ],
        "note": (
            "수강생들은 이제 직접 문의를 클릭해보면서 결과가 어떻게 달라지는지 확인합니다. "
            "이때부터는 기능 구현보다 품질 판단의 눈을 함께 가져가야 합니다."
        ),
        "speak_seconds": "실습 포함 10분",
    },
    {
        "no": 54,
        "type": "review",
        "title": "응답 초안에서 봐야 할 것",
        "lead": "정책상 확정할 수 없는 것을 확정하지 않는가",
        "body": [
            "친절한가",
            "과도하게 확정하지 않는가",
            "FAQ 근거와 맞는가",
            "추가 확인이 필요한 부분을 남기는가",
        ],
        "note": (
            "응답 초안의 품질은 말투만의 문제가 아닙니다. 정책상 확정할 수 없는 것을 "
            "확정하지 않는지, 운영자가 확인해야 할 부분을 남겼는지가 중요합니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 55,
        "type": "comparison",
        "title": "기능 v2의 기준",
        "columns": [
            {"title": "v1",
             "body": ["API 응답만 확인",
                       "추천 결과를 raw로 봄"]},
            {"title": "v2",
             "body": ["목록 → 상세 흐름",
                       "추천 결과 / 초안 / 검토 포인트",
                       "데모 중 끊기지 않음"], "accent": True},
        ],
        "body": ["거창한 완성본이 아니라, 핵심 흐름이 끊기지 않으면 충분"],
        "note": (
            "기능 v2는 거창한 완성본이 아닙니다. 운영자가 문의를 보고 AI 초안을 검토하는 "
            "핵심 흐름이 끊기지 않으면 오늘 목표에는 충분합니다."
        ),
        "speak_seconds": "60초",
    },
    # ====================================================== PART 8.
    {
        "no": 56,
        "type": "section_divider",
        "title": "AI 기능은 구현 후부터 진짜 시작된다",
        "part_no": "08",
        "section_title": "AI 품질 개선",
        "section_sub": "Generate → Review → Tune → Test",
        "section_outcomes": [
            "분류 / 응답 / 검토 품질 진단",
            "Edge case 대응 룰",
            "Prompt v2",
        ],
        "body": [
            "초안 생성은 시작점이다",
            "결과를 보고 기준을 조정한다",
            "Edge case를 넣어봐야 한다",
            "프롬프트와 정책 기준을 함께 개선한다",
        ],
        "note": (
            "AI 기능은 한 번 만들고 끝나는 기능이 아닙니다. 결과를 보고 무엇이 부족한지 "
            "판단하고, 그 기준을 다시 프롬프트와 로직에 반영하는 반복이 필요합니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 57,
        "type": "badge_row",
        "title": "품질 개선의 세 축",
        "badges": ["분류 품질", "응답 품질", "검토 품질"],
        "body": [
            "문의를 잘 분류하는지",
            "답변 초안이 적절한지",
            "운영자 확인 포인트를 잘 남기는지",
        ],
        "note": (
            "오늘의 AI 품질은 세 가지로 나눠봅니다. 문의를 잘 분류하는지, 답변 초안이 적절한지, "
            "그리고 운영자가 확인해야 할 포인트를 잘 남기는지입니다."
        ),
        "speak_seconds": "65초",
    },
    {
        "no": 58,
        "type": "card_grid",
        "title": "Edge Case 예시",
        "card_cols": 3,
        "cards": [
            {"title": "FAQ에 없는 문의",
             "body": ["근거 없는 답변 위험"]},
            {"title": "감정이 강한 민원",
             "body": ["톤 조절 필요"]},
            {"title": "정책 판단 필요",
             "body": ["담당자 확인 유도"], "accent": True},
            {"title": "개인정보 포함",
             "body": ["로그/응답 처리 주의"]},
            {"title": "여러 주제 혼재",
             "body": ["분류 모호성"]},
            {"title": "—",
             "body": ["일부러 넣어보는 습관"]},
        ],
        "note": (
            "AI는 평범한 입력에서는 그럴듯하게 보이지만, 실제 서비스에서는 애매한 입력과 "
            "위험한 입력이 더 중요합니다. Edge case를 일부러 넣어보는 습관이 필요합니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 59,
        "type": "comparison",
        "title": "프롬프트 튜닝 방향",
        "columns": [
            {"title": "Before",
             "body": ["단정적인 답변",
                       "FAQ 없어도 추측",
                       "검토 포인트 누락"]},
            {"title": "After",
             "body": ["모르는 것은 모른다",
                       "정책 확인 필요 문구",
                       "검토용 초안임을 명시",
                       "민감 문의는 담당자 확인 유도"], "accent": True},
        ],
        "body": ["답할 수 있는 것과 확인해야 하는 것을 구분하게 만든다"],
        "note": (
            "좋은 프롬프트는 더 자신 있게 답하게 만드는 것이 아니라, 답할 수 있는 것과 "
            "확인해야 하는 것을 구분하게 만드는 방향이어야 합니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 60,
        "type": "document",
        "title": "Prompt v2 요청 예시",
        "badge": "Prompt v2",
        "body": [
            "분류 정확도 향상",
            "FAQ 미매칭 처리",
            "과도한 확정 표현 줄이기",
            "운영자 검토 포인트 강화",
            "공공기관에 맞는 톤 유지",
        ],
        "box_title": "claude/prompts/05-prompt-tuning.md",
        "box_lines": [
            "현재 분류 결과와 응답 초안에서",
            "다음 문제가 보인다:",
            "- FAQ 미매칭 시 무리한 추측",
            "- 정책 판단 영역의 단정",
            "- 검토 포인트 누락",
            "",
            "Prompt v2 에서는",
            "- 모르는 것은 모른다고 남기게",
            "- 정책 확인 필요 문구를 포함하게",
            "- 검토용 초안임을 명시하게",
            "- 공공기관 어조를 유지하게",
            "수정해줘.",
        ],
        "note": (
            "Prompt v2에서는 더 멋진 문장보다 더 안전한 판단 기준을 강화합니다. 특히 공공기관 "
            "맥락에서는 확정 표현과 책임 소재를 조심해야 합니다."
        ),
        "speak_seconds": "70초",
    },
    {
        "no": 61,
        "type": "review",
        "title": "실습 6 · 응답 품질 개선하기",
        "lead": "'더 좋게'가 아니라 '어떤 기준으로 더 좋게'",
        "body": [
            "문의 하나를 선택한다",
            "응답 초안의 문제를 찾는다",
            "Claude에게 개선 기준을 준다",
            "변경 후 결과를 비교한다",
        ],
        "note": (
            "이제 수강생들이 직접 품질 개선을 해보겠습니다. 중요한 것은 '더 좋게 해줘'가 "
            "아니라 어떤 기준으로 더 좋아져야 하는지 말하는 것입니다."
        ),
        "speak_seconds": "실습 포함 12분",
    },
    {
        "no": 62,
        "type": "review",
        "title": "품질 개선 결과 공유",
        "lead": "좋아진 점만 보지 말고 새 부작용도 본다",
        "body": [
            "어떤 문제가 있었는가",
            "어떤 지시를 추가했는가",
            "결과가 어떻게 달라졌는가",
            "새로 생긴 부작용은 없는가",
        ],
        "note": (
            "품질 개선은 좋아진 점만 보는 것이 아닙니다. 새 지시 때문에 답변이 너무 길어졌는지, "
            "지나치게 보수적으로 변했는지도 같이 봐야 합니다."
        ),
        "speak_seconds": "6분",
    },
    # ====================================================== PART 9.
    {
        "no": 63,
        "type": "section_divider",
        "title": "AI가 만든 코드도 리뷰가 필요하다",
        "part_no": "09",
        "section_title": "코드 리뷰 & 테스트",
        "section_sub": "동작한다고 충분하지 않다",
        "section_outcomes": [
            "PRD 기준 리뷰 노트",
            "최소 테스트 케이스",
            "Fix Now / Later 분리",
        ],
        "body": [
            "동작한다고 충분하지 않다",
            "문서와 구현이 일치해야 한다",
            "예외 상황이 처리되어야 한다",
            "다음 사람이 읽을 수 있어야 한다",
        ],
        "note": (
            "AI가 코드를 만들어도 리뷰는 사라지지 않습니다. 오히려 빠르게 만들어진 코드일수록 "
            "문서와 맞는지, 예외를 놓치지 않았는지를 확인해야 합니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 64,
        "type": "document",
        "title": "Claude / Codex 리뷰 요청 방법",
        "badge": "Review Prompt",
        "body": [
            "버그와 회귀 중심으로 본다",
            "PRD와 설계 문서를 기준으로 비교",
            "테스트가 필요한 지점을 찾는다",
            "개선 제안과 실제 수정 범위를 분리",
        ],
        "box_title": "Review Request Template",
        "box_lines": [
            "현재 apps/api, apps/web 코드를",
            "다음 기준으로 리뷰해줘:",
            "",
            "- docs/04-prd-faq-automation.md 와의 일치 여부",
            "- docs/05-architecture-faq-automation.md 와의 일치 여부",
            "- 발견한 버그와 회귀 가능성",
            "- 누락된 테스트 케이스",
            "",
            "출력은",
            "1) 발견 사항 / 위험도",
            "2) 지금 고쳐야 할 것",
            "3) 나중에 다룰 것",
            "으로 분리해줘.",
        ],
        "note": (
            "리뷰 요청도 구체적이어야 합니다. '코드 봐줘'보다 PRD와 설계 문서 기준으로 버그, "
            "회귀, 테스트 누락을 찾아달라고 요청하는 편이 훨씬 좋습니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 65,
        "type": "api_table",
        "title": "최소 테스트 케이스",
        "headers": ["케이스", "기대 결과"],
        "col_widths": [None, None],
        "rows": [
            ("문의 목록 조회", "비어 있지 않다"),
            ("존재하지 않는 문의 id", "404 응답"),
            ("FAQ 미매칭 문의", "무리한 답변을 만들지 않는다"),
            ("응답 초안 생성", "검토 포인트가 함께 포함된다"),
        ],
        "body": ["AI 기능에서는 실패했을 때의 행동이 더 중요"],
        "note": (
            "오늘 모든 테스트를 자동화하지는 않더라도, 어떤 케이스를 테스트해야 하는지 감각을 "
            "가져가는 것이 중요합니다. 특히 AI 기능에서는 실패했을 때의 행동이 중요합니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 66,
        "type": "review",
        "title": "실습 7 · 리뷰 노트 만들기",
        "lead": "리뷰의 목적은 비판이 아니라 다음 액션",
        "body": [
            "Claude 또는 Codex에 리뷰를 요청한다",
            "발견된 리스크를 정리한다",
            "바로 고칠 것과 나중에 할 것을 나눈다",
            "리뷰 노트를 산출물로 남긴다",
        ],
        "note": (
            "리뷰의 목적은 비판이 아니라 다음 액션을 정하는 것입니다. 지금 고칠 것과 나중에 "
            "확장할 것을 나누는 연습을 하겠습니다."
        ),
        "speak_seconds": "실습 포함 10분",
    },
    {
        "no": 67,
        "type": "card_grid",
        "title": "코드 리뷰에서 남겨야 할 질문",
        "card_cols": 2,
        "cards": [
            {"title": "PRD 부합도",
             "body": ["기능이 PRD 목표와 맞는가"]},
            {"title": "사용자 판단",
             "body": ["사용자가 실제로 판단하기 쉬운가"]},
            {"title": "위험한 자동화",
             "body": ["숨어 있지 않은가"], "accent": True},
            {"title": "구조적 견고성",
             "body": ["데이터/모델 변경에 버틸 수 있는가"]},
        ],
        "note": (
            "AI 기능 리뷰에서는 기술 구현뿐 아니라 제품 판단도 같이 봐야 합니다. 특히 위험한 "
            "자동화가 숨어 있지 않은지 확인하는 것이 중요합니다."
        ),
        "speak_seconds": "65초",
    },
    # ====================================================== PART 10.
    {
        "no": 68,
        "type": "section_divider",
        "title": "실무 적용 시 필요한 것",
        "part_no": "10",
        "section_title": "실무 확장 &\nWrap-up",
        "section_sub": "Prototype → Production",
        "section_outcomes": [
            "실무 도입 로드맵",
            "AI PM / 개발자 Best Practice",
            "오늘의 한 줄 요약",
        ],
        "body": [
            "실제 DB 연동",
            "FAQ 관리 체계",
            "승인 이력 관리",
            "개인정보 보호",
            "LLM 호출 로그와 평가 데이터",
        ],
        "note": (
            "오늘 만든 것은 프로토타입입니다. 실제 기관에 적용하려면 데이터, 승인, 보안, 로그, "
            "평가 체계가 추가되어야 합니다."
        ),
        "speak_seconds": "80초",
    },
    {
        "no": 69,
        "type": "process",
        "title": "조직에 AI 기능을 도입할 때의 순서",
        "flow_items": [
            "반복 업무 발견",
            "기준 문서 수집",
            "검토 가능한 초안",
            "로그 / 피드백 축적",
            "단계적 자동화 확장",
        ],
        "emphasize_index": 2,
        "body": [
            "처음부터 완전 자동화를 목표로 잡지 않는다",
            "사람이 검토 가능한 초안 생성부터 시작",
        ],
        "note": (
            "조직에서 AI를 도입할 때는 처음부터 완전 자동화를 목표로 잡기보다, 사람이 검토 "
            "가능한 초안 생성부터 시작하는 것이 훨씬 현실적입니다."
        ),
        "speak_seconds": "85초",
    },
    {
        "no": 70,
        "type": "wrap_up",
        "title": "AI PM 관점의 Best Practice",
        "body": [
            "문제를 작게 자른다",
            "문서를 먼저 만든다",
            "AI에게 기준을 준다",
            "결과를 사람 기준으로 검토한다",
            "반복 개선을 운영 구조로 만든다",
        ],
        "note": (
            "AI PM의 역할은 AI에게 일을 던지는 것이 아니라, AI가 좋은 결과를 만들 수 있는 "
            "작업 구조를 설계하는 것입니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 71,
        "type": "wrap_up",
        "title": "개발자 관점의 Best Practice",
        "body": [
            "작은 단위로 구현 요청",
            "실행 가능한 상태 자주 확인",
            "타입과 API 계약 유지",
            "Mock 데이터로 먼저 검증",
            "리뷰와 테스트를 마지막에 몰지 않기",
        ],
        "note": (
            "개발자에게도 AI Native 방식은 생산성을 크게 올릴 수 있습니다. 다만 작은 단위로 "
            "요청하고, 자주 실행하고, 계약을 지키는 습관이 있어야 합니다."
        ),
        "speak_seconds": "75초",
    },
    {
        "no": 72,
        "type": "process",
        "title": "오늘 만든 흐름을 다시 정리하면",
        "flow_items": [
            "Problem", "PRD", "Design",
            "Implementation", "Prompt v2", "Review",
        ],
        "body": [
            "차이는 이 과정을 Claude Desktop과 함께",
            "문서와 코드가 이어지는 방식으로 진행했다는 점",
        ],
        "note": (
            "오늘 우리가 한 일은 하나의 작은 서비스 개발 사이클입니다. 차이는 이 과정을 "
            "Claude Desktop과 함께 문서와 코드가 이어지는 방식으로 진행했다는 점입니다."
        ),
        "speak_seconds": "65초",
    },
    {
        "no": 73,
        "type": "card_grid",
        "title": "Q&A · 확장 논의",
        "card_cols": 2,
        "cards": [
            {"title": "실제 LLM API",
             "body": ["붙이면 무엇이 달라질까"]},
            {"title": "RAG",
             "body": ["붙이면 어떤 구조가 필요할까"], "accent": True},
            {"title": "운영자 승인 플로우",
             "body": ["어떻게 설계할까"]},
            {"title": "개인정보와 로그",
             "body": ["어떻게 관리할까"]},
        ],
        "note": (
            "이제 확장 질문을 받아보겠습니다. 오늘은 프로토타입이지만, 실제 서비스로 가려면 "
            "RAG, 승인, 로그, 개인정보 보호 같은 주제가 함께 따라옵니다."
        ),
        "speak_seconds": "Q&A 포함 12분",
    },
    {
        "no": 74,
        "type": "tree",
        "title": "수강생이 가져갈 수 있는 프롬프트 자산",
        "body": [
            "문제 정의 / PRD / 설계 / 구현 / 품질 / 리뷰",
            "각자 업무 도메인에 맞게 변형해서 사용",
        ],
        "tree_lines": [
            "claude/",
            "├─ CLAUDE.md",
            "├─ PROJECT_CONTEXT.md",
            "└─ prompts/",
            "    ├─ 01-problem-framing.md",
            "    ├─ 02-prd-writing.md",
            "    ├─ 03-system-design.md",
            "    ├─ 04-implementation.md",
            "    ├─ 05-prompt-tuning.md",
            "    └─ 06-review-checklist.md",
        ],
        "note": (
            "오늘 만든 저장소의 좋은 점은 수업이 끝나도 프롬프트 자산이 남는다는 것입니다. "
            "각자의 업무 도메인에 맞게 이 프롬프트들을 바꿔서 쓰면 됩니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 75,
        "type": "one_liner",
        "title": "오늘의 한 줄 요약",
        "body": [
            "AI Native는 AI에게 정답을 묻는 방식이 아니라,\n"
            "AI와 함께 일을 끝내는 구조를 만드는 방식이다.",
        ],
        "note": (
            "오늘 내용을 한 문장으로 요약하면 이것입니다. AI Native는 질문을 잘하는 기술을 "
            "넘어, AI와 사람이 함께 일을 끝내는 구조를 만드는 방식입니다."
        ),
        "speak_seconds": "45초",
    },
    {
        "no": 76,
        "type": "review",
        "title": "마지막 체크리스트",
        "lead": "도구 사용법보다 흐름을 자기 업무에 적용하는 능력",
        "body": [
            "Claude에게 맥락을 먼저 읽혔는가",
            "문서가 구현 기준으로 쓰였는가",
            "자동화 제외 범위를 정했는가",
            "운영자 검토 포인트가 남았는가",
            "다음 확장 방향을 설명할 수 있는가",
        ],
        "note": (
            "이 체크리스트에 답할 수 있다면 오늘 강의의 핵심을 가져가신 겁니다. 도구 사용법보다 "
            "중요한 것은 이 흐름을 자기 업무에 다시 적용하는 능력입니다."
        ),
        "speak_seconds": "60초",
    },
    {
        "no": 77,
        "type": "wrap_up",
        "title": "끝 · 감사합니다",
        "body": [
            "질문 — 자유롭게",
            "실무 적용 아이디어 공유",
            "GitHub 저장소 안내",
        ],
        "note": (
            "여기까지가 오늘 강의입니다. 질문을 받고, 각자 업무에 어떤 문제부터 적용해볼 수 "
            "있을지 짧게 이야기해보겠습니다."
        ),
        "speak_seconds": "30초",
    },
]
