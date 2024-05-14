import os
from googletrans import Translator, constants

translator = Translator()
# note: for the translator, i used both the google translator from browser and the one from python package(i.e googletrans).
class ATM:
    def __init__(self, option):
        self.option = option
        self.balance = 1000. 

    def display_welcome_screen(self):
        if self.option == "1":
            print("\nwelcome to our ATM!")
        elif self.option == "2":
            print("\nnabata na ATM anyị!")
        elif self.option == "3":
            print("\nbarka da zuwa ATM din mu!")
        elif self.option == "4":
            print("\nkaabo si ATM wa!")
        else:
            print("Invalid choice of option! try again.")
            

    def check_account_balance(self):
        if self.option == "1":
            print(f"your current balance is {self.balance} NGN")
            print("will you like to continue?")
            print("""
                        1. YES.
                        2. NO
                    """)
            select_option = input("Enter the option>")
            if select_option == "1":
                print("will you like to print transaction slip?")
                print("""
                        1. To display menu.
                        2. To print transaction slip.
            """)
            input_option = input("enter your option here>>")
            if input_option == "2":
                self.run()
            elif input_option == "2":
                self.print_transaction_slip()
                print("will you like to continue?")
                print("""
                        1. YES.
                        2. NO
            """)
            select_option2 = input("Enter the option>")
            if select_option2 == "1":
                self.run()
            elif select_option2 == "2":
                self.cancel_and_exit()

            elif select_option == "2":
                self.cancel_and_exit()


        elif self.option == "2":
            print(f"gị ugbu a itule bụ {self.balance} NGN")
            translation = translator.translate("\nwill you like to continue?", dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            options_1 = {
                "1": "YES",
                "2": "No"
            }
            translation = translator.translate(options_1, dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            select_option = input("Tinye nhọrọ>")
            translation = translator.translate(select_option, dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            if select_option == "1":
                translation = translator.translate("will you like to print transaction slip?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_2 = {
                    "1": "To display menu",
                    "2": "To print transaction slip"
                }
            translation = translator.translate(options_2, dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            input_option = input("tinye nhọrọ gị ebe a>>")
            translation = translator.translate(input_option, dest="Igbo")
            if input_option == "1":
                self.run() 
            elif input_option == "2":
                self.print_transaction_slip()
                translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
            translation = translator.translate(options_1, dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            select_option2 = input("Tinye nhọrọ>")
            translation = translator.translate(select_option2, dest="Igbo")
            print(f"{translation.text} ({translation.dest})")
            if select_option2 == "1":
                self.run()
            elif select_option2 == "2":
                self.cancel_and_exit()
            elif select_option == "2":
                self.cancel_and_exit()

        elif self.option == "3":
            print(f"Ma'aunin ku na yanzu shine {self.balance} NGN")
            print("\nza ku so ku yi ƙarin ayyuka?")
            translation = translator.translate("\nwill you like to continue?", dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            options_1 = {
                "1": "YES",
                "2": "No"
            }
            translation = translator.translate(options_1, dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            select_option = input("Shigar da zaɓi>")
            translation = translator.translate(select_option, dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            if select_option == "1":
                translation = translator.translate("will you like to print transaction slip?", dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                options_2 = {
                    "1": "To display menu",
                    "2": "To print transaction slip"
                }
            translation = translator.translate(options_2, dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            input_option = input("shigar da zabin ku a nan>>")
            translation = translator.translate(input_option, dest="Hausa")
            if input_option == "1":
                self.run() 
            elif input_option == "2":
                self.print_transaction_slip()
                translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
            translation = translator.translate(options_1, dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            select_option2 = input("Shigar da zaɓi>")
            translation = translator.translate(select_option2, dest="Hausa")
            print(f"{translation.text} ({translation.dest})")
            if select_option2 == "1":
                self.run()
            elif select_option2 == "2":
                self.cancel_and_exit()
            elif select_option == "2":
                self.cancel_and_exit()  


        elif self.option == "4":
            print(f"iwontunwonsi rẹ lọwọlọwọ jẹ {self.balance} NGN")
            translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            options_1 = {
                "1": "YES",
                "2": "No"
            }
            translation = translator.translate(options_1, dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            select_option = input("Tẹ aṣayan sii>")
            translation = translator.translate(select_option, dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            if select_option == "1":
                translation = translator.translate("will you like to print transaction slip?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_2 = {
                    "1": "To display menu",
                    "2": "To print transaction slip"
                }
            translation = translator.translate(options_2, dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            input_option = input("tẹ aṣayan rẹ nibi>>")
            translation = translator.translate(input_option, dest="Yoruba")
            if input_option == "1":
                self.run()
            elif input_option == "2":
                self.print_transaction_slip()
                translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
            translation = translator.translate(options_1, dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            select_option2 = input("Tẹ aṣayan sii>")
            translation = translator.translate(select_option2, dest="Yoruba")
            print(f"{translation.text} ({translation.dest})")
            if select_option2 == "1":
                self.run()
            elif select_option2 == "2":
                self.cancel_and_exit()
            elif select_option == "2":
                self.cancel_and_exit()              
            
    def withdraw_money(self):
        if self.option == "1":
            amount = float(input("please enter the amount: "))
        elif self.option == "2":
            amount = float(input("biko banye ọnụego ahụ: "))
        elif self.option == "3":
            amount = float(input("da fatan za a shiga adadin: "))
        elif self.option == "4":
            amount = float(input("jọwọ wọle oye: "))

        if amount > self.balance:
            if self.option == "1":
                print("Insufficient funds!")
                print("will you like to continue?")
                print("""
                        1. YES.
                        2. NO
                    """)
                select_option = input("Enter the option>")
                if select_option == "1":
                    print("will you like to print transaction slip?")
                    print("""
                            1. To display menu.
                            2. To print transaction slip.
                """)
                input_option = input("enter your option here>>")
                if input_option == "2":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    print("will you like to continue?")
                    print("""
                            1. YES.
                            2. NO
                """)
                select_option2 = input("Enter the option>")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()

                elif select_option == "2":
                    self.cancel_and_exit()

            elif self.option == "2":
                print("Ego ezughi oke!")
                translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tinye nhọrọ>")
                translation = translator.translate(select_option, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tinye nhọrọ gị ebe a>>")
                translation = translator.translate(input_option, dest="Igbo")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tinye nhọrọ>")
                translation = translator.translate(select_option2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()

            elif self.option == "3":
                print("Rashin isassun kuɗi!")
                translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Shigar da zaɓi>")
                translation = translator.translate(select_option, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                        translation = translator.translate("will you like to print transaction slip?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_2 = {
                            "1": "To display menu",
                            "2": "To print transaction slip"
                        }
                translation = translator.translate(options_2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("shigar da zabin ku a nan>>")
                translation = translator.translate(input_option, dest="Hausa")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                        self.print_transaction_slip()
                        translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_1 = {
                            "1": "YES",
                            "2": "No"
                        }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Shigar da zaɓi>")
                translation = translator.translate(select_option2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                        self.run()
                elif select_option2 == "2":
                        self.cancel_and_exit()
                elif select_option == "2":
                        self.cancel_and_exit()  


            elif self.option == "4":
                print("Awọn owo ti ko to!")
                translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tẹ aṣayan rẹ nibi>>")
                translation = translator.translate(input_option, dest="Yoruba")
                if input_option == "1":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()              
                
                
        else:
            self.balance -= amount
            if self.option == "1":
                print(f"Withdrawal successful!. your new account balance is {self.balance} NGN")
                print("will you like to continue?")
                print("""
                        1. YES.
                        2. NO
                    """)
                select_option = input("Enter the option>")
                if select_option == "1":
                    print("will you like to print transaction slip?")
                    print("""
                            1. To display menu.
                            2. To print transaction slip.
                """)
                input_option = input("enter your option here>>")
                if input_option == "2":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    print("will you like to continue?")
                    print("""
                            1. YES.
                            2. NO
                """)
                select_option2 = input("Enter the option>")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()

                elif select_option == "2":
                    self.cancel_and_exit()

                
            elif self.option == "2":
                print(f"Mwepụ gara nke ọma!. nkwụnye ego akaụntụ ọhụrụ gị bụ {self.balance} NGN")
                translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tinye nhọrọ>")
                translation = translator.translate(select_option, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tinye nhọrọ gị ebe a>>")
                translation = translator.translate(input_option, dest="Igbo")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tinye nhọrọ>")
                translation = translator.translate(select_option2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()

            elif self.option == "3":
               print(f"Janye nasara!. Ma'auni na sabon asusun ku shine {self.balance} NGN")
               translation = translator.translate("\nwill you like to continue?", dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               options_1 = {
                    "1": "YES",
                    "2": "No"
                }
               translation = translator.translate(options_1, dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               select_option = input("Shigar da zaɓi>")
               translation = translator.translate(select_option, dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Hausa")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
               translation = translator.translate(options_2, dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               input_option = input("shigar da zabin ku a nan>>")
               translation = translator.translate(input_option, dest="Hausa")
               if input_option == "1":
                   self.run() 
               elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
               translation = translator.translate(options_1, dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               select_option2 = input("Shigar da zaɓi>")
               translation = translator.translate(select_option2, dest="Hausa")
               print(f"{translation.text} ({translation.dest})")
               if select_option2 == "1":
                    self.run()
               elif select_option2 == "2":
                    self.cancel_and_exit()
               elif select_option == "2":
                    self.cancel_and_exit()  

            elif self.option == "4":
                print(f"Yiyọ kuro ni aṣeyọri!. titun àkọọlẹ rẹ iwontunwonsi ni {self.balance} NGN")
                translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tẹ aṣayan rẹ nibi>>")
                translation = translator.translate(input_option, dest="Yoruba")
                if input_option == "1":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()              
                
    def Transfer_money(self):
        if self.option == "1":
            amount = float(input("please enter the amount to transfer: "))
            recipient = input("please enter the recipient's account number: ")
        elif self.option == "2":
            amount = float(input("biko tinye ego ị ga-ebufe: "))
            recipient = input("biko tinye nọmba akaụntụ onye nnata: ")
        elif self.option == "3":
            amount = float(input("da fatan za a shigar da adadin don canja wuri: "))
            recipient = input("da fatan za a shigar da lambar asusun mai karɓa: ")
        elif self.option == "4":
            amount = float(input("jọwọ tẹ iye lati gbe: "))
            recipient = input("jọwọ tẹ nọmba akọọlẹ olugba naa sii: ")

        if amount > self.balance:
            if self.option == "1":
                print("Insufficient funds!")
                print("will you like to continue?")
                print("""
                        1. YES.
                        2. NO
                    """)
                select_option = input("Enter the option>")
                if select_option == "1":
                    print("will you like to print transaction slip?")
                    print("""
                            1. To display menu.
                            2. To print transaction slip.
                """)
                input_option = input("enter your option here>>")
                if input_option == "2":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    print("will you like to continue?")
                    print("""
                            1. YES.
                            2. NO
                """)
                select_option2 = input("Enter the option>")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()

                elif select_option == "2":
                    self.cancel_and_exit()


            elif self.option == "2":
                print("Ego ezughi oke!")
                translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tinye nhọrọ>")
                translation = translator.translate(select_option, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tinye nhọrọ gị ebe a>>")
                translation = translator.translate(input_option, dest="Igbo")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tinye nhọrọ>")
                translation = translator.translate(select_option2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()

            elif self.option == "3":
                print("Rashin isassun kuɗi!")
                translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Shigar da zaɓi>")
                translation = translator.translate(select_option, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                        translation = translator.translate("will you like to print transaction slip?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_2 = {
                            "1": "To display menu",
                            "2": "To print transaction slip"
                        }
                translation = translator.translate(options_2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("shigar da zabin ku a nan>>")
                translation = translator.translate(input_option, dest="Hausa")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                        self.print_transaction_slip()
                        translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_1 = {
                            "1": "YES",
                            "2": "No"
                        }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Shigar da zaɓi>")
                translation = translator.translate(select_option2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                        self.run()
                elif select_option2 == "2":
                        self.cancel_and_exit()
                elif select_option == "2":
                        self.cancel_and_exit()  


            elif self.option == "4":
                print("Awọn owo ti ko to!")
                translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tẹ aṣayan rẹ nibi>>")
                translation = translator.translate(input_option, dest="Yoruba")
                if input_option == "1":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()              
                
        else:
            self.balance -= amount
            if self.option == "1":
                print(f"Transfer of {amount} to {recipient} was successful!.")
                print(f"Transfer successful!. your account balance is {self.balance} NGN")
                print("will you like to continue?")
                print("""
                        1. YES.
                        2. NO
                    """)
                select_option = input("Enter the option>")
                if select_option == "1":
                    print("will you like to print transaction slip?")
                    print("""
                            1. To display menu.
                            2. To print transaction slip.
                """)
                input_option = input("enter your option here>>")
                if input_option == "2":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    print("will you like to continue?")
                    print("""
                            1. YES.
                            2. NO
                """)
                select_option2 = input("Enter the option>")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()

                elif select_option == "2":
                    self.cancel_and_exit()


            elif self.option == "2":
                print(f"Nyefee nke {amount} ka {recipient} mere nke ọma!.")
                print(f"Nyefee gara nke ọma!. akaụntụ gị itule bụ {self.balance} NGN")
                translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tinye nhọrọ>")
                translation = translator.translate(select_option, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tinye nhọrọ gị ebe a>>")
                translation = translator.translate(input_option, dest="Igbo")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Igbo")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tinye nhọrọ>")
                translation = translator.translate(select_option2, dest="Igbo")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()

            elif self.option == "3":
                print(f"Canja wurin {amount} ku {recipient} ya yi nasara!.")
                print(f"Canja wurin yayi nasara!. Ma'auni na asusun ku shine {self.balance} NGN")
                translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Shigar da zaɓi>")
                translation = translator.translate(select_option, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                        translation = translator.translate("will you like to print transaction slip?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_2 = {
                            "1": "To display menu",
                            "2": "To print transaction slip"
                        }
                translation = translator.translate(options_2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("shigar da zabin ku a nan>>")
                translation = translator.translate(input_option, dest="Hausa")
                if input_option == "1":
                    self.run() 
                elif input_option == "2":
                        self.print_transaction_slip()
                        translation = translator.translate("\nwill you like to continue?", dest="Hausa")
                        print(f"{translation.text} ({translation.dest})")
                        options_1 = {
                            "1": "YES",
                            "2": "No"
                        }
                translation = translator.translate(options_1, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Shigar da zaɓi>")
                translation = translator.translate(select_option2, dest="Hausa")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                        self.run()
                elif select_option2 == "2":
                        self.cancel_and_exit()
                elif select_option == "2":
                        self.cancel_and_exit()  

            elif self.option == "4":
                print(f"Gbigbe ti{amount} si {recipient} je aseyori!.")
                print(f"Gbigbe ni aṣeyọri!. iwontunwonsi àkọọlẹ rẹ ni {self.balance} NGN")
                translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                options_1 = {
                    "1": "YES",
                    "2": "No"
                }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option == "1":
                    translation = translator.translate("will you like to print transaction slip?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_2 = {
                        "1": "To display menu",
                        "2": "To print transaction slip"
                    }
                translation = translator.translate(options_2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                input_option = input("tẹ aṣayan rẹ nibi>>")
                translation = translator.translate(input_option, dest="Yoruba")
                if input_option == "1":
                    self.run()
                elif input_option == "2":
                    self.print_transaction_slip()
                    translation = translator.translate("\nwill you like to continue?", dest="Yoruba")
                    print(f"{translation.text} ({translation.dest})")
                    options_1 = {
                        "1": "YES",
                        "2": "No"
                    }
                translation = translator.translate(options_1, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                select_option2 = input("Tẹ aṣayan sii>")
                translation = translator.translate(select_option2, dest="Yoruba")
                print(f"{translation.text} ({translation.dest})")
                if select_option2 == "1":
                    self.run()
                elif select_option2 == "2":
                    self.cancel_and_exit()
                elif select_option == "2":
                    self.cancel_and_exit()              
                

    def print_transaction_slip(self):
            file_name = "transaction_slip.txt"
            if self.option == "1":
                transaction_details = f"Transaction: Balance check\naccount Balance: {self.balance} NGN"
                
            elif self.option == "2":
                transaction_details = f"Azumahia: Nyochaa nha nha\nakauntu Nhazi: {self.balance} NGN"
                
            elif self.option == "3":
                transaction_details = f"Ma'amala: Duban ma'auni\nasusu Ma'auni: {self.balance} NGN"
                
            elif self.option == "4":
                transaction_details = f"Idunadura: Ayewo iwontunwonsi\niroyin Iwontunwonsi: {self.balance} NGN"
                
            with open(os.path.join(os.path.expanduser("~"), "Documents", file_name), "w") as file:
                file.write(transaction_details)
                if self.option == "1":
                    print(f"Transaction slip printed and saved as {file_name}")
                    
                elif self.option == "2":
                    print(f"Ebiputara ma chekwaa akwukwo azumahia di ka {file_name}")
                    
                elif self.option == "3":
                    print(f"An buga ma'amalar ciniki kuma an adana shi azaman {file_name}")
                    
                elif self.option == "4":
                    print(f"Titejade isokuso isowo ati fipamo bi {file_name}")
                    
    def cancel_and_exit(self):
        if self.option == "1":
            print("Thank you for using our ATM")
        elif self.option == "2":
            print("Daalụ maka iji ATM anyị")
        elif self.option == "3":
            print("Mun gode da amfani da ATM ɗin mu")
        elif self.option == "4":
            print("O ṣeun fun lilo ATM wa")
            exit()
        

    def run(self):
        self.display_welcome_screen()
        
        while True:
            if self.option == "1":
                print("\nwhat would you like to do?")
                print("1. check account balance.")
                print("2. withdraw money.")
                print("3. Transfer money.")
                
            elif self.option == "2":
                print("\nkedu ihe ga-amasị gị ime?")
                print("1. lelee nguzozi akaụntụ")
                print("2. wepụ ego")
                print("3. nyefee ego")
                
            elif self.option == "3":
                print("\nme kuke so kuyi?")
                print("1. duba ma'auni")
                print("2. cire kudi")
                print("3. Canja wurin kuɗi")
                
            elif self.option == "4":
                print("\nKí l'ó wù ẹ láti ṣe?")
                print("1. ṣayẹwo iwontunwonsi iroyin")
                print("2. yọ owo kuro")
                print("3. owo gbigbe")
                print("4. tẹjade idunadura isokuso ")
                print("5. fagilee ati jade")

            if self.option == "1":
                choice = input("please enter your corresponding choice> ")
                
            elif self.option == "2":
                choice = input("biko tinye nhọrọ gị kwekọrọ> ")
            elif self.option == "3":
                choice = input("don Allah shigar da daidai zabinku> ")
            elif self.option == "4":
                choice = input("jọwọ tẹ rẹ ti o baamu wun> ")

            if choice == "1":
                self.check_account_balance()
                break
            elif choice == "2":
                self.withdraw_money()
                break
            elif choice == "3":
                self.Transfer_money()
                break
            
            else:
                if self.option == "1":
                    print("Invalid choice! please try again")
                elif self.option == "2":
                    print("Nhọrọ ezighi ezi! biko nwaa ọzọ")
                elif self.option == "3":
                    print("Zaɓin mara inganci! da fatan za a sake gwadawa")
                elif self.languahe == "4":
                    print("Yiyan aiṣedeede! Jọwọ gbiyanju lẹẹkansi")
                        
# detecting operating system to determine Documents folder path

if os.name == "nt":
    default_option = "1"
elif os.name == "posix":
    default_option = "1"
else:
      default_option = "1"
print("\nWELCOME TO OUR ATM!")

option = input("""\nPlease enter your prefered language option:
               
1. English.
2. Igbo.
3. Hausa.
4. Yoruba.            
Enter the option here>>> """)
if option not in ["1", "2", "3", "4"]:
    print("Invalid option selected. Using default option(1)")
    option = default_option



# run the ATM programe
atm = ATM(option)
atm.run()


       

