
.. FactoryBoy slides file, created by
   hieroglyph-quickstart on Tue Jul 22 21:21:54 2014.


.. slide::

  .. figure:: /_static/tesla.jpg
    :class: fill

    https://www.flickr.com/photos/pestoverde/8763129679/


FactoryBoy: What is it
======================

Django testing tool to build models for you.

Similar tools:

* Model Mommy
* Creating models by hand (God help you)
* fixtures (don't. Seriously just don't)


Meh?
====

If you have ever tested models that depend on models, which themselves depend
on other models (think ``null=False`` on ``ForeignKey`` fields two or three
levels deep), you've run into this.

Because you're writing tests, right?


Code Crawl
==========

.. figure:: /_static/compiling.png

  http://xkcd.com/303/


Why is this better than...
==========================
Model mommy?

It isn't, that one just comes down to the tool you get use to first.


.. nextslide::

Doing it by hand?

Because if we change our schema we have might have to touch a LOT of test code.

E.g. How would I update my tests if I made the name unique


.. nextslide::

Fixtures?

Because editing json by hand to account for schema changes... down that path
lies madness


Things I do
===========

* Name your Factories ``ModelNameFactory``

  * Makes it a lot easier to see what's happening in your tests if you've got a
    lot of models
  * Fancy magic testing... which is of debatable value

.. nextslide::

* Put all your factories for an app in a factories module.

  * In the worst case a factories package.
  * Whatever you do, don't name it factory (name clash)

* Make a setup.py for your project.
* Use a virutalenv


Things I didn't do in here
==========================

* Use cookiecutter, but you should!

  * It's super opinionated so if you disagree with some of it just fork it to
    your own cookiecutter settings. It's actually pretty easy to do.


Tools Used
==========



* ``Django`` https://github.com/django/django
* ``factory_boy`` https://github.com/rbarrois/factory_boy
* ``pytest-django`` https://github.com/pelme/pytest_django note: there are
  several forks of this project. This is the currently maintained one.


.. slide::

  .. figure:: /_static/canhaz.jpeg
    :class: fill

    http://cheezburger.com/4803862528

