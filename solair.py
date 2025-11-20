import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from typing import Dict, List, Any

# Import the database
from Solbase import load_verified_mechanical_materials
logo = "logo.png"

# =============================================================================
# 3D VISUALIZATION FUNCTIONS
# =============================================================================

def create_crystal_structure_plot(crystal_data: Dict, material_name: str) -> go.Figure:
    """Create complete 3D crystal structure visualization with all atoms"""
    
    if not crystal_data or not crystal_data.get("atomic_positions"):
        fig = go.Figure()
        fig.add_annotation(
            text="Crystal structure data not available for this material",
            xref="paper", yref="paper",
            x=0.5, y=0.5,
            showarrow=False,
            font=dict(size=16)
        )
        return fig
    
    lattice = crystal_data["lattice_parameters"]
    atoms = crystal_data["atomic_positions"]
    
    fig = go.Figure()
    
    # Element colors and sizes
    element_colors = {
        'Fe': '#FFA500', 'Al': '#BFBFBF', 'Si': '#F0E68C', 'O': '#FF0000',
        'Ti': '#808080', 'Cu': '#B87333', 'Cr': '#8DB6CD', 'Ni': '#50C878',
        'Mg': '#8A2BE2', 'C': '#000000', 'Mn': '#9ACD32'
    }
    
    # Atom sizes based on type
    atom_sizes = {
        'corner': 12, 'body_center': 15, 'face_center': 14,
        'base_plane': 12, 'mid_plane': 12, 'fcc_corner': 12,
        'fcc_face': 14, 'internal': 13
    }
    
    # Add atoms with different colors and sizes based on type
    for atom in atoms:
        element = atom["element"]
        atom_type = atom.get("type", "unknown")
        
        # Convert fractional to absolute coordinates
        x_abs = atom["x"] * lattice["a"]
        y_abs = atom["y"] * lattice["b"] 
        z_abs = atom["z"] * lattice["c"]
        
        # Determine color based on atom type
        if atom_type == "corner":
            color = element_colors.get(element, '#FF6B6B')  # Red for corners
            name_suffix = " (Corner)"
        elif atom_type == "body_center":
            color = element_colors.get(element, '#4ECDC4')  # Teal for body center
            name_suffix = " (Body Center)"
        elif atom_type == "face_center":
            color = element_colors.get(element, '#45B7D1')  # Blue for face centers
            name_suffix = " (Face Center)"
        elif atom_type in ["base_plane", "mid_plane"]:
            color = element_colors.get(element, '#96CEB4')  # Green for HCP planes
            name_suffix = f" ({atom_type.replace('_', ' ').title()})"
        elif atom_type == "internal":
            color = element_colors.get(element, '#FECA57')  # Yellow for internal
            name_suffix = " (Internal)"
        else:
            color = element_colors.get(element, '#FF00FF')  # Magenta for unknown
            name_suffix = ""
        
        fig.add_trace(go.Scatter3d(
            x=[x_abs], y=[y_abs], z=[z_abs],
            mode='markers',
            marker=dict(
                size=atom_sizes.get(atom_type, 12),
                color=color,
                opacity=0.9,
                line=dict(width=2, color='darkgray')
            ),
            name=f'{element}{name_suffix}',
            hovertemplate=(
                f'Element: {element}<br>'
                f'Type: {atom_type}<br>'
                f'Position: ({atom["x"]:.3f}, {atom["y"]:.3f}, {atom["z"]:.3f})<br>'
                f'Absolute: ({x_abs:.2f}, {y_abs:.2f}, {z_abs:.2f}) Å<br>'
                '<extra></extra>'
            )
        ))
    
    # Add unit cell edges
    unit_cell_edges = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],  # Bottom face
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1],  # Top face
        [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 1]  # Vertical edges
    ]
    
    edges_x, edges_y, edges_z = [], [], []
    for edge in unit_cell_edges:
        edges_x.append(edge[0] * lattice["a"])
        edges_y.append(edge[1] * lattice["b"])
        edges_z.append(edge[2] * lattice["c"])
    
    fig.add_trace(go.Scatter3d(
        x=edges_x, y=edges_y, z=edges_z,
        mode='lines',
        line=dict(color='black', width=4),
        name='Unit Cell',
        showlegend=False,
        hoverinfo='none'
    ))
    
    # Add crystal information to title
    structure_info = crystal_data.get("description", "")
    atoms_per_cell = crystal_data.get("atoms_per_unit_cell", "")
    coordination = crystal_data.get("coordination_number", "")
    
    title = f"{material_name} - {crystal_data['structure_type']} Crystal Structure"
    if atoms_per_cell:
        title += f" ({atoms_per_cell} atoms/unit cell)"
    
    fig.update_layout(
        title=title,
        scene=dict(
            xaxis_title="X (Å)",
            yaxis_title="Y (Å)", 
            zaxis_title="Z (Å)",
            aspectmode='data',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        height=600,
        showlegend=True,
        margin=dict(l=0, r=0, b=0, t=40)
    )
    
    return fig

# =============================================================================
# MAIN APPLICATION CLASS
# =============================================================================

class MechanicalEngineeringMaterialsApp:
    def __init__(self):
        self.materials_data = load_verified_mechanical_materials()
    
    def display_material_details(self, material_key: str):
        """Display detailed material information"""
        material = self.materials_data[material_key]
        
        st.header(f"🔬 {material['name']}")
        st.caption(f"Category: {material['category'].replace('_', ' ').title()} • Class: {material['class'].title()}")
        
        # Create tabs
        tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
            "📊 Properties", "🔬 Crystal Structure", "🏗️ Applications", 
            "🧪 Composition", "🎓 Educational", "📚 Sources"
        ])
        
        with tab1:
            self.display_properties(material)
        
        with tab2:
            self.display_crystal_structure(material, material_key)
        
        with tab3:
            self.display_applications(material)
        
        with tab4:
            self.display_composition(material)
        
        with tab5:
            self.display_educational(material)
        
        with tab6:
            self.display_sources(material)
    
    def display_properties(self, material: Dict):
        """Display material properties"""
        props = material["properties"]
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.subheader("📐 Basic Properties")
            st.metric("Density", f"{props['density']} g/cm³")
            st.metric("Young's Modulus", f"{props['youngs_modulus']} GPa")
            st.metric("Poisson's Ratio", f"{props['poissons_ratio']}")
            st.metric("Melting Point", f"{props['melting_point']} °C")
        
        with col2:
            st.subheader("💪 Mechanical Properties")
            st.metric("Yield Strength", f"{props['yield_strength']} MPa")
            st.metric("Tensile Strength", f"{props['tensile_strength']} MPa")
            st.metric("Elongation", f"{props['elongation']} %")
            st.metric("Hardness", f"{props['hardness']} BHN")
            st.metric("Fatigue Strength", f"{props['fatigue_strength']} MPa")
        
        with col3:
            st.subheader("🔥 Thermal & Electrical")
            st.metric("Thermal Conductivity", f"{props['thermal_conductivity']} W/m·K")
            st.metric("Thermal Expansion", f"{props['thermal_expansion']} μm/m·K")
            st.metric("Electrical Resistivity", f"{props['electrical_resistivity']:.2e} Ω·m")
            st.metric("Fracture Toughness", f"{props['fracture_toughness']} MPa√m")
            
    
    def display_crystal_structure(self, material: Dict, material_key: str):
        """Display crystal structure"""
        if "crystal_structure" in material:
            crystal_data = material["crystal_structure"]
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Crystal Information")
                st.write(f"**Crystal System**: {crystal_data['crystal_system']}")
                st.write(f"**Structure Type**: {crystal_data['structure_type']}")
                st.write(f"**Space Group**: {crystal_data['space_group']}")
                st.write(f"**Coordination Number**: {crystal_data['coordination_number']}")
                st.write(f"**Atomic Packing Factor**: {crystal_data['atomic_packing_factor']}")
                st.write(f"**Atoms per Unit Cell**: {crystal_data.get('atoms_per_unit_cell', 'N/A')}")
                
                if "description" in crystal_data:
                    st.info(f"**Structure Description**: {crystal_data['description']}")
                
                st.subheader("Lattice Parameters")
                lat = crystal_data["lattice_parameters"]
                st.write(f"**a**: {lat['a']} Å")
                st.write(f"**b**: {lat['b']} Å")
                st.write(f"**c**: {lat['c']} Å")
                st.write(f"**α**: {lat['alpha']}°")
                st.write(f"**β**: {lat['beta']}°")
                st.write(f"**γ**: {lat['gamma']}°")
            
            with col2:
                st.subheader("3D Crystal Structure")
                fig = create_crystal_structure_plot(crystal_data, material["name"])
                st.plotly_chart(fig, use_container_width=True)
                
                
    def display_applications(self, material: Dict):
        """Display applications and characteristics"""
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("🏗️ Common Applications")
            for app in material["applications"]:
                st.write(f"• {app}")
        
        with col2:
            st.subheader("📋 Key Characteristics")
            for char in material["characteristics"]:
                st.write(f"• {char}")
            
            if "heat_treatment" in material:
                st.subheader("🔥 Heat Treatment")
                for process, temp in material["heat_treatment"].items():
                    st.write(f"**{process.replace('_', ' ').title()}**: {temp}")
    
    def display_composition(self, material: Dict):
        """Display chemical composition"""
        composition = material["composition"]
        
        st.subheader("🧪 Chemical Composition")
        
        # Create composition table
        comp_data = []
        for element, fraction in composition.items():
            comp_data.append({
                "Element": element,
                "Weight %": f"{fraction * 100:.3f}",
                "Atomic %": f"{fraction * 100:.1f}"  # Simplified
            })
        
        df = pd.DataFrame(comp_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # Pie chart for visualization
        if len(composition) > 1:
            fig = px.pie(
                values=list(composition.values()),
                names=list(composition.keys()),
                title="Composition Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)
    
    def display_educational(self, material: Dict):
        """Display educational insights"""
        st.subheader("🎓 Educational Insights")
        
        for insight in material["educational_insights"]:
            st.info(f"💡 {insight}")
        
        # Crystal structure insights if available
        if "crystal_structure" in material:
            crystal = material["crystal_structure"]
            st.subheader("🔬 Crystal Structure Insights")
            
            if crystal["structure_type"] == "BCC":
                st.write("""
                **Body-Centered Cubic (BCC):**
                - 8 nearest neighbors (coordination number = 8)
                - Lower packing density (68%) than FCC
                - Exhibits ductile-to-brittle transition temperature
                - Common in ferritic steels at room temperature
                """)
            elif crystal["structure_type"] == "FCC":
                st.write("""
                **Face-Centered Cubic (FCC):**
                - 12 nearest neighbors (coordination number = 12)
                - Highest packing density (74%) for monatomic crystals
                - Multiple slip systems enable excellent ductility
                - Common in austenitic steels and many non-ferrous metals
                """)
            elif crystal["structure_type"] == "HCP":
                st.write("""
                **Hexagonal Close-Packed (HCP):**
                - 12 nearest neighbors (coordination number = 12)
                - Same packing density as FCC (74%) but different symmetry
                - Limited slip systems at room temperature
                - Anisotropic mechanical properties
                """)
            elif crystal["structure_type"] == "Diamond Cubic":
                st.write("""
                **Diamond Cubic:**
                - 4 nearest neighbors (tetrahedral coordination)
                - Very low packing density (34%) due to directional bonding
                - Covalent bonding makes materials hard and brittle
                - Characteristic of semiconductors like silicon and diamond
                """)
        
        # Learning objectives
        st.subheader("🎯 Why Important for Mechanical Engineers")
        st.write("""
        This material is essential for mechanical engineering students because:
        - It represents a fundamental material class used in industry
        - It demonstrates key material science principles
        - It shows important property trade-offs relevant to design
        - It's widely used in real engineering applications
        - Understanding its crystal structure helps predict mechanical behavior
        """)
    
    def display_sources(self, material: Dict):
        """Display data sources"""
        st.subheader("📚 Verified Data Sources")
        
        
        st.write("**Primary Sources:**")
        for source in material.get("sources", []):
            st.write(f"• {source}")
        

    
    def show_comparison_tool(self):
        """Show material comparison tool"""
        st.header("📈 Material Comparison Tool")
        
        material_options = {data["name"]: key for key, data in self.materials_data.items()}
        selected_materials = st.multiselect(
            "Select materials to compare:",
            options=list(material_options.keys()),
            default=[]
        )
        
        if len(selected_materials) < 2:
            st.warning("Please select at least 2 materials for comparison")
            return
        
        comparison_type = st.selectbox(
            "Comparison Type:",
            ["Mechanical Properties", "Physical Properties", "Crystal Structures"]
        )
        
        if comparison_type == "Mechanical Properties":
            self.compare_mechanical_properties(selected_materials, material_options)
        elif comparison_type == "Physical Properties":
            self.compare_physical_properties(selected_materials, material_options)
        else:
            self.compare_crystal_structures(selected_materials, material_options)
    
    def compare_mechanical_properties(self, selected_materials, material_options):
        """Compare mechanical properties"""
        properties = ["yield_strength", "tensile_strength", "youngs_modulus", "hardness", "elongation"]
        property_names = ["Yield Strength (MPa)", "Tensile Strength (MPa)", "Young's Modulus (GPa)", "Hardness (BHN)", "Elongation (%)"]
        
        fig = go.Figure()
        
        for prop, prop_name in zip(properties, property_names):
            values = []
            for material_name in selected_materials:
                material_key = material_options[material_name]
                values.append(self.materials_data[material_key]["properties"][prop])
            
            fig.add_trace(go.Bar(
                name=prop_name,
                x=selected_materials,
                y=values
            ))
        
        fig.update_layout(
            title="Mechanical Properties Comparison",
            barmode='group',
            xaxis_title="Materials",
            yaxis_title="Property Values"
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def compare_physical_properties(self, selected_materials, material_options):
        """Compare physical properties"""
        properties = ["density", "thermal_conductivity", "thermal_expansion", "melting_point"]
        property_names = ["Density (g/cm³)", "Thermal Conductivity (W/m·K)", "Thermal Expansion (μm/m·K)", "Melting Point (°C)"]
        
        fig = go.Figure()
        
        for prop, prop_name in zip(properties, property_names):
            values = []
            for material_name in selected_materials:
                material_key = material_options[material_name]
                values.append(self.materials_data[material_key]["properties"][prop])
            
            fig.add_trace(go.Bar(
                name=prop_name,
                x=selected_materials,
                y=values
            ))
        
        fig.update_layout(
            title="Physical Properties Comparison",
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    
        
    
    def compare_crystal_structures(self, selected_materials, material_options):
        """Compare crystal structures"""
        st.subheader("Crystal Structure Comparison")
        
        for material_name in selected_materials:
            material_key = material_options[material_name]
            material_data = self.materials_data[material_key]
            
            if "crystal_structure" in material_data:
                crystal = material_data["crystal_structure"]
                st.write(f"**{material_name}**: {crystal['structure_type']} - {crystal.get('description', '')}")
                st.write(f"Coordination Number: {crystal['coordination_number']}, Packing Factor: {crystal['atomic_packing_factor']}")
            else:
                st.write(f"**{material_name}**: Crystal structure data not available")
            
            st.write("---")
    
    def browse_materials(self):
        """Browse materials by category"""
        st.header("📚 Materials Database")
        
        # Group by category
        categories = {}
        for key, material in self.materials_data.items():
            cat = material["category"]
            if cat not in categories:
                categories[cat] = []
            categories[cat].append((key, material))
        
        # Category selector
        selected_category = st.selectbox(
            "Select Material Category:",
            ["All Categories"] + list(categories.keys())
        )
        
        if selected_category == "All Categories":
            materials_to_show = list(self.materials_data.items())
        else:
            materials_to_show = categories[selected_category]
        
        # Material selection
        material_names = [data["name"] for _, data in materials_to_show]
        selected_material_name = st.selectbox(
            "Select a material:",
            options=material_names
        )
        
        # Find the selected material key
        selected_material_key = None
        for key, data in materials_to_show:
            if data["name"] == selected_material_name:
                selected_material_key = key
                break
        
        if selected_material_key:
            self.display_material_details(selected_material_key)
    
    
    
    def run(self):
        """Main application runner"""
        st.set_page_config(
            page_title="MEMD",
            page_icon=logo,
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        st.title("⚙️ Mechanical Engineering Materials Database(MEMD)")
        
        st.logo(logo)
        
        # Sidebar
        
        
        st.sidebar.title("🧭 Navigation")
        
        app_mode = st.sidebar.radio(
            "Select Mode:",
            ["📚 Browse Materials", "📈 Compare Materials"]
        )
        
        st.sidebar.title("📊 Database Info")
        
        
        st.sidebar.info(f"**Total Materials**: {len(self.materials_data)}")

        
        
        
        
        # Main content
        if app_mode == "📚 Browse Materials":
            self.browse_materials()
        elif app_mode == "📈 Compare Materials":
            self.show_comparison_tool()
        else:
            self.show_learning_guide()

# =============================================================================
# RUN APPLICATION
# =============================================================================

if __name__ == "__main__":
    app = MechanicalEngineeringMaterialsApp()
    app.run()
