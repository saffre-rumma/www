============
saffre-rumma
============

These are the Nikola source files for generating our
`company website <http://www.saffre-rumma.net>`__.

Instructions:

- clone this project to your computer (using ssh, not https because
  you will want to write to it)::

    $ cd ~/repositories
    $ git clone git@github.com:saffre-rumma/www.git
  
- Create a Python3 environment below your repository::

    $ cd ~/repositories/www
    $ virtualenv -p python3 env
    
  Activate it and install Nikola::
    
    $ . env/bin/activate
    $ pip install nikola
    $ pip install ghp-import2

  See `virtualenv --help` if needed.

- Modify your :file:`.rst` files and deploy them::

    $ nikola github_deploy

  You need of course write permission to the repository.
