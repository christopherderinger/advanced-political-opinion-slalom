docker build -t test-mt .
docker run --user root -p 8887:8888 -it test-mt start.sh jupyter lab --LabApp.token=''
