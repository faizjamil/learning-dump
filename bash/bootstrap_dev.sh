OS=$(uname -s)
echo $OS

checkDistro() {
    DISTRO=""
    if [[ $OS = "Linux" ]]
    then
      if [[ -f "/etc/debian_version" ]]
        then
          # echo "debian"
          # we know it's debian based
          if [[ -f "/etc/lsb-release" ]]
          then
            if [[ -f "/usr/bin/wslinfo" ]]
            then
                DISTRO="ubuntu_wsl"
            else
                DISTRO="ubuntu"
            fi
          else
            DISTRO="debian"
          fi
        elif [[ -f "/etc/fedora-release" ]]
        then
          DISTRO="fedora"
        else 
          DISTRO="unknown"
        fi
    elif [[ $OS = "Darwin" ]]
    then
      DISTRO="macOS"
    fi
    
    echo $DISTRO
        
}

# echo $(checkDistro)

if [[ $(checkDistro) = "ubuntu_wsl" ]]
then
  echo "distro is Ubuntu on WSL"
fi
