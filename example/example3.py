from semester_stats_report import ScoreReport, StudentReport, SubjectReport
from semester_stats_report import SemesterClient
import csv
from typing import Set
import glob
import asyncio

# This is the Main Client, Use it to POST data.
cl = SemesterClient("http://localhost:9000")


# We are keeping Sets to Avoid Duplication.
stu_keep: Set[StudentReport] = set()
sub_keep: Set[SubjectReport] = set()
sco_keep: Set[ScoreReport] = set()


def chunk(lst, n):
    # Helper Function for The Code Below
    # This just Splits up the Below into sublists.
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


# Using An Old Format of the CSV, We Scrub the Data.
# USN, Name, ignore,
# [SubCode, Subname,Internals,Externals,Total,F/P]*AttemptedSubjects
for filename in glob.glob("*.csv"):
    with open(filename) as f:
        _data = csv.reader(f.readlines(), delimiter=",")
        # For Each Row:
        print(filename)
        for x in _data:
            if not any(x):
                continue
            x = x[: len(x) - 2]
            # Create Student
            stu_keep.add(StudentReport(Name=x[1], Usn=x[0]))
            for y in chunk(x[3:], 6):
                # Subject And Score for Each.
                sub_keep.add(
                    SubjectReport(
                        Code=y[0],
                        Name=y[1],
                        MinExt=19,
                        MinTotal=40,
                        MaxTotal=100,
                        Credits=4,
                    )
                )

                sco_keep.add(
                    ScoreReport(
                        Usn=x[0], SubjectCode=y[0], Internals=y[2], Externals=y[3]
                    )
                )

# Data is scrubbed!


# ALWAYS FOLLOW THE ORDER OF STUDENTS OR SUBJECTS FIRST THEN SCORES.
# ALWAYS
# DO NOT IGNORE THE ABOVE. THE METHOD USAGE IS TO CREATE THE MISSING RESOURCES FIRST.
# IGNORING THE ABOVE WILL CAUSE MISSING DATA.
# YOU ARE WARNED.


async def main():
    # Send the StudentReports First
    await cl.bulk().student(list(stu_keep))

    # Send Subject Reports Second.
    await cl.bulk().subject(list(sub_keep))

    # Send the Score Reports AT THE LAST:
    await cl.bulk().scores(list(sco_keep))

    # Yay, Data is Sent and Assimilated.
    # Lets Fetch Some Data.

    stu = await cl.student("1CR17CS001").get()
    print(stu)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)
result = loop.run_until_complete(main())
# Program should run as-is, provided all of the depts are up to date.
