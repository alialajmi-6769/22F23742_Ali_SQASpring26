def tourist_density(location_type, current_visitors, capacity):

    if capacity <= 0:
        return "Invalid capacity"

    occupancy_rate = (current_visitors / capacity) * 100

    if location_type == 1:
            location_name = "Beach"
    elif location_type == 2:
            location_name = "Museum"
    elif location_type == 3:
            location_name = "Historic Site"
    else:
            location_name = "Unknown"

    if occupancy_rate < 40:
        density_status = "Low"
    elif occupancy_rate < 70:
        density_status = "Moderate"
    elif occupancy_rate < 90:
        density_status = "High"
    else:
        density_status = "Critical"

    return location_name, round(occupancy_rate, 2), density_status
