"""
prompts.py

Dynamic prompt compiler for the Marketing Copy Generator.
"""

from models import CopyRequest


def build_prompt(request: CopyRequest) -> str:
    """
    Builds a dynamic prompt from a validated CopyRequest.
    """

    prompt = f"""
You are an expert marketing copywriter.

Your task is to create compelling marketing copy.

PRODUCT
-------
{request.product_name}

TARGET PLATFORM
---------------
{request.platform}

DESIRED TONE
------------
{request.tone}

CONSTRAINTS
-----------
Maximum length: {request.char_limit} characters.

GENERAL REQUIREMENTS
--------------------
- Be persuasive.
- Be grammatically correct.
- Do not invent product features.
- Keep the tone consistent.
- Avoid repetition.
- Produce only the requested copy.
"""

    prompt += get_platform_instructions(request.platform)

    prompt += get_tone_instructions(request.tone)

    return prompt












def get_platform_instructions(platform: str) -> str:

    platforms = {

        "Instagram": """

PLATFORM RULES
--------------
- Make it energetic.
- Use emojis naturally.
- Include 3-5 hashtags.
- Short paragraphs.
- Strong call-to-action.

""",

        "LinkedIn": """

PLATFORM RULES
--------------
- Professional writing.
- No emojis unless appropriate.
- Around 150–200 words.
- Highlight value.
- End with a thoughtful takeaway.

""",

        "Email": """

PLATFORM RULES
--------------
- Write a subject line.
- Professional formatting.
- Greeting.
- Body.
- Strong closing CTA.

""",

        "Twitter": """

PLATFORM RULES
--------------
- Hard limit of 280 characters.
- One or two hashtags.
- Punchy.
- High engagement.

""",

        "Facebook": """

PLATFORM RULES
--------------
- Friendly.
- Storytelling style.
- Invite comments.
- Medium-length paragraphs.

"""
    }

    return platforms.get(platform, "")









def get_tone_instructions(tone: str):

    tones = {

        "Professional": """

TONE
----
Write formally.
Focus on credibility.
Use polished language.

""",

        "Friendly": """

TONE
----
Warm.
Approachable.
Conversational.

""",

        "Luxury": """

TONE
----
Elegant.
Premium.
Sophisticated.
Exclusive wording.

""",

        "Urgent": """

TONE
----
Create urgency.
Encourage immediate action.
Do not sound spammy.

""",

        "Casual": """

TONE
----
Relaxed.
Simple language.
Natural wording.

""",

        "Witty": """

TONE
----
Clever.
Playful.
Humorous.
Avoid cringe jokes.

"""
    }

    return tones.get(tone, "")










request = CopyRequest(

    product_name="AirPods Pro",

    platform="Instagram",

    tone="Witty",

    char_limit=180

)

prompt = build_prompt(request)

#print(prompt)






