# Semester Stats Report

A Python Module Designed to be of use to any person who wishes to interact with the Semester-Stats API.

Please Check the [Documentation](https://rushyanth111.github.io/Semester-Stats-Report/) on How to use it.

## Requirements:

- `Python` > `3.7.0`

# Installation:

Install it via the Tarball from the main Master Branch.

```zsh
pip install https://github.com/Rushyanth111/Semester-Stats-Report/tarball/master
```

# How to Use:

Import the Client into your Application.

```py
from semester_stats_report import SemesterClient

# To Get A Particular Report Mechanism.
from semester_stats_report import StudentReport
```

Creating A Report:

```py
from semester_stats_report import StudentReport

#Creating the report is Simple

new_report = StudentReport.create("1CR14CS001", "Some Name")
```

The Above can be done for many of the Other reports too, Use the `.create()` method.

## Using the SemesterClient:

The Rest Client is Aware of the various Path that the Main application can take. As Such, the Path Is Encoded Purely inside the SemesterClient, without requiring any additional Information from the user.

The API Endpoints are reflections of the Actual Endpoints from the api itself. It just requires the Base URL of the API to Communicate with it.

## Using the Helpers:

Should you need, when Constructing the Dataset, there is a dire requirement of keeping out duplicates, using the set when when where is required. The Helper class can be very useful in dealing with large datasets.

## Examples

```py
# Examples Here.
```
