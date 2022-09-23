build: docker build . --tag aitracker-oracle
tag: docker tag aitracker-oracle id997/aitracker-oracle:0.1.0
push: docker push id997/aitracker-oracle:0.1.0
hash: docker pull id997/aitracker-oracle:0.1.0 | grep "Digest: sha256:" | sed 's/.*sha256:/0x/'
link: registry.hub.docker.com/id997/aitracker-oracle:0.1.0


run with input_files: docker run \
    -v /home/id/Projects/iexec-aitracker/aitracker-oracle/io/iexec_in:/iexec_in \
    -v /home/id/Projects/iexec-aitracker/aitracker-oracle/io/iexec_out:/iexec_out \
    -e IEXEC_IN=/iexec_in \
    -e IEXEC_OUT=/iexec_out \
    -e IEXEC_INPUT_FILE_NAME_1=result.json \
    -e IEXEC_INPUT_FILES_NUMBER=1 \
    aitracker-oracle