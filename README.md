# django-thresher
data warehouse denormalization tooling for Django

This project is experimental software. In fact, it does not yet work at all.

## Features

* Track additions to a primary model. Update historical BI record with new additions as
they are inserted into the primary model.
* Specify associated data to denormalize into a single record.
* Specify associated data which should be updated rather than kept static if it
is changed.

## Todo List

* Register signals on secondary models (tracked changes, like first_name)
* Consider how you would implement this using database triggers (ORM for triggers?)

