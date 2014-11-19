
.. Deployment slides file, created by
   hieroglyph-quickstart on Tue Nov 11 16:49:45 2014.


.. slide::

  .. figure:: /_static/wordcloud.svg
    :class: fill

    Deployment


whoami
======
* Paul Collins
* full stack web dev
* Using Python since 2002 (those good ole college days)
* highly opinionated since birth
* usually wrong since about the same time.


Quick notes
===========
* Good spirited snarking at me is OKAY!
* Random questions at the end please
* Burning oh God I can't help myself questions whenever. I reserve the right to
  "come back to those" though.

Deployment
==========
The art of taking it from "It works on my computer!" to "Oh look a website!"
and if you do it right to "Oh hai! Reddit came by and our servers didn't die"

.. rst-class:: centered-things

.. slide:: You can be a badass like this guy

  .. figure:: /_static/deploy.gif
    :class: center-img

    http://devopsreactions.tumblr.com/

  .. note::
    It doesn't have to be super complicated, but you do get to look like a badass
    when you're done


How do people deploy
====================
* Worst case: by hand
* Fabric or as I like to call it bash scripts for Python
* janky scripts running on Jenkins server somewhere
* other janky scripts in puppet / chef / bash that do "MAGIC!" and "Oh look it
  worked!"

.. note::
  What I typically see in small to medium size companies is "Deployment is hard
  and we have to move fast" that forces the devs to have to do it. This WORKS
  for a while, but eventually you lose that one guy who know about the one
  script that flipped the magic bit in the environment that turned on the
  server in US-East-1 which connected to the DB and wait what were we talking
  about again?
  Deploying you code should be as automated as possible. A developer should just
  run the tests, and then have something that can be deployed.


.. rst-class:: centered-things

If you do this you will fail. Eventually
========================================

.. figure:: /_static/failure.gif

  http://devopsreactions.tumblr.com/post/98456803030/last-commit-on-friday-5pm


.. rst-class:: centered-things

Millions of "How To!"
=====================

.. figure:: /_static/standards.png

  http://xkcd.com/927/


Let me add mine
===============
* Deploy via native packages, inspired by
  https://hynek.me/articles/python-app-deployment-with-native-packages/

  published in *2012* but we're still talking about it today

* Code --> Vagrant --> Ansible --> FPM --> .deb --> S3 bucket
* Run on
* CloudFormation + autoscaling + custom AMI --> shellscript --> Ansible --> DEPLOYED!

.. note::
  Yes that's a bit of handwaving at the end there so let's break this down a bit
  That first line gets you to the point where managing things is easy in
  deployment because your debian package handles nasty things like "I need
  package X installed for my package to run." That second line is getting that
  package out in the "real world" where it's running on your server. Ansible
  simply has to say "Install this latest package from this location" and you're
  basically done. The rest is just configuration which all CM's are built for.


Why a native package when I can...
==================================
* Use my magic bash script...
* Just ask my Operations guy to do it
* Run my server in a screen / tmux session
* ``manage.py runserver`` IS deployment!

.. note::
  Every single one of those answers will have your operations guy want to
  murder you in your sleep. Since those guys tend to have access to all the
  db's in the company, they probably know where you live. Think about that one.

So what are we talking about specifically
=========================================
* Python 3.4 / Django 1.7 on Amazon served up by gunicorn
* Focusing on the "Build me a .deb" portion from before

  * I can talk a bit about the amazon portion too if we have time

.. note::
  everyone has a different deployment environment, there simply are too many
  variables to account for. heroku or amazon (trick question bwahaha). ruby or
  python? gunicorn or uwsgi? Additionally everyone has different security
  requirements. Can everything run on the same server or do you have to have
  real seperation between those services? Do you have enough traffic where load
  balancing suddenly becomes a real concern? Etc. For now let's just go with this.


Pick a configuration management thing
=====================================
* Puppet
* Chef
* Salt
* Ansible

Then use it EVERYWHERE

.. note::
  any of those work and there are pluses and minus to all of them. at this
  point I personally prefer ansible because it's fairly easy to write plugins
  for. Be warned, every one of those tools has some repository out there
  where the internet can give you modules. Those modules are generally
  variations of something horrible or something that doesn't fit with your
  infastruture / needs and often written by someone who's just now learning
  how to work with whatever tool you've chosen. Puppet Forge, Kitchen, Ansible
  Galaxy being examples of this.


Choose your VM
==============
* Docker or Vagrant really...
* VMWare if you have $$$ to burn

.. note::
  Docker is the new kid on the block, but if you're trying to build your code on
  anything other than a native linux machine, just use vagrant directly.
  There's some code syncing issues with Boot2Docker in OSX, and seriously just
  good luck on Windows. Vagrant at least you can get a VM up and running once
  you've got VirtualBox going which is pretty easy to do at this point. Oh you can
  do this on VMWare too, but then you're shelling out some cash to do it.


Other "local" tools
===================
* FPM to build a package
  https://github.com/jordansissel/fpm

  * It's Ruby, and it works well.

* virtualenv, pip and friends
* some significant scripting

.. note::
  By local I mean local inside the the virtual machine. You can have a good
  chunk of these tools on your actual machine you're doing development on of
  course, but some of these are really going to be specific to building you a
  package


And at this point
=================
You're probably wondering "Why should I go through the effort?"

.. figure:: /_static/rube_goldberg.gif

  http://philosulfur.tumblr.com/post/24339784017

.. note::
  Honestly it's a good question because there's a LOT of setup involved in
  this. For a small company or as a single open source project just starting
  out this is a lot of bind and grind work, which distracts from solving the
  fun problems. All this tooling just to build a package. The package solves
  some difficult deployment concerns though. What happens when you install a
  new python library, and then suddnely realize that your code doesn't actually
  work with it? How hard is rollback for you? How long does it take? Across how
  many servers? Are you certain that you took care of all the compiled files as
  well? Why not just let someone else solve those problems for you because
  Debian and Redhat did that a long time ago. We just need to build a package
  ourselves in a fire and forget kind of way. Otherwise we're back at the
  problem where we have the one brilliant employee who knew all the things
  about all the scripts with all the power. That person got bored one day and
  left for greener pastures (e.g. Google) and dumped their collection of hacks
  in YOUR lap to "deal with"


So back to our "solution"
=========================
* Code leads to bugs
* Bugs lead to anger
* Anger leads to .... <gasp> downtime


So back to our "solution"
=========================
* Starting at The Code

  * Use a ``setup.py``
  * Using node? Make a ``package.json``
  * Using bower? Make a ``bower.json``
  * If you've got those you probably want Gulp.js or Grunt too

.. note::
  That setup.py thing is kinda important. I see lots of new devs try to tack
  shortcuts and just do thing globally. Once they try to tell their coworker
  what they did, a step is missed and now everyone has to go on a spirit quest
  to find the one library said new dev used. If you use a setup.py from the
  beginning, you elminate this pain.

  * Show the datanav setup.py
  * Point out pinned dependencies

    * not maintaining an open source thing then pinning versions hard in a setup.py is OKAY!


Virtually Consistent
====================
* Add Vagrant to the mix
* Pick a base image close to your AMI

  * At least the same os version and platform

.. note::
  If you have to deal with deploying to multiple architectures
  then this still works, it just gets a bit harder because you
  have to worry about more things during your setup.

  * Show the vagrant file and describe the sections


Bashing scripts for great justice
=================================
The initial ``bootstrap.sh`` gets us going from a fresh install

.. note::
  * Show the bootstrap.sh file


A now the crazy bits
====================
Ansible, requires a bit of reading. All configuration management engines do.
Take the time to read the docs. Then do it again.

Let's do the quickstart version of this for now.

* Localhost only eliminates a lot of complexity at this stage

.. note::
  Ansible is yaml with some special syntax for looping. It allows for
  variables, and it uses Jinja2 syntax (looks a lot like a django template) but
  it doesn't let you use jinja for building loops. Just variable filters which
  also look a LOT like django's variable filters.


Module Structure
================
Best practices are called that for a reason that might not be apparent at first.

http://docs.ansible.com/playbooks_best_practices.html

.. note::
  * Describe the directory structure on that page then code dive
  * Start at the site.yaml
  * Work through the datanav build

A Shiny deb Appears
===================

.. rst-class:: build

* What's next?
* Sign the package
* Upload the package
* Maybe deploy the package
* Test it to make sure it really works

.. rst-class:: centered-things

That sounds like a lot of work
==============================

.. figure:: /_static/lotta_work.gif

  http://devopsreactions.tumblr.com/post/95899896591/boss-comes-back-2-days-earlier


Jenkins to the rescue
=====================
* Automated build system originally built for Java projects
* Can be used to do any kind of "build"
* Kinda like cron, but with a java web interface

.. figure:: /_static/jenkins.png
  :class: pull-left

.. figure:: /_static/chuck.jpg
  :class: pull-right

.. note::
  So Jenkins handles some of the remaining hand waving bits for us with setting
  up a deployment thing. You script up how to sign a package and get that to
  S3, you slam that into Jenkins and then fire away. Jenkins has plugins to
  handle doing build on pull requests from github, and you can have it check a
  repo on a schedule to try to do a build. If you're going for CI then have it
  run your tests on every pull request. If you're going for CD, then have it do
  your deployment after every merge to master. Just make sure you don't merge
  something bad!


Home sweet repository
=====================
* ``reprepro`` commands, see a handy tutorial
  https://www.digitalocean.com/community/tutorials/how-to-use-reprepro-for-a-secure-package-repository-on-ubuntu-14-04
* Host your repo on S3 easily
* LOCK YOUR PERMISSIONS DOWN CAREFULLY IN S3

  * Unless you want the world to have access to install your code on their machine? Maybe that's okay...

.. note::
  Once you've got that deb built, then you run a few more scripts to sign it
  and then upload those results to S3. There's a bit of trickery going on here,
  because the reprepro command builds a debian repository, so you'll have to do
  some fancy syncing. You could also host the files on another small machine in
  amazon and lock permissions down in there. Either works, S3 is just a bit
  cheaper and more durable then EC2 & EBS.


Separate Dev / Stage / Prod
===========================
Easy: Different S3 buckets

Smarter: Different S3 buckets AND different signing keys

.. note::
  Because you should only install packages into production that have been
  tested. Testing in dev can be fully automated, if that infastrucutre burns
  down around your ears WHO CARES! Terminate the instance and let it
  reprovision. If PROD burns down though...

  Basically protect yourself, from yourself. If you have to take a few extra
  steps to release something, that's probably a good thing. Unless you really
  really trust your tests. In which case, can I see your code because that
  sound freaking amazing. I don't trust my tests that much.



TEST YOUR STUFF ON DEV
======================

.. rst-class:: build

* "Doing it live" these are not words to live by.
* Bad things will happen to your systems
* probably not the first time
* or the second


.. rst-class:: centered-things

But one day your deployment will do this
========================================

.. figure:: /_static/bad_deployment.gif

  http://media.tumblr.com/8be7468534d182692141c44fdcc708ca/tumblr_inline_mw67p0IfnW1raprkq.gif

.. note::
  And you will be very sad if you "did it live."


Hitting the deploy button
=========================
* Shouldn't be scary
* A Developer should know what's going to happen

  * or at least be able to figure out what's going to happen

* A Operations person shouldn't be standing over you with fear in their eyes

Because...


.. rst-class:: centered-things

Launching things should be amazing, not painful
===============================================

.. figure:: /_static/launch.gif

  http://todaysdocument.tumblr.com/post/91947538528/a-saturn-v-rocket-launches-from-kennedy-space


Questions
=========
.. figure:: /_static/paul.jpg
  :class: pull-right

* paul.collins.iii@gmail.com
* paul.collins@brightscope.com
* github: ``paulcollinsiii``
* twitter: ``paul_collins``

Thanks!

