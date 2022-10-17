Feature: whonix user test
 In order to ensure whonix is working
 I as a whonix user
 Need to be able to create and delete users
 
 Scenario: I create a user and verify they exist
  When I run the command "sudo useradd" with the options "testuser1234" programmatically with root permissions my password being "changeme"
  Then the user "testuser1234" exists

 Scenario: I delete a user and verify they're gone
  When I run the command "sudo userdel" with the options "testuser1234" programmatically
  Then the user "testuser1234" no longer exists
