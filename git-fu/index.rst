
.. Git-Fu slides file, created by
   hieroglyph-quickstart on Tue Aug 26 09:03:18 2014.

.. rst-class:: whitetext

Git-Fu
======

.. figure:: /_static/bruce-lee.jpg
  :class: fill

  http://www.wallconvert.com/wallpapers/male-celebrities/bruce-lee-16283.html


Covering
========

* Commands I tend to use that make my life better
* Some of my workflow in git, and why

  * Quick tips to annoy your release manager / open source repository owner


Quick check
===========

You know these commands and their flags?

* ``git commit`` (-a, -m)
* ``git add`` (-a)
* ``git checkout`` (-b v.s. -B)
* ``git reset`` (--hard v.s. --soft)

.. note::
  * Make sure to ask if people know the flags that I'm listing there. If not go
    over briefly


Slightly sneaky
===============
We'll cover these more later

* ``git commit -v``
* ``git add -p``
* ``git stash`` (maybe with -p)

.. note::
  * -v for showing the diff inside your editor
  * -p for adding via patch. Show a quick demo of this

Even more sneaky
================

* ``git diff stash@{0}`` for iterative refactoring
* ``git diff --ignore-space-change`` because what language uses whitespace...

.. note::
  The idea being you're using sed / awk to do a refactor or maybe PyCharm and
  you want an easy way to see what changes happen between refactors wihle being
  able to rollback. Easiest to think of this as a transaction with sub-transactions.


A GUI suggestion
================

Sourcetree is the one I know

* Windows / Mac
* Slightly annoying license thing (Atlassian)

There are others on Linux as well, but I'm less familiar with them (sorry)


.. rst-class:: absposition

GUIs are the devil
==================

Things I've had GUI's "help" me with

* merging things... like master
* merge conflicts... RESOLVED!
* not really stashing commits
* force pushing

.. figure:: /_static/freebsd-logo.jpg
  :class: daemon

  http://linax.files.wordpress.com/2008/11/freebsd-logo.jpg

.. note::
  * merging always picked mine, or theirs. Poof conflicts resolved!
  * stashing would say it stashed then not actually show up in git, but some
    other magic gui land where stash didn't really mean stash. Eclipse did
    this.
  * Because why just push when you can push like a BOSS



The devil you know
==================

Reading history, especially tangled history is MUCH easier in a GUI.

``git log --graph --pretty --oneline -n ###`` if you really want to though.

.. note::
  Show an example from EnvConfig


Merge Conflicts
===============

* Is it really a conflict?::

    git merge -s recursive -X patience

* No really, is it a conflict::

    git merge --no-commit --ignore-space-change
    git merge --abort

* Maybe you meant to use ``rebase``?

.. note::
  Conflicts generally mean someone beat you to merging your code to master! Now
  you fight to the death.


Rebasing
========
.. code-block:: bash

    git fetch --all
    git branch -b mybranch_redux # If you're paranoid
    git rebase -i [[commit sha you forked from]]
    git rebase origin/master

#. Check your history, find when you started this branch
#. Squish commits down before rebasing off ``origin/master``

  * That might take a few rounds before you're happy

.. note::
  * Always do a fetch before you rebase, otherwise you'll be doing some work over again
  * Squish work down so you have fewer commits to deal with conflicts on
  * show the magic of reflog
  * ``rebase --abort``


F = MA
======

  Force pushing without care can lead to outright destruction of data. It's like
  handling nuclear waste. Handled with care, no big deal. If it leaks, then the
  land is poisoned and lots of people die. Horribly.

  So on that note...


.. slide::

  .. figure:: /_static/homer-plant.jpg

    http://qph.is.quoracdn.net/main-qimg-0f7369e84c038230ac00a60d38ffeb03?convert_to_webp=true


Pushing with force, safely
==========================

* After ``rebase``
* Assuming you're the ONLY person working on the branch
* Check with ``git push -f -n``, the ``-n`` being the important bit

  * Should push to one and ONLY one branch.

.. note::
  * ONLY means you and only you have checked out that branch. If you
    know everyone who is working on it and you're going to force push it then
    you need to sync up with them. In that case just push to a new branch it's
    a LOT safer

Typical story
=============
So my ticket flow goes something like

.. code-block:: bash

    git checkout master
    git pull -r
    git checkout -b DI-TICKET
    # code code, commit, code, WIP commit, code some more
    git push -u origin DI-TICKET
    # check my diff
    # run my tests
    # ... fix my failing tests, commit
    # code some more, commit a few more times

By the end of which I have MANY commits. Lots of them "WIP" (Work In Progress)


Our continuing saga
===================
That collection of "work" then goes through

.. code-block:: bash

    git fetch --all
    git log -n 25  # To find my first commit during code code code
    git rebase -i COMMIT-SHA
    # reword, squish, squish, maybe edit
    # continue until commit logs "make sense"
    git rebase origin/master
    # hope there are no conflicts, then
    git push -fn
    # Assuming that's okay
    git push -f

.. note::
  The idea is that the commit logs should show some kind of logical progression
  of features without a lot of "WIP" and "Fixing derp" or "Gah typos, then I
  moved a bunch of things because it felt cleaner." All of that goes away and
  you have something resembling the final result.


So what happens
===============
http://pcottle.github.io/learnGitBranching/?NODEMO


A note on merging
=================

* Branches merge INTO master. Not the other way around
* Merging master into your branch breaks our ability to ship it out as a hotfix easily
* Merging master into your branch makes the "tree" look more like a tangled mess

.. note::
  Example. I branch master at commit A to branch 1. Because I see green button
  on my PR isn't green I "merge master" into my branch but not master is at
  commit ZZ. An RC was cut at commit G, but my branch is hotfix worthy!
  In order for the release manager to release my feature and only my feature
  that person has to go into my branch and be VERY careful about what's being
  cherry-picked, because otherwise everything from G TO ZZ will be cherry
  picked in due to my "merging master"


When I see...
=============

Merged "master" inside a PR


.. figure:: /_static/table_flip.gif

  http://i.imgur.com/ForPOJQ.gif
