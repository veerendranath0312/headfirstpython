# Learnings form Chapter 04

- The **def** keyword defines a new, bespoke function.

- When you put code in it’s own file (with a .py extension), you create a **module**.

- The **import** statements lets you reuse a module, e.g., `import swimclub`.

- Use a **fully qualified name** to invoke a function from a module, e.g., `swimclub.read_swim_data`.

- The **return** statement allows a bespoke function to return a result.

- If a function tries to return more than one result, the collection of returned values are **bundled together** as a single **tuple**. This is due to the fact that Python functions only ever return a single result.

- A tuple is an **immutable sequence** data structure. Once a tuple is assigned values, the tuple cannot change.

- Lists are like tuples, expect for the fact that lists are **mutable**.

- The `os` module (included as part of the PSL) lets your Python code talk to your underlying operating system.

- *Although lists come with a handy sort method, be careful using it as the ordering is applied in-place. If you want to keep any list’s current order, use the **sorted** BIF instead (which always returns a sorted copy of your data).*

- Lists come built in with lots of methods (not just **sort**), including the useful **remove** method.

- *The **in** operator is one of our favorites, and should be one of yours, too. It’s great at searching (aka checking for membership).*

- When you need to make a decision, nothing beats the **if else** combo.

- An often overlooked, but truly wonderful, BIF is **enumerate**. It can be used to number the iterations of any **for** loop.