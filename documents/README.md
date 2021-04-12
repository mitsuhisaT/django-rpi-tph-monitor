# Development
This is setup protocol for developing Home automation with Raspberry PI and AI.

## Requirements

* Python modules
  * Django
  * djangorestframework
  * django-filter
  * markdown
* recommended IDE(Integrated Development Environment)
  * [Atom][atom] ; base editor
  * [atom-ide][atomide] ; make IDE base package
  * [ide-python][idepython] ; support Atom-IDE Python language
  * [atom-ide-debugger-python][aidp] ; DEBUG Python

## make 

```shell
Python manage.py startapp monitor
```

## Set up your data base
```shell
Python manage.py migrate
```

```shell
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
```

## Using SCSS/SASS
Set up use [Sass][sass] my Django project.  
See and install 
[How to use SCSS/SASS in your Django Project(Python Way)][htus].

Download Bootstrap Source file [here][bss].  
And copy SCSS files to `static/bootstrap`.

```shell
cp -r your/bootstrap-4.x.x/scss/* tph/static/bootstrap
```

Install some Python modules.  

### Django 3.0.x
```shell
pip install django_compressor
pip install django-libsass
```

### Django 3.0.x
~~[How to use Bootstrap4 Sass in Django 3.0](for-Django3-upgrade.md)~~

### Background tasks
I selected [Django Background Tasks][bts] for save datas interval.  
For Django 3.0, `pip install django-background-tasks`.  
~~But Django 3.0, not yet support.~~

#### Django 3.0
You must use this protocol until official released.  
See PR(pull requests) [#210][pr210]. This was Closed at Dec 11, 2019.  

I did 

1. fork django-background-tasks
1. `git remote add upstream https://github.com/arteria/django-background-tasks.git`
1. `git remote add monarchmoney https://github.com/monarchmoney/django-background-tasks.git`
1. `git merge monarchmoney/master`
1. `git push`

And `pip install` from my GitHub repository.

```shell
$ pip install git+git://github.com/mitsuhisaT/django-background-tasks.git@master#egg=django-background-tasks
```

#### Registration background tasks and execute
First run server.

```shell
$ ./manage.py runserver
```

You have to get another shell(terminal).
Second registration task.

```shell
$ curl -X POST http://localhost:8000/monitor/tasks/5/30
```
Third run process tasks.

```shell
$ ./manage.py process_tasks
```

You can check tasks from your database that default is db.sqlite3.
See background_task, background_task_completed_tasks, or monitor_bme280 tables.

----
[atom]: https://atom.io
[atomide]: https://ide.atom.io
[idepython]: https://atom.io/packages/ide-python
[aidp]: https://atom.io/packages/atom-ide-debugger-python
[sass]: https://sass-lang.com
[htus]: https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/
[bss]: https://getbootstrap.com/docs/4.3/getting-started/download/#source-files
[bts]: https://github.com/arteria/django-background-tasks
[pr210]: https://github.com/arteria/django-background-tasks/pull/210
