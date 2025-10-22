import random, uuid

first_names = ["Alex", "Jordan", "Taylor", "Morgan", "Casey"]
last_names  = ["Smith", "Johnson", "Brown", "Garcia", "Miller"]

def random_name():
    return random.choice(first_names), random.choice(last_names)

def random_email(first, last):
    return f"{first.lower()}.{last.lower()}_{uuid.uuid4().hex[:5]}@example.com"

def random_az_phone():
    area = random.choice(["480", "602", "623", "520"])
    prefix = random.randint(200, 999)
    line = random.randint(1000, 9999)
    return f"{area}{prefix}{line}"
