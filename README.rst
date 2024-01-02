============
saffre-rumma
============

No longer maintained. These are the Nikola source files we used UNTIL DECEMBER 2020 for generating our
`company website <https://www.saffre-rumma.net>`__. We switched from Nikola to Sphinx and from GitHub to GitLab: https://gitlab.com/saffre-rumma/www

Instructions:

- clone this project to your computer (using ssh, not https because
  you will want to write to it)::

    $ cd ~/repositories
    $ git clone git@github.com:saffre-rumma/www.git
  
- Install Nikola::

    $ pip install nikola

- Modify your :file:`.rst` files
  
- Build your local copy::    

    $ inv bd
    
- Deploy your files::

    $ inv pd

  You need of course to configure atelier and write permission to the
  repository.
