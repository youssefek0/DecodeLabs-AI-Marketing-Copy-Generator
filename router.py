"""
router.py

Routes generation settings based on the target platform.
"""

from dataclasses import dataclass


@dataclass
class GenerationSettings:
    """
    Stores all generation parameters.
    """

    temperature: float

    max_completion_tokens: int

    top_p: float

    frequency_penalty: float

    presence_penalty: float


PLATFORM_CONFIG = {

    "Instagram":

        GenerationSettings(

            temperature=0.85,

            max_completion_tokens=180,

            top_p=0.95,

            frequency_penalty=0.2,

            presence_penalty=0.3

        ),

    "LinkedIn":

        GenerationSettings(

            temperature=0.30,

            max_completion_tokens=400,

            top_p=0.90,

            frequency_penalty=0.10,

            presence_penalty=0.0

        ),

    "Email":

        GenerationSettings(

            temperature=0.20,

            max_completion_tokens=350,

            top_p=0.90,

            frequency_penalty=0.0,

            presence_penalty=0.0

        ),

    "Twitter":

        GenerationSettings(

            temperature=0.80,

            max_completion_tokens=100,

            top_p=0.95,

            frequency_penalty=0.20,

            presence_penalty=0.40

        ),

    "Facebook":

        GenerationSettings(

            temperature=0.60,

            max_completion_tokens=250,

            top_p=0.90,

            frequency_penalty=0.10,

            presence_penalty=0.20

        )

}

def get_generation_settings(platform: str) -> GenerationSettings:
    """
    Returns the settings for a platform.
    """

    return PLATFORM_CONFIG[platform]