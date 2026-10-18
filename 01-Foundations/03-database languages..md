# Database Languages

## Definition
Database languages woh special languages hain jinse database mein data ko **define, manipulate aur control** kiya jaata hai. Inse hum tables banate hain, data insert/update/read karte hain, permissions dete hain aur transactions manage karte hain.

**Simple example:** Ek school ke kaam alag-alag hote hain: building banana (DDL), students ka record bharna (DML), record padhna (DQL), kisko kaunsa room kholne ki permission hai (DCL), aur din ke end mein sab save karna (TCL).

```
         SQL / Database Languages
 ┌────────┬────────┬────────┬────────┬────────┐
 │  DDL   │  DML   │  DQL   │  DCL   │  TCL   │
 │Structure│ Data  │ Padhna │Permission│Transaction│
 └────────┴────────┴────────┴────────┴────────┘
```

---

## 1. DDL (Data Definition Language)
- **Kaam:** Database ka **structure** (schema, tables, indexes) define karna.
- **Auto-commit:** Changes turant permanent ho jaate hain (jaise MySQL aur Oracle mein).

| Command | Kaam |
|---|---|
| **CREATE** | Naya object banana (table, view, index, schema) |
| **ALTER** | Existing structure badalna (column add/drop) |
| **DROP** | Object ko permanently delete karna |
| **TRUNCATE** | Table ki saari rows hataana, structure rehta hai |
| **RENAME** | Object ka naam badalna |
| **COMMENT** | Data dictionary mein comment jodna |

```sql
CREATE TABLE Student (id INT PRIMARY KEY, name VARCHAR(50));
ALTER TABLE Student ADD phone VARCHAR(15);
TRUNCATE TABLE Student;
DROP TABLE Student;
```

---

## 2. DML (Data Manipulation Language)
- **Kaam:** Table ke andar ka **data** badalna.
- **Rollback:** `COMMIT` hone se pehle undo ho sakta hai.

| Command | Kaam |
|---|---|
| **INSERT** | Nayi row add karna |
| **UPDATE** | Existing row badalna |
| **DELETE** | Row hataana (`WHERE` se selected rows) |
| **MERGE** | Hai toh update, nahi hai toh insert (**UPSERT**) |
| **CALL** | PL/SQL ya Java subprogram call karna |
| **EXPLAIN PLAN** | Query kaise chalegi (data access path) |
| **LOCK TABLE** | Concurrency control |

```sql
INSERT INTO Student VALUES (1, 'Rahul', '9876543210');
UPDATE Student SET phone = '9999999999' WHERE id = 1;
DELETE FROM Student WHERE id = 1;
```

**DML ke 2 types:**

| Type | Matlab |
|---|---|
| **Procedural** | Batata hai **kya** chahiye aur **kaise** nikalna hai |
| **Non-procedural (Declarative)** | Sirf batata hai **kya** chahiye, kaise nahi (SQL aisi hi hai) |

---

## 3. DQL (Data Query Language)
- **Kaam:** Data **padhna**, bina badle.
- **Main command:** `SELECT`. Iske saath `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` use hote hain (yeh actually **clauses** hain).

```sql
SELECT dept, COUNT(*)
FROM Student
WHERE marks > 50
GROUP BY dept
HAVING COUNT(*) > 5
ORDER BY dept;
```

> Kuch books `SELECT` ko **DML ka part** maanti hain, aur kuch alag **DQL** ki tarah. MCQ mein options dekhke decide karo.

---

## 4. DCL (Data Control Language)
- **Kaam:** **Permissions** control karna (security).

| Command | Kaam |
|---|---|
| **GRANT** | Permission dena |
| **REVOKE** | Di hui permission wapas lena |

```sql
GRANT SELECT, INSERT ON Student TO intern_user;
REVOKE INSERT ON Student FROM intern_user;
```

---

## 5. TCL (Transaction Control Language)
- **Kaam:** **Transactions** manage karna taaki ACID properties bani rahein.

| Command | Kaam |
|---|---|
| **COMMIT** | Changes permanently save |
| **ROLLBACK** | Changes undo (last COMMIT ya SAVEPOINT tak) |
| **SAVEPOINT** | Transaction ke beech ek point, jahan tak partial rollback ho sake |
| **SET TRANSACTION** | Transaction ki properties set karna |

```sql
START TRANSACTION;
UPDATE Account SET balance = balance - 500 WHERE id = 1;
SAVEPOINT sp1;
UPDATE Account SET balance = balance + 500 WHERE id = 2;
ROLLBACK TO sp1;   -- sirf doosra update undo
COMMIT;
```

---

## Quick comparison

| Language | Kaam | Commands |
|---|---|---|
| DDL | Structure | CREATE, ALTER, DROP, TRUNCATE, RENAME |
| DML | Data change | INSERT, UPDATE, DELETE, MERGE |
| DQL | Data padhna | SELECT |
| DCL | Permissions | GRANT, REVOKE |
| TCL | Transactions | COMMIT, ROLLBACK, SAVEPOINT |

## DELETE vs TRUNCATE vs DROP (bahut important)

| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Type | DML | DDL | DDL |
| Kya hataata hai | Selected/saari rows | Saari rows | Poora table (structure bhi) |
| `WHERE` | ✅ | ❌ | ❌ |
| Structure rehta hai? | ✅ | ✅ | ❌ |
| Speed | Slower | Faster | Fast |

---

## Applications of DBMS
1. Banking 🏦

Example: SBI ya HDFC ka app.
Kya store hota hai: Aapka account number, balance, transactions.
DBMS kya karta hai: Aapne ₹500 bheje toh aapke account se kam hote hain aur doosre ke account mein jaate hain. Dono saath hone chahiye, warna paisa gayab ho jaayega.

2. E-commerce 🛒

Example: Amazon ya Flipkart.
Kya store hota hai: Products, price, stock, aapke orders, address.
DBMS kya karta hai: Aapne order kiya toh stock kam hota hai, aur order history mein dikhta hai. Do log ek saath last piece kharidein toh sirf ek ko milta hai.

3. Healthcare 🏥

Example: Hospital ka record system.
Kya store hota hai: Patient ka naam, bimari, dawaiyan, reports.
DBMS kya karta hai: Doctor kisi bhi branch se patient ki purani history dekh sakta hai. Sirf authorized log hi dekh sakte hain (security).

4. Education 🎓

Example: College ka portal.
Kya store hota hai: Students ka naam, attendance, marks, timetable.
DBMS kya karta hai: Result aate hi saare students apne marks dekh lete hain. Sab ka data ek jagah hai.

5. Social Media 📱

Example: Instagram ya WhatsApp.
Kya store hota hai: Profile, posts, likes, followers, messages.
DBMS kya karta hai: Aapne post daali toh followers ko dikhti hai. Karodon users ka data saath mein chalta hai.

6. Data Science 📊

Example: Netflix ka “aapko yeh pasand aayega” wala feature.
Kya store hota hai: Aapne kya dekha, kitni der dekha.
DBMS kya karta hai: Bahut bada data ek jagah rakhta hai, jisse analysis karke predictions bante hain.

---

## Yaad rakhne wali baatein 🚨
1. **TRUNCATE DDL hai, DML nahi**, jabki yeh rows delete karta hai.
2. **DELETE** mein `WHERE` laga sakte ho (selected rows). GFG ki line "delete all records" adhoori hai.
3. **DDL auto-commit** hota hai (MySQL, Oracle). Lekin yeh **har DB mein nahi**: SQL Server aur PostgreSQL mein DDL ko transaction ke andar rollback bhi kar sakte ho. Exam mein jo book/GFG kehta hai wahi likho, interview mein "DB par depend karta hai" bolo.
4. **DML ko `COMMIT` se pehle rollback** kar sakte ho.
5. `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY` **commands nahi, clauses** hain.
6. `MERGE`, `CALL`, `EXPLAIN PLAN`, `LOCK TABLE` ki classification (DML) Oracle-style hai, books mein thodi alag ho sakti hai.

---

## Quick quiz

**Q1.** `TRUNCATE` kaunsi language ka command hai? (a) DML (b) DDL (c) DCL (d) TCL

**Q2.** Table ki sirf kuch rows hataani hain (jaise `id = 5`). Kaunsa command use karoge, aur kyun?

**Q3.** `GRANT` aur `REVOKE` kaunsi category mein aate hain?

**Q4.** Kaunsa command rollback ke saath partial undo ke liye use hota hai?
(a) COMMIT (b) SAVEPOINT (c) GRANT (d) MERGE
