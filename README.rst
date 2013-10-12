lumberjack
==========

A commandline tool to render static web sites from restructured text with jinja templates. In other words: yet another static site generator.


.. epigraph::

   "He walks down trees, he parses files *mumble*, *mumble*, suspenders and a bra!"


Why another one?
----------------

The existing crop of (python based) site generators all make a great deal of assumptions regarding their usage. Even those that come closest to our idea of a general 'HTML compiler' (the excellent `mynt <http://mynt.mirroredwhite.com>`_ and `Blogofile <http://www.blogofile.com>`_) made implementing our use cases unneccessarily cumbersome.

Specifically, lumberjack is designed to:

 * build general-purpose websites (IOW sites that are not blogs, like `Pelican <http://docs.getpelican.com/en/3.3.0/>`_ and `Blogofile <http://www.blogofile.com>`_ do)
 * explicitly support existing tools such as `GruntJS <http://gruntjs.com>`_ and `Bower <http://bower.io>`_ (no need to re-invent the wheel here Python people, the JS folks got this down to a science!)
 * be fast (like already mynt is, for example). Rendering a typical site should never take longer than 1s.
 * *complete* separation of content and theme
