import { Router } from "express";
import { getFaqs } from "../lib/mockData.js";

export const faqRouter = Router();

faqRouter.get("/", (_request, response) => {
  response.json({ items: getFaqs() });
});
