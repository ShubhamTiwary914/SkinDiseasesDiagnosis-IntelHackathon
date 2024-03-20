
# Skin Diseases Analysis 
### Using Intel OneAPI Deep Learning CNN Model + Hugging Face Open Source LLAMA-2-7B Model 

<br />


## Problem Statement 

Skin diseases are pervasive health concerns affecting millions of individuals worldwide, posing significant challenges in diagnosis and treatment.
<br />
Despite advances in medical science, the accurate and timely identification of various skin conditions remains a considerable obstacle, leading to delayed interventions, misdiagnoses, and prolonged suffering for patients. 
<br />
Therefore, this Solution aims to develop robust ML & LLMsmodels capable of accurately identifying and classifying different skin diseases.


<br />


## Project Workflow

<h3>1. Image Classification CNN Model</h3>

 -  The CNN Model acts as a first step multi-label classification via open source skin diseases datasets.
 -  Trained on `Intel Developer Cloud (IDC)` provided Next Gen `Intel Xeon-based Premium CPUs` with oneAPI Toolkit such as:
    - `Modin`: Intel One API Extensions for pandas
    - `ITEX`:  Intel OneAPI Extensions for Tensorflow
  

<br />

<h3>2. LLM (RAG) based Symptom QA Checker </h3>

- Further symptom checking process is passed on using Q/A LLM App that Processes Medical Books and Generates questions on the suspected disease
- Using Open Source `Meta/LLAMA-2(7B) Model` via `Hugging Face Hub + Langchain `
- Stores Contents from Books onto a VectorDB by `Text Splitting + Storing the Vector Embeddings` and then use a Retriever to Generate Question-Answers


<br />


## Worflow Diagram

![psworkflow](https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT/assets/67773966/478eee40-7314-48e5-b6d4-42f56b541ef2)



## Setup and Getting Started

To check the Application running, view it live on:
```
  https://huggingface.co/spaces/shubhamtw/qaBot
```



<h4> Running the Application Locally </h4>

1. Clone the Repository
```
  git clone https://github.com/ShubhamTiwary914/skinDiseasesCNN-IIT.git
```

2. Install the Dependencies
```
  cd skinDiseasesCNN-IIT
  pip install -r requirements.txt
```

3. Run the Application (Using Streamlit)
```
  streamlit run app.py
```


<br />


## Screenshots
    
