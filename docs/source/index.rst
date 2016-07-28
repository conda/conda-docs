.. conda documentation master file, created by
   sphinx-quickstart on Sat Nov  3 16:08:12 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

=====
Conda
=====

Conda is an open source package management system and environment management system for installing multiple
versions of software packages and their dependencies and switching easily between them. It works on
Linux, OS X and Windows, and was created for Python programs but can package and distribute any software.

Conda is included in Anaconda and Miniconda. Conda is also included in the Continuum `subscriptions <https://www.continuum.io/anaconda-subscriptions>`_
of Anaconda, which provide on-site enterprise package and environment management for Python, R, Node.js, Java, and other application
stacks. Conda is also available on pypi, although that approach may not be as up-to-date.

* Miniconda is a small “bootstrap” version that includes only conda and conda-build, and installs Python. Over 720
  scientific packages and their dependencies can be installed individually from the Continuum repository with
  the “conda install” command.
* Anaconda includes conda, conda-build, Python, and over 150 automatically installed scientific packages and
  their dependencies. As with Miniconda, over 250 additional scientific packages can be installed individually with
  the “conda install” command.
* pip install conda uses the released version on pypi.  This version allows you to create new conda environments using
  any python installation, and a new version of Python will then be installed into those environments.  These environments
  are still considered "Anaconda installations."

The `conda` command is the primary interface for managing `Anaconda
<http://docs.continuum.io/anaconda/index.html>`_ installations. It can query
and search the Anaconda package index and current Anaconda installation,
create new conda environments, and install and update packages into existing
conda environments.


.. raw:: html

        <!-- Begin MailChimp Signup Form -->
        <link href="//cdn-images.mailchimp.com/embedcode/classic-10_7.css" rel="stylesheet" type="text/css">
        <style type="text/css">
          #mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }
          /* Add your own MailChimp form style overrides in your site stylesheet or in this style block.
             We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */
        </style>
        <div id="mc_embed_signup">
        <form action="//pydata.us13.list-manage.com/subscribe/post?u=28f85eefa68de727efcbd93f9&amp;id=cb4ca49e7d" method="post" id="mc-embedded-subscribe-form" name="mc-embedded-subscribe-form" class="validate" target="_blank" novalidate>
            <div id="mc_embed_signup_scroll">
          <h2>Conda Announcements</h2>
        <div class="indicates-required"><span class="asterisk">*</span> indicates required</div>
        <div class="mc-field-group">
          <label for="mce-EMAIL">Email Address  <span class="asterisk">*</span>
        </label>
          <input type="email" value="" name="EMAIL" class="required email" id="mce-EMAIL">
        </div>
        <div class="mc-field-group">
          <label for="mce-NAME">Name </label>
          <input type="text" value="" name="NAME" class="" id="mce-NAME">
        </div>
        <div class="mc-field-group">
          <label for="mce-AFFILIATIO">Affiliations (e.g. Company, Projects) </label>
          <input type="text" value="" name="AFFILIATIO" class="" id="mce-AFFILIATIO">
        </div>
        <p><a href="http://us13.campaign-archive2.com/home/?u=28f85eefa68de727efcbd93f9&id=cb4ca49e7d" title="View previous campaigns">View previous campaigns.</a></p>
          <div id="mce-responses" class="clear">
            <div class="response" id="mce-error-response" style="display:none"></div>
            <div class="response" id="mce-success-response" style="display:none"></div>
          </div>    <!-- real people should not fill this in and expect good things - do not remove this or risk form bot signups-->
            <div style="position: absolute; left: -5000px;" aria-hidden="true"><input type="text" name="b_28f85eefa68de727efcbd93f9_cb4ca49e7d" tabindex="-1" value=""></div>
            <div class="clear"><input type="submit" value="Subscribe" name="subscribe" id="mc-embedded-subscribe" class="button"></div>
            </div>
        </form>
        </div>

        <!--End mc_embed_signup-->


.. toctree::
   :hidden:

   get-started
   using/index
   building/build
   help/help
   get-involved

Presentations & Blog Posts
--------------------------

`Packaging and Deployment with conda - Travis Oliphant <https://speakerdeck.com/teoliphant/packaging-and-deployment-with-conda>`_

`Python 3 support in Anaconda - Ilan Schnell <https://www.continuum.io/content/python-3-support-anaconda>`_

`New Advances in conda - Ilan Schnell <https://www.continuum.io/blog/developer/new-advances-conda>`_

`Python Packages and Environments with conda - Bryan Van de Ven <https://www.continuum.io/content/python-packages-and-environments-conda>`_

`Advanced features of Conda, part 1 - Aaron Meurer <https://www.continuum.io/blog/developer/advanced-features-conda-part-1>`_

`Advanced features of Conda, part 2 - Aaron Meurer <https://www.continuum.io/blog/developer/advanced-features-conda-part-2>`_

Requirements
------------

* python 2.7, 3.4, or 3.5
* pycosat
* pyyaml
* requests
