## Docker commands

### Build
```
docker build . --tag aitracker-oracle-rlcusdt
```
### Tag
```
docker tag aitracker-oracle-rlcusdt id997/aitracker-oracle-rlcusdt:1.0.0
```
### Push
```
docker push id997/aitracker-oracle-rlcusdt:1.0.0
```
### Get hash
```
docker pull id997/aitracker-oracle-xmrusdt:1.0.0 | grep "Digest: sha256:" | sed 's/.*sha256:/0x/'
```

### Links
```
link: registry.hub.docker.com/id997/aitracker-oracle:0.1.0
link: registry.hub.docker.com/id997/aitracker-oracle-xmrusdt:1.0.0
link: registry.hub.docker.com/id997/aitracker-oracle-rlcusdt:1.0.0
```

### Run with input files
```
run with input_files: docker run \
    -v /home/id/Projects/iexec-aitracker/aitracker-oracle/io/iexec_in:/iexec_in \
    -v /home/id/Projects/iexec-aitracker/aitracker-oracle/io/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    -e IEXEC_INPUT_FILE_NAME_1=result.json \
    -e IEXEC_INPUT_FILES_NUMBER=1 \
    aitracker-oracle
```