#!/usr/bin/env bash
#
# requires :
# bash
# purpose of this script :
# Run react programme

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
export NEW_IP=$1
export REACT_JS_EN_FILE=/opt/frontend/.env
export OLD_IP=$(cat $REACT_JS_EN_FILE | grep predict | cut -d '/' -f 3 | cut -d ':' -f 1)
source ~/.bashrc
#=========================================
#Set IP Local Machine
#=========================================
Display_step "Set the new IP for frontend apps"

sed -i -e s/${OLD_IP}/${NEW_IP}/ ${REACT_JS_EN_FILE}


#=========================================
# Start Reactjs server
#=========================================
cd /opt/frontend
Display_step "Start React JS server"
npm run start
