# MedvAIsor
The MedvAIsor acronym is a fusion of the word Medicine + (Advisor + AI). This hackathon project built a web-based tool that showcases a GBM case study where we can perform virtual drug screening for seven FDA-approved GBM drugs. The tool takes the GBM cancer cell line of 657 genes as input and predicts the efficacy of the seven drugs. The tool screens individual cancer cell lines and shows the effectiveness of each drug along with its threshold values. In this project, we also showcase the use of NLP to process the drugs SMILES in a novel way, and this method enables us to build a competent model that we used in our MedvAIsor tool. This project also shows that the ML model we developed for MedvAIsor generalizes performing drug repurposing. We proved this by predicting the efficiently repurposing of two drugs, Temozolomide and Carmustine, with MAE of (0.5 and 0.4, respectively). These two drugs are already approved for GBM treatment by FDA.

## Motivation
Personalized drug screening is one of the vital drug development phases for precision oncology. In this phase, each patient is screened for the efficacy of a given drug on a particular type of cancer. For this phase, the in-vivo screening is challenging; therefore, in-vitro screening is widespread. Cancer samples are screened for drug perturbations on tumors, and treatment can be recommended. The duration of in-vitro screening also varies from 6 to 72 hours (but can be longer). The drug perturbation screening facility is also unavailable in most clinics; therefore, logistics delay the screening time. One can view model-based virtual screening as a solution to such delays. Thus, in-silico drug screening is also becoming essential for precision oncology.

## Project Overview
![project-Page-8 drawio](https://user-images.githubusercontent.com/56318274/183274235-28ad53c6-de52-4bd3-aa15-7c04e469dbf4.png)
In this hackathon, we attempt to build a personalized drug screening tool called MedvAIsor that uses Gene Expression data of patients’ tumor cell lines and predicts the efficacy of the drugs in LN(IC50). The demonstrator of the tool is built using the Python Streamilit App. The tool is dedicated to showcasing the study of the Glioblastoma Multiform (GBM) case study.  Besides the tool, the project also put forward an innovative way of processing the drug data (SMILES) using Natural Language Procession. We also show how the ML model used by MedvAIsor for drug screening can be used to perform drug repurposing for the approved FDA drugs for GBM cancer. ![image](https://user-images.githubusercontent.com/56318274/183274287-fd45deb8-3e39-4c7d-87df-9eef730f9737.png)

# Project Highlights

## This Project Uses a unique Combination of Drug-Disease-Gene Expression data to perform Personalized Drug Screening
![projectDiagram-Page-19 drawio (2)-Page-6 drawio](https://user-images.githubusercontent.com/56318274/183274399-cfdd6861-18dc-4056-8141-b2e4fbe4a74a.png)

## The ML model is a LightGBM Regression Algorithm and Predicts Drug Perturbations in the form of LN(IC50)

![projectDiagram-Page-19 drawio (2)-Page-7 drawio](https://user-images.githubusercontent.com/56318274/183274512-e5dd46b6-7ca6-4160-97ed-a245ba8f0541.png)

## NLP is used to extract Features from Drug Smiles
![image](https://user-images.githubusercontent.com/56318274/183274573-27d76652-87ac-4780-a7b6-9f5fdbf320d3.png)

## The Model also Generalizes to repurpose FDA approved Glioblastoma Drugs (Temozolomide and Carmustine)

![image](https://user-images.githubusercontent.com/56318274/183274651-73ad8e57-200d-441f-aa00-74ba1a8ddfb8.png)
![image](https://user-images.githubusercontent.com/56318274/183274666-6145edb1-09d2-4087-8655-78b0c6020933.png)

# Applications
## Impact of Project in Medicine Domain (Drug Recommendations)
The GBM case study of the MedvAIsor web app shows the potential of our tool where the doctor can provide the gene expression (657 genes) of a patient’s tumor to the software and get the screening values of the seven drugs. This result will help the doctor make the Monotherapy treatment plan for the patient.
## Impact of work in Drug Discovery (Drug Screening & repurposing)
The ML model built in this hackathon can be you to check the varying effects of the seven drugs on multiple patients. This helps select a cohort for clinical trials for de-novo drug discovery or drug repurposing (this screening is only possible with drugs that are structurally similar to the seven drugs)


## Team Members
Arsalan Ahmad | aahmad@asfaschool.org | Data Analysis work

DaVonte Curtis | davontecurtis4@gmail.com | Product Developer

Kermit Glenn Booker Jr | kermit.booker@bulldogs.aamu.edu | Product Developer

Rizwan Ahmad | rizwanahmad95@outlook.com | Data Analysis work

Mary Doamekpor | mdoam5@uab.edu | Biologist

Radomir Slominski | rslom@uab.edu | Biologist

Dr. Ehsan Saghapour | ehsan.saghapour@gmail.com | Machine Learning and Data Science

Dr. Rahul Sharma | rsharma3@uab.edu | Team Lead

Dr. Jake Y. Chen | jakechen@uab.edu | Mentor
