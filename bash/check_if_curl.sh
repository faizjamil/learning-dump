CURL_INSTALLED=1
if [[ -f "/bin/curl" || -f "/usr/bin/curl"  ]]
then
  echo "curl is installed"
  CURL_INSTALLED=0
else 
  echo "curl is not installed"
fi