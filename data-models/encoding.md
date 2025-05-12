# Data Encoding and Storage: Implications for B-tree Indexing

## What is Data Encoding?

Encoding refers to how structured data (like strings, numbers, or objects) is converted into a byte sequence for storage or transmission.

### Examples:
- UTF-8 for strings
- Variable-length encoding for integers
- Protocol Buffers, Avro, JSON for documents

---

## Why Encoding Matters for Indexing

B-tree indexes operate on **byte-ordered keys**.

Hence, encoding impacts:

| Aspect               | Encoding Impact                                                                 |
|----------------------|----------------------------------------------------------------------------------|
| **Sort order**       | Must ensure that encoded bytes preserve logical ordering (e.g., 2 < 10)         |
| **Prefix compression** | Efficient for sorted data; used by B-tree variants to reduce space            |
| **Key comparisons**  | Performed byte-by-byte; encoding must make this semantically correct            |
| **Range queries**    | BETWEEN, >=, <= require consistent byte order over encoded keys                 |

---

## Practical Example

Imagine these keys in a B-tree index:

- `2`, `10`, `20`

If encoded as UTF-8 strings:  
→ `'10' < '2' < '20'` ❌ (lexical order is incorrect for numeric values)

If encoded as fixed-width integers:  
→ `002 < 010 < 020` ✅ (correct for numeric sorting)

---

## Binary Encoding in Storage Engines

| Storage Engine | Encoding Strategies                                   |
|----------------|--------------------------------------------------------|
| InnoDB (MySQL) | Uses compact row format, stores encoded keys for clustering |
| RocksDB        | Uses prefix compression, memtable encoding             |
| MongoDB        | BSON encoding → field order and key serialization affect index usage |

---

## Design Principle

> **Index performance depends not only on structure (like B-tree), but also on the layout of keys.**

- Well-designed encodings preserve ordering, reduce disk I/O, and support range scans.
- Poor encodings break indexing guarantees or degrade performance.

---

## Summary

- B-trees depend on byte-wise key comparisons.
- Correct encoding ensures correct order, efficient range scans, and disk layout optimization.
- When designing indexes or modeling data, always consider how the data is serialized before being indexed.
