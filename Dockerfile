# Use the official Python 3.9 image as the base
FROM python:3.9-slim-buster

RUN mkdir -p src

WORKDIR /src

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY src/ . 

# Set the default command to be executed when the container starts
# CMD [ "python", "etl.py" ]
# CMD [ "python", "etl.py", "&&", "python", "run_tests.py" ]
# CMD [ "python", "run_tests.py" , "&&", "python", "etl.py"]
# CMD ["python", "run_tests.py", "&&", "python", "etl.py"]
# CMD [ "python", "run_tests.py" ]
# CMD [ "python", "etl.py" ]
CMD ["python", "execute_pipeline.py"]