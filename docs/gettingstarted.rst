###########
Development
###########

This is setup protocol for developing Home automation with Raspberry PI
and AI.

Not yet complete this project.

***************
Getting started
***************

************
Requirements
************

Python modules
==============

-  Django
-  djangorestframework
-  django-filter
-  django-background-tasks
-  dash
-  plotly
-  and so on.

.. code-block:: shell

    $ cd tph

You may install Python packages via `pip`.

.. code-block:: shell

    $ pip install -r requirements.txt

On your development Mac, Ubuntu, or MS-Windows.

.. code-block:: shell

    $ pip install -r requirements_dev.txt

On your target Raspberry Pi
---------------------------

About my Raspberry Pi 3B.

.. code-block:: shell

    $ cat /etc/debian_version
    10.9
    $ uname -a
    Linux raspi3b 5.10.17-v7+ #1403 SMP Mon Feb 22 11:29:51 GMT 2021 armv7l GNU/Linux

Enable i2c via raspi-config.

.. code-block:: shell

    $ sudo raspi-config

Add i2c group your user account.

.. code-block:: shell

    $ sudo usermod -aG i2c pi


.. code-block:: shell

    $ pip install -r requirements_rpi.txt

And edit your tph/tph/settings.py

.. code-block:: Python
    :lineno-start: 274

    ON_RASPBERRY_PI = True
    USE_SMBUS2 = True

recommended IDE(Integrated Development Environment)
===================================================

-  `Atom <https://atom.io>`__ ; base editor
-  `atom-ide <https://ide.atom.io>`__ ; make IDE base package
-  `ide-python <https://atom.io/packages/ide-python>`__ ; support Atom-IDE Python language
-  `atom-ide-debugger-python <https://atom.io/packages/atom-ide-debugger-python>`__ ; DEBUG Python

****
make
****

.. code-block:: shell

    $ Python manage.py startapp monitor

.. code-block:: shell

    $ Python manage.py makemigrations monitor


Set up your data base
=====================

.. code-block:: shell

    $ Python manage.py migrate

.. code-block:: shell

    Operations to perform:
     Apply all migrations: admin, auth, contenttypes, sessions
    Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     Applying admin.0002_logentry_remove_auto_add... OK
     Applying admin.0003_logentry_add_action_flag_choices... OK
     Applying contenttypes.0002_remove_content_type_name... OK
     Applying auth.0002_alter_permission_name_max_length... OK
     Applying auth.0003_alter_user_email_max_length... OK
     Applying auth.0004_alter_user_username_opts... OK
     Applying auth.0005_alter_user_last_login_null... OK
     Applying auth.0006_require_contenttypes_0002... OK
     Applying auth.0007_alter_validators_add_error_messages... OK
     Applying auth.0008_alter_user_username_max_length... OK
     Applying auth.0009_alter_user_last_name_max_length... OK
     Applying auth.0010_alter_group_name_max_length... OK
     Applying auth.0011_update_proxy_permissions... OK
     Applying sessions.0001_initial... OK

Using SCSS/SASS
===============

| Set up use `Sass <https://sass-lang.com>`_ my Django project.
| See and install `How to use SCSS/SASS in your Django Project(Python
  Way) <https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/>`__.

| Download Bootstrap Source file
  `here <https://getbootstrap.com/docs/4.3/getting-started/download/#source-files>`__.
| And copy SCSS files to ``static/bootstrap``.

.. code-block:: shell

    $ cp -r your/bootstrap-4.x.x/scss/* tph/static/bootstrap

Install some Python modules.

.. code-block:: shell

    pip install django_compressor
    pip install django-libsass

Background tasks
================

| I selected `Django Background
  Tasks <https://github.com/arteria/django-background-tasks>`__ for save
  datas interval.
| For Django 3.0, ``pip install django-background-tasks``.

.. code-block:: shell

    pip install django-background-tasks

Registration background tasks and execute


First step
----------

Create your Django Project.

.. code-block:: shell

    mkdir django-rpi-tph-monitor
    cd django-rpi-tph-monitor

.. code-block:: shell

    django-admin startproject tph
    cd tph

.. code-block:: shell

    python manage.py runserver

Access ``http://localhost:8000/`` on your browser. |Django First Boot|

For access from remote computer to Raspberry Pi, on your Raspberry Pi:

.. code-block:: shell

    python manage.py runserver 192.168.xxx.xxx:8000


.. |Django First Boot| image:: ../assets/images/first-django.png


You have to get another shell(terminal). Second registration task.

.. code-block:: shell

    $ curl -X GET http://localhost:8000/monitor/tasks/5/30

Third run process tasks.

.. code-block:: shell

    $ ./manage.py process_tasks

You can check tasks from your database that default is db.sqlite3. See
background_task, background_task_completed_tasks, or monitor_bme280
tables.

*************
Documentation
*************

This project's documents are making with `SPHINX <https://www.sphinx-doc.org/en/master/>`_. How to use, please see `Installing Sphinx <https://www.sphinx-doc.org/en/master/usage/installation.html>`_.

.. note::

    If you are using PyEnv, you must install via ``pip``.

.. code-block:: shell

    $ pyenv virtualenv 3.9.4 dj32rpi394docs
    $ cd ${your django-rpi-monitor}/docs
    $ pyenv local dj32rpi394docs
    $ pip install --upgrade pip
    $ pip install -r requirements.txt 

Additional packages.
====================

Sphinx-copybutton
-----------------

`Sphinx-copybutton <https://sphinx-copybutton.readthedocs.io/>`_

.. code-block:: shell
 
    $ pip install --upgrade sphinx-copybutton

Read the Docs Theme
-------------------

.. code-block:: shell

    $ pip install --upgrade sphinx-rtd-theme


Making our documents.
=====================

You can create document.

.. code-block:: shell

    cd docs
    make html
