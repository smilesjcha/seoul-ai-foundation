import type {
  FaqItem,
  InquiryDetailResponse,
  InquiryItem,
  InquiryRecommendation
} from "./types.js";

const categoryKeywords: Record<string, string[]> = {
  program: ["교육", "신청", "모집", "프로그램"],
  facility: ["시설", "이용", "예약", "주말"],
  parking: ["주차", "차량"],
  document: ["서류", "마감", "추가", "접수"]
};

function detectCategory(text: string): string {
  const normalized = text.toLowerCase();

  for (const [category, keywords] of Object.entries(categoryKeywords)) {
    if (keywords.some((keyword) => normalized.includes(keyword.toLowerCase()))) {
      return category;
    }
  }

  return "general";
}

function matchFaqs(category: string, inquiry: InquiryItem, faqs: FaqItem[]): FaqItem[] {
  const inquiryText = `${inquiry.subject} ${inquiry.message}`.toLowerCase();

  const scored = faqs.map((faq) => {
    const categoryBonus = faq.category === category ? 2 : 0;
    const tagScore = faq.tags.filter((tag: string) => inquiryText.includes(tag.toLowerCase())).length;
    return { faq, score: categoryBonus + tagScore };
  });

  return scored
    .filter((item) => item.score > 0)
    .sort((a, b) => b.score - a.score)
    .slice(0, 2)
    .map((item) => item.faq);
}

function buildReviewNotes(category: string, matchedFaqs: FaqItem[]): string[] {
  const notes = [
    "최종 발송 전 기관별 최신 정책과 공지사항을 반드시 확인하세요."
  ];

  if (matchedFaqs.length === 0) {
    notes.push("FAQ에 직접 매칭되는 항목이 없어 담당 부서 확인이 필요할 수 있습니다.");
  }

  if (category === "document") {
    notes.push("추가 접수 가능 여부는 프로그램별 예외 규정이 있을 수 있어 운영자 확인이 필요합니다.");
  }

  if (category === "parking") {
    notes.push("행사별 주차 지원 여부가 달라질 수 있으므로 개별 행사 안내를 재확인하세요.");
  }

  return notes;
}

function buildDraftReply(inquiry: InquiryItem, matchedFaqs: FaqItem[]): string {
  const opening = `${inquiry.citizenName}님, 안녕하세요. 문의 주셔서 감사합니다.`;
  const faqAnswer =
    matchedFaqs[0]?.answer ??
    "현재 문의 내용만으로는 정확한 안내가 어려워 담당 부서 확인 후 상세히 안내드리는 것이 적절합니다.";

  const closing =
    "추가로 확인이 필요한 사항이 있는 경우 다시 안내드리겠습니다. 감사합니다.";

  return [opening, faqAnswer, closing].join("\n\n");
}

export function generateRecommendation(
  inquiry: InquiryItem,
  faqs: FaqItem[]
): InquiryRecommendation {
  const category = detectCategory(`${inquiry.subject} ${inquiry.message}`);
  const matchedFaqs = matchFaqs(category, inquiry, faqs);

  return {
    inquiryId: inquiry.id,
    category,
    matchedFaqIds: matchedFaqs.map((faq) => faq.id),
    draftReply: buildDraftReply(inquiry, matchedFaqs),
    reviewNotes: buildReviewNotes(category, matchedFaqs)
  };
}

export function buildInquiryDetailResponse(
  inquiry: InquiryItem,
  faqs: FaqItem[]
): InquiryDetailResponse {
  return {
    inquiry,
    recommendation: generateRecommendation(inquiry, faqs)
  };
}
