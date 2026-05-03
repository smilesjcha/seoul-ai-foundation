import { useEffect, useState } from "react";
import { fetchInquiryDetail, fetchInquiries } from "./api";
import type { InquiryDetailResponse, InquiryItem } from "./types";

function formatDate(value: string) {
  return new Intl.DateTimeFormat("ko-KR", {
    dateStyle: "medium",
    timeStyle: "short"
  }).format(new Date(value));
}

export default function App() {
  const [items, setItems] = useState<InquiryItem[]>([]);
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [detail, setDetail] = useState<InquiryDetailResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const inquiries = await fetchInquiries();
      setItems(inquiries);
      setSelectedId(inquiries[0]?.id ?? null);
      setLoading(false);
    }

    void load();
  }, []);

  useEffect(() => {
    async function loadDetail() {
      if (!selectedId) {
        return;
      }

      const nextDetail = await fetchInquiryDetail(selectedId);
      setDetail(nextDetail);
    }

    void loadDetail();
  }, [selectedId]);

  return (
    <div className="page">
      <header className="hero">
        <div>
          <p className="eyebrow">Claude Desktop Workshop Demo</p>
          <h1>민원/FAQ 자동화 운영 콘솔</h1>
          <p className="subtitle">
            문의를 빠르게 분류하고, FAQ 기반 응답 초안과 검토 포인트를 확인하는
            강의용 프로토타입입니다.
          </p>
        </div>
      </header>

      <main className="layout">
        <section className="panel list-panel">
          <div className="panel-header">
            <h2>문의 목록</h2>
            <span>{items.length}건</span>
          </div>

          {loading ? <p>불러오는 중...</p> : null}

          <div className="inquiry-list">
            {items.map((item) => (
              <button
                key={item.id}
                className={`inquiry-card ${selectedId === item.id ? "active" : ""}`}
                onClick={() => setSelectedId(item.id)}
                type="button"
              >
                <div className="inquiry-top">
                  <span className={`badge priority-${item.priority}`}>{item.priority}</span>
                  <span className="badge neutral">{item.status}</span>
                </div>
                <h3>{item.subject}</h3>
                <p>{item.citizenName}</p>
                <small>{formatDate(item.receivedAt)}</small>
              </button>
            ))}
          </div>
        </section>

        <section className="panel detail-panel">
          <div className="panel-header">
            <h2>상세 및 추천 결과</h2>
          </div>

          {!detail ? (
            <p>문의 상세를 선택해 주세요.</p>
          ) : (
            <div className="detail-content">
              <article className="detail-block">
                <p className="label">원문 문의</p>
                <h3>{detail.inquiry.subject}</h3>
                <p className="meta">
                  {detail.inquiry.citizenName} · {detail.inquiry.channel} ·{" "}
                  {formatDate(detail.inquiry.receivedAt)}
                </p>
                <p className="message">{detail.inquiry.message}</p>
              </article>

              <article className="detail-block">
                <p className="label">AI 분류 결과</p>
                <div className="pill-row">
                  <span className="badge accent">{detail.recommendation.category}</span>
                  <span className="badge neutral">
                    FAQ {detail.recommendation.matchedFaqIds.length}건 매칭
                  </span>
                </div>
              </article>

              <article className="detail-block">
                <p className="label">응답 초안</p>
                <div className="draft-box">
                  {detail.recommendation.draftReply.split("\n").map((line) => (
                    <p key={line}>{line}</p>
                  ))}
                </div>
              </article>

              <article className="detail-block">
                <p className="label">운영자 검토 포인트</p>
                <ul className="notes">
                  {detail.recommendation.reviewNotes.map((note) => (
                    <li key={note}>{note}</li>
                  ))}
                </ul>
              </article>
            </div>
          )}
        </section>
      </main>
    </div>
  );
}
