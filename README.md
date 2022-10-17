## About

The Whonix Automated Test suite is a automated testing tool used for GUI testing of Whonix builds.

The suite uses Python3. Behave is used for test cases, and Dogtail is used for GUI automation.

#### Credits
This work is built off is the excellent capstone created by the following authors:
- John Quinn
- Evan Tanner
- Cameron Dey

The original repo can be found [here](https://github.com/johncameronquinn/wats-senior-capstone)

Current collaborators on the project are Josh Everett and Rob Stringer.

### Manual Installation:

`sudo apt-get update`

Make sure python 3 is installed

`python3 --version`

`sudo apt-get install python3`

from stock Whonix, first make sure you're up-to-date, then,

`sudo apt-get install python3-behave`

`sudo apt-get install python3-pip`

`sudo apt-get install python3-pyatspi`

`pip3 install dogtail` 

`gsettings set org.gnome.desktop.interface toolkit-accessibility true`
