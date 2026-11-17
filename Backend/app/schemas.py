from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Platform = Literal[
    "Instagram",
    "LinkedIn",
    "Facebook",
    "YouTube"
]

Tone = Literal[
    "Professional",
    "Friendly",
    "Bold",
    "Luxury",
    "Playful",
    "Educational"
]


class CampaignInput(BaseModel):
    product_name: str = Field(
        min_length=2,
        max_length=100
    )

    product_description: str = Field(
        min_length=20,
        max_length=1000
    )

    target_audience: str = Field(
        min_length=3,
        max_length=300
    )

    marketing_platform: Platform

    campaign_objective: str = Field(
        min_length=5,
        max_length=200
    )

    tone: Tone

    preferred_language: str = Field(
        min_length=2,
        max_length=50
    )


class MarketingStrategy(BaseModel):

    campaign_idea: str

    campaign_objective: str

    target_audience: str

    audience_angle: str

    key_selling_points: list[str] = Field(
        min_length=3,
        max_length=6
    )

    key_message: str

    content_pillars: list[str] = Field(
        min_length=3,
        max_length=5
    )

    content_tone: str

    call_to_action: str

    suggested_content_types: list[str] = Field(
        min_length=3,
        max_length=6
    )

    platform_reason: str

    model_config = ConfigDict(
        extra="forbid"
    )


class CampaignResponse(BaseModel):
    id: int
    message: str
    strategy: MarketingStrategy


class CampaignListItem(BaseModel):
    id: int
    product_name: str
    marketing_platform: str
    campaign_objective: str
    created_at: str