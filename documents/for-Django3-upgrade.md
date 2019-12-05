# How to use Bootstrap4 Sass in Django 3.0

I set up Django 2.2 and Bootstrap4 Sass from the  
['How to use SCSS/SASS in your Django project (Python Way)'][dbs].

But can't work Django 3.0.  
This is one of resolution.

My testing environment is:  
macOS High Sierra Version 10.13.6


## prepare PyEnv Virtualenv

```shell
$ cd ~
$ pyenv virtualenv 3.7.5 dj3rpi375
$ cd your/django-rpi-tph-monitor/
$ pyenv local dj3rpi375
```

## install Django 3.0 and others

```shell
$ pip install --upgrade Django
$ pip install --upgrade djangorestframework
$ pip install --upgrade markdown
$ pip install --upgrade django-filter
$ pip install --upgrade drf-yasg
$ pip install --upgrade django-bootstrap4
$ pip install -e git://github.com/mitsuhisaT/django-compressor.git@six1.13#egg=django_compressor
$ pip install --upgrade django-libsass
```


about django-compressor [issue 963][dc963].

## test

```shell
$ ./manage.py test monitor
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
........<BME280: BME280 object (None)>
<BME280: BME280 object (None)>
<BME280: BME280 object (None)>
<BME280: BME280 object (None)>
<BME280: BME280 object (None)>
.<BME280: BME280 object (None)>
.
----------------------------------------------------------------------
Ran 10 tests in 5.034s

OK
Destroying test database for alias 'default'...
```

But, can't display web page, because 'django_libsass.SassCompiler: command not found'.

resolution hint: from stackoverflow [Django Sass Compressor django_libsass.SassCompiler: command not found][so22515611]


## install part 2

### uninstall django-libsass

```shell
$ pip uninstall django-libsass
```

### install sassc

```shell
$ brew install sassc
```

### modified settings.py

```Python
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'pysassc {infile} {outfile}'),
)
```

Success!

----
[dbs]: https://www.accordbox.com/blog/how-use-scss-sass-your-django-project-python-way/
[dc963]: https://github.com/django-compressor/django-compressor/issues/963
[so22515611]: https://stackoverflow.com/questions/22515611/django-sass-compressor-django-libsass-sasscompiler-command-not-found
