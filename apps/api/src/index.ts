import cors from "cors";
import express from "express";
import { faqRouter } from "./routes/faqs.js";
import { inquiryRouter } from "./routes/inquiries.js";

const app = express();
const port = 4000;

app.use(cors());
app.use(express.json());

app.get("/health", (_request, response) => {
  response.json({ ok: true });
});

app.use("/api/faqs", faqRouter);
app.use("/api/inquiries", inquiryRouter);

app.listen(port, () => {
  console.log(`API server is running at http://localhost:${port}`);
});
