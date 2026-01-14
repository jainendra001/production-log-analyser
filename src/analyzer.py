import os
FILE_PATH="logs/app.log"
if os.path.exists(FILE_PATH):
  # logFile=open(FILE_PATH,"r")
  with open(FILE_PATH,"r") as logFile:
    lines=logFile.readlines()
else:
  print('The logs are not available.')
  
# lines=logFile.readlines()
# logFile.close()
ERROR_COUNT=0
for line in lines :
  if 'ERROR' in line :
    ERROR_COUNT+=1

print(f"The total Errors are : {ERROR_COUNT}")

