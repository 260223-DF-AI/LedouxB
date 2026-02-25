# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# TODO: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts, name, phone, email, category):
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # TODO: Create a contact dictionary with all fields
    # TODO: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO: Append to contacts list
    # TODO: Return the new contact
    
    new_contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "category": category,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    contacts.append(new_contact)

    return new_contact


# =============================================================================
# TODO: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts):
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # TODO: Print header with contact count
    # TODO: Print table headers
    # TODO: Loop through contacts and print each row
    # TODO: Print footer
    print("=" * 44)
    print(f"            CONTACT BOOK ({len(contacts)} contacts)")
    print("=" * 44)
    print("#\t| Name\t\t\t| Phone\t\t| Category")
    print("--------|-----------------------|---------------|----------------")
    for i, contact in enumerate(contacts):
        print(f"{i}\t| {contact["name"]}\t", end='')
        if (len(contact["name"]) < 15):
            # name is too short, will offset rest of entry back one tab (8 spaces)
            print("\t", end='')
        print(f"| {contact["phone"]}\t| {contact["category"]}")
    print("=" * 44)



def display_contact_details(contact):
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # TODO: Print formatted contact details
    print("--- Contact Details ---")
    print(f"Name:\t\t{contact["name"]}")
    print(f"Phone:\t\t{contact["phone"]}")
    print(f"Email:\t\t{contact["email"]}")
    print(f"Category:\t{contact["category"]}")
    print(f"Added:\t\t{contact["created_at"]}")
    print("-" * 24)


# =============================================================================
# TODO: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # TODO: Filter contacts where query is in name (case-insensitive)
    # Hint: Use list comprehension and .lower()
    results = [c for c in contacts if query.lower() in c["name"].lower()]
    return results


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # TODO: Filter contacts by category
    results = [c for c in contacts if category == c["category"]]
    return results


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # TODO: Search for contact with matching phone
    results = [c for c in contacts if phone == c["phone"]]
    if results:
        return results[0]
    else:
        return None


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # TODO: Find contact by phone
    # TODO: Update the specified field
    # TODO: Return success/failure
    contact = find_by_phone(contacts, phone)
    if not contact:
        return False
    if field not in ["name", "phone", "email", "category"]:
        print("Invalid field") #just in case user tries to update "created_at" field
        return False
    index = contacts.index(contact) # save index of contact to replace in same spot after, would later like to implement alphabetical ordering function to throw at the end here
    contacts.remove(contact)
    contact[field] = new_value
    contacts.insert(index, contact)
    return True


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # TODO: Find and remove contact with matching phone
    contact = find_by_phone(contacts, phone)
    if not contact:
        return False
    contacts.remove(contact)
    return True


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # TODO: Count total contacts
    # TODO: Count contacts by category
    # TODO: Find most recently added contact
    print("--- Contact Book Statistics ---")
    print(f"Total Contacts: {len(contacts)}")
    print("By Category:")
    print(f" - Friends: {len(filter_by_category(contacts, "friends"))}")
    print(f" - Family: {len(filter_by_category(contacts, "family"))}")
    print(f" - Work: {len(filter_by_category(contacts, "work"))}")
    print(f" - Other: {len(filter_by_category(contacts, "other"))}")
    
    most_recent = contacts[0]
    for i, c in enumerate(contacts):
        if (i == len(contacts) - 1):
            break
        if most_recent["created_at"] <= contacts[i + 1]["created_at"]: #same exact second will prioritize contacts lower in the list since they were added later sequentially 
            most_recent = contacts[i + 1]

    print(f"Most Recent: {most_recent["name"]} (added [{most_recent["created_at"]}])")

    print("-" * 31)


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    while True:
        display_menu()
        entry = int(input("Entry: "))
        match entry:
            case 1:
                display_all_contacts(contacts)
            case 2:
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                category = input("Category: ")
                new_contact = add_contact(contacts, name, phone, email, category)
                display_contact_details(new_contact)
            case 3:
                print("-" * 24)
                print("1. Search by name")
                print("2. Search by category")
                print("3. Search by phone")
                print("0. Back")
                print("-" * 24)
                option = int(input("Entry: "))
                match option:
                    case 1:
                        query = input("Name contains: ")    
                        results = search_by_name(contacts, query)
                        if results:
                            for c in results:
                                display_contact_details(c)
                        else:
                            print("Nobody found by that name")
                    case 2:
                        query = input("Category: ")    
                        results = filter_by_category(contacts, query)
                        if results:
                            for c in results:
                                display_contact_details(c)
                        else:
                            print("Nobody found in that category")
                    case 3:
                        query = input("Phone (formatted xxx-xxx-xxxx): ")    
                        result = find_by_phone(contacts, query)
                        if result:
                            display_contact_details(result)
                        else:
                            print("Nobody found with that phone number in your contacts")
                    case 0:
                        pass # should just go back to main menu
                    case _:
                        print("Invalid entry.")
            case 4:
                phone = input("Enter phone number of contact to be updated: ")
                field = input("Which field? (name, phone, email, category): ").lower() #field is case-sensitive, take burden off user
                new_value = input(f"New value for {field}: ")
                result = update_contact(contacts, phone, field, new_value)
                if result:
                    display_contact_details(find_by_phone(contacts, phone))
                else:
                    print("Something went wrong.")
            case 5:
                phone = input("Enter phone number of contact to be deleted: ")
                result = delete_contact(contacts, phone)
                if result:
                    print(f"Success! Bye-bye {phone}")
                else:
                    print("Something went wrong.")
            case 6:
                display_statistics(contacts)
            case 0:
                quit()
            case _:
                print("Invalid choice, try again.")


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 40)
    
    # TODO: Add at least 5 sample contacts
    # add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    contacts = []
    add_contact(contacts, "Benjamin Ledoux", "603-362-3841", "bledoux2002@gmail.com", "work")
    add_contact(contacts, "McKenzie Ferrari", "978-221-xxxx", "mferrari@gmail.com", "other")
    add_contact(contacts, "Jason Ledoux", "603-362-9294", "jledoux@gmail.com", "family")
    add_contact(contacts, "Cooper", "603-845-7325", "coop@comcast.net", "family")
    add_contact(contacts, "Willow", "978-221-0327", "willow.bo.billow@yahoo.com", "family")

    # TODO: Test your functions
    # display_all_contacts(contacts)
    # results = search_by_name(contacts, "alice")
    # etc.
    '''
    display_all_contacts(contacts)

    display_contact_details(contacts[0])

    print('Contacts with "Ledoux" in the name:')
    results = search_by_name(contacts, "Ledoux")
    for c in results:
        display_contact_details(c)

    print('Contacts in the "family" category:')
    results = filter_by_category(contacts, "family")
    for c in results:
        display_contact_details(c)

    print('Contacts with my personal phone number:')
    results = find_by_phone(contacts, "603-362-3841")
    display_contact_details(c)

    print(f"Non-existant contact update return value: {update_contact(contacts, "000-000-0000", "none", "none")} (should be False)")
    print("Update contact name\nOld Contact:")
    display_contact_details(find_by_phone(contacts, "603-362-3841"))
    update_contact(contacts, "603-362-3841", "name", "Ben Ledoux")
    print("New contact:")
    display_contact_details(find_by_phone(contacts, "603-362-3841"))

    display_statistics(contacts)
    '''
    
    # STRETCH: Uncomment to run interactive menu
    main()
