import enum

class PackageStatus(enum.Enum):
    CREATED = "CREATED"
    IN_TRANSIT = "IN_TRANSIT"
    ON_HOLD = "ON_HOLD"
    DELIVERED = "DELIVERED"
    LOST = "LOST"

class EventType(enum.Enum):
    CHECKIN = "CHECKIN"
    CHECKOUT = "CHECKOUT"
    CUSTOMS_HOLD = "CUSTOMS_HOLD"
    DELIVERED = "DELIVERED"
    LOST = "LOST"