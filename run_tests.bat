@echo off

REM Run unit tests with coverage and generate HTML report
pytest --cov=agents.data_extractor --cov-report=html test_data_extractor.py

REM Open the coverage report in the default browser
start htmlcov\index.html

pause
