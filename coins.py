coin_sum = float(input())
coin_sum = int(coin_sum * 100)
coins_counter = 0
coins_counter += coin_sum // 200
coin_sum %= 200
coins_counter += coin_sum // 100
coin_sum %= 100
coins_counter += coin_sum // 50
coin_sum %= 50
coins_counter += coin_sum // 20
coin_sum %= 20
coins_counter += coin_sum // 10
coin_sum %= 10
coins_counter += coin_sum // 5
coin_sum %= 5
coins_counter += coin_sum // 2
coin_sum %= 2
coins_counter += coin_sum // 1
coin_sum %= 1

print(coins_counter)
