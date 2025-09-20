# from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class QueryRequest(BaseModel):
    question: str
    session_id: str | None = None


class QueryResponse(BaseModel):
    answer: str
    session_id: str | None = None


class IngestRequest(BaseModel):
    source_url: HttpUrl | None = None
    content: str | None = None


class IngestResponse(BaseModel):
    status: str
    items_ingested: int


@app.post("/query", response_model=QueryResponse)
async def post_query(payload: QueryRequest) -> QueryResponse:
    if not payload.question.strip():
        raise HTTPException(status_code=400, detail="Question is required")
    # TODO: delegate to query service
    return QueryResponse(
        answer="(stub) This is a placeholder answer.", session_id=payload.session_id
    )


@app.post("/ingest", response_model=IngestResponse)
async def post_ingest(payload: IngestRequest) -> IngestResponse:
    if not payload.source_url and not payload.content:
        raise HTTPException(status_code=400, detail="Provide either source_url or content")
    # TODO: delegate to ingestion service
    return IngestResponse(status="ok", items_ingested=1)
