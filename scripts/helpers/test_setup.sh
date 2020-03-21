#!/bin/bash

# Setup script to package and run whonix automated test suite on fresh Whonix VM CLI
# This script should be packaged on a new whonix system, and should only be run once
# Other helpful scripts will be added in the future

sudo apt-get install ruby git -yqq
git clone https://github.com/Mycobee/whonix_automated_test_suite.git
cd whonix_automated_test_suite/
sudo gem install bundler
bundle install
rspec
