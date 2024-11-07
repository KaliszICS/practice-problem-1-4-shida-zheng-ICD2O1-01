import os.path
import sys
import PP1_4

def test_q1_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["word"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input
  
  PP1_4.q1()
  captured = capsys.readouterr()
  assert captured.out == "Input a word: word\n"

def test_q1_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["help"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input
  
  PP1_4.q1()
  captured = capsys.readouterr()
  assert captured.out == "Input a word: help\n"

def test_q2_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["George"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q2()
  captured = capsys.readouterr()
  assert captured.out == "Input your first name: Hello George\n"

def test_q2_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["Gretta"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q2()
  captured = capsys.readouterr()
  assert captured.out == "Input your first name: Hello Gretta\n"

def test_q3_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["Alan", "Marr"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q3()
  captured = capsys.readouterr()
  assert captured.out == "Input your first name: Input your last name: Marr Alan\n"

def test_q3_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["James", "Kalisz"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q3()
  captured = capsys.readouterr()
  assert captured.out == "Input your first name: Input your last name: Kalisz James\n"

def test_q4_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["Fatima", "Wan Ling"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q4()
  captured = capsys.readouterr()
  assert captured.out == "Input a student: Input another student: Your students are Fatima and Wan Ling\n"

def test_q4_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  input_values = ["Kalie", "Steve"]
  
  def mock_input(s):
    print(s, end='')
    return input_values.pop(0)
  PP1_4.input = mock_input

  PP1_4.q4()
  captured = capsys.readouterr()
  assert captured.out == "Input a student: Input another student: Your students are Kalie and Steve\n"
