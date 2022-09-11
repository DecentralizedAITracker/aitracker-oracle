FROM renaultdigital/python-pandas:3.6_0.22
### install python dependencies if you have some


RUN pip3 install rsa
RUN pip3 install requests
RUN pip3 install numpy

COPY ./src /src


ENTRYPOINT ["python3", "/src/app.py"]