"""
models.py

Pydantic models used throughout the Marketing Copy Generator.
"""

from pydantic import BaseModel, Field, field_validator


class CopyRequest(BaseModel):
    """
    Represents one marketing copy request.
    """

    product_name: str
    platform: str
    tone: str
    char_limit: int = Field(default=300, gt=0)

    
    @field_validator("platform")
    @classmethod
    def validate_platform(cls, value: str):
        allowed = {
            "Instagram",
            "LinkedIn",
            "Email",
            "Twitter",
            "Facebook"
        }

        if value not in allowed:
            raise ValueError(
                f"Platform must be one of {allowed}"
            )

        return value


    @field_validator("tone")
    @classmethod
    def validate_tone(cls, value: str):

        allowed = {
            "Professional",
            "Friendly",
            "Luxury",
            "Urgent",
            "Casual",
            "Witty"
        }

        if value not in allowed:
            raise ValueError(
                f"Tone must be one of {allowed}"
            )

        return value


class CopyOutput(BaseModel):
    """
    Validated AI output.
    """

    platform: str
    tone: str
    copy_text: str
    word_count: int

    @field_validator("word_count")
    @classmethod
    def validate_word_count(cls, value):

        if value < 0:
            raise ValueError(
                "Word count cannot be negative."
            )

        return value