from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import config
from prompts import summary_prompt


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
)

chain = summary_prompt | model | StrOutputParser()

def summarize(text: str, length: str, style: str) -> str:
    result = chain.invoke(
        {
            "text": text,
            "length": length,
            "style": style,
        }
    )

    return result