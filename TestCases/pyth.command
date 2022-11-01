#!/bin/bash
pytest -v -s -m "sanity" --html=../Reports/report.html --capture=tee-sys TestCases/test_qwerty.py --browser chrome
