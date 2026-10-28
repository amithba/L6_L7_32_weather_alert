\# Lab 6: Code Coverage and Branch Coverage Analysis



\*\*Student Name:\*\* Amith BA  

\*\*SRN:\*\* PES1UG24AM032  

\*\*Repository:\*\* L6\_L7\_32\_weather\_alert  

\*\*Application:\*\* Weather Alert System  

\*\*Tools Used:\*\* Python, pytest, coverage.py



\## 1. Objective



The objective of this lab is to test the Weather Alert application using pytest and measure statement coverage and branch coverage using coverage.py.



\## 2. Code Coverage Testing



The code coverage tests check the application's wind, rainfall, heat, and overall alert functions. Test cases cover threshold values, different alert severities, empty input, and invalid alert types.



\*\*Test file:\*\* `CodeCoverageTest\_PES1UG24AM032\_application.py`



\*\*Observed result:\*\*

\- Tests passed: 33

\- Statement coverage: 100%

\- Statements covered: 38 out of 38



\*\*Screenshot:\*\* `screenshots/code\_coverage.png`



\## 3. Branch Coverage Testing



The branch coverage tests exercise alternative decision paths in the wind, rain, heat, and overall alert functions. They include boundary values, different severity combinations, and invalid alert input.



\*\*Test file:\*\* `BranchCoverageTest\_PES1UG24AM032\_application.py`



\*\*Observed result:\*\*

\- Tests passed: 28

\- Tests failed: 0

\- Statements covered: 38 out of 38

\- Branches covered: 28 out of 28

\- Partial branches: 0

\- Total coverage reported by coverage.py: 100%



\*\*Screenshot:\*\* `screenshots/branch\_coverage.png`



\## 4. Analysis



The code coverage run achieved 100% statement coverage. The branch coverage run also achieved 100% coverage, with all 28 reported branches covered and no partially covered branches.



These results meet the lab requirement of at least 90% coverage for both runs. The tests exercise the application's principal alert calculations, threshold boundaries, severity selection, empty input, and invalid alert handling.



\## 5. Conclusion



The Weather Alert application was tested using pytest and coverage.py. Both test runs achieved 100% reported coverage, exceeding the required minimum of 90%. The test files, terminal screenshots, and this analysis report are included as lab deliverables.



\*\*Note:\*\* Coverage results demonstrate which statements and branches were exercised by the tests; they do not prove the absence of every possible defect.



