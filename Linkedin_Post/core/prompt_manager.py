from langchain_core.prompts import PromptTemplate

def get_prompt():
    return PromptTemplate(
        input_variables=["role", "topic", "memory"],
        template="""
You are a {role} writing LinkedIn posts.

Below is the user's past journey and conversations.
You MUST treat them as real experiences and CONTINUE the story.
Reuse relevant lessons, emotions, and growth from earlier posts
to make the new post feel like a natural continuation.

Past journey:
{memory}

Current topic:
"{topic}"

Instructions:
- Explicitly connect past experiences where relevant
- Show progression (learning → struggle → growth)
- Keep a reflective, personal tone
- Do NOT repeat old content verbatim
- End with 3–5 relevant hashtags

Write only the final LinkedIn post.
"""
    )
