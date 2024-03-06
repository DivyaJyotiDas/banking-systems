import threading
from banking_system.use_cases.transactions.make_transactions_usecase import TransactionUseCase


def test_deposit_account_when_amount_positive():
    transx_obj = TransactionUseCase(
                        account_id='25c50326-5411-49bf-a585-bbcf760d8d9e', 
                        transaction_type='deposit').make_transaction(amount=500)
    
    assert transx_obj is None


    transx_obj = TransactionUseCase(
                        account_id='25c50326-5411-49bf-a585-bbcf760d8d9e', 
                        transaction_type='withdraw').make_transaction(amount=200)
    
    assert transx_obj is None

    def test_deposit_and_withdraw_when_multiple_theads_should_avoid_race_condition():
        threads = []
        def test_deposit_thread_race_condition(account_id, tranx_type, amount):
            obj = TransactionUseCase(
                        account_id=account_id, 
                        transaction_type=tranx_type).make_transaction(amount=amount)
            obj['customer_balance'] == 1000
            
        def test_withdrawl_thread_race_condition(account_id, tranx_type, amount):
            TransactionUseCase(
                        account_id=account_id, 
                        transaction_type=tranx_type).make_transaction(amount=amount)
        for _ in range(2):
            t_deposit = threading.Thread(target=test_deposit_thread_race_condition, args=('25c50326-5411-49bf-a585-bbcf760d8d9e',
                                                                                          'deposit', 1000))
            threads.append(t_deposit)
        for _ in range(2):
            t_withdraw= threading.Thread(target=test_deposit_thread_race_condition, args=('25c50326-5411-49bf-a585-bbcf760d8d9e',
                                                                                          'withdraw', 100))
            threads.append(t_withdraw)

        for _ in range(8):
            threads[_].start()
        
                


