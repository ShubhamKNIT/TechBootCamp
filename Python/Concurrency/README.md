# Concurrency

## 0️⃣ First: What “concurrency” really means (memorize this)

**Concurrency** = doing *multiple tasks that overlap in time*
**Parallelism** = doing *multiple tasks at the exact same time*

In Python:

* Concurrency ≠ faster CPU code
* Concurrency = **waiting smarter** (I/O, network, timers)

---

## 1️⃣ Mental model you MUST learn by heart

Think of tasks as **people** and CPU as **one desk**:

* **Sequential**: one person talks, everyone else waits
* **Concurrency**: people take turns while others are waiting
* **Parallel**: multiple desks (CPUs)

Python mostly does **concurrency**, not true CPU parallelism (because of the GIL).

---

## 2️⃣ The 4 concurrency tools in Python (memorize order)

Learn them **in this exact order**:

1. `threading` → shared memory, simple
2. `multiprocessing` → true parallelism
3. `asyncio` → modern, scalable, fastest for I/O
4. `concurrent.futures` → clean abstraction

If you skip this order, it gets confusing.

---

## 3️⃣ Step 1: Threads (`threading`)

### When to use

* I/O tasks (sleep, downloads, waiting)
* NOT heavy math

### Core ideas to memorize

* Threads share memory
* Race conditions are real
* Use locks when modifying shared data

### Minimal example

```python
import threading
import time

def worker(name):
    for i in range(3):
        print(name, i)
        time.sleep(1)

t1 = threading.Thread(target=worker, args=("A",))
t2 = threading.Thread(target=worker, args=("B",))

t1.start()
t2.start()

t1.join()
t2.join()
```

🧠 **Burn into memory**:

* `start()` → begins execution
* `join()` → wait for completion

---

## 4️⃣ Step 2: Race conditions (VERY IMPORTANT)

```python
counter = 0

def add():
    global counter
    for _ in range(100000):
        counter += 1
```

Run this with multiple threads → ❌ wrong result

### Fix with a Lock

```python
lock = threading.Lock()

def add():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1
```

🧠 **Rule**:

> If multiple threads **write**, you need a lock.

---

## 5️⃣ Step 3: Multiprocessing (real parallelism)

### When to use

* CPU-heavy tasks
* Math, image processing, simulations

### Key difference

* Each process has its **own memory**
* No shared variables by default

```python
from multiprocessing import Process

def work():
    print("Working")

p1 = Process(target=work)
p2 = Process(target=work)

p1.start()
p2.start()

p1.join()
p2.join()
```

🧠 Memorize:

* Threads → shared memory
* Processes → separate memory

---

## 6️⃣ Step 4: Async / Await (`asyncio`) 🔥

This is the **most important modern skill**.

### Mental model

* One thread
* Thousands of tasks
* Tasks **pause themselves** when waiting

### Minimal async example

```python
import asyncio

async def task(name):
    for i in range(3):
        print(name, i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )

asyncio.run(main())
```

🧠 Burn this pattern into your head:

* `async def`
* `await`
* `asyncio.run(main())`

---

## 7️⃣ Choosing the right tool (memorize table)

| Problem                | Use                  |
| ---------------------- | -------------------- |
| Waiting on network     | `asyncio`            |
| Simple background task | `threading`          |
| Heavy CPU work         | `multiprocessing`    |
| Clean API              | `concurrent.futures` |

---

## 8️⃣ Daily practice plan (2 weeks)

### Week 1

* Day 1–2: threading basics
* Day 3: race conditions + locks
* Day 4–5: multiprocessing
* Day 6: compare threads vs processes
* Day 7: review + rewrite examples from memory

### Week 2

* Day 8–9: async/await basics
* Day 10: asyncio.gather
* Day 11: async vs threads
* Day 12–13: build small project
* Day 14: explain concurrency **out loud**

If you can **explain it**, you own it.

---

## 9️⃣ Mini projects (do at least one)

* Download multiple URLs concurrently
* Timer app with multiple countdowns
* Chat server simulation (async)
* Web scraper (async + aiohttp later)