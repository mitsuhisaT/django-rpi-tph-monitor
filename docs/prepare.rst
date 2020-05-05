django-rpi-tph-monitor
======================

Home-automation with AI on Raspberry Pi and RIp TPH Monitor.

about
=====

This is integrated your home automation, control air-conditioner with AI
and another infrared controlled devices such as television set or
celling light and so on.

prepare
=======

You must get somethings next list.

-  `Raspberry Pi <https://www.raspberrypi.org>`__ 3B, 3B+
-  `RPi TPH Monitor
   Rev2 <https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/>`__
-  micro SD card, 16GB above(recommended)
-  USB connected key board
-  USB connected mouse
-  `Raspbian <https://www.raspbian.org>`__
-  HDMI cable and display

   -  use TV instead of display

-  Python development environment

   -  We supported only Python 3.7 upper version.

Set up Raspberry Pi
-------------------

You must set up your Raspberry Pi.

download newest Raspbian
~~~~~~~~~~~~~~~~~~~~~~~~

| I recommend using official Raspbian which can download from `Raspberry
  Pi Downloads <https://www.raspberrypi.org/downloads/>`__.
| You will choose “Raspbian Buster with desktop and recommended
  software” or “Raspbian Buster with desktop”.

Installing operating system image
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| You must read `installation
  guide <https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`__
  for installing operating system image.
| And download `balenaEtcher <https://www.balena.io/etcher/>`__.

macOS

.. code:: shell

   $ brew cask install balenaetcher

First boot
~~~~~~~~~~

| Only first boot time, You must connect USB keyboard, USB mouse, and
  monitor via HDMI.
| You must set Wi-Fi network and enable SSH via ``raspbian-config``.

Test remote connect
^^^^^^^^^^^^^^^^^^^

.. code:: shell

   $ ssh pi@192.168.xxx.xxx

Package upgrade

.. code:: shell

   $ sudo apt update
   ...

.. code:: shell

   $ sudo apt upgrade

Development environment
-----------------------

| You can development on your Raspberry Pi.
| I recommend preparing development environment on your Mac or PC.

pyenv and pyenv-virtualenv
~~~~~~~~~~~~~~~~~~~~~~~~~~

| Please install `pyenv <https://github.com/pyenv/pyenv>`__ and
  `pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`__.
| If you use MS-Windows
  `venv <https://docs.python.org/3.7/library/venv.html>`__ instead of
  pyenv.

.. _install-python-via-pyenvpyenv:

Install Python via `PyEnv <https://github.com/pyenv/pyenv>`__
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

   pyenv install 3.8.0

And setup pyenv-virtualenv

.. code:: shell

   pyenv virtualenv 3.8.0 djrpi380

c.f. my home directory.

.. code:: shell

   $ pyenv versions
   * system (set by /Users/mitsu/.pyenv/version)
     3.7.4
     3.7.4/envs/djsample374
     3.8.0
     3.8.0/envs/djrpi380
     djrpi380
     djsample374
   $ python --version
   Python 2.7.16

my environment directory.

.. code:: shell

   $ cd ~/git/hub/django-rpi-tph-monitor
   $ pyenv local djrpi380
   $ pyenv versions
     system
     3.7.4
     3.7.4/envs/djsample374
     3.8.0
     3.8.0/envs/djrpi380
   * djrpi380 (set by /Users/mitsu/git/hub/django-rpi-tph-monitor/.python-version)
     djsample374
   $ python --version
   Python 3.8.0

Development Application
=======================

Let’s development “Home automation application”.

.. _prepare-1:

Prepare
-------

Let’s setup your Python development environment.

Atom IDE
~~~~~~~~

You need additional installing for Atom
`ide-python <https://github.com/lgeiger/ide-python>`__.

.. code:: shell

   python -m pip install 'python-language-server[all]'
