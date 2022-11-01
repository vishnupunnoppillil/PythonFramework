#!/bin/bash
cd ~/PycharmProjects/PythonSelenium/TestCases
pytest -v -s -m "sanity" --html=../Reports/report.html --capture=tee-sys test_qwerty.py --browser chrome
