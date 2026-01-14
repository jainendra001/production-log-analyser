import os
FILE_PATH="logs/app.log"
if os.path.exists(FILE_PATH) :
  with open(FILE_PATH,"r") as logFile:
    lines=logFile.readlines()

service_errors={}
total_errors=0
for line in lines:
  if "ERROR" in line:
    total_errors+=1
    if "service=" in line:
      start_index=line.find("service=")
      service_start=line[start_index+8:]
      service_name=service_start.split()[0]
      if service_name in service_errors:
        service_errors[service_name]+=1
      else:
        service_errors[service_name]=1
    else:
      if "unkown" in service_errors:
        service_errors["unkown"]+=1
      else:
        service_errors["unkown"]=1

print(f"Total errors: {total_errors}")
print("\nErrors by service:")

for service_name,error_count in service_errors.items():
  print(f"{service_name}:{error_count}")
      
