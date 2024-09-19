import os.path
import sys
from PP1_4 import *

def test_q1_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q1()
  captured = capsys.readouterr()
  sys.stderr.write("word\n")
  captured += capsys.readouterr()
  assert captured.out == "Input a word: word\n"

def test_q1_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q1()
  captured = capsys.readouterr()
  sys.stderr.write("help\n")
  captured += capsys.readouterr()
  assert captured.out == "Input a word: help\n"

def test_q2_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q2()
  captured = capsys.readouterr()
  sys.stderr.write("George\n")
  captured += capsys.readouterr()
  assert captured.out == "Input your first name: Hello George\n"

def test_q2_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q2()
  captured = capsys.readouterr()
  sys.stderr.write("Gretta\n")
  captured += capsys.readouterr()
  assert captured.out == "Input your first name: Hello Gretta\n"

def test_q3_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q3()
  captured = capsys.readouterr()
  sys.stderr.write("Alan\n")
  sys.stderr.write("Marr\n")
  captured += capsys.readouterr()
  assert captured.out == "Input your first name: Input your last name: Marr Alan\n"

def test_q3_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q3()
  captured = capsys.readouterr()
  sys.stderr.write("James\n")
  sys.stderr.write("Kalisz\n")
  captured += capsys.readouterr()
  assert captured.out == "Input your first name: Input your last name: Kalisz James\n"

def test_q4_1(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q4()
  captured = capsys.readouterr()
  sys.stderr.write("Fatima\n")
  sys.stderr.write("Wan Ling\n")
  captured += capsys.readouterr()
  assert captured.out == "Input a student: Input another student: Your students are Fatima and Wan Ling\n"

def test_q4_2(capsys):

  try:
    exists = os.path.exists("PP1_4.py")
    assert exists
  except:
    sys.exit()

  q4()
  captured = capsys.readouterr()
  sys.stderr.write("Kalie\n")
  sys.stderr.write("Steve\n")
  captured += capsys.readouterr()
  assert captured.out == "Input a student: Input another student: Your students are Kalie and Steve\n"
