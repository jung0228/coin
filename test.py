import pyupbit

access = "kaxYSLkbki2c8xebBsxQk7koZI1nPitguolfS5x1"
secret = "FCucsnp1rUhMyIIheCPVJIwfRlxADMllwPnzRGey"

upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))
print(upbit.get_balance("KRW"))
