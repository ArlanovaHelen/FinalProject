import json
import random
flag = True
send = 'Можливі операції:\nRATE – отримання поточного курсу (USD/UAH),\nAVAILABLE - отримання залишків за рахунками,\nBUY XXX - покупка xxx доларів.''\nSELL XXX - продаж доларів,\nBUY ALL – купівля доларів на всі можливі гривні,\nSELL ALL - продаж всіх доларів,\n''NEXT – отримати наступний курс,\nRESTART - розпочати гру з початку (з початковими умовами)'

print(send)
# with open("config2.json", 'r', encoding='utf-8') as input_file:
#     result1 = float(json.load(input_file)['UAH'])
#     uah = round(result1, 2)
#     print(uah)

while flag:
    class ImportData:
        def read_UAH():
            with open("config2.json", 'r', encoding='utf-8') as input_file:
                uah1 = float(json.load(input_file)['UAH'])
                uah = round(uah1, 2)
            return uah

        def read_USD():
            with open("config2.json", 'r', encoding='utf-8') as input_file:
                usd1 = float(json.load(input_file)['USD'])
                usd = round(usd1, 2)
            return usd

        def read_price():
            with open("config2.json", 'r', encoding='utf-8') as input_file:
                price1 = float(json.load(input_file)['price'])
                price = round(price1, 2)
            return price


    new_usd = ImportData.read_USD()
    new_uah = ImportData.read_UAH()
    new_price = ImportData.read_price()
    try:
        chose = input('Оберіть операцію: ')
        if chose == "RATE" or chose == "Rate" or chose == "rate":
            new_price1 = round(random.uniform(ImportData.read_price() - 0.5, ImportData.read_price() + 0.5), 2)
            print(new_price1)
            with open("config2.json", 'w') as input_file:
                json.dump({'price': float(f'{new_price1}'), 'UAH': float(f'{new_uah}'), 'USD': float(f'{new_usd}')},
                          input_file,
                          indent=1)
            with open("history.json", 'a') as input_file:
                json.dump({'price': float(f'{new_price1}'), 'UAH': float(f'{new_uah}'), 'USD': float(f'{new_usd}')},
                          input_file,
                          indent=1)
        elif chose == "restart" or chose == "RESTART" or chose == "Restart":
            with open("history.json", 'w', encoding='utf-8') as input_file:
                json.dump({'price': 36.00, 'UAH': 10000.00, 'USD': 0.00}, input_file, indent=1)
            with open("config2.json", 'w') as input_file:
                json.dump({'price': 36.00, 'UAH': 10000.00, 'USD': 0.00}, input_file, indent = 1)
            print("систему оновлено")
            #видалити дані з файлу history
            print(send)
        elif chose == "AVAILABLE" or chose == "Available" or chose == "available":
            available = f"Залишок у гривні: {new_uah}, \nЗалишок у доларі: {new_usd}"
            print(available)
        elif chose == "NEXT" or chose == "next" or chose == "Next":
            new_price1 = round(random.uniform(ImportData.read_price() - 0.5, ImportData.read_price() + 0.5), 2)
            print(new_price1)
            with open("config2.json", 'w') as input_file:
                json.dump({'price': float(f'{new_price1}'), 'UAH': float(f'{new_uah}'), 'USD': float(f'{new_usd}')},
                          input_file,
                          indent=1)
            with open("history.json", 'a') as input_file:
                json.dump({'price': float(f'{new_price1}'), 'UAH': float(f'{new_uah}'), 'USD': float(f'{new_usd}')},
                          input_file,
                          indent=1)
        elif chose == "BUY ALL" or chose == "buy all" or chose == "Buy all":
            result1 = round(float(new_uah)/float(new_price), 2)
            result = round(result1+ float(new_usd), 2)
            print(result)
            with open("config2.json", 'w') as input_file:
                json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{0:00}'), 'USD': float(f'{result}')},
                          input_file,
                          indent=1)
            with open("history.json", 'a') as input_file:
                json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{0:00}'), 'USD': float(f'{result}')},
                          input_file,
                          indent=1)
            print(f"Ви придбали: {result1} доларів")
        elif chose == "SELL ALL" or chose == "sell all" or chose == "Sell all":
            result1 = round(float(new_usd) * float(new_price), 2)
            result = round(result1 + float(new_uah), 2)
            print(result)

            with open("config2.json", 'w') as input_file:
                json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{result}'), 'USD': float(f'{0:00}')},
                          input_file,
                          indent=1)
            with open("history.json", 'a') as input_file:
                json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{result}'), 'USD': float(f'{0:00}')},
                          input_file,
                          indent=1)
            print(f"Ви продали: {new_usd} доларів")
        elif chose.startswith("BUY ") or chose.startswith("Buy ") or chose.startswith("buy "):
            sum = chose[4:len(chose)]
            print(sum)
            result = round(float(sum)*float(new_price),2)
            print(result)

            if new_uah < result:
                print(f"UNAVAILABLE, REQUIRED BALANCE UAH {result}, AVAILABLE {new_uah}")
            else:
                last_uah = round(float(new_uah) - result, 2)
                last_usd = round(float(sum) + float(new_usd), 2)
                with open("config2.json", 'w') as input_file:
                    json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{last_uah}'), 'USD': float(f'{last_usd}')},
                              input_file,
                              indent=1)
                with open("history.json", 'a') as input_file:
                    json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{last_uah}'), 'USD': float(f'{last_usd}')},
                        input_file,
                        indent=1)
                print(f"You bought {sum} dollars")
        elif chose.startswith("SELL ") or chose.startswith("Sell ") or chose.startswith("sell "): #якщо після цифр букви
            sum = float(chose[4:len(chose)])
            print(sum)
            result = round(float(sum)*float(new_price), 2)
            print(result)

            if new_usd < sum:
                print(f"UNAVAILABLE, REQUIRED BALANCE USD {sum}, AVAILABLE {new_usd}")
            else:
                last_uah = round(float(new_uah) + result, 2)
                last_usd = round(float(new_usd) - sum, 2)
                with open("config2.json", 'w') as input_file:
                    json.dump({'price': float(f'{new_price}'), 'UAH': float(f'{last_uah}'), 'USD': float(f'{last_usd}')}, input_file,
                              indent=1)
                with open("history.json", 'a', encoding='utf-8') as input_file:
                    json.dump(
                        {'price': float(f'{new_price}'), 'UAH': float(f'{last_uah}'), 'USD': float(f'{last_usd}')},
                        input_file,
                        indent=1)
                print(f"You solt {sum} dollars")
        else:
            print("Ви обрали не корректну операцію, спробуйте ще")
    except ValueError:
        print('Ви ввели не число!')