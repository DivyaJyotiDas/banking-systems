Overview
================

1. This Code demonstrates Small Banking Application Demo using clean Architecture.
2. Focusses on Library Design. Layers of clean Architectures Implementation.
3. It has Domain or Entity Layer, Use_Case Layers, Gateways, and External Layers(File Based) aswell

Installing from Source
-------------------------
1. git clone https://github.com/DivyaJyotiDas/banking-systems.git -b d.das/feature/core-implementation
2. cd banking-systems
3. virtualenv -p python3 .venv ---> Create virtualenv
4. source .venv/bin/activate ---> Activate Virtualenv.
5. pip install -r requirements/dev.txt ---> Install Dependancies.
6. pytest -svv --cov --cov-report=term-missing ---> Check for Test cases and coverage.

   ---------- coverage: platform darwin, python 3.12.1-final-0 ----------
Name                                                                          Stmts   Miss  Cover   Missing
-----------------------------------------------------------------------------------------------------------
__init__.py                                                                       0      0   100%
banking_system/__init__.py                                                        0      0   100%
banking_system/domain/__init__.py                                                 0      0   100%
banking_system/domain/account.py                                                 16      5    69%   20, 28, 40, 48, 53
banking_system/domain/customer.py                                                13      1    92%   26
banking_system/repository/__init__.py                                             0      0   100%
banking_system/repository/base.py                                                14      4    71%   7, 11, 15, 19
banking_system/repository/filerepo.py                                            43      9    79%   17-18, 22-23, 35-36, 41-42, 51
banking_system/use_cases/__init__.py                                              0      0   100%
banking_system/use_cases/create_accounts/__init__.py                              0      0   100%
banking_system/use_cases/create_accounts/create_accounts_usecase.py               6      0   100%
banking_system/use_cases/transactions/__init__.py                                 0      0   100%
banking_system/use_cases/transactions/make_transactions_usecase.py               17      1    94%   32
tests/__init__.py                                                                 0      0   100%
tests/domain/__init__.py                                                          0      0   100%
tests/domain/test_account.py                                                      0      0   100%
tests/domain/test_all_scenario.py                                                24      5    79%   44-58
tests/domain/test_customer.py                                                     0      0   100%
tests/use_cases/__init__.py                                                       0      0   100%
tests/use_cases/create_accounts/__init__.py                                       0      0   100%
tests/use_cases/create_accounts/test_create_accounts_usecase.py                   5      2    60%   3, 6
tests/use_cases/create_accounts/test_generate_accounts_statement_usecase.py       5      2    60%   3, 6
tests/use_cases/transactions/__init__.py                                          0      0   100%
tests/use_cases/transactions/test_make_transactions_usecase.py                    5      2    60%   3, 6
-----------------------------------------------------------------------------------------------------------
TOTAL                                                                           148     31    79%
