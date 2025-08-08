import pandas as pd
import matplotlib.pyplot as plt
import os

# Paths
current_dir = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_dir, "..", "data", "species_growth_data.csv")
output_path = os.path.join(current_dir, "..", "output", "charts", "co2_sequestration_simulation.png")

# Create output folder if missing
os.makedirs(os.path.dirname(output_path), exist_ok=True)

# Load data
df = pd.read_csv(data_path)

# Parameters
years = list(range(1, 21))
num_trees = 1000

plt.figure(figsize=(12, 8))

for idx, row in df.iterrows():
    biomass_per_year = row['Avg_Biomass_kg_per_year']
    carbon_content = row['Carbon_Content_Ratio']
    co2_factor = row['CO2_Conversion_Factor']
    survival_rate = row['Survival_Rate']
    species = row['Species']
    
    yearly_co2 = []
    for y in years:
        # Apply survival rate progressively per year
        biomass = biomass_per_year * y * num_trees * (survival_rate ** y)
        co2 = biomass * carbon_content * co2_factor / 1000  # convert to tons
        yearly_co2.append(co2)
    
    plt.plot(years, yearly_co2, label=species)

plt.title("Estimated CO₂ Sequestration Over 20 Years (1000 Trees)")
plt.xlabel("Years")
plt.ylabel("CO₂ Sequestered (tons)")
plt.legend(loc='upper left', bbox_to_anchor=(1,1), fontsize='small')
plt.grid(True)
plt.tight_layout()
plt.savefig(output_path, bbox_inches='tight')
plt.show()
