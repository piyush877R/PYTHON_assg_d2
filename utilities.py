from sqlalchemy import create_engine, Table, Column, String, Float, MetaData
from sqlalchemy import create_engine as CE
def write_deviation_results_to_sqlite(result):
    try:
        Engine = CE('sqlite:///{}.db'.format("mapping"), echo=False)
    
        metadata = MetaData()

        mapping = Table('mapping', metadata,
                        Column("X (test func)", Float, primary_key=False),
                        Column("Y (test func)", Float),
                        Column("Delta Y (test func)", Float),
                        Column("SNo. of ideal functions", String(50))
                        )

        metadata.create_all(Engine)

        execute_map = []
        for item in result:
            point = item["point"]
            classi = item["classi"]
            delta_y = item["delta_y"]

            classi_name = None
            if classi is not None:
                classi_name = classi.tag.replace("y", "N")
            else:
                classi_name = "-"
                delta_y = -1

            res = {
                "X (test func)": point["x"],
                "Y (test func)": point["y"],
                "Delta Y (test func)": delta_y,
                "SNo. of ideal functions": classi_name
            }
            execute_map.append(res)
        with Engine.begin() as connection:
            connection.execute(mapping.insert(),execute_map)
        

        
        print("Data filled successfully to database.")
        print(result)
        print(res)
    except Exception as e:
        print("Error occurred while writing data to SQLite database:", str(e))
