import sys
import os
from termcolor import colored, cprint

def ValidationAudioInputs(drive.path, audioFile):
  file_name = audioFile

  search_path = drive.path

  if not (file_name.endswith(".wav") or file_name.endswith(".WAV")):
    file_name += '.wav'

  def find_files(filename, search_path):
     result = []

  # Error 0x0224
     for root, dir, files in os.walk(search_path):
        if filename in files:
          if file_name.endswith(".wav"):
           result.append(os.path.join(root, filename))

     return result

  def cut_files(fileActual):
    convertedFileName = ""
    for i in range(len(fileActual)):
      if not (fileActual[i] == '[' or fileActual[i] == '\'' or fileActual[i] == ']'):
        convertedFileName += fileActual[i]
    return convertedFileName

  def ver_ending_file(fileActual):
    seekingChars = '.wav'
    isValidExt = False

    if fileActual.lower().endswith(seekingChars):
      isValidExt = True
    else:
      isValidExt = False

    return isValidExt

  # Error 0x0225

  fileActual = str(find_files(file_name, search_path))
  isValidFile = find_files(file_name, search_path)
  fileActual = cut_files(fileActual)
  isValidExt = ver_ending_file(fileActual)

  assert isValidFile, lib_error("0x0225a")
  assert isValidExt, lib_error("0x0225b")

  if isValidFile:
    leFilePath = fileActual
  
  return leFilePath
