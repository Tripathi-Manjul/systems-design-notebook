# Kleppmann Chapter 1–2: Data Models – Summary & System Design Implications

## Part A: Key Concepts from Kleppmann

### 1. Data Model Abstractions

- **Relational Model**: Structured in tables with fixed schemas; supports joins, normalization.
- **Document Model**: Semi-structured (e.g., JSON), flexible schema; denormalization is common.
- **Graph Model**: Nodes and edges represent entities and relationships; useful for deeply connected data.

### 2. Schema Design

- **Schema-on-write (relational)**: Structure enforced at the time of data ingestion.
- **Schema-on-read (document/NoSQL)**: Flexibility at write time, schema applied when queried.

### 3. Normalization vs Denormalization

- **Normalization** reduces redundancy, supports consistency, enables referential integrity.
- **Denormalization** improves read performance by reducing joins but introduces duplication.

### 4. Data Encoding and Storage

- Values must be **serialized into bytes** for storage and transmission.
- Encoding affects **comparability and sort order**, which directly impacts how indexes behave.

---

## Part B: Implications for Indexing and B-trees

| Concept                          | B-tree Relevance                                                                 |
|----------------------------------|----------------------------------------------------------------------------------|
| Joins in relational model        | Require fast foreign-key lookups → B-trees provide O(log n) access to keys      |
| Range queries (e.g., BETWEEN)    | B-trees maintain keys in sorted order → supports efficient range scans          |
| Denormalized document access     | Indexes on nested fields → tree-like traversal similar to B-trees               |
| Ordered scans or pagination      | B-trees allow in-order traversal → supports LIMIT/OFFSET and cursor-based fetch |
| Encoding impact                  | Keys must be byte-comparable → incorrect encoding can break index order         |

---

## Additional Learning Outcomes

- Understand when different models are used and how indexing must adapt.
- Realize that B-trees remain core across both SQL and many NoSQL systems for ordered/indexed access.
- Prepare to implement a basic B-tree to solidify indexing logic.

---

## Next: Explore

- [`b-tree.py`](./b-tree.py): A basic B-tree implementation with search and insert operations.
- [`normalization.md`](./normalization.md): Tradeoffs in data modeling and their impact on indexing.
- [`encoding.md`](./encoding.md): How encoding formats affect indexability and comparison logic.
