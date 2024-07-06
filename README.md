    # Currrency.py
    #### Video Demo:  https://youtu.be/FwzK3-bviAI
    #### Description:
    The thing from CS50P that stuck out most to me was using APIS and how diffent applications can use the internet to send data to each other so I would like to intergrate that in my project. In addition I am plnning several overseas trips and the currency conversion has been a hassel for me. So i decided to wite a programme with a CLI interface to help me with this problem.

    I first started the porject with writting psudocode on how I want the flow of the programe to go. I wanted to user to be promted for the currency they currently have, then the amount they have in that currency, and lastly the cuurency they want to convert to. 

    I then started writting the main funtion and the basic funtions to match the control flow of the programme. I did not writeout the logic of the funtions yet, just the skeleton of the project.

    def main():
    old_currency = get_old_currency()
    money = get_money()
    new_currency = get_new_currency()
    conversion_rate = get_converstion_rate(old_currency, new_currency)
    print(f"${new_currency * conversion_rate} {new_currency}")

    There are four main funtions in my program that match the control flow I wanted. the first function is the get_old_currency which i plan to prompt the user for the currency they currently have and check in the input is a valid currency.

    The second function is the get money which promts the user for a valid float with at most 2 decimal places.

    The third function is the get_new_currency which I plan to prompt the user for the currency they want to convert to and and check if the input is a valid currency. I then realise that the get_old_currency and get_new currency serves the same function and thus i just made a function called get_currency instead.

    The last function I planned for is the get exchange rate which the backbone of the whole project. I did not know how or which API to implement yet so i initially made it return a arbitary value of 2 to make sure the rest of my code worked as intended first. I then went online and searched for a api that can get me the exchage rates. I found a free api called freecurrenciesapi i installed the freecurrencies api package using pip and read the doucmentation. I created the client object from the package. I then decided to use 2 methods from the freecurrentciesapi, the .currenceies() method to get a list of all the available currecies which will be used in the get_currencies method to check for a valid currency. I also used the .latest() method to get the latest exchange rate. I did some logic/math to calculate the value of the currency exchaged and then printed too data to the CLI. The data requested from the api was sent over in a dictionary of dictionaries. In order the access the values needed i uesed the square bracket notation to access the key value pairs.

    Lastly I wanted to add a initial messgae at the start of the program to show the users the supported currency. Using a for loop, I created a datastructure of a list of dictionaries with the keys "supported currencies" and "symbol". I then used the tablulate module to print to data structure in the CLI in a table format which is displayed to the user. 

    I then stared on the test_currency_converter.py. There we 2 main functions that were important to the logic of my code. The is_valid_currency function and the api. I the testing case for the is_valid_currency funtions are quite simple to write.

    I did not know how to chck if an the api is working. After abit of research, i found out that if a api request is sucessful, the status code of 200 will be sent out. So I imported the requests library and used the .status method. This paired with the arrest statment allowed me to check if the curretcies and latest request were working. I then implemnted that in my test file.