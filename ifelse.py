from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# brew install chromedriver
# spctl --add --label 'Approved' /usr/local/bin/chromedriver

def izvelne(sep = False):
    if (sep == True):
        print('')

    print("Ievadi 1: Bonda uzdevums.")
    print("Ievadi 2: Pāra nepāra uzdevums.")
    print("Ievadi 3: Vērtējuma uzdevums.")
    print("Ievadi 4: Gāzes uzdevums.")
    print("Ievadi x: Iziet.")
    return input("Darbība: ")

izvele = izvelne()

while True:
    if izvele == '1':
        vards = input('Ievadi savu vārdu: ')
        if (vards == 'Bond'):
            print('Esi sveicināts, 007!')
        else:
            print('Sveicināti,', vards + '!')
        izvele = izvelne(True)
    
    elif izvele == '2':
        skaitlis = int(input('Ievadi skaitli: '))
        if (skaitlis % 2 == 0):
            print('Skaitlis', skaitlis, 'ir pāra skaitlis, jo dalās ar divi.')
        else:
            print('Skaitlis', skaitlis, 'ir nepāra skaitlis, jo nedalās ar divi.')
        izvele = izvelne(True)

    elif izvele == '3':
        vertejums = int(input('Ievadi vērtējumu: '))
        if (vertejums <= 3):
            print('Tu vari labāk, zems vērtējums.')
        elif (vertejums <= 5):
            print('Gandrīz labi.')
        elif (vertejums <= 7):
            print('Labs vērtējums.')
        elif (vertejums <= 9):
            print('Ļoti labs vērtējums.')
        elif (vertejums > 9):
            print('Izcili, izcili!')
        izvele = izvelne(True)
    
    elif izvele == '4':
        kWh = int(input('Ievadi kWh: '))
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome('chromedriver', options=options)
        url = "https://lg.lv/majoklim/tarifi-un-kalkulators"
        driver.get(url)
        print("Lūdzu uzgaidiet, iegūstam informāciju…")

        # izvēlamies kWh dropdownā
        dropdown = driver.find_element_by_xpath("/html/body/div/div[2]/main/div[4]/div/div[1]/div[3]/div[1]/div[5]/div[2]/select")
        dropdown.send_keys('kwh')

        # norādam mūsu kWh vērtību
        kWhweb = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[3]/div[1]/div[5]/div[1]/div[1]/input")
        kWhweb.send_keys(kWh)

        rezultats = driver.find_element_by_xpath("/html/body/div[2]/div[2]/main/div[4]/div/div[1]/div[4]/div[2]/div[1]/div[1]").text
        print("Jūsu izmaksas būtu", rezultats, "EUR/mēn.")

    elif izvele == 'x':
        break
