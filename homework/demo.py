# homework/demo.py
import os
import pandas as pd

pd.set_option("display.notebook_repr_html", True)

def generate_csv():
    # Rutas robustas relativas al repo
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # sube desde homework/ a la raíz del repo

    input_path = os.path.join(BASE_DIR, "files", "input", "truck_event_text_partition.csv")
    output_dir = os.path.join(BASE_DIR, "files", "output")
    output_path = os.path.join(output_dir, "specific-columns.csv")

    # Carga
    truck_events = pd.read_csv(input_path)

    # Subconjuntos
    truck_events_subset = truck_events[0:10]
    specific_columns = truck_events_subset[["driverId", "eventTime", "eventType"]]

    # Asegura carpeta y escribe CSV
    os.makedirs(output_dir, exist_ok=True)
    specific_columns.to_csv(output_path, sep=",", header=True, index=False)

if __name__ == "__main__":
    generate_csv()