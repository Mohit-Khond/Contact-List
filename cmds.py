import argparse


def details():
    parser = argparse.ArgumentParser("Enter the Contacts")
    parser.add_argument("Name", help="Enter the name of the contact")
    parser.add_argument("Phone", type=int, help="Enter the phone number of the contact")
    parser.add_argument("Email", help="Enter the email of the contact")

    args = parser.parse_args()
    return args.Name, args.Phone, args.Email


details()

