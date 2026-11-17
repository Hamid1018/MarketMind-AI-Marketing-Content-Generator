from datetime import datetime

from sqlalchemy import DateTime, Integer, Text
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Campaign(Base):
    __tablename__ = "campaigns"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    product_name: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    product_description: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    target_audience: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    marketing_platform: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    campaign_objective: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    tone: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    preferred_language: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    strategy_json: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )