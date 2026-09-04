from langchain_core.prompts import ChatPromptTemplate


summary_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are an expert text summarizer.

Summarize the user's text according to the requested length and style.

Return a clear and useful summary.
Do not add information that is not present in the original text.
""",
        ),
        (
            "human",
            """Text:
{text}

Summary length:
{length}

Summary style:
{style}
""",
        ),
    ]
)