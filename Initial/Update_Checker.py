import sys
from termcolor import colored, cprint

def clearedCell():
  driveText = colored('\nSystem:', 'orange')
  print(driveText,"Please proceed to run the next cell.")

def initalStageCommit(typePrint):
  
  if typePrint == 'gpuTxt':
    gpuText = colored('Assigned GPU:', 'red')
    print(gpuText)
  elif typePrint == 'driveTxt':
    driveText = colored('\nGoogle Drive Connector:', 'red')
    print(driveText)
  elif typePrint == 'updateTxt':
    updateText = colored('\nChecking For Updates:', 'red')
    print(updateText)
  
def versionChecker(vv):
  convertedNum = '16.02'
  recentBuild = float(convertedNum)
  currentUse = vv
  needsUpdate = False
  goodVersion = colored('Build '+convertedNum, 'green')
  
  if currentUse == recentBuild:
    print("You're running the lastest version of this build.", goodVersion)
    print("There might be errors during your session, report them on discord.")
    needsUpdate = True
  else:
    exitTxt = colored('You\'re running an outdated version of this build.', 'red')
    sys.exit(exitTxt)
