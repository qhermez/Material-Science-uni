# Template for adding new materials
def get_material_template():
    """Template for adding new materials to the database"""
    template = {
        "material_key": {
            "name": "Material Name",
            "class": "metal",  # metal, polymer, ceramic, composite
            "category": "specific_category",  # steel, aluminum, stainless_steel, etc.
            "composition": {"Element1": 0.xx, "Element2": 0.xx},
            "properties": {
                "density": 0.0,  # g/cm³
                "youngs_modulus": 0.0,  # GPa
                "yield_strength": 0.0,  # MPa
                "tensile_strength": 0.0,  # MPa
                "elongation": 0.0,  # %
                "hardness": 0.0,  # Brinell/Vickers
                "thermal_conductivity": 0.0,  # W/m·K
                "melting_point": 0.0,  # °C
                "electrical_resistivity": 0.0,  # Ω·m
                "cost": 0.0,  # relative cost
                "fatigue_strength": 0.0  # MPa
            },
            "applications": ["Application 1", "Application 2"],
            "characteristics": ["Characteristic 1", "Characteristic 2"],
            "educational_insights": ["Educational insight 1", "Insight 2"],
            "manufacturing_notes": {
                "machinability": "Good/Fair/Poor",
                "weldability": "Good/Fair/Poor", 
                "formability": "Good/Fair/Poor",
                "heat_treatment": "Description"
            }
        }
    }
    return template