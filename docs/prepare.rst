######################################
TPH forecast with Raspberry Pi and AI.
######################################

I explain first boot your Raspberry Pi and set up Python environment for developing.

*********
Preparing
*********

Please get somethings next list.

-  `Raspberry Pi <https://www.raspberrypi.org>`_ 3B, 3B+
-  `RPi TPH Monitor Rev2 <https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/>`_
-  micro SD card, 16GB above(recommended)
-  USB connected key board
-  USB connected mouse
-  `Raspbian <https://www.raspbian.org>`_
-  HDMI cable and display

   -  use TV instead of display

-  Python development environment

   -  We supported only Python 3.7 upper version.

*******************
Set up Raspberry Pi
*******************

You must set up your Raspberry Pi.

On your Mac or PC(Linux, MS-Windows), you can install Raspbian to microSD card.

Download newest Raspbian
========================

I recommend using official Raspbian which can download from `Raspberry Pi Downloads <https://www.raspberrypi.org/downloads/>`_.

You will choose “Raspbian Buster with desktop and recommended software” or “Raspbian Buster with desktop”.

Installing operating system image
=================================

You must read `installation guide <https://www.raspberrypi.org/documentation/installation/installing-images/README.md>`_ for installing operating system image.

And download `balenaEtcher <https://www.balena.io/etcher/>`_.

macOS
-----

    If you use Apple Mac, you can install via ``brew``.

        .. code-block:: shell

            $ brew cask install balenaetcher

First boot
==========

Only first boot time, You must connect USB keyboard, USB mouse, and monitor via HDMI. You must set Wi-Fi network and enable SSH via ``raspbian-config``. Please set fixed IP address, for example ``192.168.0.121/24``.

Test remote connect
===================

On your Mac or PC, remote connecting test via ``ssh``.

    .. code-block:: shell

        $ ssh pi@192.168.0.121

Package upgrade
---------------

    I recommend upgrade your Raspbian.

        .. code-block:: shell

            $ sudo apt update
            ...

        .. code-block:: shell

            $ sudo apt upgrade

*******************************
Prepare development environment
*******************************

You can development on your Raspberry Pi.  

I recommend preparing development environment on your Mac or PC.

pyenv and pyenv-virtualenv
==========================

Please install 

macOS, Linux
------------

    - `pyenv <https://github.com/pyenv/pyenv>`__
    - `pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`__

    Install Python via `PyEnv <https://github.com/pyenv/pyenv>`__

        .. code-block:: shell

            $ pyenv install 3.8.0

    And setup pyenv-virtualenv

        .. code-block:: shell

            $ pyenv virtualenv 3.8.0 djrpi380

    c.f. my home directory.

        .. code-block:: shell

            $ pyenv versions
            * system (set by /Users/mitsu/.pyenv/version)
             3.7.4
             3.7.4/envs/djsample374
             3.8.0
             3.8.0/envs/djrpi380
             djrpi380
             djsample374

        .. code-block:: shell

            $ python --version
            Python 2.7.16

    my environment directory.

        .. code-block:: shell

            $ cd ~/git/hub/django-rpi-tph-monitor

        .. code-block:: shell

            $ pyenv local djrpi380

        .. code-block:: shell

            $ pyenv versions
             system
             3.7.4
             3.7.4/envs/djsample374
             3.8.0
             3.8.0/envs/djrpi380
            * djrpi380 (set by /Users/mitsu/git/hub/django-rpi-tph-monitor/.python-version)
             djsample374


        .. code-block:: shell

            $ python --version
            Python 3.8.0

MS-Windows
----------

    If you use MS-Windows, `venv <https://docs.python.org/3.7/library/venv.html>`__ instead of pyenv.


Let’s begin development “Home automation application”.
