import type { InquiryDetailResponse, InquiryItem } from "./types";

const API_BASE = "http://localhost:4000/api";

export async function fetchInquiries(): Promise<InquiryItem[]> {
  const response = await fetch(`${API_BASE}/inquiries`);
  const payload = await response.json();
  return payload.items;
}

export async function fetchInquiryDetail(id: string): Promise<InquiryDetailResponse> {
  const response = await fetch(`${API_BASE}/inquiries/${id}`);
  return response.json();
}
