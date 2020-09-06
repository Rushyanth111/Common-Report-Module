# Report API

The Report API is the backbone of the Report Structure, there are various reports here.

- SubjectReport
- StudentReport
- DepartmentReport
- ScoreReport

Each of the Following Members have their own `create` methods with their own requirements.

They are Static methods that create an object that you need to store and send to the server when requesting something, most methods use only a string or an integer but some methods (Bulk Methods, Put and POST) require that you send an Object.

# Example of the `create` method

```py
#Create the object and Store it in Obj
obj = SubjectReport.create(code="17CS68", name="Some Random Subject")

# Add it to some List so that it doens't get lost
some_list.append(obj)
```

That's it!
