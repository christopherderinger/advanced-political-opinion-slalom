docker rm $(docker ps -a --filter ancestor=test-mt -q)
docker rmi test-mt
docker build -t test-mt .
docker run --mount type=bind,source=/Users/christopher/Development/mt_final_structure/big_datasets,target=/home/jovyan/mt/big_datasets --user root -e GRANT_SUDO=yes -p 8887:8888 -i test-mt start.sh jupyter lab --LabApp.token='' 
