@torbrowser
Feature: internet browsing using the tor browser
 In order to use the whonix operating system
 As a whonix user
 I need to be able to browse the internet

 Background:
  Given the file "/home/user/.tb/tor-browser/Browser/Downloads/websitetest.html" does not exist
  And the tor browser is running

 Scenario Outline: Navigating to various websites
  When I press the key combination "ctrl t"
  And I type "<webaddress>"
  And I press the key combination "Enter"
  And I press the key combination "ctrl u"
  And I press the key combination "ctrl s"
  And I type "websitetest"
  And I press the key combination "Enter"
  Then the file "/home/user/.tb/tor-browser/Browser/Downloads/websitetest.html" exists
  And the file "/home/user/.tb/tor-browser/Browser/Downloads/websitetest.html" contains the "<oracletext>"

  Examples:
   | webaddress | oracletext |
   | https://check.torproject.org | Congratulations. This browser is configured to use Tor. |
   | http://dds6qkxpwdeubwucdiaord2xgbbeyds25rbsgr73tbfpqpt4a6vjwsyd.onion | https://www.whonix.org/wiki/Why_Whonix_is_Freedom_Software |

 Scenario: Close the browser cleanly
  When I press the key combination "alt F4"
  and I press the key combination "Enter"
  Then the tor browser closes successfully