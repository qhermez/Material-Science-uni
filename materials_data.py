"""
Mechanical Engineering Materials Database
Complete dataset for mechanical engineering students
"""

def load_mechanical_engineering_materials():
    """Load all essential materials for mechanical engineering students"""
    
    materials_data = {
        # CARBON & ALLOY STEELS
        "low_carbon_steel": {
            "name": "Low Carbon Steel (AISI 1020)",
            "class": "metal",
            "category": "steel",
            "composition": {"Fe": 0.99, "C": 0.002, "Mn": 0.003},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 350,
                "tensile_strength": 420,
                "elongation": 25,
                "hardness": 121,
                "thermal_conductivity": 51.9,
                "melting_point": 1520,
                "electrical_resistivity": 1.5e-7,
                "cost": 0.8,
                "fatigue_strength": 210
            },
            "applications": [
                "Car body panels",
                "Structural beams", 
                "Pipes and tubing",
                "Bolts and fasteners",
                "Machine frames"
            ],
            "characteristics": [
                "Excellent weldability and formability",
                "Good ductility and toughness",
                "Low cost and widely available",
                "Can be case hardened"
            ],
            "educational_insights": [
                "Most common structural steel - foundation material",
                "Demonstrates ferrite-pearlite microstructure",
                "Good balance of strength and ductility for general applications",
                "Surface hardening possible via carburizing"
            ],
            "manufacturing_notes": {
                "machinability": "Good",
                "weldability": "Excellent", 
                "formability": "Excellent",
                "heat_treatment": "Case hardening only"
            }
        },
        
        "medium_carbon_steel": {
            "name": "Medium Carbon Steel (AISI 1040)",
            "class": "metal",
            "category": "steel", 
            "composition": {"Fe": 0.98, "C": 0.004, "Mn": 0.006},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 415,
                "tensile_strength": 620,
                "elongation": 25,
                "hardness": 149,
                "thermal_conductivity": 51.2,
                "melting_point": 1520,
                "electrical_resistivity": 1.6e-7,
                "cost": 0.9,
                "fatigue_strength": 240
            },
            "applications": [
                "Shafts and axles",
                "Gears and sprockets",
                "Connecting rods",
                "Machine parts",
                "High-strength bolts"
            ],
            "characteristics": [
                "Good balance of strength and ductility",
                "Responds well to heat treatment",
                "Good wear resistance when hardened",
                "Versatile for many applications"
            ],
            "educational_insights": [
                "Workhorse material for machine components",
                "Demonstrates quench and temper heat treatment",
                "Shows pearlite-ferrite microstructure with more pearlite than 1020",
                "Ideal for understanding heat treatment principles"
            ],
            "manufacturing_notes": {
                "machinability": "Good",
                "weldability": "Good (preheat recommended)",
                "formability": "Good",
                "heat_treatment": "Quench and temper"
            }
        },
        
        "high_carbon_steel": {
            "name": "High Carbon Steel (AISI 1095)",
            "class": "metal",
            "category": "steel",
            "composition": {"Fe": 0.98, "C": 0.0095, "Mn": 0.003},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 550,
                "tensile_strength": 980,
                "elongation": 9,
                "hardness": 248,
                "thermal_conductivity": 49.8,
                "melting_point": 1520,
                "electrical_resistivity": 1.7e-7,
                "cost": 1.2,
                "fatigue_strength": 350
            },
            "applications": [
                "Cutting tools and blades",
                "Springs and high-stress components",
                "Wear-resistant parts",
                "Knives and tools",
                "Ball bearings"
            ],
            "characteristics": [
                "Very high strength and hardness",
                "Poor ductility and toughness",
                "Excellent wear resistance",
                "Can be heat treated to high hardness"
            ],
            "educational_insights": [
                "Demonstrates strength-ductility tradeoff clearly",
                "Shows pearlite-cementite microstructure",
                "Foundation for understanding tool steels",
                "Important for wear and cutting applications"
            ],
            "manufacturing_notes": {
                "machinability": "Fair (annealed state)",
                "weldability": "Poor (cracking risk)",
                "formability": "Poor",
                "heat_treatment": "Full hardening"
            }
        },
        
        "alloy_steel_4140": {
            "name": "Alloy Steel 4140",
            "class": "metal",
            "category": "steel",
            "composition": {"Fe": 0.96, "C": 0.004, "Cr": 0.01, "Mo": 0.002, "Mn": 0.008},
            "properties": {
                "density": 7.85,
                "youngs_modulus": 200,
                "yield_strength": 655,
                "tensile_strength": 1020,
                "elongation": 17,
                "hardness": 197,
                "thermal_conductivity": 42.7,
                "melting_point": 1427,
                "electrical_resistivity": 2.2e-7,
                "cost": 1.8,
                "fatigue_strength": 480
            },
            "applications": [
                "High-strength shafts and axles",
                "Gears and sprockets",
                "Bolts and fasteners",
                "Machine tool components",
                "Automotive crankshafts"
            ],
            "characteristics": [
                "Excellent strength-toughness combination",
                "Deep hardenability due to alloying elements",
                "Good fatigue resistance",
                "Oil-hardenable"
            ],
            "educational_insights": [
                "Industry standard for high-strength components",
                "Demonstrates effects of Cr and Mo on hardenability",
                "Shows tempered martensite microstructure",
                "Important for understanding alloy design"
            ],
            "manufacturing_notes": {
                "machinability": "Good (annealed)",
                "weldability": "Fair (preheat and postheat required)",
                "formability": "Fair",
                "heat_treatment": "Quench and temper"
            }
        },
        
        # STAINLESS STEELS
        "stainless_304": {
            "name": "304 Stainless Steel",
            "class": "metal",
            "category": "stainless_steel",
            "composition": {"Fe": 0.68, "Cr": 0.18, "Ni": 0.08, "C": 0.0008},
            "properties": {
                "density": 8.0,
                "youngs_modulus": 193,
                "yield_strength": 215,
                "tensile_strength": 505,
                "elongation": 70,
                "hardness": 170,
                "thermal_conductivity": 16.2,
                "melting_point": 1400,
                "electrical_resistivity": 7.2e-7,
                "cost": 3.0,
                "fatigue_strength": 240
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
                "Most common stainless steel - austenitic type",
                "Chromium >10.5% enables passive oxide layer",
                "Nickel stabilizes FCC austenitic structure",
                "Demonstrates corrosion mechanisms and prevention"
            ],
            "manufacturing_notes": {
                "machinability": "Poor (work hardens quickly)",
                "weldability": "Excellent",
                "formability": "Excellent",
                "heat_treatment": "Solution annealing only"
            }
        },
        
        "stainless_316": {
            "name": "316 Stainless Steel",
            "class": "metal", 
            "category": "stainless_steel",
            "composition": {"Fe": 0.665, "Cr": 0.17, "Ni": 0.12, "Mo": 0.025, "C": 0.0008},
            "properties": {
                "density": 8.0,
                "youngs_modulus": 193,
                "yield_strength": 240,
                "tensile_strength": 550,
                "elongation": 50,
                "hardness": 217,
                "thermal_conductivity": 16.3,
                "melting_point": 1400,
                "electrical_resistivity": 7.4e-7,
                "cost": 4.5,
                "fatigue_strength": 260
            },
            "applications": [
                "Marine components and fittings",
                "Chemical processing equipment",
                "Pharmaceutical equipment",
                "Medical implants",
                "Coastal architecture"
            ],
            "characteristics": [
                "Superior corrosion resistance (especially to chlorides)",
                "Marine grade stainless",
                "Good high-temperature strength",
                "Excellent pitting resistance"
            ],
            "educational_insights": [
                "Molybdenum addition improves chloride resistance",
                "Demonstrates alloying effects on corrosion resistance",
                "Shows how small composition changes create property differences",
                "Important for chemical and marine applications"
            ],
            "manufacturing_notes": {
                "machinability": "Poor",
                "weldability": "Excellent",
                "formability": "Excellent", 
                "heat_treatment": "Solution annealing"
            }
        },
        
        # ALUMINUM ALLOYS
        "aluminum_6061": {
            "name": "6061 Aluminum",
            "class": "metal",
            "category": "aluminum",
            "composition": {"Al": 0.98, "Mg": 0.01, "Si": 0.006},
            "properties": {
                "density": 2.70,
                "youngs_modulus": 68.9,
                "yield_strength": 276,
                "tensile_strength": 310,
                "elongation": 17,
                "hardness": 95,
                "thermal_conductivity": 167,
                "melting_point": 660,
                "electrical_resistivity": 3.7e-8,
                "cost": 2.5,
                "fatigue_strength": 96
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
                "Most common structural aluminum alloy",
                "Demonstrates precipitation hardening (T6 temper)",
                "Shows FCC crystal structure benefits",
                "Important for lightweight design principles"
            ],
            "manufacturing_notes": {
                "machinability": "Good",
                "weldability": "Excellent",
                "formability": "Good",
                "heat_treatment": "Precipitation hardening (T6)"
            }
        },
        
        "aluminum_7075": {
            "name": "7075 Aluminum",
            "class": "metal",
            "category": "aluminum",
            "composition": {"Al": 0.90, "Zn": 0.06, "Mg": 0.025, "Cu": 0.016},
            "properties": {
                "density": 2.81,
                "youngs_modulus": 71.7,
                "yield_strength": 503,
                "tensile_strength": 572,
                "elongation": 11,
                "hardness": 150,
                "thermal_conductivity": 130,
                "melting_point": 660,
                "electrical_resistivity": 5.2e-8,
                "cost": 4.0,
                "fatigue_strength": 159
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
                "Aerospace standard aluminum alloy",
                "Demonstrates high-strength aluminum capabilities",
                "Shows tradeoff between strength and corrosion resistance",
                "Important for understanding material selection in aerospace"
            ],
            "manufacturing_notes": {
                "machinability": "Fair",
                "weldability": "Poor",
                "formability": "Fair",
                "heat_treatment": "Precipitation hardening"
            }
        },
        
        # TITANIUM ALLOYS
        "titanium_64": {
            "name": "Ti-6Al-4V Titanium",
            "class": "metal",
            "category": "titanium",
            "composition": {"Ti": 0.90, "Al": 0.06, "V": 0.04},
            "properties": {
                "density": 4.43,
                "youngs_modulus": 113.8,
                "yield_strength": 828,
                "tensile_strength": 895,
                "elongation": 10,
                "hardness": 334,
                "thermal_conductivity": 6.7,
                "melting_point": 1660,
                "electrical_resistivity": 1.7e-6,
                "cost": 15.0,
                "fatigue_strength": 620
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
                "Most common titanium alloy - workhorse material",
                "HCP structure at room temperature, transitions to BCC at 882°C",
                "Demonstrates alpha-beta titanium microstructure",
                "Important for premium applications where cost is secondary"
            ],
            "manufacturing_notes": {
                "machinability": "Poor",
                "weldability": "Good (inert atmosphere)",
                "formability": "Fair",
                "heat_treatment": "Solution treat and age"
            }
        },
        
        # COPPER ALLOYS
        "copper_etp": {
            "name": "Copper C11000",
            "class": "metal",
            "category": "copper",
            "composition": {"Cu": 0.999},
            "properties": {
                "density": 8.96,
                "youngs_modulus": 110,
                "yield_strength": 69,
                "tensile_strength": 210,
                "elongation": 45,
                "hardness": 89,
                "thermal_conductivity": 401,
                "melting_point": 1085,
                "electrical_resistivity": 1.7e-8,
                "cost": 8.5,
                "fatigue_strength": 62
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
                "Standard for electrical conductivity",
                "FCC structure enables high ductility and conductivity",
                "Demonstrates work hardening behavior",
                "Important for thermal and electrical applications"
            ],
            "manufacturing_notes": {
                "machinability": "Poor (gummy)",
                "weldability": "Excellent",
                "formability": "Excellent",
                "heat_treatment": "Annealing only"
            }
        },
        
        "brass_360": {
            "name": "Brass C36000",
            "class": "metal",
            "category": "copper",
            "composition": {"Cu": 0.61, "Zn": 0.035, "Pb": 0.003},
            "properties": {
                "density": 8.50,
                "youngs_modulus": 97,
                "yield_strength": 124,
                "tensile_strength": 338,
                "elongation": 53,
                "hardness": 78,
                "thermal_conductivity": 115,
                "melting_point": 930,
                "electrical_resistivity": 6.2e-8,
                "cost": 4.5,
                "fatigue_strength": 125
            },
            "applications": [
                "Fittings and valves",
                "Decorative hardware",
                "Gears and bearings",
                "Electrical connectors",
                "Musical instruments"
            ],
            "characteristics": [
                "Excellent machinability",
                "Good corrosion resistance",
                "Attractive gold-like appearance",
                "Good strength and ductility"
            ],
            "educational_insights": [
                "Free-machining brass with lead addition",
                "Demonstrates alpha-beta brass microstructure",
                "Shows how alloying improves manufacturability",
                "Important for understanding non-ferrous alloys"
            ],
            "manufacturing_notes": {
                "machinability": "Excellent",
                "weldability": "Fair",
                "formability": "Good",
                "heat_treatment": "Stress relief only"
            }
        },
        
        # CAST IRON
        "gray_cast_iron": {
            "name": "Gray Cast Iron",
            "class": "metal",
            "category": "cast_iron", 
            "composition": {"Fe": 0.96, "C": 0.035, "Si": 0.018},
            "properties": {
                "density": 7.2,
                "youngs_modulus": 110,
                "yield_strength": 275,
                "tensile_strength": 275,
                "elongation": 0.6,
                "hardness": 210,
                "thermal_conductivity": 46,
                "melting_point": 1200,
                "electrical_resistivity": 9.5e-7,
                "cost": 1.0,
                "fatigue_strength": 124
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
                "Demonstrates brittle fracture behavior",
                "Important for understanding cast materials"
            ],
            "manufacturing_notes": {
                "machinability": "Excellent",
                "weldability": "Poor",
                "formability": "None (casting only)",
                "heat_treatment": "Stress relief only"
            }
        },
        
        # POLYMERS
        "abs_plastic": {
            "name": "ABS Plastic",
            "class": "polymer",
            "category": "thermoplastic",
            "composition": {"Acrylonitrile": 0.20, "Butadiene": 0.25, "Styrene": 0.55},
            "properties": {
                "density": 1.05,
                "youngs_modulus": 2.3,
                "yield_strength": 45,
                "tensile_strength": 40,
                "elongation": 25,
                "hardness": 105,
                "thermal_conductivity": 0.25,
                "melting_point": 105,
                "electrical_resistivity": 1e14,
                "cost": 2.0,
                "fatigue_strength": 28
            },
            "applications": [
                "Automotive trim and dashboards",
                "Electronic enclosures",
                "Consumer products and toys",
                "Pipes and fittings",
                "Protective headgear"
            ],
            "characteristics": [
                "Good impact strength and toughness",
                "Easily injection molded",
                "Good surface finish",
                "Moderate temperature resistance"
            ],
            "educational_insights": [
                "Common engineering thermoplastic",
                "Demonstrates polymer toughness from rubber particles",
                "Shows amorphous polymer structure",
                "Important for injection molding applications"
            ],
            "manufacturing_notes": {
                "machinability": "Good",
                "weldability": "Good (ultrasonic/solvent)",
                "formability": "Good (injection molding)",
                "heat_treatment": "None"
            }
        },
        
        "nylon_66": {
            "name": "Nylon 6/6",
            "class": "polymer",
            "category": "thermoplastic",
            "composition": {"Polyamide": 1.0},
            "properties": {
                "density": 1.14,
                "youngs_modulus": 3.0,
                "yield_strength": 70,
                "tensile_strength": 80,
                "elongation": 60,
                "hardness": 118,
                "thermal_conductivity": 0.25,
                "melting_point": 265,
                "electrical_resistivity": 1e13,
                "cost": 3.5,
                "fatigue_strength": 35
            },
            "applications": [
                "Gears and bearings",
                "Fasteners and screws",
                "Bushings and wear pads",
                "Electrical insulators",
                "Textile fibers"
            ],
            "characteristics": [
                "Good strength and stiffness",
                "Excellent wear resistance",
                "Absorbs moisture (dimensional changes)",
                "Good fatigue resistance"
            ],
            "educational_insights": [
                "Crystalline thermoplastic with good mechanical properties",
                "Demonstrates polymer wear applications",
                "Shows moisture absorption effects on properties",
                "Important for understanding engineering plastics"
            ],
            "manufacturing_notes": {
                "machinability": "Excellent",
                "weldability": "Good",
                "formability": "Good (injection molding)",
                "heat_treatment": "None"
            }
        }
    }
    
    return materials_data


def load_mechanical_crystal_structures():
    """Load crystal structure data for mechanical engineering materials"""
    
    crystal_structures = {
        "low_carbon_steel": {
            "crystal_system": "Cubic",
            "structure_type": "BCC",
            "space_group": "Im-3m",
            "lattice_parameters": {"a": 2.87, "b": 2.87, "c": 2.87, "alpha": 90, "beta": 90, "gamma": 90},
            "atomic_positions": [
                {"element": "Fe", "x": 0, "y": 0, "z": 0},
                {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5}
            ],
            "coordination_number": 8,
            "atomic_packing_factor": 0.68,
            "slip_systems": ["{110}<111>", "{112}<111>"],
            "close_packed_directions": ["<111>"],
            "close_packed_planes": ["{110}"]
        },
        
        "medium_carbon_steel": {
            "crystal_system": "Cubic",
            "structure_type": "BCC",
            "space_group": "Im-3m", 
            "lattice_parameters": {"a": 2.87, "b": 2.87, "c": 2.87, "alpha": 90, "beta": 90, "gamma": 90},
            "atomic_positions": [
                {"element": "Fe", "x": 0, "y": 0, "z": 0},
                {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5}
            ],
            "coordination_number": 8,
            "atomic_packing_factor": 0.68,
            "slip_systems": ["{110}<111>", "{112}<111>"],
            "close_packed_directions": ["<111>"],
            "close_packed_planes": ["{110}"]
        },
        
        "stainless_304": {
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
            "atomic_packing_factor": 0.74,
            "slip_systems": ["{111}<110>"],
            "close_packed_directions": ["<110>"],
            "close_packed_planes": ["{111}"]
        },
        
        "aluminum_6061": {
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
            "atomic_packing_factor": 0.74,
            "slip_systems": ["{111}<110>"],
            "close_packed_directions": ["<110>"],
            "close_packed_planes": ["{111}"]
        },
        
        "titanium_64": {
            "crystal_system": "Hexagonal",
            "structure_type": "HCP",
            "space_group": "P6₃/mmc",
            "lattice_parameters": {"a": 2.95, "b": 2.95, "c": 4.68, "alpha": 90, "beta": 90, "gamma": 120},
            "atomic_positions": [
                {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.25},
                {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.75}
            ],
            "coordination_number": 12,
            "atomic_packing_factor": 0.74,
            "slip_systems": ["{0001}<1120>", "{1010}<1120>"],
            "close_packed_directions": ["<1120>"],
            "close_packed_planes": ["{0001}"]
        },
        
        "copper_etp": {
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
            "atomic_packing_factor": 0.74,
            "slip_systems": ["{111}<110>"],
            "close_packed_directions": ["<110>"],
            "close_packed_planes": ["{111}"]
        }
    }
    
    return crystal_structures


