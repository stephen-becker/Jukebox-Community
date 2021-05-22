import sys
from termcolor import colored, cprint

def clearedCell(GPU):
  currentDriver = GPU
  
  if not "K80" not in currentDriver:
    driveText = colored('\nWarning:', 'red')
    print(driveText,"It has been detected that you are using a 'K80' type of GPU which can lead to problems. Please try again for another GPU or you may find you have issues during your run. Proceed with caution!")
  else:
    driveText = colored('\nSystem:', 'yellow')
    print(driveText,"Please proceed to run the next cell!")

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
  currentUse = vv
  convertedNum = '16.02'
  #betaNum = convertedNum+'01'
  recentBuild = float(convertedNum)
  needsUpdate = False
  goodVersion = colored('Build '+convertedNum, 'green')
  
  if currentUse == recentBuild:
    print("You're running the lastest version of this build.", goodVersion)
    print("There might be errors during your session, report them on discord.")
    needsUpdate = True
  #elif currentUse == betaNum:
  #  print("You're running a beta version of this build. There may/will be errors as this notebook is not optimized.")
  else:
    exitTxt = colored('You\'re running an outdated version of this build. This notebook version is', currentUse)
    sys.exit(exitTxt)
