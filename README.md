
# QAP-4-Files-CC

## Description

This Python program is designed for the One Stop Insurance Company to facilitate the entry and calculation of new insurance policies. The program collects customer information, calculates insurance costs based on various parameters, and generates a policy receipt. The program also maintains a record of all policies and updates the necessary files accordingly.

## Author

**Cody Collins**

## Date

**July 17, 2024**

## Features

- Collect customer information including name, address, phone number, and insurance requirements.
- Calculate premium costs based on the number of cars insured and additional coverages selected.
- Generate and display a detailed policy receipt.
- Maintain a record of previous policies.
- Update constants and policy records automatically.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/QAP-4-Files-CC.git
    cd QAP-4-Files-CC
    ```

2. **Install required libraries:**

    Ensure you have Python installed. The required libraries include:
    - `datetime`
    - `FormatValues` (This should be a custom module, make sure it is available in the repository)
    - `sys`
    - `time`

3. **Create necessary files:**

    Ensure you have `Const.dat` and `Policies.dat` files in the same directory as the program. These files should be formatted as follows:

    - **Const.dat:**
      ```
      PolicyNum, BASIC_PREMIUM, ADD_CARS_DISC, EXT_LIAB_COST, GLASS_COV_COST, LOANER_COST, HST_RATE, PROC_FEE
      ```

    - **Policies.dat:**
      ```
      (Leave it empty or add some initial policies in the format)
      ```

## Usage

1. **Run the program:**

    ```bash
    python OneStop.py
    ```

2. **Enter customer details and insurance requirements:**

    The program will prompt you to enter the following information:
    - Customer's first and last name
    - Street address, city, province, and postal code
    - Phone number
    - Number of cars being insured
    - Additional coverages (extra liability, glass coverage, loaner car)
    - Payment method (Full, Monthly, Down Pay)

3. **Receive a detailed policy receipt:**

    The program will display a detailed policy receipt with the calculated costs and payment information.

4. **View previous policies:**

    The program will list previous policies from the `Policies.dat` file.

5. **Continue or exit:**

    The program will prompt you to enter another policy or exit. If you choose to exit, it will update the `Const.dat` file with the new policy number.

## Files

- **OneStop.py:** Main program file.
- **Const.dat:** Contains constants used in the program.
- **Policies.dat:** Stores all policy records.

## Acknowledgements

Thank you for using the One Stop Insurance Company Policy Management Program.
