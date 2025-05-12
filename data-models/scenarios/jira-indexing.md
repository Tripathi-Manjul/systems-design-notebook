# Case Study: Indexing in a Ticket Management System (Jira)

## Problem Statement

Design an indexing strategy for a ticketing system (like Jira) that handles:

- 100M+ tickets
- Frequent reads by `project_id`
- Range filters by `created_at`

## Indexing Strategy

- Use a **composite B-tree index** on `(project_id, created_at)`
- Allows fast retrieval of tickets for a given project sorted by creation date
- Supports pagination and time-bound queries efficiently

## Trade-offs

| Aspect        | Pros                                 | Cons                                |
|---------------|--------------------------------------|-------------------------------------|
| Read Latency  | Fast range scans                     |                                     |
| Write Cost    | Moderate — insertions may trigger B-tree rebalancing | Slight latency for ticket creation |
| Storage       | Efficient due to ordered structure   | Index size grows with ticket volume |

## Real-world Relevance

- Similar indexing strategies are used in systems like:
  - **PostgreSQL** with `btree` indexes
  - **ElasticSearch** with timestamp+project filters
  - **MongoDB** with compound indexes on documents
