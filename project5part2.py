import random

def main():
    # Define port numbers and corresponding protocols
    portNumArray = ["20", "21", "22", "23", "25", "53", "67", "68", "80", "110", "137", "139", "143", "161", "162", "389", "443", "445", "3389"]
    portNameArray = ["FTP", "FTP", "SSH", "Telnet", "SMTP", "DNS", "DHCP", "DHCP", "HTTP", "POP3", "NetBIOS", "NetBIOS", "IMAP", "SNMP", "SNMP", "LDAP", "HTTPS", "SMB", "RDP"]

    def numToName(portNumArray: list[str], portNameArray: list[str], portNumber: str) -> str:
        for i in range(len(portNumArray)):
            if portNumArray[i] == portNumber:
                return portNameArray[i]
        else:
            return ""

    def nameToNum(portNumArray: list[str], portNameArray: list[str], portName: str) -> list[str]:
        portNumbers = []
        for m in range(len(portNameArray)):
            if portNameArray[m].lower() == portName.lower():
                portNumbers.append(portNumArray[m])
        return portNumbers

    def getInput() -> str:
        valid_choices = ['1', '2', '3', 'm']
        choice = input("Enter your choice (1, 2, 3, m): ").rstrip()
        while choice not in valid_choices:
            choice = input("Invalid choice. Please enter 1, 2, 3, or m: ").rstrip()
        return choice



    while True:

        # Main menu

        print("\nMain Menu:")
        print("1. Given a port number, identify the PROTOCOL (use abbreviation).")
        print("2. Given a port protocol, identify a port NUMBER.")
        print("3. Exit")

        choice = getInput()

        if choice == '1':

            # Identify the protocol for port number

            print("Option 1: Identify the port's PROTOCOL.")
            print("----------------------------------------")
            while True:
                portNumber = random.choice(portNumArray)
                user_input = input(f"What is the protocol for port {portNumber} (m=Main Menu)? ").strip()

                if (user_input.lower() == 'm'):
                    break

                correct_protocol = numToName(portNumArray, portNameArray, portNumber)

                if (user_input.upper() == correct_protocol):
                    print("Correct answer!")

                else:
                    print(f"Incorrect. The correct answer is {correct_protocol}.")



        elif (choice == '2'):
            # Option 2: Identify the port number given a protocol
            print("Option 2: Identify the port's NUMBER.")
            print("----------------------------------------")

            while True:
                portProtocol = random.choice(portNameArray)
                user_input = input(f"What is the number for protocol {portProtocol} (m=Main Menu)? ").strip()

                if (user_input.lower() == 'm'):
                    break
                correct_numbers = nameToNum(portNumArray, portNameArray, portProtocol)

                if user_input in correct_numbers:
                    print("Correct answer!")

                else:
                    correct_numbers_str = ', '.join(correct_numbers)
                    print(f"Incorrect. The correct answer is {correct_numbers_str}.")

                    

        elif choice == '3':
            print("Program Complete. I hope this has helped in studying for the CompTIA A+ certification.")
            break

if __name__ == "__main__":
    main()
