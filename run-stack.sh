#!/usr/bin/env sh
#
# requires :
# bash
# purpose of this script :
# Run react and python programme

Display_step()
{
  # Check_argument_equal $# 1 "Display_step"
  local message
  message=$1
  echo ""
  echo "************************************************************"
  echo "* ${message}"
  echo "************************************************************"
  return 0
}

#=========================================
#global variables
#=========================================
export IP=$1

# #=========================================
# #Build react app
# #=========================================
cd REACT
Display_step "Build react app"
docker build -t react-app:1.0 .

#=========================================
# Run react app
#=========================================
Display_step "Run react app"
docker run -p 3000:3000 react-app:1.0 $IP &

#=========================================
#Build API App
#=========================================
cd ../FastApi
Display_step "Build API App"
docker build -t api-app:1.0 .

#=========================================
#Run Api app
#=========================================
Display_step "Run Api app"
docker run -p 8000:8000 api-app:1.0 $IP &