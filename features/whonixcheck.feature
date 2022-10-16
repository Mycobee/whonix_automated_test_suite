Feature: whonix check terminal command
 In order to ensure whonix is working
 As a whonix user
 I need to be able to use the whonixcheck command
 
 Scenario: run whonixcheck --verbose --leak-tests --gui --cli
  When I run the command "whonixcheck" with the options "--verbose --leak-tests --gui --cli" programmatically
  Then there is CLI output
  And the GUI window appears and is dismissed
