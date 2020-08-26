# python-dogs-fact

A Python module to retrieve facts from a CSV data set.

This module responds with a sorted fact about dogs, with data learned from 
[Purina](
https://www.purina.co.uk/dogs/behaviour-and-training/understanding-dog-behaviours/amazing-dog-facts), 
[Drake Center Vet](
https://www.thedrakecenter.com/services/dogs/blog/23-amazing-facts-about-dogs-you-probably-didnt-know), 
[Pet Assure](https://www.petassure.com/new-newsletters/50-fascinating-facts-about-dogs/) and 
[Petfinder](https://www.petfinder.com/dogs/bringing-a-dog-home/facts-about-new-dog/).


&nbsp;  
&nbsp;  
## Retrive from command line

    $ python -m dogs_fact | python -m json.tool


## From Python interpreter

    $ python
    >>>
    import dogs_fact
    dogs_fact.get_fact()


## Automatic tests
Python tests are available using unittest manually or via Makefile.  

- Run ` python3 -m unittest tests/test_* `.
- Or use make as in ` make test ` to setup, run the tests and clean up.


## Run Docker compose
_If not installed, please [Install Docker Compose](https://docs.docker.com/compose/install/)._

There are Makefile rules to simplify this option. See the list of commands:

- ` $ make ` to build and run (up) the application.
    - or run `$ make compose && make run ` _(note: run calls compose)_.
- ` $ make stop ` and ` make start ` to restart the container.

We should be now able to browse: http://localhost:5000/  

_Note: the default 5000 http port can be changed in [.env](.env) or running:_

    $ HTTP_PORT=8080 make


## Clean up
After running command line, using interpreter or running tests, execute:

    $ make clean

To remove container and built image, run:

    $ make rm

_(note: make rm also calls make clean)_


## Documentation
Please try from python console:

    $ python3
    >>> import proxy
    >>> help(proxy)

Or try from command line:

    $ python3 -c "import proxy; help(proxy.config)"

All documentation can be found in [docs](docs).


## To do

* Automatic rotation of log files.
* Improve docstring.

