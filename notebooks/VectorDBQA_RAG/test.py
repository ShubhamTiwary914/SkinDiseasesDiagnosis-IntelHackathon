from langchain.llms import CTransformers
llm=CTransformers(
    model="TheBloke/Llama-2-7B-Chat-GGML",              
    model_type="llama",
    config={'max_new_tokens':512,
    'temperature':0.8}
)
llm