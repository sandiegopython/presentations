Python Tricks
=============

Files
-----

* `talk.ipynb <talk.ipynb>`_: IPython notebook for the talk
* `talk.rst <talk.rst>`_: reStructuredText for the talk

Giving the talk
---------------

Before giving the talk the requirements need to be installed:

.. code-block:: bash

    $ pip install -r requirements.txt

How to run the ipython notebook for this talk:

.. code-block:: bash

    $ ipython notebook talk.ipynb

How to create a reStructuredText file from the ipython notebook:

.. code-block:: bash

    $ ipython nbconvert --to rst talk.ipynb
