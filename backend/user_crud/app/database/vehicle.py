from app.database import get_db
import sqlite3

def output_formatter(results):
    out = []
    for result in results:
        result_dict = {
            "id": result[0],
            "color": result[1],
            "license_plate": result[2],
            "v_type": result[3],
            "owener_id": result[4],
            "active": result[5],
        }
        out.append(result_dict)
    return out

def insert(vihicle_dict):
    value_tuple = (
        vihicle_dict.get("color"),
        vihicle_dict.get("license_plate"),
        vihicle_dict.get("v_type"),
        vihicle_dict.get("owner_id")
    )
    statement = """
        INSERT INTO vehicle (
            color,
            license_plate,
            v_type,
            owner_id
        ) VALUES (?,?,?,?)
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()

def scan():
    cursor = get_db()
    results = cursor.execute('SELECT * FROM vehicle WHERE active=1').fetchall()
    cursor.close()
    return output_formatter(results)

def select_by_id(pk):
    cursor = get_db()
    results = cursor.execute('SELECT * FROM vehicle WHERE id=?', (pk,)).fetchall()
    cursor.close()
    return output_formatter(results)

def update(pk, vehicle_data):
    value_tuple = (
        vehicle_data.get("color"),
        vehicle_data.get("license_plate"),
        vehicle_data.get("v_type"),
        vehicle_data.get("owner_id"),
        pk
    )
    statement = """
        UPDATE vehicle
        SET color=?,
            license_plate=?,
            v_type=?,
            owner_id=?
        WHERE id=?
    """
    cursor = get_db()
    cursor.execute(statement, value_tuple)
    cursor.commit()
    cursor.close()


def deactivate(pk):
    cursor = get_db()
    statement = """
        UPDATE vehicle
        SET active=0
        WHERE id=?
    """
    cursor.execute(statement, (pk,))
    cursor.commit()
    cursor.close()
    

