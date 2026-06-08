# UCCIS-Signal-Layer-Input-System

## Project Overview

This project implements a structured Signal Layer / Input System using FastAPI.

The system generates deterministic and structured signals using real/semi-real CSV ingestion.

The implementation focuses on:

* trusted signal generation
* strict schema enforcement
* traceability
* reliable API outputs

---

## Tech Stack

* Python
* FastAPI
* Pandas
* Uvicorn

---

## Features

* Strict Signal Schema
* Deterministic Trace ID Generation
* CSV Based Data Ingestion
* Multi-Zone Signal Generation
* Multi-Domain Support
* Failure Handling
* Structured API Responses
* Console Logging

---

## Project Structure

```text
signal-layer-project
│
├──  traffic.csv
│
├── review_packets
│   
│
├── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Project

```bash
uvicorn app:app --reload
```

---

## API Endpoints

### Home Endpoint

```text
GET /
```

---

### Get All Signals

```text
GET /signals
```

---

### Get Single Signal

```text
GET /signal?zone_id=zone_1
```

---

## Sample Signal Output

```json
{
  "trace_id": "TRACE_ab12cd34",
  "zone_id": "zone_1",
  "domain": "traffic",
  "timestamp": "2026-01-01",
  "metrics": {
    "traffic_density": 60,
    "violations": 3
  }
}
```

---

## Failure Handling

The system handles:

* invalid zone IDs
* corrupted datasets
* missing data

---

## Logging

Console logs include:

* signal generation
* trace_id
* payload details

## Screenshots

1. FastAPI Server Running

<img width="1919" height="1030" alt="image" src="https://github.com/user-attachments/assets/d5063dac-d051-4512-aa99-d26518f97272" />

---
2. /signal?zone_id=zone_1

<img width="1914" height="1000" alt="image" src="https://github.com/user-attachments/assets/6ef85530-6d60-4450-a00f-5fd038f55d93" />

---
3. /signals

<img width="1918" height="991" alt="image" src="https://github.com/user-attachments/assets/a0f11562-2997-457d-b42f-fde3c95bc1bb" />


