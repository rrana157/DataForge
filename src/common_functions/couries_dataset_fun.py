import random
import string
from pandas import DataFrame
from resources.config import *

# --------------------------------------------
# Selects a value from a dictionary using weight-based probability.
# Example: {"Express": 60, "Standard": 35, "Bulk": 5}
# If weights fail validation, falls back to a random key.

# Main row generator for synthetic shipment dataset
# Ensures:
# - No Faker dependency
# - Shipment logic constraints respected
# - Safe fallbacks prevent failures during bulk generation
# --------------------------------------------


def weighted_choice(choices):
    try:
        if not choices or not isinstance(choices, dict):
            raise ValueError("Choices must be a non-empty dictionary.")

        items = list(choices.keys())
        weights = list(choices.values())

        if len(items) != len(weights) or sum(weights) == 0:
            raise ValueError("Invalid weights configuration.")

        return random.choices(items, weights=weights, k=1)[0]

    except Exception as e:
        print(f"[Warning] weighted_choice failed: {e}")
        return random.choice(list(choices.keys())) if choices else None


def random_gstin():
    try:
        letters = string.ascii_uppercase
        numbers = string.digits

        gstin = (
            f"{random.randint(10, 29)}"
            f"{''.join(random.choices(letters, k=5))}"
            f"{''.join(random.choices(numbers, k=4))}"
            f"{random.choice(letters)}"
            f"{random.choice(numbers)}"
        )
        return gstin

    except Exception as e:
        print(f"[Warning] GSTIN generation failed: {e}")
        return "UNKNOWNGSTIN"


def random_phone():
    try:
        return ''.join(random.choices(string.digits, k=10))
    except Exception as e:
        print(f"[Warning] Phone generation failed: {e}")
        return "0000000000"


def random_weight():
    try:
        return round(random.uniform(0.3, 12.0), 2)
    except Exception as e:
        print(f"[Warning] Weight generation failed: {e}")
        return 0.0


def generate_secondary_address():
    try:
        options = ['Near Park', 'Opposite Mall', 'Behind School', 'Above Shop']
        return random.choice(options)
    except Exception as e:
        print(f"[Warning] Secondary address selection failed: {e}")
        return "Unknown Landmark"


def generate_address(city, state):
    try:
        if not city or not state:
            raise ValueError("City and state must not be empty.")

        house_no = random.randint(1, 300)
        street_name = random.choice(['MG Road', 'Station Road', 'Ring Road', 'Gandhi Nagar', 'Market Street'])
        secondary = generate_secondary_address()
        pincode = ''.join(random.choices(string.digits, k=6))

        full_address = f"{house_no} {street_name}, {secondary}, {city}, {state} - {pincode}"
        return " ".join(full_address.split()), pincode

    except Exception as e:
        print(f"[Warning] Address generation failed: {e}")
        return "Unknown Address", "000000"


import random
import string
from datetime import timedelta, date

# Utility to simulate short random identifiers like UUIDs
def random_id(length=12):
    try:
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    except Exception as e:
        print(f"[Warning] random_id failed: {e}")
        return "UNKNOWN_ID"


# Utility to generate short random codes (alternative to fake.bothify)
def random_code(prefix="DTDC", digits=8):
    try:
        return prefix + ''.join(random.choices(string.digits, k=digits))
    except Exception as e:
        print(f"[Warning] random_code failed: {e}")
        return prefix + "00000000"


# Utility to create random short sentences (placeholder logistics remarks)
def random_sentence(word_count=4):
    try:
        sample_words = ["Pickup", "Delivered", "Priority", "Shipment", "Urgent", "Dispatch", "Fragile"]
        return " ".join(random.choices(sample_words, k=word_count)).capitalize()
    except Exception as e:
        print(f"[Warning] random_sentence failed: {e}")
        return "No remarks"


# Generates a random shipping date within last 30 days
def random_date():
    try:
        days_ago = random.randint(0, 30)
        today = date.today()
        return today - timedelta(days=days_ago)
    except Exception as e:
        print(f"[Warning] random_date failed: {e}")
        return date.today()


def generate_row():
    try:
        # ---------------- Origin & Destination ----------------
        origin, origin_state = random.choice(city_state_pairs)
        destination, dest_state = random.choice(city_state_pairs)

        # Avoid identical pickup and drop points
        while destination == origin:
            destination, dest_state = random.choice(city_state_pairs)

        # ---------------- Sender ----------------
        sender_type = random.choices(['Company', 'Individual'], weights=[0.6, 0.4])[0]

        # Generate sender name based on type
        sender_name = (
            f"{random.choice(['Tech', 'Global', 'Prime', 'NextGen'])} Pvt Ltd"
            if sender_type == 'Company'
            else f"{random.choice(['Amit', 'Ravi', 'Sarika', 'Pooja'])} {random.choice(['Sharma', 'Patel', 'Singh', 'Nair'])}"
        )

        sender_address, sender_pincode = generate_address(origin, origin_state)
        sender_phone = random_phone()

        # 90% of companies have GSTIN; individuals mostly do not
        sender_gstin = random_gstin() if sender_type == 'Company' and random.random() < 0.9 else ""
        sender_signature = "Yes" if sender_type == 'Company' else ""

        # ---------------- Receiver ----------------
        receiver_type = random.choices(['Individual', 'Company'], weights=[0.6, 0.4])[0]

        recipient_name = (
            f"{random.choice(['Cargo', 'Velocity', 'LogiCorp', 'Metro'])} Ltd"
            if receiver_type == 'Company'
            else f"{random.choice(['Sneha', 'Aakash', 'Neha', 'Rohit'])} {random.choice(['Verma', 'Shetty', 'Gupta', 'Rao'])}"
        )

        recipient_address, recipient_pincode = generate_address(destination, dest_state)

        # Avoid identical sender/receiver addresses
        while recipient_address == sender_address:
            recipient_address, recipient_pincode = generate_address(destination, dest_state)

        recipient_phone = random_phone()
        recipient_gstin = random_gstin() if receiver_type == 'Company' and random.random() < 0.7 else ""
        receiver_signature = "Yes" if receiver_type == 'Company' else ""

        # ---------------- Shipment Metrics ----------------
        shipment_date = random_date()
        receive_date = shipment_date + timedelta(days=random.randint(1, 5))
        expire_date = shipment_date + timedelta(days=30)

        total_pcs = random.randint(1, 5)
        actual_wt = random_weight()
        volumetric_wt = round(actual_wt + random.uniform(0.1, 3.0), 2)
        chargeable_wt = max(actual_wt, volumetric_wt)

        vas = weighted_choice(value_added_weights)
        vas_charges = round(random.uniform(20, 150), 2) if vas != 'None' else 0.0

        mode_choice = random.choices(mode, weights=[0.6, 0.2, 0.2])[0]

        # Pricing logic based on mode variation
        base_rate_map = {'Surface': 45, 'Air Cargo': 65, 'Express': 85}
        base_rate = base_rate_map.get(mode_choice, 50)

        tariff = round(chargeable_wt * random.uniform(base_rate * 0.9, base_rate * 1.1), 2)
        total_amt = round(tariff + vas_charges, 2)

        nature_of_consignment_choice = random.choice(nature_of_consignment)

        # Risk logic based on conditions
        risk_surcharge_choice = (
            "Carrier" if (chargeable_wt > 5 or vas != 'None' or mode_choice == 'Surface' or nature_of_consignment_choice == 'Non-Dox')
            else "Owner"
        )

        # Payment selection rules
        payment_mode = random.choices(
            population=['Cash', 'Card'] if sender_type == 'Company' else ['Cash', 'Card', 'Wallet'],
            weights=[0.6, 0.4] if sender_type == 'Company' else [0.6, 0.3, 0.1], k=1
        )[0]

        # ---------------- Return structured dataset row ----------------
        return [
            origin, destination, random_id(), shipment_date, sender_name, sender_phone,
            sender_address, origin, origin_state, sender_pincode, sender_gstin,
            total_pcs, actual_wt, volumetric_wt, chargeable_wt, random.choice(['Yes', 'No']),
            sender_signature, shipment_date, recipient_name, recipient_phone,
            recipient_address, destination, dest_state, recipient_pincode,
            random_sentence(), vas, random_code(),
            expire_date, random_code(prefix="BR", digits=3), recipient_gstin, recipient_name,
            random.choice(['Self', 'Family', 'Friend', 'Colleague']), receiver_signature,
            receiver_signature, receive_date, tariff, vas_charges, total_amt,
            mode_choice, risk_surcharge_choice, payment_mode,
            nature_of_consignment_choice
        ]

    except Exception as e:
        print(f"[Error] Row generation failed: {e}")
        return ["ERROR"] * 45  # Ensures CSV structure isn't broken


