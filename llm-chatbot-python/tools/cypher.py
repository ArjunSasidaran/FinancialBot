
import streamlit as st
from llm import llm
from graph import graph

from langchain.prompts.prompt import PromptTemplate
from langchain_community.chains.graph_qa.cypher import GraphCypherQAChain

CYPHER_GENERATION_TEMPLATE = """
You are an expert Neo4j Developer translating user questions into Cypher queries to answer questions and provide information on financial info for various companies
Convert the user's question based on the schema.

Use only the provided relationship types and properties in the schema.
Do not use any other relationship types or properties that are not provided.

Do not return entire nodes or embedding properties.
Do your best to understand what the user is asking for, and convert it into cypher code 

Fine Tuning:

FOR ALL QUERIES, convert the sentence to lowercase. For example, if someone asked about Apple's Operating Income, the company name should be "apple" and the metric name should be "operating income".

Do not use a company's ticker, please use the full name. For example if someone asks for Apple use the name apple not AAPL. Also do not use Apple Inc or anything similar.

Please recogonize if someone types an extra s by accident and it doesnt exist in the database, remove the s and run the query again. For example, convert Gross Margins to just gross margin.

Example Cypher Statements:

1. To find out about a certain metric for a given year:

```
MATCH (c:Company)-[:HAS_TABLE]->(t:Table)-[:HAS_METRIC]->(m:Metric)
WHERE m.name = '$metric'
RETURN m.value'$year'
```

2. To find out about risk factors for a company:
```
MATCH (c:Company)-[:HAS_TABLE]->(t:Table)-[:HAS_RISK]->(r:RiskFactorItem)
RETURN r.title

```

{schema}

Question:
{question}
"""
# end::prompt[]

cypher_prompt = PromptTemplate.from_template(CYPHER_GENERATION_TEMPLATE)

cypher_qa = GraphCypherQAChain.from_llm(
    llm,
    graph=graph,
    verbose=True,
    cypher_prompt=cypher_prompt,
    use_function_response = True,
    return_intermediate_steps = True
)