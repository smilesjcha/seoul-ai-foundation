import { Router } from "express";
import { buildInquiryDetailResponse, generateRecommendation } from "../lib/ai.js";
import { getFaqs, getInquiryById, getInquiries } from "../lib/mockData.js";

export const inquiryRouter = Router();

inquiryRouter.get("/", (_request, response) => {
  response.json({ items: getInquiries() });
});

inquiryRouter.get("/:id", (request, response) => {
  const inquiry = getInquiryById(request.params.id);

  if (!inquiry) {
    response.status(404).json({ message: "Inquiry not found" });
    return;
  }

  response.json(buildInquiryDetailResponse(inquiry, getFaqs()));
});

inquiryRouter.post("/:id/recommendation", (request, response) => {
  const inquiry = getInquiryById(request.params.id);

  if (!inquiry) {
    response.status(404).json({ message: "Inquiry not found" });
    return;
  }

  response.json(generateRecommendation(inquiry, getFaqs()));
});
