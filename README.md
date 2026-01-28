# Semantic Search using Endee

## Overview
This project demonstrates a simple semantic search system built using embeddings and the Endee vector database.  
Instead of matching exact keywords, the system retrieves results based on the meaning of the query.

## Problem Statement
Traditional keyword-based search often fails when different words are used to express the same idea.  
This project shows how vector-based semantic search can retrieve relevant information based on intent rather than exact text matches.

## System Design
The system works in the following steps:
1. Text data is read from a file
2. Each text is converted into an embedding using a sentence-transformer model
3. Embeddings are stored as vectors in the Endee vector database
4. User queries are embedded and matched using cosine similarity
5. The most semantically relevant results are returned

## How Endee is Used
Endee is used as the vector database to:
- Store embeddings efficiently
- Perform fast similarity search using cosine distance
- Retrieve metadata associated with the closest vectors

The index is created locally and queried through the Endee Python SDK.

## Setup and Running the Project

### Prerequisites
- Python 3.10+
- Docker (for running Endee locally)

### Steps
1. Start the Endee server locally using Docker
2. Install Python dependencies
3. Ingest data into Endee
4. Run semantic search queries

```bash
pip install -r requirements.txt
python ingest.py
python search.py
