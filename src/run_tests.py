import sys
import pytest
from io import StringIO

def main():
  print("Running all the tests")  
  pytest.main()  

def capture_output():  
  return StringIO()

if __name__ == "__main__":
  main()