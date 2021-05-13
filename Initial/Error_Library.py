def lib_error(typeOfError):
  
  global errorRtrn
  
  if typeOfError == "0x0227b":
    errorRtrn = "Invalid input for 'AudioGenre', either it was incorrectly entered or selected genre does not exist on this model."
  
  if typeOfError == "0x0227":
    errorRtrn = "Invalid input for 'AudioArtist', either it was incorrectly entered or selected artist does not exist on this model."
  
  if typeOfError == "0x0226":
    errorRtrn = "Invalid input for 'ColabMembershipStatus', please try again with a valid input of either 'Pro' or 'Free'."

  if typeOfError == "0x0225a":
    errorRtrn = "The inputed file could not be found, please type the file name again or check if it exists."

  if typeOfError == "0x0225b":
    errorRtrn = "The inputed file does not have a valid ending extension (.wav?)."

  if typeOfError == "0x0224a":
    errorRtrn = "Too many '/' in the entered string, did you correctly enter the path?"

  if typeOfError == "0x0224b":
    errorRtrn = "You entered something else besides 'Y' or 'N' try again"

  if typeOfError == "0x0224d":
    errorRtrn = "Directory (folder) does not exist."
  
  if typeOfError == "1x0001":
    errorRtrn = "An internal error has occured."

  return errorRtrn;
