FROM python:3.12

WORKDIR /usr/src/CodePaste

COPY . /usr/src/CodePaste

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install .

ENTRYPOINT ["codepaste"]