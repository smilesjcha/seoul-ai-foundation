import faqs from "../../../../data/mock/faqs.json";
import inquiries from "../../../../data/mock/inquiries.json";
import type { FaqItem, InquiryItem } from "./types.js";

export function getFaqs(): FaqItem[] {
  return faqs as FaqItem[];
}

export function getInquiries(): InquiryItem[] {
  return inquiries as InquiryItem[];
}

export function getInquiryById(id: string): InquiryItem | undefined {
  return getInquiries().find((item) => item.id === id);
}
