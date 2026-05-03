export type InquiryStatus = "new" | "reviewed" | "sent";
export type InquiryPriority = "low" | "medium" | "high";

export interface FaqItem {
  id: string;
  category: string;
  question: string;
  answer: string;
  tags: string[];
}

export interface InquiryItem {
  id: string;
  channel: string;
  status: InquiryStatus;
  citizenName: string;
  subject: string;
  message: string;
  receivedAt: string;
  priority: InquiryPriority;
}

export interface InquiryRecommendation {
  inquiryId: string;
  category: string;
  matchedFaqIds: string[];
  draftReply: string;
  reviewNotes: string[];
}

export interface InquiryDetailResponse {
  inquiry: InquiryItem;
  recommendation: InquiryRecommendation;
}
