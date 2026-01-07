# Threading

## 1️⃣ What a thread is (absolute basics)

You must clearly know:

* A thread is a **lightweight unit of execution**
* Threads **share the same memory**
* Context switching happens automatically

🧠 Memorize:

> Threads share memory, processes don’t.

---

## 2️⃣ Thread lifecycle (very important)

States to know:

* **New**
* **Runnable**
* **Running**
* **Blocked / Waiting**
* **Terminated**

In Python:

* `start()` → thread begins
* `join()` → wait for thread to finish

```python
t.start()
t.join()
```

---

## 3️⃣ The GIL (Python-specific, critical)

You must understand:

* Only **one thread executes Python bytecode** at a time
* Threads ≠ parallel CPU execution in CPython
* Threads are still useful for **I/O**

🧠 Rule:

> Python threads are for waiting, not computing.

---

## 4️⃣ Race conditions 🔥 (non-negotiable)

You MUST understand:

* What a race condition is
* Why shared data breaks
* Why bugs are unpredictable

Example concept:

```text
Read → Modify → Write
```

If two threads do this → ❌ chaos

---

## 5️⃣ Locks (mutex)

Core idea:

* Only **one thread at a time** can enter critical section

```python
lock = threading.Lock()

with lock:
    # safe code
```

Know:

* What a **critical section** is
* Why locking too much is bad (slow)

---

## 6️⃣ Deadlocks ⚠️

You MUST recognize this pattern:

```text
Thread A holds Lock 1 → wants Lock 2
Thread B holds Lock 2 → wants Lock 1
```

Result: ❌ frozen program

How to prevent:

* Always acquire locks in the same order
* Minimize lock usage

---

## 7️⃣ Starvation & livelock

Understand:

* **Starvation** → a thread never gets CPU or lock
* **Livelock** → threads run but make no progress

These are subtle but real.

---

## 8️⃣ Thread-safe data structures

Know what’s safe:

* `queue.Queue` ✅
* `collections.deque` (with care)
* `list`, `dict` ❌ (not thread-safe for writes)

Example:

```python
from queue import Queue

q = Queue()
q.put(1)
q.get()
```

🧠 Rule:

> Prefer thread-safe structures over manual locks.

---

## 9️⃣ Condition variables (coordination)

Used when:

* Threads must **wait for a condition**

Example use case:

* Producer–consumer

Concepts:

* `Condition`
* `wait()`
* `notify()`

---

## 🔟 Thread pools (real-world usage)

You should know:

* Why thread pools exist
* How to limit thread count

Python way:

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as ex:
    ex.map(task, data)
```

🧠 This is preferred over manual thread creation.

---

## 1️⃣1️⃣ Daemon threads

Know:

* Daemon threads die when main thread exits
* Used for background tasks

```python
t.daemon = True
```

---

## 1️⃣2️⃣ Common multithreading mistakes

You should be able to explain:

* Forgetting `join()`
* Overusing locks
* Locking too much code
* Using threads for CPU-bound work
* Assuming execution order

---

## 1️⃣3️⃣ When NOT to use multithreading

Understand alternatives:

* CPU-bound → `multiprocessing`
* High-scale I/O → `asyncio`

---

## 🧠 Final “by heart” summary

If you can explain these **without notes**, you know multithreading:

1. Threads share memory
2. GIL limits CPU parallelism
3. Race conditions exist
4. Locks protect critical sections
5. Deadlocks can freeze programs
6. Thread pools are best practice