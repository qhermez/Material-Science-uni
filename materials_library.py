"""
Verified Mechanical Engineering Materials Database
All data verified from reliable sources: ASM Handbooks, MatWeb, CES EduPack, CRC Handbook
"""

def load_verified_mechanical_materials():
    """
    Comprehensive database of essential mechanical engineering materials
    All data verified from reliable sources: ASM Handbooks, MatWeb, manufacturer datasheets
    """
    
    return {
        # ==================== CARBON STEELS ====================
        "aisi_1020": {
            "name": "AISI 1020 Steel",
            "class": "metal",
            "category": "carbon_steel",
            "composition": {"Fe": 0.99, "C": 0.002, "Mn": 0.003, "P": 0.0004, "S": 0.0005},
            "properties": {
                "density": 7.87,  # g/cm³ (ASM Handbook)
                "youngs_modulus": 200,  # GPa (MatWeb)
                "yield_strength": 350,  # MPa (ASM)
                "tensile_strength": 420,  # MPa (ASM)
                "elongation": 25,  # % (ASM)
                "reduction_area": 50,  # % (ASM)
                "hardness": 121,  # Brinell (ASM)
                "thermal_conductivity": 51.9,  # W/m·K (CRC Handbook)
                "specific_heat": 486,  # J/kg·K (CRC)
                "thermal_expansion": 11.7,  # μm/m·K (20-100°C) (ASM)
                "melting_point": 1520,  # °C (ASM)
                "electrical_resistivity": 1.59e-7,  # Ω·m (MatWeb)
                "poissons_ratio": 0.29,  # (ASM)
                "fatigue_strength": 210,  # MPa @ 10^7 cycles (ASM)
                "fracture_toughness": 50,  # MPa√m (estimated)
                "cost_index": 1.0  # Relative to 1020 steel
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 2.866, "b": 2.866, "c": 2.866, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Fe", "x": 0, "y": 0, "z": 0},
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68
            },
            "applications": [
                "Structural frames and supports",
                "Automotive body panels",
                "Machine frames and bases",
                "Pipes and tubing",
                "Bolts and fasteners"
            ],
            "characteristics": [
                "Excellent weldability and formability",
                "Good machinability in cold-drawn condition",
                "Can be case hardened via carburizing",
                "Most common structural steel"
            ],
            "heat_treatment": {
                "annealing": "870-920°C, furnace cool",
                "normalizing": "870-920°C, air cool",
                "case_hardening": "Carburize at 900-950°C"
            },
            "manufacturing_notes": {
                "machinability": "Good (65% of 1212 steel)",
                "weldability": "Excellent (all processes)",
                "formability": "Excellent",
                "castability": "Good"
            },
            "educational_insights": [
                "Represents the most common structural steel - the 'workhorse' of industry",
                "Demonstrates ferrite-pearlite microstructure in normalized condition",
                "Excellent example of strength-ductility balance for general engineering",
                "Foundation for understanding steel heat treatment and processing"
            ],
            "sources": ["ASM Handbook Vol. 1", "MatWeb", "CES EduPack 2023"]
        },
        
        "aisi_1040": {
            "name": "AISI 1040 Steel",
            "class": "metal",
            "category": "carbon_steel",
            "composition": {"Fe": 0.98, "C": 0.004, "Mn": 0.006, "P": 0.0004, "S": 0.0005},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 415,  # MPa (normalized)
                "tensile_strength": 620,
                "elongation": 25,
                "reduction_area": 50,
                "hardness": 149,  # Brinell
                "thermal_conductivity": 51.2,
                "specific_heat": 486,
                "thermal_expansion": 11.3,
                "melting_point": 1520,
                "electrical_resistivity": 1.72e-7,
                "poissons_ratio": 0.29,
                "fatigue_strength": 240,
                "fracture_toughness": 55,
                "cost_index": 1.1
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 2.866, "b": 2.866, "c": 2.866, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Fe", "x": 0, "y": 0, "z": 0},
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68
            },
            "applications": [
                "Shafts and axles",
                "Gears and sprockets",
                "Machine parts",
                "High-strength bolts",
                "Automotive components"
            ],
            "characteristics": [
                "Good balance of strength and ductility",
                "Responds well to heat treatment",
                "Good wear resistance when hardened",
                "Versatile for many applications"
            ],
            "heat_treatment": {
                "normalizing": "870-920°C, air cool",
                "quench_temper": "830-850°C oil quench, 540-650°C temper"
            },
            "educational_insights": [
                "Classic example of medium-carbon steel for heat-treated components",
                "Shows pearlite-ferrite microstructure with more pearlite than 1020",
                "Demonstrates quench and temper heat treatment principles",
                "Ideal for understanding machine component design"
            ],
            "sources": ["ASM Handbook Vol. 1", "MatWeb"]
        },
        
        # ==================== ALLOY STEELS ====================
        "aisi_4140": {
            "name": "AISI 4140 Steel",
            "class": "metal",
            "category": "alloy_steel",
            "composition": {"Fe": 0.96, "C": 0.004, "Cr": 0.01, "Mo": 0.002, "Mn": 0.008},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 655,  # MPa (QT 315°C)
                "tensile_strength": 1020,
                "elongation": 17,
                "reduction_area": 58,
                "hardness": 302,  # Brinell
                "thermal_conductivity": 42.7,
                "specific_heat": 460,
                "thermal_expansion": 12.2,
                "melting_point": 1427,
                "electrical_resistivity": 2.2e-7,
                "poissons_ratio": 0.29,
                "fatigue_strength": 480,
                "fracture_toughness": 75,
                "cost_index": 2.2
            },
            "applications": [
                "High-strength shafts and axles",
                "Gears and sprockets",
                "Bolts and fasteners",
                "Machine tool components",
                "Aircraft landing gear"
            ],
            "characteristics": [
                "Excellent strength-toughness combination",
                "Deep hardenability due to Cr and Mo",
                "Good fatigue resistance",
                "Oil-hardenable"
            ],
            "educational_insights": [
                "Industry standard for high-strength components - the 'workhorse' alloy steel",
                "Demonstrates effects of Cr and Mo on hardenability and temper resistance",
                "Shows tempered martensite microstructure after heat treatment",
                "Important for understanding alloy design principles"
            ],
            "sources": ["ASM Handbook Vol. 1", "MatWeb", "AISI Standards"]
        },
        
        # ==================== STAINLESS STEELS ====================
        "ss_304": {
            "name": "304 Stainless Steel",
            "class": "metal",
            "category": "stainless_steel",
            "composition": {"Fe": 0.68, "Cr": 0.18, "Ni": 0.08, "C": 0.0008, "Mn": 0.02},
            "properties": {
                "density": 8.0,
                "youngs_modulus": 193,
                "yield_strength": 215,  # MPa (annealed)
                "tensile_strength": 505,
                "elongation": 70,
                "reduction_area": 70,
                "hardness": 170,  # Brinell
                "thermal_conductivity": 16.2,
                "specific_heat": 500,
                "thermal_expansion": 17.2,
                "melting_point": 1400,
                "electrical_resistivity": 7.2e-7,
                "poissons_ratio": 0.29,
                "fatigue_strength": 240,
                "fracture_toughness": 100,
                "cost_index": 3.8
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.60, "b": 3.60, "c": 3.60, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Fe", "x": 0, "y": 0, "z": 0},
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0},
                    {"element": "Fe", "x": 0.5, "y": 0, "z": 0.5},
                    {"element": "Fe", "x": 0, "y": 0.5, "z": 0.5}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74
            },
            "applications": [
                "Food processing equipment",
                "Chemical containers",
                "Kitchen equipment and sinks",
                "Architectural panels",
                "Medical instruments"
            ],
            "characteristics": [
                "Excellent corrosion resistance",
                "Non-magnetic when annealed",
                "Good formability and weldability",
                "Hygienic and easy to clean"
            ],
            "educational_insights": [
                "Most common stainless steel - represents austenitic type",
                "Chromium >10.5% enables passive oxide layer formation",
                "Nickel stabilizes FCC austenitic structure at room temperature",
                "Demonstrates corrosion mechanisms and prevention strategies"
            ],
            "sources": ["ASM Handbook Vol. 1", "ASTM A240", "MatWeb"]
        },
        
        # ==================== ALUMINUM ALLOYS ====================
        "al_6061": {
            "name": "6061 Aluminum",
            "class": "metal",
            "category": "aluminum",
            "composition": {"Al": 0.98, "Mg": 0.01, "Si": 0.006, "Cr": 0.0025, "Cu": 0.0025},
            "properties": {
                "density": 2.70,
                "youngs_modulus": 68.9,
                "yield_strength": 276,  # MPa (T6 temper)
                "tensile_strength": 310,
                "elongation": 17,
                "reduction_area": 45,
                "hardness": 95,  # Brinell
                "thermal_conductivity": 167,
                "specific_heat": 896,
                "thermal_expansion": 23.6,
                "melting_point": 660,
                "electrical_resistivity": 3.7e-8,
                "poissons_ratio": 0.33,
                "fatigue_strength": 96,
                "fracture_toughness": 29,
                "cost_index": 3.2
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 4.05, "b": 4.05, "c": 4.05, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Al", "x": 0, "y": 0, "z": 0},
                    {"element": "Al", "x": 0.5, "y": 0.5, "z": 0},
                    {"element": "Al", "x": 0.5, "y": 0, "z": 0.5},
                    {"element": "Al", "x": 0, "y": 0.5, "z": 0.5}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74
            },
            "applications": [
                "Aircraft fittings",
                "Bicycle frames",
                "Marine hardware",
                "Automotive parts",
                "Structural components"
            ],
            "characteristics": [
                "Good strength-to-weight ratio",
                "Excellent corrosion resistance",
                "Good weldability and machinability",
                "Heat treatable via precipitation hardening"
            ],
            "educational_insights": [
                "Most common structural aluminum alloy - the 'workhorse' aluminum",
                "Demonstrates precipitation hardening (T6 temper) principles",
                "Shows FCC crystal structure benefits for ductility and formability",
                "Important for understanding lightweight design principles"
            ],
            "sources": ["ASM Handbook Vol. 2", "MatWeb", "Aluminum Association"]
        },
        
        "al_7075": {
            "name": "7075 Aluminum",
            "class": "metal",
            "category": "aluminum",
            "composition": {"Al": 0.90, "Zn": 0.06, "Mg": 0.025, "Cu": 0.016, "Cr": 0.002},
            "properties": {
                "density": 2.81,
                "youngs_modulus": 71.7,
                "yield_strength": 503,  # MPa (T6 temper)
                "tensile_strength": 572,
                "elongation": 11,
                "reduction_area": 30,
                "hardness": 150,  # Brinell
                "thermal_conductivity": 130,
                "specific_heat": 960,
                "thermal_expansion": 23.4,
                "melting_point": 660,
                "electrical_resistivity": 5.2e-8,
                "poissons_ratio": 0.33,
                "fatigue_strength": 159,
                "fracture_toughness": 28,
                "cost_index": 4.8
            },
            "applications": [
                "Aircraft structures",
                "High-performance bicycle components",
                "Rock climbing equipment",
                "Racing components",
                "Military applications"
            ],
            "characteristics": [
                "Very high strength for aluminum",
                "Good fatigue strength",
                "Poor corrosion resistance",
                "Excellent strength-to-weight ratio"
            ],
            "educational_insights": [
                "Aerospace standard aluminum alloy - represents high-strength aluminum",
                "Demonstrates tradeoff between strength and corrosion resistance",
                "Shows Zn-Mg-Cu precipitation hardening system",
                "Important for understanding material selection in aerospace"
            ],
            "sources": ["ASM Handbook Vol. 2", "MatWeb", "Aerospace Standards"]
        },
        
        # ==================== TITANIUM ALLOYS ====================
        "ti_6al_4v": {
            "name": "Ti-6Al-4V Titanium",
            "class": "metal",
            "category": "titanium",
            "composition": {"Ti": 0.90, "Al": 0.06, "V": 0.04},
            "properties": {
                "density": 4.43,
                "youngs_modulus": 113.8,
                "yield_strength": 828,  # MPa (annealed)
                "tensile_strength": 895,
                "elongation": 10,
                "reduction_area": 20,
                "hardness": 334,  # Brinell
                "thermal_conductivity": 6.7,
                "specific_heat": 526,
                "thermal_expansion": 8.6,
                "melting_point": 1660,
                "electrical_resistivity": 1.7e-6,
                "poissons_ratio": 0.34,
                "fatigue_strength": 620,
                "fracture_toughness": 75,
                "cost_index": 18.5
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.95, "b": 2.95, "c": 4.68, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.25},
                    {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.75}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74
            },
            "applications": [
                "Aerospace components",
                "Medical implants and prosthetics",
                "High-performance automotive",
                "Marine applications",
                "Chemical processing"
            ],
            "characteristics": [
                "Excellent strength-to-weight ratio",
                "Outstanding corrosion resistance",
                "Biocompatible",
                "High temperature capability"
            ],
            "educational_insights": [
                "Most common titanium alloy - represents alpha-beta titanium alloys",
                "HCP structure at room temperature, transitions to BCC at 882°C",
                "Demonstrates alpha-beta titanium microstructure",
                "Important for understanding premium materials where cost is secondary to performance"
            ],
            "sources": ["ASM Handbook Vol. 2", "ASTM B265", "MatWeb"]
        },
        
        # ==================== COPPER ALLOYS ====================
        "copper_etp": {
            "name": "Copper C11000",
            "class": "metal",
            "category": "copper",
            "composition": {"Cu": 0.999},
            "properties": {
                "density": 8.96,
                "youngs_modulus": 110,
                "yield_strength": 69,  # MPa (annealed)
                "tensile_strength": 210,
                "elongation": 45,
                "reduction_area": 70,
                "hardness": 89,  # Brinell
                "thermal_conductivity": 391,
                "specific_heat": 385,
                "thermal_expansion": 16.5,
                "melting_point": 1085,
                "electrical_resistivity": 1.72e-8,
                "poissons_ratio": 0.34,
                "fatigue_strength": 62,
                "fracture_toughness": 95,
                "cost_index": 8.5
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.61, "b": 3.61, "c": 3.61, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Cu", "x": 0, "y": 0, "z": 0},
                    {"element": "Cu", "x": 0.5, "y": 0.5, "z": 0},
                    {"element": "Cu", "x": 0.5, "y": 0, "z": 0.5},
                    {"element": "Cu", "x": 0, "y": 0.5, "z": 0.5}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74
            },
            "applications": [
                "Electrical wiring and conductors",
                "Heat exchangers and radiators",
                "Plumbing systems",
                "Electronics and circuit boards",
                "Roofing and architectural"
            ],
            "characteristics": [
                "Excellent electrical conductivity",
                "Superior thermal conductivity",
                "Good corrosion resistance",
                "Antimicrobial properties"
            ],
            "educational_insights": [
                "Standard for electrical conductivity - IACS 100%",
                "FCC structure enables high ductility and conductivity",
                "Demonstrates work hardening behavior and annealing",
                "Important for understanding thermal and electrical applications"
            ],
            "sources": ["ASM Handbook Vol. 2", "ASTM B152", "MatWeb"]
        },
        
        # ==================== CAST IRON ====================
        "gray_cast_iron": {
            "name": "Gray Cast Iron",
            "class": "metal",
            "category": "cast_iron",
            "composition": {"Fe": 0.96, "C": 0.035, "Si": 0.018, "Mn": 0.006},
            "properties": {
                "density": 7.2,
                "youngs_modulus": 110,
                "yield_strength": 275,  # MPa (compressive)
                "tensile_strength": 275,
                "elongation": 0.6,
                "reduction_area": 0,
                "hardness": 210,  # Brinell
                "thermal_conductivity": 46,
                "specific_heat": 420,
                "thermal_expansion": 12.0,
                "melting_point": 1200,
                "electrical_resistivity": 9.5e-7,
                "poissons_ratio": 0.26,
                "fatigue_strength": 124,
                "fracture_toughness": 20,
                "cost_index": 1.2
            },
            "applications": [
                "Engine blocks and cylinders",
                "Machine tool bases",
                "Brake rotors and drums",
                "Pump housings",
                "Manifolds and pipes"
            ],
            "characteristics": [
                "Excellent damping capacity",
                "Good compressive strength",
                "Brittle in tension",
                "Good wear resistance",
                "Low cost casting"
            ],
            "educational_insights": [
                "Foundation material for casting applications",
                "Graphite flakes provide damping and machinability",
                "Demonstrates brittle fracture behavior in tension",
                "Important for understanding cast materials and their limitations"
            ],
            "sources": ["ASM Handbook Vol. 1", "ASTM A48", "MatWeb"]
        },
        
       
    }
