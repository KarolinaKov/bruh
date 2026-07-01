import random

from yourapp.models import (
    Appliance,
    Endpoint,
    Room,
    RoomTOTP,
    EndpointApplianceStateRoom,
)

# -----------------
# Appliances
# -----------------
appliances = [
    ("Pračka", 50),
    ("Sušička", 40),
]

for name, price in appliances:
    Appliance.objects.get_or_create(
        name=name,
        defaults={
            "price_per_unit": price
        }
    )


# -----------------
# Rooms + TOTP
# -----------------
rooms = []

for i in range(1, 6):
    room, created = Room.objects.get_or_create(
        key=i,
        defaults={
            "balance": random.randint(100, 1000)
        }
    )

    rooms.append(room)

print("✔ Rooms created")

# -----------------
# Endpoints
# -----------------
endpoints = []

for i in range(1, 4):
    endpoint, created = Endpoint.objects.get_or_create(
        ip_add=f"192.168.1.{100+i}",
        defaults={
            "connection": True,
            "token": random.randint(1000, 999999)
        }
    )

    endpoints.append(endpoint)

print("✔ Endpoints created")

# -----------------
# Endpoint States
# -----------------
appliances = list(Appliance.objects.all())

for endpoint in endpoints:
    for appliance in appliances:

        EndpointApplianceStateRoom.objects.get_or_create(
            endpoint=endpoint,
            appliance=appliance,
            is_occupied =False)

print("✔ Endpoint states created")
print("Database successfully seeded.")