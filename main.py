import  Food_donation_system_database
from login import login 
from donor import add_donor
from donation import add_donation, check_expired_food
from reports import donation_report
from recipient import add_recipient
from crud import view_donors,update_donor,delete_donor

if not login():
    exit()


while True: 
    print("\n =========================")
    print("Food Donation Management")
    print("============================")
    print("1.Add Donor")
    print("2.Add Donation")
    print("3.Register Recipient")
    print("4.View Donors")
    print("5.Search Donor")
    print("6.Update Donor")
    print("7.Delete Donor")
    print("8.Check Expired food")
    print("9.Donation Report")
    print("10.Exit")
          

    choice = input("Choose Option:")

    if choice == "1":
        add_donor()

    elif choice == "2":
        add_donation() 

    elif choice == "3":
        add_recipient()

    elif choice == "4":
        view_donors()
        
    elif choice =="5":
        search_donor()

    elif choice =="6":
        update_donor()

    elif choice =="7":
        delete_donor() 

    elif choice =="8":
        check_expired_food()

    elif choice =="9":
        donation_report()
 
    elif choice =="10":
        print("Thank you.")
        break  
      

    else:
        print("invalid choice")
