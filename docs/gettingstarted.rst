Development
===========

This is setup protocol for developing Home automation with Raspberry PI
and AI.

Requirements
------------

-  Python modules

    -  Django
    -  djangorestframework
    -  django-filter
    -  django-background-tasks
    -  dash
    -  plotly
    -  and so on.

    You may install Python packages via `pip`.

    .. code:: shell

        cd tph
        pip install -r requirements.txt

    On your development Mac, Ubuntu, or MS-Windows.

    .. code:: shell

        cd tph
        pip install -r requirements_dev.txt

    On your target Raspberry Pi.

    .. code:: shell

        cd tph
        pip install -r requirements_rpi.txt

-  recommended IDE(Integrated Development Environment)

    -  `Atom <https://atom.io>`__ ; base editor
    -  `atom-ide <https://ide.atom.io>`__ ; make IDE base package
    -  `ide-python <https://atom.io/packages/ide-python>`__ ; support Atom-IDE Python language
    -  `atom-ide-debugger-python <https://atom.io/packages/atom-ide-debugger-python>`__ ; DEBUG Python

make
----

.. code:: shell

   Python manage.py startapp monitor

Set up your data base
---------------------

.. code:: shell

   Python manage.py migrate

.. code:: shell

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
---------------

| Set up use `Sass <https://sass-lang.com>`__ my Django project.
| See and install `How to use SCSS/SASS in your Django Project(Python
  Way) <https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/>`__.

| Download Bootstrap Source file
  `here <https://getbootstrap.com/docs/4.3/getting-started/download/#source-files>`__.
| And copy SCSS files to ``static/bootstrap``.

.. code:: shell

   cp -r your/bootstrap-4.x.x/scss/* tph/static/bootstrap

Install some Python modules.

Django 3.0.x
~~~~~~~~~~~~

.. code:: shell

   pip install django_compressor
   pip install django-libsass

.. _django-3.0.x-1:

Django 3.0.x
~~~~~~~~~~~~

`How to use Bootstrap4 Sass in Django 3.0 <for-Django3-upgrade.md>`__

Background tasks
~~~~~~~~~~~~~~~~

| I selected `Django Background
  Tasks <https://github.com/arteria/django-background-tasks>`__ for save
  datas interval.
| For Django 3.0, ``pip install django-background-tasks``.

Django 3.0
^^^^^^^^^^

| You must use this protocol until official released.
| See PR(pull requests)
  `#210 <https://github.com/arteria/django-background-tasks/pull/210>`__.
  This was Closed at Dec 11, 2019.

I did

1. fork django-background-tasks
2. ``git remote add upstream https://github.com/arteria/django-background-tasks.git``
3. ``git remote add monarchmoney https://github.com/monarchmoney/django-background-tasks.git``
4. ``git merge monarchmoney/master``
5. ``git push``

And ``pip install`` from my GitHub repository.

.. code:: shell

   $ pip install git+git://github.com/mitsuhisaT/django-background-tasks.git@master#egg=django-background-tasks

Registration background tasks and execute
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First run server.

.. code:: shell

   $ $ ./manage.py runserver

First step
----------

Create your Django Project.

.. code:: shell

  mkdir django-rpi-tph-monitor
  cd django-rpi-tph-monitor

.. code:: shell

  django-admin startproject tph
  cd tph

.. code:: shell

  python manage.py runserver

Access ``http://localhost:8000/`` on your browser. |Django First Boot|


.. |Django First Boot| image:: ../assets/images/first-django.png


You have to get another shell(terminal). Second registration task.

.. code:: shell

   $ curl -X POST http://localhost:8000/monitor/tasks/5/30

Third run process tasks.

.. code:: shell

   $ ./manage.py process_tasks

You can check tasks from your database that default is db.sqlite3. See
background_task, background_task_completed_tasks, or monitor_bme280
tables.