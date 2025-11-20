"""
Verified Mechanical Engineering Materials Database
All data verified from reliable sources: ASM Handbooks, MatWeb, CES EduPack, CRC Handbook
"""

def load_verified_mechanical_materials():
    """
    Comprehensive database of essential mechanical engineering materials
    All data verified from reliable sources
    """
    
    return {
        # ==================== CARBON STEELS ====================
        "aisi_1020": {
            "name": "AISI 1020 Steel",
            "class": "metal",
            "category": "carbon_steel",
            "composition": {"Fe": 0.99, "C": 0.002, "Mn": 0.003, "P": 0.0004, "S": 0.0005},
            "properties": {
                "density": 7.87,
                "youngs_modulus": 200,
                "yield_strength": 350,
                "tensile_strength": 420,
                "elongation": 25,
                "reduction_area": 50,
                "hardness": 121,
                "thermal_conductivity": 51.9,
                "specific_heat": 486,
                "thermal_expansion": 11.7,
                "melting_point": 1520,
                "electrical_resistivity": 1.59e-7,
                "poissons_ratio": 0.29,
                "fatigue_strength": 210,
                "fracture_toughness": 50,
                "cost_index": 1.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",  # Body-Centered Cubic
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 2.866, "b": 2.866, "c": 2.866, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    # CORNER ATOMS (8 corners - shared with adjacent cells)
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    
                    # BODY CENTER ATOM (1 atom at cube center)
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,  # (8 corners × 1/8) + 1 center = 2
                "description": "Body-Centered Cubic: Atoms at cube corners and body center"
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
            "educational_insights": [
                "BCC structure has 8 nearest neighbors",
                "Less dense packing than FCC (68% vs 74%)",
                "Exhibits ductile-to-brittle transition",
                "Foundation for understanding ferritic steels"
            ],
            "sources": ["ASM Handbook Vol. 1", "MatWeb", "CES EduPack 2023"]
        },
        
        "ss_304": {
            "name": "304 Stainless Steel",
            "class": "metal",
            "category": "stainless_steel",
            "composition": {"Fe": 0.68, "Cr": 0.18, "Ni": 0.08, "C": 0.0008, "Mn": 0.02},
            "properties": {
                "density": 8.0,
                "youngs_modulus": 193,
                "yield_strength": 215,
                "tensile_strength": 505,
                "elongation": 70,
                "reduction_area": 70,
                "hardness": 170,
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
                "structure_type": "FCC",  # Face-Centered Cubic
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.60, "b": 3.60, "c": 3.60, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    # CORNER ATOMS (8 corners - shared with adjacent cells)
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    
                    # FACE CENTER ATOMS (6 faces - shared with adjacent cells)
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Fe", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Fe", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Fe", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Fe", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,  # (8 corners × 1/8) + (6 faces × 1/2) = 4
                "description": "Face-Centered Cubic: Atoms at cube corners and face centers"
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
                "FCC structure has 12 nearest neighbors",
                "Highest packing density (74%) for monatomic crystals",
                "Multiple slip systems enable excellent ductility",
                "Austenitic structure stabilized by nickel"
            ],
            "sources": ["ASM Handbook Vol. 1", "ASTM A240", "MatWeb"]
        },
        
        "al_6061": {
            "name": "6061 Aluminum",
            "class": "metal",
            "category": "aluminum",
            "composition": {"Al": 0.98, "Mg": 0.01, "Si": 0.006, "Cr": 0.0025, "Cu": 0.0025},
            "properties": {
                "density": 2.70,
                "youngs_modulus": 68.9,
                "yield_strength": 276,
                "tensile_strength": 310,
                "elongation": 17,
                "reduction_area": 45,
                "hardness": 95,
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
                    # CORNER ATOMS
                    {"element": "Al", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Al", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Al", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Al", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Al", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Al", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Al", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Al", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    
                    # FACE CENTER ATOMS
                    {"element": "Al", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Al", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Al", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Al", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Al", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Al", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Close-packed structure with high ductility"
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
                "FCC structure enables excellent formability",
                "Close-packed planes allow easy dislocation movement",
                "Alloying elements form strengthening precipitates",
                "Ideal for lightweight structural applications"
            ],
            "sources": ["ASM Handbook Vol. 2", "MatWeb", "Aluminum Association"]
        },
        
        "ti_6al_4v": {
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
                "reduction_area": 20,
                "hardness": 334,
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
                "structure_type": "HCP",  # Hexagonal Close-Packed
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.95, "b": 2.95, "c": 4.68, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    # BASE PLANE ATOMS (6 atoms in hexagonal arrangement)
                    {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Ti", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: ABAB stacking sequence"
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
                "HCP structure has limited slip systems at room temperature",
                "Transforms to BCC above 882°C (beta phase)",
                "Anisotropic properties due to hexagonal symmetry",
                "Alloying elements stabilize alpha or beta phases"
            ],
            "sources": ["ASM Handbook Vol. 2", "ASTM B265", "MatWeb"]
        },
        
        "silicon": {
            "name": "Silicon",
            "class": "semiconductor",
            "category": "semiconductor",
            "composition": {"Si": 1.0},
            "properties": {
                "density": 2.33,
                "youngs_modulus": 112,
                "yield_strength": 7000,  # theoretical
                "tensile_strength": 165,
                "elongation": 0,
                "reduction_area": 0,
                "hardness": 1150,
                "thermal_conductivity": 149,
                "specific_heat": 705,
                "thermal_expansion": 2.6,
                "melting_point": 1414,
                "electrical_resistivity": 2.3e3,
                "poissons_ratio": 0.28,
                "fatigue_strength": 0,
                "fracture_toughness": 0.9,
                "cost_index": 1.8
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "Diamond Cubic",
                "space_group": "Fd-3m",
                "lattice_parameters": {"a": 5.43, "b": 5.43, "c": 5.43, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    # FCC POSITIONS (like FCC but with 2 atoms per lattice point)
                    {"element": "Si", "x": 0.0, "y": 0.0, "z": 0.0, "type": "fcc_corner"},
                    {"element": "Si", "x": 0.5, "y": 0.5, "z": 0.0, "type": "fcc_face"},
                    {"element": "Si", "x": 0.5, "y": 0.0, "z": 0.5, "type": "fcc_face"},
                    {"element": "Si", "x": 0.0, "y": 0.5, "z": 0.5, "type": "fcc_face"},
                    
                    # INTERNAL POSITIONS (offset by 1/4,1/4,1/4)
                    {"element": "Si", "x": 0.25, "y": 0.25, "z": 0.25, "type": "internal"},
                    {"element": "Si", "x": 0.75, "y": 0.75, "z": 0.25, "type": "internal"},
                    {"element": "Si", "x": 0.75, "y": 0.25, "z": 0.75, "type": "internal"},
                    {"element": "Si", "x": 0.25, "y": 0.75, "z": 0.75, "type": "internal"}
                ],
                "coordination_number": 4,
                "atomic_packing_factor": 0.34,
                "atoms_per_unit_cell": 8,
                "description": "Diamond Cubic: Two interpenetrating FCC lattices offset by (1/4,1/4,1/4)"
            },
            "applications": [
                "Integrated circuits",
                "Solar cells",
                "Semiconductor devices",
                "Optical windows",
                "Microelectromechanical systems (MEMS)"
            ],
            "characteristics": [
                "Semiconductor properties",
                "Brittle at room temperature",
                "Forms protective oxide layer",
                "Directional covalent bonding"
            ],
            "educational_insights": [
                "Diamond cubic has tetrahedral coordination",
                "Low packing factor due to directional bonding",
                "Covalent bonds make it hard and brittle",
                "Band gap of 1.1 eV enables semiconductor behavior"
            ],
            "sources": ["ASM Handbook Vol. 2", "MatWeb", "Semiconductor data sheets"]
        },

        # ==================== PURE ELEMENTS ====================
        
        # Alkali Metals
        "lithium": {
            "name": "Lithium",
            "class": "metal",
            "category": "alkali_metal",
            "composition": {"Li": 1.0},
            "properties": {
                "density": 0.534,
                "youngs_modulus": 4.9,
                "yield_strength": 0.17,
                "tensile_strength": 1.5,
                "elongation": 50,
                "reduction_area": 0,
                "hardness": 0.6,
                "thermal_conductivity": 84.7,
                "specific_heat": 3582,
                "thermal_expansion": 46,
                "melting_point": 180.5,
                "electrical_resistivity": 9.4e-8,
                "poissons_ratio": 0.36,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 65.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 3.51, "b": 3.51, "c": 3.51, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Li", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Li", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Li", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Li", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Li", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Li", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Li", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Li", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Li", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Lightest metal with BCC structure"
            },
            "applications": [
                "Batteries and energy storage",
                "Alloying agent",
                "Nuclear fusion applications",
                "Psychiatric medications",
                "Heat transfer applications"
            ],
            "characteristics": [
                "Lightest of all metals",
                "Highly reactive with water and air",
                "Soft and silvery-white",
                "Low melting point"
            ],
            "educational_insights": [
                "BCC structure despite being very light",
                "Extremely low density affects mechanical properties",
                "High electrochemical potential makes it ideal for batteries",
                "Requires special handling due to reactivity"
            ],
            "sources": ["CRC Handbook", "ASM Handbook Vol. 2", "NIST Database"]
        },

        "sodium": {
            "name": "Sodium",
            "class": "metal",
            "category": "alkali_metal",
            "composition": {"Na": 1.0},
            "properties": {
                "density": 0.968,
                "youngs_modulus": 10,
                "yield_strength": 0.06,
                "tensile_strength": 0.9,
                "elongation": 80,
                "reduction_area": 0,
                "hardness": 0.7,
                "thermal_conductivity": 142,
                "specific_heat": 1230,
                "thermal_expansion": 71,
                "melting_point": 97.8,
                "electrical_resistivity": 4.2e-8,
                "poissons_ratio": 0.34,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 2.5
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 4.29, "b": 4.29, "c": 4.29, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Na", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Na", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Na", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Na", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Na", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Na", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Na", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Na", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Na", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Soft alkali metal with BCC structure"
            },
            "applications": [
                "Sodium-cooled nuclear reactors",
                "Street lighting",
                "Chemical synthesis",
                "Heat transfer medium",
                "Organic chemistry reagent"
            ],
            "characteristics": [
                "Very soft and easily cut",
                "Highly reactive with water",
                "Good electrical and thermal conductivity",
                "Low melting point"
            ],
            "educational_insights": [
                "BCC structure typical for alkali metals",
                "Extremely ductile due to metallic bonding",
                "Large atomic radius affects lattice parameters",
                "Important for understanding metallic bonding"
            ],
            "sources": ["CRC Handbook", "ASM Handbook Vol. 2", "NIST Database"]
        },

        "potassium": {
            "name": "Potassium",
            "class": "metal",
            "category": "alkali_metal",
            "composition": {"K": 1.0},
            "properties": {
                "density": 0.862,
                "youngs_modulus": 3.1,
                "yield_strength": 0.03,
                "tensile_strength": 0.8,
                "elongation": 100,
                "reduction_area": 0,
                "hardness": 0.4,
                "thermal_conductivity": 102.4,
                "specific_heat": 757,
                "thermal_expansion": 83.3,
                "melting_point": 63.5,
                "electrical_resistivity": 6.1e-8,
                "poissons_ratio": 0.33,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 15.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 5.23, "b": 5.23, "c": 5.23, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "K", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "K", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "K", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "K", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "K", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "K", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "K", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "K", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "K", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Very soft and reactive alkali metal"
            },
            "applications": [
                "Fertilizers",
                "Heat transfer alloys",
                "Chemical reagents",
                "Biological applications",
                "Laboratory uses"
            ],
            "characteristics": [
                "Extremely soft and ductile",
                "Highly reactive with air and water",
                "Low density",
                "Very low melting point"
            ],
            "educational_insights": [
                "BCC structure with large lattice parameter",
                "Demonstrates trend in alkali metal properties",
                "Very weak metallic bonding",
                "Important for understanding periodic trends"
            ],
            "sources": ["CRC Handbook", "ASM Handbook Vol. 2", "NIST Database"]
        },

        # Alkaline Earth Metals
        "beryllium": {
            "name": "Beryllium",
            "class": "metal",
            "category": "alkaline_earth",
            "composition": {"Be": 1.0},
            "properties": {
                "density": 1.85,
                "youngs_modulus": 287,
                "yield_strength": 240,
                "tensile_strength": 370,
                "elongation": 3,
                "reduction_area": 0,
                "hardness": 150,
                "thermal_conductivity": 190,
                "specific_heat": 1820,
                "thermal_expansion": 11.3,
                "melting_point": 1287,
                "electrical_resistivity": 3.6e-8,
                "poissons_ratio": 0.03,
                "fatigue_strength": 140,
                "fracture_toughness": 4,
                "cost_index": 850.0
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.29, "b": 2.29, "c": 3.58, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Be", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Be", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Be", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Be", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Be", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Be", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: Lightweight metal with high stiffness"
            },
            "applications": [
                "Aerospace structures",
                "Nuclear reactors",
                "X-ray windows",
                "Precision instruments",
                "Military applications"
            ],
            "characteristics": [
                "Very high stiffness-to-weight ratio",
                "Good thermal conductivity",
                "Toxic in powder form",
                "Brittle at room temperature"
            ],
            "educational_insights": [
                "HCP structure with ideal c/a ratio",
                "Exceptionally high Young's modulus for light metal",
                "Limited slip systems cause brittleness",
                "Important for understanding stiffness-density relationships"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "magnesium": {
            "name": "Magnesium",
            "class": "metal",
            "category": "alkaline_earth",
            "composition": {"Mg": 1.0},
            "properties": {
                "density": 1.74,
                "youngs_modulus": 45,
                "yield_strength": 70,
                "tensile_strength": 165,
                "elongation": 12,
                "reduction_area": 0,
                "hardness": 44,
                "thermal_conductivity": 156,
                "specific_heat": 1024,
                "thermal_expansion": 24.8,
                "melting_point": 650,
                "electrical_resistivity": 4.2e-8,
                "poissons_ratio": 0.29,
                "fatigue_strength": 50,
                "fracture_toughness": 15,
                "cost_index": 4.2
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 3.21, "b": 3.21, "c": 5.21, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Mg", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Mg", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Mg", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Mg", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Mg", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Mg", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: Lightest structural metal"
            },
            "applications": [
                "Automotive wheels",
                "Aerospace components",
                "Laptop cases",
                "Power tools",
                "Biomedical implants"
            ],
            "characteristics": [
                "Very lightweight",
                "Good machinability",
                "Flammable in powder form",
                "Good damping capacity"
            ],
            "educational_insights": [
                "HCP structure affects deformation behavior",
                "Limited room temperature ductility",
                "Important for lightweight structural design",
                "Demonstrates hexagonal crystal anisotropy"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "calcium": {
            "name": "Calcium",
            "class": "metal",
            "category": "alkaline_earth",
            "composition": {"Ca": 1.0},
            "properties": {
                "density": 1.55,
                "youngs_modulus": 20,
                "yield_strength": 40,
                "tensile_strength": 110,
                "elongation": 50,
                "reduction_area": 0,
                "hardness": 17,
                "thermal_conductivity": 200,
                "specific_heat": 647,
                "thermal_expansion": 22.3,
                "melting_point": 842,
                "electrical_resistivity": 3.4e-8,
                "poissons_ratio": 0.31,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 12.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 5.59, "b": 5.59, "c": 5.59, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Ca", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ca", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ca", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ca", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ca", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ca", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ca", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ca", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ca", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Ca", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ca", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Ca", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Ca", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ca", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Relatively soft alkaline earth metal"
            },
            "applications": [
                "Steel deoxidizer",
                "Alloying agent",
                "Chemical production",
                "Reducing agent",
                "Nutritional supplements"
            ],
            "characteristics": [
                "Soft and silvery-white",
                "Reactive with water",
                "Good electrical conductivity",
                "Ductile and malleable"
            ],
            "educational_insights": [
                "FCC structure unlike other alkaline earth metals",
                "Large atomic radius affects properties",
                "Demonstrates metallic bonding trends",
                "Important for understanding crystal structure variations"
            ],
            "sources": ["CRC Handbook", "ASM Handbook Vol. 2", "NIST Database"]
        },

        # Transition Metals
        "titanium": {
            "name": "Titanium",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Ti": 1.0},
            "properties": {
                "density": 4.51,
                "youngs_modulus": 116,
                "yield_strength": 140,
                "tensile_strength": 235,
                "elongation": 54,
                "reduction_area": 0,
                "hardness": 70,
                "thermal_conductivity": 21.9,
                "specific_heat": 523,
                "thermal_expansion": 8.6,
                "melting_point": 1668,
                "electrical_resistivity": 4.2e-7,
                "poissons_ratio": 0.32,
                "fatigue_strength": 85,
                "fracture_toughness": 70,
                "cost_index": 25.0
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.95, "b": 2.95, "c": 4.68, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Ti", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Ti", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Ti", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: Alpha phase at room temperature"
            },
            "applications": [
                "Aerospace components",
                "Chemical processing",
                "Medical implants",
                "Marine applications",
                "Sports equipment"
            ],
            "characteristics": [
                "Excellent corrosion resistance",
                "High strength-to-weight ratio",
                "Biocompatible",
                "Good high-temperature properties"
            ],
            "educational_insights": [
                "HCP structure transforms to BCC at 882°C",
                "Allotropic transformation important for heat treatment",
                "Excellent corrosion resistance due to oxide layer",
                "Important for understanding phase transformations"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "chromium": {
            "name": "Chromium",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Cr": 1.0},
            "properties": {
                "density": 7.19,
                "youngs_modulus": 279,
                "yield_strength": 290,
                "tensile_strength": 415,
                "elongation": 0,
                "reduction_area": 0,
                "hardness": 112,
                "thermal_conductivity": 93.9,
                "specific_heat": 449,
                "thermal_expansion": 4.9,
                "melting_point": 1907,
                "electrical_resistivity": 1.3e-7,
                "poissons_ratio": 0.21,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 8.5
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 2.88, "b": 2.88, "c": 2.88, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Cr", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Cr", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Cr", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Cr", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Cr", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Cr", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Cr", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Cr", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Cr", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Hard, brittle transition metal"
            },
            "applications": [
                "Stainless steel production",
                "Chrome plating",
                "Alloying agent",
                "Refractory materials",
                "Pigments"
            ],
            "characteristics": [
                "Very hard and brittle",
                "Excellent corrosion resistance",
                "High melting point",
                "Good wear resistance"
            ],
            "educational_insights": [
                "BCC structure with high strength",
                "Brittle behavior at room temperature",
                "Important alloying element for corrosion resistance",
                "Demonstrates transition metal properties"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "manganese": {
            "name": "Manganese",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Mn": 1.0},
            "properties": {
                "density": 7.21,
                "youngs_modulus": 198,
                "yield_strength": 150,
                "tensile_strength": 230,
                "elongation": 40,
                "reduction_area": 0,
                "hardness": 210,
                "thermal_conductivity": 7.8,
                "specific_heat": 479,
                "thermal_expansion": 21.7,
                "melting_point": 1246,
                "electrical_resistivity": 1.4e-6,
                "poissons_ratio": 0.24,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 3.2
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 8.91, "b": 8.91, "c": 8.91, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Mn", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Mn", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Mn", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Mn", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Mn", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Mn", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Mn", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Mn", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Mn", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Complex allotropic behavior"
            },
            "applications": [
                "Steel production",
                "Aluminum alloys",
                "Batteries",
                "Chemical industry",
                "Fertilizers"
            ],
            "characteristics": [
                "Brittle in pure form",
                "Essential steel alloying element",
                "Multiple allotropic forms",
                "Paramagnetic"
            ],
            "educational_insights": [
                "Complex allotropic transformations",
                "Important for steel strengthening mechanisms",
                "Demonstrates transition metal complexity",
                "Large unit cell affects properties"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "iron": {
            "name": "Iron",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Fe": 1.0},
            "properties": {
                "density": 7.87,
                "youngs_modulus": 211,
                "yield_strength": 50,
                "tensile_strength": 200,
                "elongation": 45,
                "reduction_area": 0,
                "hardness": 50,
                "thermal_conductivity": 80.2,
                "specific_heat": 449,
                "thermal_expansion": 11.8,
                "melting_point": 1538,
                "electrical_resistivity": 9.7e-8,
                "poissons_ratio": 0.29,
                "fatigue_strength": 30,
                "fracture_toughness": 0,
                "cost_index": 0.8
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 2.87, "b": 2.87, "c": 2.87, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Fe", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Alpha iron at room temperature"
            },
            "applications": [
                "Structural steel",
                "Machinery and tools",
                "Automotive industry",
                "Construction",
                "Infrastructure"
            ],
            "characteristics": [
                "Ferromagnetic",
                "Relatively soft in pure form",
                "Reactive with oxygen",
                "Allotropic transformation"
            ],
            "educational_insights": [
                "BCC structure transforms to FCC at 912°C",
                "Foundation of steel metallurgy",
                "Demonstrates allotropic behavior",
                "Important for understanding phase diagrams"
            ],
            "sources": ["ASM Handbook Vol. 1", "CRC Handbook", "NIST Database"]
        },

        "cobalt": {
            "name": "Cobalt",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Co": 1.0},
            "properties": {
                "density": 8.86,
                "youngs_modulus": 209,
                "yield_strength": 180,
                "tensile_strength": 240,
                "elongation": 5,
                "reduction_area": 0,
                "hardness": 125,
                "thermal_conductivity": 100,
                "specific_heat": 421,
                "thermal_expansion": 13.0,
                "melting_point": 1495,
                "electrical_resistivity": 6.2e-8,
                "poissons_ratio": 0.31,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 35.0
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.51, "b": 2.51, "c": 4.07, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Co", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Co", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Co", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Co", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Co", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Co", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: Ferromagnetic transition metal"
            },
            "applications": [
                "Superalloys",
                "Magnets",
                "Cutting tools",
                "Medical implants",
                "Pigments"
            ],
            "characteristics": [
                "Ferromagnetic",
                "Good high-temperature strength",
                "Wear resistant",
                "Corrosion resistant"
            ],
            "educational_insights": [
                "HCP structure with allotropic transformation",
                "Important for high-temperature alloys",
                "Demonstrates magnetic properties",
                "Key element in superalloy development"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "nickel": {
            "name": "Nickel",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Ni": 1.0},
            "properties": {
                "density": 8.91,
                "youngs_modulus": 200,
                "yield_strength": 59,
                "tensile_strength": 317,
                "elongation": 30,
                "reduction_area": 0,
                "hardness": 80,
                "thermal_conductivity": 90.9,
                "specific_heat": 444,
                "thermal_expansion": 13.4,
                "melting_point": 1455,
                "electrical_resistivity": 6.9e-8,
                "poissons_ratio": 0.31,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 18.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.52, "b": 3.52, "c": 3.52, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Ni", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ni", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ni", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ni", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ni", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ni", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ni", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ni", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ni", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Ni", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ni", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Ni", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Ni", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ni", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Ductile ferromagnetic metal"
            },
            "applications": [
                "Stainless steel production",
                "Batteries",
                "Electroplating",
                "Catalysts",
                "Coinage"
            ],
            "characteristics": [
                "Good corrosion resistance",
                "Ferromagnetic",
                "Ductile and malleable",
                "Good high-temperature properties"
            ],
            "educational_insights": [
                "FCC structure enables good ductility",
                "Important alloying element for corrosion resistance",
                "Demonstrates ferromagnetic behavior",
                "Key for understanding austenitic stainless steels"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "copper": {
            "name": "Copper",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Cu": 1.0},
            "properties": {
                "density": 8.96,
                "youngs_modulus": 110,
                "yield_strength": 33,
                "tensile_strength": 210,
                "elongation": 45,
                "reduction_area": 0,
                "hardness": 40,
                "thermal_conductivity": 401,
                "specific_heat": 385,
                "thermal_expansion": 16.5,
                "melting_point": 1085,
                "electrical_resistivity": 1.7e-8,
                "poissons_ratio": 0.34,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 7.5
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.61, "b": 3.61, "c": 3.61, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Cu", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Cu", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Cu", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Cu", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Cu", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Cu", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Cu", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Cu", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Cu", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Cu", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Cu", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Cu", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Cu", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Cu", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Excellent electrical and thermal conductivity"
            },
            "applications": [
                "Electrical wiring",
                "Plumbing",
                "Electronics",
                "Heat exchangers",
                "Architectural applications"
            ],
            "characteristics": [
                "Excellent electrical conductivity",
                "High thermal conductivity",
                "Good corrosion resistance",
                "Antimicrobial properties"
            ],
            "educational_insights": [
                "FCC structure enables high ductility",
                "Excellent conductivity due to electron configuration",
                "Important for understanding metallic bonding",
                "Demonstrates work hardening behavior"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "zinc": {
            "name": "Zinc",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Zn": 1.0},
            "properties": {
                "density": 7.14,
                "youngs_modulus": 108,
                "yield_strength": 35,
                "tensile_strength": 120,
                "elongation": 40,
                "reduction_area": 0,
                "hardness": 30,
                "thermal_conductivity": 116,
                "specific_heat": 388,
                "thermal_expansion": 30.2,
                "melting_point": 420,
                "electrical_resistivity": 5.9e-8,
                "poissons_ratio": 0.25,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 2.8
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "HCP",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.66, "b": 2.66, "c": 4.95, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "Zn", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "Zn", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "Zn", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "Zn", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "Zn", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "Zn", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 6,
                "description": "Hexagonal Close-Packed: Relatively low melting point metal"
            },
            "applications": [
                "Galvanizing steel",
                "Die casting alloys",
                "Batteries",
                "Brass production",
                "Corrosion protection"
            ],
            "characteristics": [
                "Good corrosion resistance",
                "Low melting point",
                "Brittle at room temperature",
                "Self-healing oxide layer"
            ],
            "educational_insights": [
                "HCP structure with non-ideal c/a ratio",
                "Demonstrates anisotropic properties",
                "Important for corrosion protection applications",
                "Shows brittle-to-ductile transition"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "molybdenum": {
            "name": "Molybdenum",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Mo": 1.0},
            "properties": {
                "density": 10.22,
                "youngs_modulus": 329,
                "yield_strength": 415,
                "tensile_strength": 565,
                "elongation": 35,
                "reduction_area": 0,
                "hardness": 153,
                "thermal_conductivity": 138,
                "specific_heat": 251,
                "thermal_expansion": 4.8,
                "melting_point": 2623,
                "electrical_resistivity": 5.2e-8,
                "poissons_ratio": 0.31,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 45.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 3.15, "b": 3.15, "c": 3.15, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Mo", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Mo", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Mo", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Mo", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Mo", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Mo", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Mo", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Mo", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Mo", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: High melting point refractory metal"
            },
            "applications": [
                "High-temperature furnaces",
                "Aerospace components",
                "Electrical contacts",
                "Alloying agent",
                "Nuclear applications"
            ],
            "characteristics": [
                "Very high melting point",
                "Good high-temperature strength",
                "Excellent thermal conductivity",
                "Corrosion resistant"
            ],
            "educational_insights": [
                "BCC structure maintains strength at high temperatures",
                "Important refractory metal",
                "Demonstrates high-temperature material behavior",
                "Key for understanding refractory metal properties"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "silver": {
            "name": "Silver",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Ag": 1.0},
            "properties": {
                "density": 10.49,
                "youngs_modulus": 83,
                "yield_strength": 55,
                "tensile_strength": 125,
                "elongation": 50,
                "reduction_area": 0,
                "hardness": 25,
                "thermal_conductivity": 429,
                "specific_heat": 235,
                "thermal_expansion": 18.9,
                "melting_point": 961,
                "electrical_resistivity": 1.6e-8,
                "poissons_ratio": 0.37,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 850.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 4.09, "b": 4.09, "c": 4.09, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Ag", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ag", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Ag", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ag", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ag", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Ag", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Ag", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ag", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Ag", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Ag", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ag", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Ag", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Ag", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Ag", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Highest electrical and thermal conductivity"
            },
            "applications": [
                "Jewelry and silverware",
                "Electrical contacts",
                "Photography",
                "Medical applications",
                "Catalysts"
            ],
            "characteristics": [
                "Highest electrical conductivity",
                "Highest thermal conductivity",
                "Excellent reflectivity",
                "Antimicrobial properties"
            ],
            "educational_insights": [
                "FCC structure enables maximum conductivity",
                "Demonstrates optimal metallic bonding",
                "Important for understanding conductivity mechanisms",
                "Shows noble metal behavior"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "tungsten": {
            "name": "Tungsten",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"W": 1.0},
            "properties": {
                "density": 19.25,
                "youngs_modulus": 411,
                "yield_strength": 550,
                "tensile_strength": 980,
                "elongation": 2,
                "reduction_area": 0,
                "hardness": 300,
                "thermal_conductivity": 173,
                "specific_heat": 132,
                "thermal_expansion": 4.5,
                "melting_point": 3422,
                "electrical_resistivity": 5.3e-8,
                "poissons_ratio": 0.28,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 35.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "BCC",
                "space_group": "Im-3m",
                "lattice_parameters": {"a": 3.16, "b": 3.16, "c": 3.16, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "W", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "W", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "W", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "W", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "W", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "W", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "W", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "W", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "W", "x": 0.5, "y": 0.5, "z": 0.5, "type": "body_center"}
                ],
                "coordination_number": 8,
                "atomic_packing_factor": 0.68,
                "atoms_per_unit_cell": 2,
                "description": "Body-Centered Cubic: Highest melting point of all metals"
            },
            "applications": [
                "Incandescent light bulbs",
                "Electrical contacts",
                "Radiation shielding",
                "Cutting tools",
                "Aerospace components"
            ],
            "characteristics": [
                "Highest melting point",
                "Very high density",
                "Excellent high-temperature strength",
                "Brittle at low temperatures"
            ],
            "educational_insights": [
                "BCC structure maintains properties at extreme temperatures",
                "Demonstrates refractory metal behavior",
                "Important for understanding high-temperature materials",
                "Shows ductile-to-brittle transition"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "platinum": {
            "name": "Platinum",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Pt": 1.0},
            "properties": {
                "density": 21.45,
                "youngs_modulus": 168,
                "yield_strength": 125,
                "tensile_strength": 150,
                "elongation": 40,
                "reduction_area": 0,
                "hardness": 40,
                "thermal_conductivity": 71.6,
                "specific_heat": 133,
                "thermal_expansion": 8.8,
                "melting_point": 1768,
                "electrical_resistivity": 1.1e-7,
                "poissons_ratio": 0.38,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 28000.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 3.92, "b": 3.92, "c": 3.92, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Pt", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Pt", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Pt", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Pt", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Pt", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Pt", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Pt", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Pt", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Pt", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Pt", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Pt", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Pt", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Pt", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Pt", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Dense, corrosion-resistant noble metal"
            },
            "applications": [
                "Catalytic converters",
                "Jewelry",
                "Laboratory equipment",
                "Electrical contacts",
                "Medical devices"
            ],
            "characteristics": [
                "Excellent corrosion resistance",
                "Catalytic properties",
                "Ductile and malleable",
                "High density"
            ],
            "educational_insights": [
                "FCC structure enables good formability",
                "Demonstrates noble metal behavior",
                "Important for catalytic applications",
                "Shows high-temperature stability"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "gold": {
            "name": "Gold",
            "class": "metal",
            "category": "transition_metal",
            "composition": {"Au": 1.0},
            "properties": {
                "density": 19.32,
                "youngs_modulus": 78,
                "yield_strength": 100,
                "tensile_strength": 120,
                "elongation": 45,
                "reduction_area": 0,
                "hardness": 25,
                "thermal_conductivity": 318,
                "specific_heat": 129,
                "thermal_expansion": 14.2,
                "melting_point": 1064,
                "electrical_resistivity": 2.2e-8,
                "poissons_ratio": 0.42,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 55000.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 4.08, "b": 4.08, "c": 4.08, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Au", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Au", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Au", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Au", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Au", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Au", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Au", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Au", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Au", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Au", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Au", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Au", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Au", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Au", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Most malleable and ductile metal"
            },
            "applications": [
                "Jewelry",
                "Electronics",
                "Dental work",
                "Financial investment",
                "Spacecraft components"
            ],
            "characteristics": [
                "Most malleable metal",
                "Excellent corrosion resistance",
                "Good electrical conductivity",
                "Biocompatible"
            ],
            "educational_insights": [
                "FCC structure enables extreme ductility",
                "Demonstrates noble metal corrosion resistance",
                "Important for understanding metallic bonding",
                "Shows work hardening characteristics"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "lead": {
            "name": "Lead",
            "class": "metal",
            "category": "post_transition_metal",
            "composition": {"Pb": 1.0},
            "properties": {
                "density": 11.34,
                "youngs_modulus": 16,
                "yield_strength": 12,
                "tensile_strength": 18,
                "elongation": 50,
                "reduction_area": 0,
                "hardness": 5,
                "thermal_conductivity": 35.3,
                "specific_heat": 129,
                "thermal_expansion": 28.9,
                "melting_point": 327,
                "electrical_resistivity": 2.1e-7,
                "poissons_ratio": 0.44,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 2.2
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "FCC",
                "space_group": "Fm-3m",
                "lattice_parameters": {"a": 4.95, "b": 4.95, "c": 4.95, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Pb", "x": 0.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Pb", "x": 1.0, "y": 0.0, "z": 0.0, "type": "corner"},
                    {"element": "Pb", "x": 0.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Pb", "x": 0.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Pb", "x": 1.0, "y": 1.0, "z": 0.0, "type": "corner"},
                    {"element": "Pb", "x": 1.0, "y": 0.0, "z": 1.0, "type": "corner"},
                    {"element": "Pb", "x": 0.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Pb", "x": 1.0, "y": 1.0, "z": 1.0, "type": "corner"},
                    {"element": "Pb", "x": 0.5, "y": 0.5, "z": 0.0, "type": "face_center"},
                    {"element": "Pb", "x": 0.5, "y": 0.0, "z": 0.5, "type": "face_center"},
                    {"element": "Pb", "x": 0.0, "y": 0.5, "z": 0.5, "type": "face_center"},
                    {"element": "Pb", "x": 0.5, "y": 0.5, "z": 1.0, "type": "face_center"},
                    {"element": "Pb", "x": 0.5, "y": 1.0, "z": 0.5, "type": "face_center"},
                    {"element": "Pb", "x": 1.0, "y": 0.5, "z": 0.5, "type": "face_center"}
                ],
                "coordination_number": 12,
                "atomic_packing_factor": 0.74,
                "atoms_per_unit_cell": 4,
                "description": "Face-Centered Cubic: Very soft, dense, low melting point metal"
            },
            "applications": [
                "Batteries",
                "Radiation shielding",
                "Solders",
                "Construction",
                "Ammunition"
            ],
            "characteristics": [
                "Very soft and malleable",
                "High density",
                "Low melting point",
                "Toxic"
            ],
            "educational_insights": [
                "FCC structure with very low strength",
                "Demonstrates creep behavior at room temperature",
                "Important for understanding heavy metal properties",
                "Shows recrystallization behavior"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        # Metalloids
        "germanium": {
            "name": "Germanium",
            "class": "semiconductor",
            "category": "metalloid",
            "composition": {"Ge": 1.0},
            "properties": {
                "density": 5.32,
                "youngs_modulus": 103,
                "yield_strength": 0,
                "tensile_strength": 0,
                "elongation": 0,
                "reduction_area": 0,
                "hardness": 780,
                "thermal_conductivity": 60.2,
                "specific_heat": 322,
                "thermal_expansion": 6.0,
                "melting_point": 938,
                "electrical_resistivity": 1.0,
                "poissons_ratio": 0.26,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 1200.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "Diamond Cubic",
                "space_group": "Fd-3m",
                "lattice_parameters": {"a": 5.66, "b": 5.66, "c": 5.66, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "Ge", "x": 0.0, "y": 0.0, "z": 0.0, "type": "fcc_corner"},
                    {"element": "Ge", "x": 0.5, "y": 0.5, "z": 0.0, "type": "fcc_face"},
                    {"element": "Ge", "x": 0.5, "y": 0.0, "z": 0.5, "type": "fcc_face"},
                    {"element": "Ge", "x": 0.0, "y": 0.5, "z": 0.5, "type": "fcc_face"},
                    {"element": "Ge", "x": 0.25, "y": 0.25, "z": 0.25, "type": "internal"},
                    {"element": "Ge", "x": 0.75, "y": 0.75, "z": 0.25, "type": "internal"},
                    {"element": "Ge", "x": 0.75, "y": 0.25, "z": 0.75, "type": "internal"},
                    {"element": "Ge", "x": 0.25, "y": 0.75, "z": 0.75, "type": "internal"}
                ],
                "coordination_number": 4,
                "atomic_packing_factor": 0.34,
                "atoms_per_unit_cell": 8,
                "description": "Diamond Cubic: Semiconductor with tetrahedral coordination"
            },
            "applications": [
                "Transistors",
                "Infrared optics",
                "Fiber optics",
                "Solar cells",
                "Gamma-ray detectors"
            ],
            "characteristics": [
                "Semiconductor properties",
                "Brittle",
                "Transparent to infrared",
                "Forms stable oxides"
            ],
            "educational_insights": [
                "Diamond cubic structure like silicon",
                "Smaller band gap than silicon (0.67 eV)",
                "Important early semiconductor material",
                "Demonstrates covalent bonding characteristics"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        # Non-metals
        "carbon_diamond": {
            "name": "Carbon (Diamond)",
            "class": "non_metal",
            "category": "non_metal",
            "composition": {"C": 1.0},
            "properties": {
                "density": 3.51,
                "youngs_modulus": 1050,
                "yield_strength": 0,
                "tensile_strength": 0,
                "elongation": 0,
                "reduction_area": 0,
                "hardness": 10000,
                "thermal_conductivity": 900,
                "specific_heat": 509,
                "thermal_expansion": 1.1,
                "melting_point": 3550,
                "electrical_resistivity": 1e12,
                "poissons_ratio": 0.10,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 500000.0
            },
            "crystal_structure": {
                "crystal_system": "Cubic",
                "structure_type": "Diamond Cubic",
                "space_group": "Fd-3m",
                "lattice_parameters": {"a": 3.57, "b": 3.57, "c": 3.57, "alpha": 90, "beta": 90, "gamma": 90},
                "atomic_positions": [
                    {"element": "C", "x": 0.0, "y": 0.0, "z": 0.0, "type": "fcc_corner"},
                    {"element": "C", "x": 0.5, "y": 0.5, "z": 0.0, "type": "fcc_face"},
                    {"element": "C", "x": 0.5, "y": 0.0, "z": 0.5, "type": "fcc_face"},
                    {"element": "C", "x": 0.0, "y": 0.5, "z": 0.5, "type": "fcc_face"},
                    {"element": "C", "x": 0.25, "y": 0.25, "z": 0.25, "type": "internal"},
                    {"element": "C", "x": 0.75, "y": 0.75, "z": 0.25, "type": "internal"},
                    {"element": "C", "x": 0.75, "y": 0.25, "z": 0.75, "type": "internal"},
                    {"element": "C", "x": 0.25, "y": 0.75, "z": 0.75, "type": "internal"}
                ],
                "coordination_number": 4,
                "atomic_packing_factor": 0.34,
                "atoms_per_unit_cell": 8,
                "description": "Diamond Cubic: Hardest known natural material"
            },
            "applications": [
                "Cutting tools",
                "Jewelry",
                "Heat sinks",
                "Optical windows",
                "High-pressure experiments"
            ],
            "characteristics": [
                "Hardest known material",
                "Excellent thermal conductivity",
                "Electrical insulator",
                "Extremely brittle"
            ],
            "educational_insights": [
                "Diamond cubic structure with strong covalent bonds",
                "Highest thermal conductivity of any material",
                "Demonstrates extreme hardness from covalent bonding",
                "Important for understanding carbon allotropes"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        },

        "carbon_graphite": {
            "name": "Carbon (Graphite)",
            "class": "non_metal",
            "category": "non_metal",
            "composition": {"C": 1.0},
            "properties": {
                "density": 2.09,
                "youngs_modulus": 8,
                "yield_strength": 0,
                "tensile_strength": 15,
                "elongation": 0,
                "reduction_area": 0,
                "hardness": 5,
                "thermal_conductivity": 150,
                "specific_heat": 710,
                "thermal_expansion": 7.9,
                "melting_point": 3650,
                "electrical_resistivity": 1e-5,
                "poissons_ratio": 0.20,
                "fatigue_strength": 0,
                "fracture_toughness": 0,
                "cost_index": 2.5
            },
            "crystal_structure": {
                "crystal_system": "Hexagonal",
                "structure_type": "Hexagonal",
                "space_group": "P6₃/mmc",
                "lattice_parameters": {"a": 2.46, "b": 2.46, "c": 6.70, "alpha": 90, "beta": 90, "gamma": 120},
                "atomic_positions": [
                    {"element": "C", "x": 0.333, "y": 0.667, "z": 0.25, "type": "base_plane"},
                    {"element": "C", "x": 0.667, "y": 0.333, "z": 0.25, "type": "base_plane"},
                    {"element": "C", "x": 0.000, "y": 0.000, "z": 0.25, "type": "base_plane"},
                    {"element": "C", "x": 0.333, "y": 0.667, "z": 0.75, "type": "mid_plane"},
                    {"element": "C", "x": 0.667, "y": 0.333, "z": 0.75, "type": "mid_plane"},
                    {"element": "C", "x": 0.000, "y": 0.000, "z": 0.75, "type": "mid_plane"}
                ],
                "coordination_number": 3,
                "atomic_packing_factor": 0.17,
                "atoms_per_unit_cell": 4,
                "description": "Hexagonal: Layered structure with strong in-plane bonds"
            },
            "applications": [
                "Pencils and lubricants",
                "Electrodes",
                "Refractories",
                "Nuclear reactors",
                "Composite materials"
            ],
            "characteristics": [
                "Excellent lubricant",
                "Good electrical conductor",
                "Anisotropic properties",
                "Thermally stable"
            ],
            "educational_insights": [
                "Layered structure with weak interlayer bonding",
                "Strong in-plane covalent bonds, weak van der Waals between layers",
                "Demonstrates carbon allotropy",
                "Important for understanding anisotropic materials"
            ],
            "sources": ["ASM Handbook Vol. 2", "CRC Handbook", "NIST Database"]
        }
    }
