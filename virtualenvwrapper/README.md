note: Since the talk I've modified some details and added
the Getting Started section

#virtualenvwrapper

##virtualenv
<http://www.virtualenv.org/en/latest/virtualenv.html>  
virtualenv is a tool to create self-contained python environments

###Why virtualenv
* clean versioning
  * app X gets pylib v1
  * app Y gets pylib v2
  * the sysadmin can maintain the distro/enterprise versions (avoid a grumpy sysadmin)
* reliability
  * You don't have to upgrade your codebase until you're ready
  * You don't have to upgrade all codebases at the same time
* permissions
  * The BoFH won't stop you

#### What does virtualenv technically do?
* Modifies your PATH variable to use the python binary inside the virtualenv folder
* Uses the site-packages folder within the virtualenv; Found via a relative path search by the python binary within your the virtualenv folder (Thanks Paul Collins for looking this up)

##Requirements

In order to use virtualenvwrapper in unix you must be running one of these shells:

* bash
* zsh
* ksh


#####Let's See!
    cd /tmp
    virtualenv delme_env
    echo $PATH |cut -d: -f1
    python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
    source delme_env/bin/activate
    echo $PATH |cut -d: -f1
    python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"
    deactivate


##virtualenvwrapper

<http://virtualenvwrapper.readthedocs.org/en/latest/>

###Advantages over vanilla virtualenv
* Standardizes environment locations
* Easier environment management (create, delete, copy)
* single command to switch environments (workon)
* tab completion
* hooks for just about anything you'd want a hook for

#### Check out the hooks while my DJ revolves it!
    cd ~/.virtualenvs
    find . -maxdepth 1 -type f
    mkvirtualenv delme
    cd ~/.virtualenvs/delme/bin
    ls -1


### pip
virtualenv(wrapper) and pip were made for each other.

#### pip example

    mkvirtualenv test-driven-env
    cd /www/sites/
    git clone test-driven-blog example-blog
    cp test-driven-blog/db.sqlite3 example-blog/
    cd example-blog
    pip install -r requirements.txt
    ./manage.py runserver
    coverage run manage.py test blog
    deactivate
    coverage run manage.py test blog
    workon test-driven-env
    coverage run manage.py test blog
    lssitepackages

### Windows
There is some sort of windows support:
pip search virtualenvwrapper-win
pip search virtualenvwrapper-powershell

###Pretty virtualenvwrapper
If you liked my pretty bash prompt, feel free to add your voice hereabouts:
<https://github.com/pypa/virtualenv/pull/551>


## Getting Started

###Install virtualenvwrapper

    pip install virtualenvwrapper

###Load virtualenvwrapper in your shell
Put this file at the end of your shell configuration file, probably .bashrc.  
note: you may have to change the path to virtualenvwrapper.sh depending on where it is installed

    if [ -f /usr/local/bin/virtualenvwrapper.sh ]; then
      source /usr/local/bin/virtualenvwrapper.sh
    fi

Now source your updated shell configuration file by either:

    source ~/.bashrc #assumes you're using bash

Or, logout and back in.

If you've never used virtualenvwrapper before, you should see something like this:

    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/initialize
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/premkvirtualenv
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postmkvirtualenv
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/prermvirtualenv
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postrmvirtualenv
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/predeactivate
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postdeactivate
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/preactivate
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postactivate
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/get_env_details
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/premkproject
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postmkproject
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/prermproject
    virtualenvwrapper.user_scripts creating /home/username/.virtualenvs/postrmproject


###Use virtualenvwrapper

####Creating a virtualenv

    mkvirtualenv test-delme

You should see something like:

    New python executable in test-delme/bin/python
    Installing distribute.............................................................................................................................................................................................done.
    Installing pip...............done.
    virtualenvwrapper.user_scripts creating /home/jb/.virtualenvs/test-delme/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/jb/.virtualenvs/test-delme/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/jb/.virtualenvs/test-delme/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/jb/.virtualenvs/test-delme/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/jb/.virtualenvs/test-delme/bin/get_env_details

And you are now working in the virtualenvironment "test-delme". Your command prompt was probably modified to show this at the beginning, e.g.:

    (test-delme)username@hostname:~$

####Installing custom libraries into the virtualenv
Now you can install your own personal versions of python libraries in this virtual environment

    pip install numpy


Output:

    Downloading/unpacking numpy
      Downloading numpy-1.8.1.tar.gz (3.8Mb): 3.8Mb downloaded
      Running setup.py egg_info for package numpy
        Running from numpy source directory.
    ...


After the installation, you will have the latest version of numpy accessible.


    python -c "import numpy; print(numpy.version.version)"


Output:

    1.8.1


####Deactivating a virtualenv
Now let's deactivate the virtualenv (you should notice your bash prompt returns to normal afterwards):

    deactivate

You're no longer using the virtual environment - you're using the system environment again.

    python -c "import numpy; print(numpy.version.version)"

Output:

    1.6.2

note: you may also get an error on import, if numpy is not installed in your system environment.



####Activating a virtualenv

    workon test-delme


####Switching to another virtualenv
It's the same as activation

    workon test-delme2

####Deleting a virtualenv


    rmvirtualenv test-delme

Output:

    Removing test-delme...


###Best Practices
####requirements.txt

#####Using requirements.txt
A lot of python projects will ship with a requirements.txt file. This file lists the libraries and corresponding versions required by the project.

To setup a new project's environment, simply create a new virtual environment and install what's in requirements.txt in two easy steps:

    mkvirtualenv project
    pip install -r requirements.txt 


#####Creating requirements.txt
To create requirements.txt just do this in your project's folder:

    pip freeze > requirements.txt


###Python 3
To setup a python3 project just do this:

    mkvirtualenv -p $(which python3) py3-project

Output:

    Running virtualenv with interpreter /usr/bin/python3
    New python executable in py3-project/bin/python3
    Also creating executable in py3-project/bin/python
    ...

Test python3 inside the new virtualenv:

    python --version

Output:

    Python 3.2.3


Now install python3 libraries

    pip-3.2 install numpy

###References

[Official Documentation for virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)

[Official Documentation for virtalenv](http://virtualenv.readthedocs.org/en/latest/)
