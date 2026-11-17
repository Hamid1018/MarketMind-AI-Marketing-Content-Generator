import json

from groq import Groq

from .database import settings
from .prompts import SYSTEM_PROMPT, build_user_prompt
from .schemas import CampaignInput, MarketingStrategy
from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from backend/.env

groq_api_key = os.getenv("GROQ_API_KEY")

STRATEGY_SCHEMA = {

    "type": "object",

    "properties": {

        "campaign_idea": {
            "type": "string"
        },

        "campaign_objective": {
            "type": "string"
        },

        "target_audience": {
            "type": "string"
        },

        "audience_angle": {
            "type": "string"
        },

        "key_selling_points": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        "key_message": {
            "type": "string"
        },

        "content_pillars": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        "content_tone": {
            "type": "string"
        },

        "call_to_action": {
            "type": "string"
        },

        "suggested_content_types": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },

        "platform_reason": {
            "type": "string"
        }
    },

    "required": [
        "campaign_idea",
        "campaign_objective",
        "target_audience",
        "audience_angle",
        "key_selling_points",
        "key_message",
        "content_pillars",
        "content_tone",
        "call_to_action",
        "suggested_content_types",
        "platform_reason"
    ],

    "additionalProperties": False
}


def generate_strategy(
    campaign: CampaignInput
) -> MarketingStrategy:

    if not groq_api_key:

        raise RuntimeError(
            "GROQ_API_KEY is not configured. "
            "Add it to backend/.env."
        )

    client = Groq(
        api_key=settings.GROQ_API_KEY
    )

    response = client.chat.completions.create(

        model=settings.GROQ_MODEL,

        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": build_user_prompt(
                    campaign.model_dump()
                )
            }
        ],

        temperature=0.3,

        response_format={
            "type": "json_schema",

            "json_schema": {
                "name": "marketing_strategy",

                "strict": True,

                "schema": STRATEGY_SCHEMA
            }
        }
    )

    raw_output = response.choices[0].message.content

    if not raw_output:

        raise RuntimeError(
            "Groq returned an empty response."
        )

    try:

        parsed = json.loads(raw_output)

        return MarketingStrategy.model_validate(
            parsed
        )

    except (
        json.JSONDecodeError,
        ValueError
    ) as exc:

        raise RuntimeError(
            f"Groq returned invalid strategy JSON: {exc}"
        ) from exc