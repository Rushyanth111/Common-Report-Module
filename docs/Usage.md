# Usage

The Usage of the Client is Very Simple.

We First Initialize a Client.

I'll be using Localhost for this particular One, but you are free to use any other link,
as long as the server is present at that location, else, will get undefined behaviour.

## Initializing the Client

Firstly Import the `SemesterClient` from the package.

This Client Holds Everything you need for Interacting with the remote API.

```python hl_lines="1"
from semester_stats_report import SemesterClient

cl = SemesterClient("http://localhost:9000")
```

Then initialize the client by passing it a link to the server, remember, there should be no `/` (Trailing slash).

```python hl_lines="3"
from semester_stats_report import SemesterClient

cl = SemesterClient("http://localhost:9000")
```

## Fetching From the Client

The `cl` object then becomes the method in which we fetch the data from the endpoint.

The Client is a rest endpoint that constructs the link as we go.

```py

result = cl.batch(2017).get()

print(result)
# Some Result will be printed.
```

Check out the Various Clients to get an Idea on how to chain them.
