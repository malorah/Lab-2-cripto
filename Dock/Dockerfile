FROM debian
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt install curl -y
RUN  bash -c "$(curl --fail --show-error --silent --location https://raw.githubusercontent.com/IamCarron/DVWA-Script/main/Install-DVWA.sh)"

