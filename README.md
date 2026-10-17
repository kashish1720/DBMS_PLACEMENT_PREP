<div align="center">

# 🗄️ DBMS Placement Notes

### 10-Day Roadmap · Concepts + SQL + MCQs + Interview Traps

![Status](https://img.shields.io/badge/Status-In_Progress-yellow?style=for-the-badge)

*4th-year engineering student · preparing for service & product company placements*

</div>

---

## 📊 Progress Tracker

<!-- PROGRESS:START -->
![Progress](https://img.shields.io/badge/Progress-4%25-red?style=for-the-badge) ![Tasks](https://img.shields.io/badge/Tasks-2%2F49-blue?style=for-the-badge)

**Overall:** `⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜` **4%** (2/49 tasks done)
<!-- PROGRESS:END -->

👉 **Tick karne ke liye:** [📈 Progress Tracker issue kholo](../../issues) aur checkbox par click karo. Yeh bar apne aap update ho jaayega.

---

## 🎯 Priority List (kya zyada important hai)

> Yeh general pattern hai. Apni target company ka exact OA/interview pattern uski official careers page aur recent interview experiences se verify karo.

| Priority | Topic | OA / MCQ | Interview |
|---|---|---|---|
| 🔴 **Tier 1** | SQL queries (joins, GROUP BY/HAVING, subquery, aggregates) | Output + coding | Live query |
| 🔴 **Tier 1** | Normalization (FD, closure, candidate key, 1NF to BCNF) | Numerical MCQs | 3NF vs BCNF |
| 🔴 **Tier 1** | Keys (super, candidate, primary, foreign) | Direct MCQs | Har interview |
| 🔴 **Tier 1** | ACID + Transactions + Isolation levels | MCQs | Almost guaranteed |
| 🔴 **Tier 1** | Indexing (clustered vs non-clustered, B+ tree basics) | Kam | Product companies |
| 🟠 **Tier 2** | ER model, cardinality | Medium | Basic |
| 🟠 **Tier 2** | Relational algebra | Medium | Kam |
| 🟠 **Tier 2** | Serializability, schedules, deadlock, locking | Numerical MCQs | Concept level |
| 🟠 **Tier 2** | DBMS vs File system, architecture, data independence | Easy marks | Warm-up |
| 🟢 **Tier 3** | 4NF/5NF, view serializability, recovery, denormalization | Rare | Rare |

**80/20 rule:** Tier 1 pakka kar lo, zyada tar OA aur interview questions cover ho jaate hain.

---

## 🗓️ 10-Day Schedule

> Tick karne ka kaam Progress Tracker issue mein hota hai. Yeh section sirf reference hai.

### Day 1: Foundations 🟠
- Data vs information, database, DBMS
- File system ke problems vs DBMS advantages
- 1-tier / 2-tier / 3-tier architecture
- Three-schema architecture, data independence
- DBA, DDL / DML / DCL / TCL
- 20 MCQs
- **Trap:** 3-tier architecture aur 3-schema architecture alag cheezein hain.

### Day 2: ER Model + Keys + Relational Algebra 🔴
- Entity, weak entity, attributes (simple, composite, multivalued, derived)
- Relationships, cardinality (1:1, 1:N, M:N), participation
- ER diagram to tables
- Super / Candidate / Primary / Alternate / Foreign key
- Relational algebra: σ π ∪ − × ⋈
- Keys numericals + 20 MCQs
- **Trap:** Primary key NULL nahi ho sakti.

### Day 3: SQL Basics 🔴
- CREATE, ALTER, DROP, TRUNCATE vs DELETE
- INSERT, UPDATE, SELECT
- Constraints (PK, UNIQUE, NOT NULL, CHECK, FK, DEFAULT)
- WHERE, LIKE, IN, BETWEEN, IS NULL
- Aggregates, GROUP BY, HAVING
- SQLBolt + 6 LeetCode problems
- **Trap:** `COUNT(*)` vs `COUNT(column)`, WHERE mein aggregate nahi chalta.

### Day 4: SQL Joins, Subqueries, Views, Indexes 🔴
- INNER, LEFT, RIGHT, FULL, SELF, CROSS join
- Subqueries, correlated subqueries, EXISTS, IN
- UNION vs UNION ALL, INTERSECT
- Views, indexes, stored procedures (overview)
- 8 LeetCode problems
- **Trap:** `NOT IN` aur NULL ka issue.

### Day 5: SQL Practice Day 🔴
- Window functions: ROW_NUMBER, RANK, DENSE_RANK
- 2nd / Nth highest salary, duplicates, dept-wise max
- 10 LeetCode problems
- GFG SQL quiz

### Day 6: Functional Dependency + Closure 🔴
- Insert / update / delete anomalies
- Functional dependency, Armstrong's axioms
- Attribute closure
- Candidate key nikalna
- 15 numericals

### Day 7: Normal Forms 🔴
- 1NF, 2NF (partial dependency), 3NF (transitive), BCNF
- Lossless join, dependency preservation
- 4NF / 5NF (definition level), denormalization
- 15 numericals + MCQs
- **Trap:** Har BCNF relation 3NF hota hai, lekin ulta nahi.

### Day 8: Transactions + ACID + Schedules 🔴🟠
- Transaction states
- ACID (har property ka example)
- Dirty read, non-repeatable read, phantom read, lost update
- Isolation levels
- Serial / serializable / recoverable / cascadeless / strict schedules
- Conflict serializability (precedence graph)
- 10-15 precedence graphs
- **Trap:** ACID wali Consistency, CAP wali consistency nahi hai.

### Day 9: Concurrency + Indexing + Extras 🟠
- Shared / exclusive locks, 2PL, strict 2PL
- Deadlock (conditions, prevention, detection), starvation
- Clustered vs non-clustered index, B-tree vs B+ tree
- SQL vs NoSQL
- 30 MCQs

### Day 10: Mock Day 🎯
- 30-MCQ timed test
- 10 SQL problems timed
- Mock technical interview
- Mistake notebook revision

---

## 📁 Contents

| # | Block | Folder |
|---|---|---|
| 1 | Foundations | [01-Foundations](01-Foundations/) |
| 2 | ER Model + Keys | [02-ER-and-Keys](02-ER-and-Keys/) |
| 3 | SQL | [03-SQL](03-SQL/) |
| 4 | Normalization | [04-Normalization](04-Normalization/) |
| 5 | Transactions | [05-Transactions](05-Transactions/) |
| 6 | Indexing + NoSQL | [06-Indexing-and-NoSQL](06-Indexing-and-NoSQL/) |
| 7 | Interview Q&A | [interview-questions](interview-questions/) |
| 8 | MCQ Mistakes | [mcq-practice/mistake-notebook.md](mcq-practice/mistake-notebook.md) |

> Links tab kaam karenge jab aap woh folders bana loge.

---

## 🧪 Where to Practice

| Purpose | Platform |
|---|---|
| SQL coding | LeetCode SQL 50, HackerRank SQL, DataLemur |
| SQL basics | SQLBolt, SQLZoo |
| DBMS MCQs | GFG DBMS quizzes, Sanfoundry |
| Normalization / serializability numericals | GATE previous year questions |
| Theory interview Q&A | InterviewBit DBMS |

---

## 🔁 Revision System

1. **Same day:** 10 minute, bina notes dekhe yaad karo.
2. **Next day:** pichhle din ke 10 MCQs dobara.
3. **Day 3 aur Day 7:** mistake notebook se revision.
4. **Day 10:** timed mock.

---

## 📚 References

- [GeeksforGeeks DBMS](https://www.geeksforgeeks.org/dbms/dbms/)
- [GeeksforGeeks SQL](https://www.geeksforgeeks.org/sql/sql-tutorial/)
- [LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/)

---

<div align="center">

⭐ **Consistency > Intensity** · Roz commit karo, roz seekho ⭐

</div>
