import os
from dotenv import load_dotenv

load_dotenv(override=True)

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class Company(BaseModel):
    name: str = Field(description="The Company Name")
    ticker: str = Field(description="The Stock Ticker")
    founded_year: int = Field(description="The year that the Company was founded")


llm = ChatOpenAI(model="gpt-5.4-mini")

structured_llm = llm.with_structured_output(Company)

company = structured_llm.invoke("Tell me about Google Technology Company")


print(company)
print(company.ticker)