def create_account(name : str, holder : str , account_holders : list = []):
    account_holders.append(holder)
    print(id(account_holders))
    return {
        'name': name,
        'maim_account_holder' : holder,
        'accouny_holders': account_holders
    }

a1 = create_account('checking', 'ayush')
a2 = create_account('savings' , 'prabha')

print(a2)

def create_account_without_default_parameters(name : str, holder : str , account_holders = None ):
    if not account_holders:
        account_holders = []
    account_holders.append(holder)
    print(id(account_holders))
    return {
        'name': name,
        'main_account_holder' : holder,
        'account_holders': account_holders
    }
a3 = create_account_without_default_parameters('checking','aditya')
a4 = create_account_without_default_parameters('fixed_deposit', 'ashish')

print(a3)
print(a4)