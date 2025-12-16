from database import initialize_db
from models import *

def main():
    initialize_db()

    while True:
        print("\n================WARDROBE MANAGER================")
        print("1. ADD ITEM")
        print("2. SHOW ITEMS")
        print("3. DELETE ITEM")
        print("4. UPDATE ITEM")
        print("5. SEARCH BY NAME")
        print("6. SUGGEST OUTFIT")
        print("7. EXIT")

        ch=int(input("ENTER YOUR CHOICE: "))
        if ch==1:
            name=input("ENTER NAME OF THE ITEM: ")
            category=input("ENTER CATEGORY OF THE ITEM: ")
            color=input("ENTER COLOR OF THE ITEM: ")
            season=input("ENTER THE SEASON YOU CAN WEAR THE ITEM: ")
            occasion=input("ENTER OCCASION OF THE ITEM: ")
            add_items(name,category,color,season,occasion)
            print("ITEM ADDED!!")
        elif ch==2:
            items=list_items()
            if not items:
                print("YOUR WARDROBE IS EMPTY!!")
            else:
                print("\n------------------YOUR ITEMS--------------------")
                for item in items:
                    print(f"ID: {item[0]}")
                    print(f"NAME: {item[1]}")
                    print(f"CATEGORY: {item[2]}")
                    print(f"COLOR: {item[3]}")
                    print(f"SEASON: {item[4]}")
                    print(f"OCCASION: {item[5]}")
                    print(f"IMAGE: {item[6]}")
                    print("-------------------------------------------------")
        elif ch==3:
            id=int(input("ENTER THE ID YOU WANT TO DELETE: "))
            items=list_items()
            found=False
            for item in items:
                if item[0]==id:
                    found=True
                    delete_items(id)
                    print("ITEM DELETED!!")
            if not found:
                print("INVALID ID!!") 
        elif ch==4:
            id=int(input("ENTER THE ID YOU WANT TO UPDATE: "))
            items=list_items()
            found=False
            for item in items:
                if item[0]==id:
                    found=True
                    name=input("ENTER THE NEW NAME: ")
                    category=input("ENTER THE NEW CATEGORY: ")
                    color=input("ENTER THE NEW COLOR: ")
                    season=input("ENTER THE NEW SEASON: ")
                    occasion=input("ENTER THE NEW OCCASION: ")
                    update_item(name,category,color,season,occasion,id)
                    print("ITEM UPDATED!!")
                    break
            if not found:
                print("INVALID ID!!")
        elif ch==5:
            name=input("ENTER NAME KEYWORD: ")
            record=search_name(name)
            print("\n------------------YOUR ITEMS--------------------")
            for item in record:
                print(f"ID: {item[0]}")
                print(f"NAME: {item[1]}")
                print(f"CATEGORY: {item[2]}")
                print(f"COLOR: {item[3]}")
                print(f"SEASON: {item[4]}")
                print(f"OCCASION: {item[5]}")
                print(f"IMAGE: {item[6]}")
                print("-------------------------------------------------")
        elif ch==6:
            season=input("ENTER SEASON (SUMMER/WINTER/FALL/ALL): ")
            occasion=input("ENTER OCCASION (CASUAL/PARTY/FORMAL): ")
            suggest_outfit(season,occasion)
           
        elif ch==7:
            print("THANK YOU FOR USING WARDROBE MANAGER!!")
            break
        else:
            print("INVALID CHOICE!!")
        choice=input("WANT TO CONTINUE? (Y/N): ")
        if choice.lower()=='n':
            print("THANK YOU FOR USING WARDROBE MANAGER!!")
            break
if __name__=="__main__":
    main()


