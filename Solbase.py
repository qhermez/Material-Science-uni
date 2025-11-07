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
        }
    }
