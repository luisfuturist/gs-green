from sqlalchemy.orm import sessionmaker
from sqlalchemy import func, select
from db_config import engine
from models import EnergyConsumption

# Initialize a session
Session = sessionmaker(bind=engine)
session = Session()

def calculate_per_capita_consumption():
    """
    Analyze per capita energy consumption.
    """
    try:
        # Assuming you have population data for Brazil in the database or as a static value.
        brazil_population = 213_000_000  # Update this with dynamic or database values if available

        # Query total energy consumption and calculate per capita value
        total_energy = session.query(func.sum(EnergyConsumption.vlr_mercado)).scalar()

        print("\n--- Per Capita Energy Consumption ---")

        if total_energy:
            per_capita_consumption = total_energy / brazil_population
            print(f"Per capita energy consumption: {per_capita_consumption:.2f} kWh")
        else:
            print("No energy consumption data available for analysis.")

    except Exception as e:
        print(f"Error during analysis: {e}")
    finally:
        print("\n")
        session.close()

def get_trend_data():
    """
    Fetch and analyze energy trends over time.
    """
    try:
        # Example: Group data by year and calculate total consumption for each year
        results = (
            session.query(
                func.extract('year', EnergyConsumption.dat_competencia).label("year"),
                func.sum(EnergyConsumption.vlr_mercado).label("total_consumption")
            )
            .group_by(func.extract('year', EnergyConsumption.dat_competencia))
            .order_by("year")
        ).all()
        
        print("\n--- Energy Consumption Trends ---")

        # Display the results
        for result in results:
            year, total = result
            print(f"Year: {int(year)}, Total Consumption: {total:.2f} kWh")
    except Exception as e:
        print(f"Error during trend analysis: {e}")
    finally:
        print("\n")
        session.close()

if __name__ == "__main__":
    calculate_per_capita_consumption()
    get_trend_data()
