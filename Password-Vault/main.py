while True:
    PasswordVault = input("Enter your password vault - ")
    if PasswordVault == "ABC123":
        print("Welcome to PasswordVault!")
        while True:
            print("===== PASSWORD VAULT =====")
            print("1. save a password")
            print("2. view saved passwords")
            print("3. Show All Websites")
            print("4. Search Website")
            print("5. Update Password")
            print("6. Delete Password")
            print("7. Password Generator")
            print("8. Password Strength Checker")
            print("9. Total Saved Passwords")
            print("10. Clear Vault")
            print("11. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                website = input("Enter the website name: ")
                password = input("Enter the password: ")
                with open("passwords.txt", "a") as file:
                    file.write(f"{website}: {password}\n")
                    print("Password saved successfully!")
            elif choice == "2":
                print("Saved Passwords:")
                with open("passwords.txt", "r") as file:
                    for line in file:
                        print(line.strip())
            elif choice == "3":
                print("All Websites:")
                with open("passwords.txt", "r") as file:
                    for line in file:
                        website = line.split(":")[0]
                        print(website)
            elif choice == "4":
                search_website = input("Enter the website name to search: ")
                found = False
                with open("passwords.txt", "r") as file:
                    for line in file:
                        website, password = line.strip().split(":")
                        if website == search_website:
                            print(f"Password for {website}: {password}")
                            found = True
                            break
                if not found:
                    print(f"No password found for {search_website}.")
            elif choice == "5":
                update_website = input("Enter the website name to update the password: ")
                updated = False
                with open("passwords.txt", "r") as file:
                    lines = file.readlines()
                with open("passwords.txt", "w") as file:
                    for line in lines:
                        website, password = line.strip().split(":")
                        if website == update_website:
                            new_password = input(f"Enter the new password for {website}: ")
                            file.write(f"{website}: {new_password}\n")
                            updated = True
                        else:
                            file.write(line)
                if updated:
                    print(f"Password for {update_website} updated successfully!")
                else:
                    print(f"No password found for {update_website}.")
            elif choice == "6":
                delete_website = input("Enter the website name to delete the password: ")
                deleted = False
                with open("passwords.txt", "r") as file:
                    lines = file.readlines()
                with open("passwords.txt", "w") as file:
                    for line in lines:
                        website, password = line.strip().split(":")
                        if website != delete_website:
                            file.write(line)
                        else:
                            deleted = True
                if deleted:
                    print(f"Password for {delete_website} deleted successfully!")
                else:
                    print(f"No password found for {delete_website}.")
            elif choice == "7":
                import random
                import string
                length = int(input("Enter the desired password length: "))
                characters = string.ascii_letters + string.digits + string.punctuation
                generated_password = ''.join(random.choice(characters) for _ in range(length))
                print(f"Generated Password: {generated_password}")
            elif choice == "8":
                import string
                password_to_check = input("Enter the password to check its strength: ")
                strength = "Weak"
                if len(password_to_check) >= 8:
                    if any(char.isdigit() for char in password_to_check):
                        if any(char.isupper() for char in password_to_check):
                            if any(char.islower() for char in password_to_check):
                                if any(char in string.punctuation for char in password_to_check):
                                    strength = "Strong"
                print(f"Password Strength: {strength}")
            elif choice == "9":
                with open("passwords.txt", "r") as file:
                    total_passwords = sum(1 for line in file)
                print(f"Total Saved Passwords: {total_passwords}")
            elif choice == "10":
                with open("passwords.txt", "w") as file:
                    file.write("")
                print("Password vault cleared successfully!")
            elif choice == "11":
                print("Exiting PasswordVault. Goodbye!")
                break
            
    else:
        print("Incorrect password. Please try again.")
