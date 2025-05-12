# Normalization vs Denormalization: Indexing Trade-offs

## What is Normalization?

Normalization is the process of structuring data to eliminate redundancy and ensure consistency. It typically involves:

- Splitting data into multiple tables.
- Using foreign keys to reference related records.
- Enforcing integrity constraints.

### Example (Relational Schema – Normalized)

```sql
Users(id, name)
Orders(id, user_id, total_amount)
```

### Implication for Indexing

 - Frequent joins between tables (e.g., Orders JOIN Users ON user_id) require fast foreign-key lookups.
 - B-trees are used on user_id to provide O(log n) lookup during joins.

### What is Denormalization?

 - Denormalization duplicates data across records to reduce join overhead and optimize read performance.

### Example (Document Schema – Denormalized)
```sql
{
  "order_id": 101,
  "user": { "id": 1, "name": "Alice" },
  "total_amount": 500
}
```

### Implication for Indexing

 - Data is often nested or repeated, but needs to be indexed by fields inside documents (e.g., user.id).
 - B-tree–like structures or composite indexes are used to index nested fields efficiently.

### Trade-offs and Role of B-trees

| Feature             | Normalized (Relational)      | Denormalized (Document)             |
| ------------------- | ---------------------------- | ----------------------------------- |
| Access Pattern      | Joins → key lookups          | Direct access → fewer joins         |
| Index Use           | Foreign key indexes (B-tree) | Nested field indexes (B-tree-style) |
| Write Amplification | Low (minimal duplication)    | High (redundant writes)             |
| Read Performance    | Slower due to joins          | Faster for common queries           |
| Indexing Complexity | Moderate                     | Higher for deep/nested fields       |


### Why B-trees Remain Core

Regardless of model:
 - B-trees support efficient range and equality queries.
 - Ordered nature of B-trees makes them ideal for BETWEEN, LIMIT, and foreign-key lookups.
 - Most storage engines (InnoDB, RocksDB, WiredTiger) use B-tree or LSM tree variants under the hood.