#!/usr/bin/env sh
# requires :
# bash
# purpose of this script :
# Run python programme

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
export API_URL_1="http://$IP"
export API_URL_2="http://$IP:3000"

#=========================================
# Install python packages
#=========================================
cd /opt/api
Display_step "Install python modules"
pip3 install -r requirements.txt

#=========================================
# Start API server
#=========================================
cd /opt/api
Display_step "Start api server"
python main.py
