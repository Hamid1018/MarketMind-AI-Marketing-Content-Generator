from fastapi import FastAPI

app = FastAPI()

import json

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import Base, engine, get_db, settings
from .llm import generate_strategy
from .models import Campaign
from .schemas import (
    CampaignInput,
    CampaignListItem,
    CampaignResponse,
)


# Create database tables
Base.metadata.create_all(bind=engine)


# IMPORTANT: this is the app that Uvicorn looks for
app = FastAPI(
    title="AI Marketing Content Generator",
    version="1.0.0",
)


# Allow React frontend to communicate with FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "marketing-strategy-api",
    }


@app.post(
    "/api/campaigns/strategy",
    response_model=CampaignResponse,
)
def create_strategy(
    campaign: CampaignInput,
    db: Session = Depends(get_db),
):
    try:
        strategy = generate_strategy(campaign)

    except RuntimeError as exc:
        raise HTTPException(
            status_code=502,
            detail=str(exc),
        ) from exc

    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"LLM request failed: {exc}",
        ) from exc

    record = Campaign(
        **campaign.model_dump(),
        strategy_json=json.dumps(
            strategy.model_dump(),
            ensure_ascii=False,
        ),
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return CampaignResponse(
        id=record.id,
        message="Marketing strategy generated successfully.",
        strategy=strategy,
    )


@app.get(
    "/api/campaigns",
    response_model=list[CampaignListItem],
)
def list_campaigns(
    db: Session = Depends(get_db),
):
    rows = (
        db.query(Campaign)
        .order_by(Campaign.id.desc())
        .limit(20)
        .all()
    )

    return [
        CampaignListItem(
            id=row.id,
            product_name=row.product_name,
            marketing_platform=row.marketing_platform,
            campaign_objective=row.campaign_objective,
            created_at=row.created_at.isoformat(),
        )
        for row in rows
    ]