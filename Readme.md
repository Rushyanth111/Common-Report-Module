# Semester Stats Report

A Python Module Designed to be of use to any person who wishes to interact with the Semester-Stats API.

## Requirements:

- `Python` > `3.7.0`

# Installation:

Install it via the Tarball from the main Master Branch.

```zsh
pip install https://github.com/Rushyanth111/Semester-Stats-Report/tarball/master
```

# How to Use:

Import the Library in your application.

```py
import semester_stats_report as ssr
```

## Building a Report:

There are some majour Structures that are present within the package, Utilize them with the help of the HTTP Client to Interact with the API in a feesible Manner.

Like so:

```py
ssr.DepartmentReport(Code="15CSL66", Name="Something")
```

## Using the RestClient:

The Rest Client is Aware of the various Path that the Main application can take, Do not Attempt to Manually Make that path, it is intricate to build on the path that easily.

## Using the Helpers:

Should you need, when Constructing the Dataset, there is a dire requirement of keeping out duplicates, using the set when when where is required. The Helper class can be very useful in dealing with large datasets.

## Examples

```py
# Examples Here.
```
