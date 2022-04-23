from app.database import get_db

def get_all_users_and_vehicles():
    statment = """
        SELECT user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.description
        FROM user 
        INNER JOIN vehicle on user.id = vehicle.owner_id
        INNER JOIN vehicle_type on vehicle.v_type = vehicle_type.id;
    """
    cursor = get_db()
    results = cursor.execute(statment).fetchall()
    cursor.close()
    out = []
    for result in results:
        temp_dict = {
            "last_name": result[0],
            "first_name": result[1],
            "hobbies": result[2],
            "user_active": result[3],
            "vehicle_license_plate": result[4],
            "vehicle_color": result[5],
            "vehicle_description": result[6]
        }
        out.append(temp_dict)
    return out

def get_all_users_and_vehicles_by_user_id(user_id):
    statment = """
        SELECT user.last_name,
            user.first_name,
            user.hobbies,
            user.active,
            vehicle.license_plate,
            vehicle.color,
            vehicle_type.description
        FROM user 
        INNER JOIN vehicle on user.id = vehicle.owner_id
        INNER JOIN vehicle_type on vehicle.v_type = vehicle_type.id;
        WHERE user.id = ?
    """
    cursor = get_db
    cursor.execute(statment, user_id)