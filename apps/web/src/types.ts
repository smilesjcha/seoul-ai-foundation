export interface InquiryItem {
  id: string;
  channel: string;
  status: string;
  citizenName: string;
  subject: string;
  message: string;
  receivedAt: string;
  priority: string;
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
