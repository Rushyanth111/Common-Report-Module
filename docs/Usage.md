# Usage

The Usage of the Client is Very Simple.

We First Initialize a Client.

I'll be using Localhost for this particular One, but you are free to use any other link.

```py
from semester_stats_report import SemesterClient

cl = SemesterClient("http://localhost:9000")
```

Collect the Data you need/Create the Data you need.

Then Utilize the Methods from the SemesterClient, using the reports if needed.

Say, for example, sending obtaining the students of a batch:

```py

result = cl.batch(2017).get()

print(result)
# Some Result will be printed.
```
