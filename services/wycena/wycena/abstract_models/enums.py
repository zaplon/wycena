import enum


class PropertyType(str, enum.Enum):
    APARTMENT = "APARTMENT"
    HOUSE = "HOUSE"
    COMMERCIAL = "COMMERCIAL"


class QueryFilterType(enum.Enum):
    EQUAL = 'EQUAL'
    GREATER_THAN = 'GREATER_THAN'
    LOWER_THAN = 'LOWER_THAN'
    IN = 'IN'
