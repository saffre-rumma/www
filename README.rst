============
saffre-rumma
============

These are the Nikola source files for generating our
`company website <http://www.saffre-rumma.net>`__.

Instructions:

- fork the repo on GitHub

- clone your repo to your computer (using ssh, not https because you
  will want to write to it)::

    $ cd ~/repositories
    $ mkdir sr
    $ cd sr
    $ git clone git@github.com:username/saffre-rumma.git
  
- Create a Python3 environment and install Nikola::

    $ virtualenv -p python3 env
    $ . env/bin/activate
    $ pip install nikola
    $ pip install ghp-import2

  See `virtualenv --help` if needed.

- Build the html files by invoking::

    $ nikola build

- Before deploying for the first time    
