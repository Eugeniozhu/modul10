import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f"Запрос на {amount}")

            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

# Создаём объект класса Bank
bk = Bank()

# Создаём два потока для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ждём завершения потоков
th1.join()
th2.join()

# Итоговый баланс
print(f'Итоговый баланс: {bk.balance}')
