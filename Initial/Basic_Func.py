import sys
import os
from termcolor import colored, cprint

def SafeProceed():
  driveText = colored('\nSystem:', 'yellow')
  print(driveText,"Please proceed to run the next cell!")

def StepProcess(userInput):
  if userInput == "ColabMembershipStatus":
    driveText = colored('\nSystem:', 'yellow')
    print(driveText,"Colab membership value is good.")
  
  if userInput == "AudioFileName":
    driveText = colored('\nSystem:', 'yellow')
    print(driveText,"Audio file was found and selected.")
    
  if userInput == "DirOutput":
    driveText = colored('\nSystem:', 'yellow')
    print(driveText,"File output path folder was found and selected.")
  
  if userInput == "JukeboxModel":
    driveText = colored('\nSystem:', 'yellow')
    print(driveText,"Jukebox model was selected.")

def ValidationHold():
  driveText = colored('\nSystem:', 'yellow')
  print(driveText,"Please wait while the system scans and validates your entries. This may take a few seconds to one or two minutes.")
