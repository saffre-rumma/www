.. title: New website using Nikola
.. slug: new-website-using-nikola
.. date: 2015-11-22 06:06:02 UTC+02:00
.. tags: 
.. category: 
.. link: 
.. description: 
.. type: text
.. author: Luc Saffre

This weekend I finally invested some time into a task which had been
waiting since :doc:`20151027`: make the Rumma & Ko website
multilingual, and add information in French about our pricing policy.

.. TEASER_END

In a first step I converted the existing Sphinx site to
multilingual. Took me 45 minutes.  Then I said to myself
"Wait... isn't there some more modern way to create cool
commercial-style web sites using reStructuredText?" Google helped me
to find `Nikola <https://getnikola.com>`_.

Nikola has no chance against Sphinx for writing technical
documentation about a Python package.  But for writing a "normal"
website, the big advantage of Nikola against Sphinx is that I have a
cool responsive website with a blog, RSS feed and a built-in concept
for multilingual content with no effort. Congratulations!

One big problem in Nikola is that your website gets "flat": you have
no possibility to hierarchize your pages. You just have "posts" (news)
and "stories" (pages). It is their ticket `#765
<https://github.com/getnikola/nikola/issues/765>`_.

