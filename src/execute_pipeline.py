import subprocess
import sys

def run_script(script_name):
  """
  Runs a Python script and checks the exit code.
  """
  try:
      result = subprocess.run(["python", script_name], check=True)
      print(f"{script_name} executed successfully!")
  except subprocess.CalledProcessError as e:
      print(f"Error executing {script_name}: {e}")
      sys.exit(1)

def main():
  """
  Executes the pipeline: tests first, then ETL.
  """
  run_script("run_tests.py")
  run_script("etl.py")

if __name__ == "__main__":
  main()