# Multi-Agent LLM System Using Gemini API

## Overview

This project implements a multi-agent system utilizing the Gemini API, where agents communicate with each other collaboratively generate reports. The system consists of three agents: the **Customer Relation Officer**, the **Report Author**, and the **Editor**. Each agent plays a distinct role in the process of gathering information, drafting, reviewing, and finalizing reports.

## Table of Contents

- [Project Description](#project-description)
- [Agents Overview](#agents-overview)
- [System Workflow](#system-workflow)
- [Requirements](#requirements)

---

## Project Description

This project aims to create a collaborative environment for generating reports. Using the **Gemini API**, agents will communicate and handle tasks in the following sequence:

1. **Customer Relation Officer (CRO)**: Initiates the interaction with the user to gather report requirements, and delivers the collected data to the **Report Author**.
2. **Report Author**: Drafts the report based on the provided information and prepares it for review by the **Editor**.
3. **Editor**: Reviews the report for completeness, accuracy, and relevance. If necessary, provides revision feedback to the **Report Author** until the report is finalized.

The communication between the agents is structured using JSON, ensuring a clear and organized exchange of information and instructions.

---

## Agents Overview

### 1. Customer Relation Officer (CRO)
The **Customer Relation Officer (CRO)** is responsible for interacting with the user. The agent's main tasks include:
- Asking the user for the details of the report they need.
- Determining if any information is missing and requesting further clarification from the user.
- Sending the gathered data to the **Report Author** for drafting the report.

**Key tasks:**
- Gather report topics and required details.
- Request additional information if needed.
- Deliver the final collected information to the **Report Author**.

### 2. Report Author
The **Report Author** uses the collected data from the **Customer Relation Officer (CRO)** to begin drafting the report. The **Report Author** is responsible for:
- Writing the report based on the details received from the **CRO**.
- Revising the report based on feedback provided by the **Editor** until the report is satisfactory.

**Key tasks:**
- Draft the initial report.
- Revise the report as per **Editor**'s suggestions.
- Finalize the report when no further revisions are required.

### 3. Editor
The **Editor** reviews the report written by the **Report Author**. The **Editor** is responsible for:
- Checking the report's completeness and ensuring that it aligns with the user's expectations.
- Providing revision feedback to the **Report Author** if necessary.

**Key tasks:**
- Review the report.
- Provide revision requests if needed.
- Confirm when the report is complete and finalize it.

---

## System Workflow

1. **Customer Relation Officer** (CRO) initiates a conversation with the user to understand their needs.
2. CRO gathers necessary information and forwards it to the **Report Author**.
3. **Report Author** drafts the report based on the provided details.
4. The **Editor** reviews the report and provides feedback for revisions.
5. Once the **Editor** is satisfied, the report is finalized.

The interaction between agents follows a well-defined process, where JSON-structured data is exchanged to ensure clarity and consistency.

---

## Requirements

- Python 3.8 or higher
- `google-generativeai` library for integrating with Gemini API
- `python-dotenv` to manage environment variables
- Other dependencies listed in `requirements.txt`

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/multi-agent-llm.git
cd multi-agent-llm
