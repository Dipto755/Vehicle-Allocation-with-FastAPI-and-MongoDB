#schemas for allocation data
def allocation(item) -> dict:
    return {
        "id": str(item["_id"]),
        "employee_id": item["employee_id"],
        "vehicle_id": item["vehicle_id"],
        "driver_id": item["driver_id"],
        "allocation_date": item["allocation_date"]
    }
    
def allocations(entity) -> list:
    return [allocation(item) for item in entity]