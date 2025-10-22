import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from typing import Dict, List, Any

# Import from our separate data file
from materials_data import load_mechanical_engineering_materials, load_mechanical_crystal_structures

# Configure the page
st.set_page_config(
    page_title="Material Science Learning App",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

class MaterialScienceApp:
    def __init__(self):
        # Load data from separate file
        self.materials_data = load_mechanical_engineering_materials()
        self.crystal_structures = load_mechanical_crystal_structures()
    
    def create_crystal_structure_plot(self, material_key: str) -> go.Figure:
        """Generate 3D crystal structure visualization"""
        # ... (keep the same visualization code from previous version)
        crystal_data = self.crystal_structures[material_key]
        lattice_param = crystal_data["lattice_parameters"]["a"]
        
        fig = go.Figure()
        
        # Add atoms
        atom_colors = {"Al": "blue", "Fe": "gray", "Si": "orange", "Ti": "silver", "Cu": "brown"}
        
        for atom in crystal_data["atomic_positions"]:
            element = atom["element"]
            # Convert fractional to absolute coordinates
            x_abs = atom["x"] * lattice_param
            y_abs = atom["y"] * lattice_param  
            z_abs = atom["z"] * lattice_param
            
            fig.add_trace(go.Scatter3d(
                x=[x_abs], y=[y_abs], z=[z_abs],
                mode='markers',
                marker=dict(
                    size=12,
                    color=atom_colors.get(element, "red"),
                    opacity=0.8,
                    line=dict(width=2, color='darkgray')
                ),
                name=f'{element} Atom',
                hovertemplate=f'Element: {element}<br>Position: ({atom["x"]:.2f}, {atom["y"]:.2f}, {atom["z"]:.2f})<extra></extra>'
            ))
        
        # Add unit cell edges (same as before)
        unit_cell_edges = [
            [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],  # bottom face
            [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1],  # top face
            [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 1]  # vertical edges
        ]
        
        # Convert to absolute coordinates
        edges_x, edges_y, edges_z = [], [], []
        for edge in unit_cell_edges:
            edges_x.append(edge[0] * lattice_param)
            edges_y.append(edge[1] * lattice_param)
            edges_z.append(edge[2] * lattice_param)
        
        fig.add_trace(go.Scatter3d(
            x=edges_x, y=edges_y, z=edges_z,
            mode='lines',
            line=dict(color='black', width=4),
            name='Unit Cell',
            hovertemplate=None,
            showlegend=False
        ))
        
        # Update layout
        material_name = self.materials_data[material_key]["name"]
        structure_type = crystal_data["structure_type"]
        
        fig.update_layout(
            title=f"{material_name} - {structure_type} Crystal Structure",
            scene=dict(
                xaxis_title="X (Å)",
                yaxis_title="Y (Å)", 
                zaxis_title="Z (Å)",
                aspectmode='cube',
                camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
            ),
            height=600,
            showlegend=True
        )
        
        return fig
    
    def create_property_comparison_chart(self, selected_materials: List[str], property_name: str) -> go.Figure:
        """Create bar chart comparing material properties"""
        # ... (keep the same comparison code from previous version)
        materials = []
        values = []
        
        for material_key in selected_materials:
            material = self.materials_data[material_key]
            materials.append(material["name"])
            values.append(material["properties"][property_name])
        
        fig = px.bar(
            x=materials,
            y=values,
            title=f"Comparison: {property_name.replace('_', ' ').title()}",
            labels={'x': 'Material', 'y': property_name.replace('_', ' ').title()},
            color=values,
            color_continuous_scale='viridis'
        )
        
        fig.update_layout(
            xaxis_title="Material",
            yaxis_title=property_name.replace('_', ' ').title(),
            showlegend=False
        )
        
        return fig
    
    def create_radar_chart(self, selected_materials: List[str]) -> go.Figure:
        """Create radar chart for multiple property comparison"""
        # ... (keep the same radar chart code from previous version)
        properties = ['density', 'youngs_modulus', 'yield_strength', 'thermal_conductivity', 'hardness']
        property_labels = ['Density (g/cm³)', 'Young\'s Modulus (GPa)', 'Yield Strength (MPa)', 
                          'Thermal Conductivity (W/m·K)', 'Hardness (Brinell)']
        
        fig = go.Figure()
        
        for material_key in selected_materials:
            material = self.materials_data[material_key]
            values = []
            
            for prop in properties:
                raw_value = material["properties"][prop]
                normalized_value = raw_value / max(self.materials_data[m]["properties"][prop] for m in selected_materials)
                values.append(normalized_value)
            
            values.append(values[0])
            radar_properties = property_labels + [property_labels[0]]
            
            fig.add_trace(go.Scatterpolar(
                r=values,
                theta=radar_properties,
                fill='toself',
                name=material["name"]
            ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 1]
                )
            ),
            title="Material Properties Radar Chart",
            showlegend=True
        )
        
        return fig
    
    def display_material_details(self, material_key: str):
        """Display detailed information about a specific material"""
        material = self.materials_data[material_key]
        crystal = self.crystal_structures[material_key]
        
        st.header(f"📚 {material['name']}")
        
        # Create tabs for different information sections
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Properties", "🔬 Crystal Structure", "🏗️ Applications", "🧪 Composition", "🎓 Educational"])
        
        with tab1:
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Mechanical Properties")
                props = material["properties"]
                st.metric("Density", f"{props['density']} g/cm³")
                st.metric("Young's Modulus", f"{props['youngs_modulus']} GPa")
                st.metric("Yield Strength", f"{props['yield_strength']} MPa")
                st.metric("Tensile Strength", f"{props['tensile_strength']} MPa")
                st.metric("Hardness", f"{props['hardness']} Brinell")
            
            with col2:
                st.subheader("Thermal & Electrical Properties")
                st.metric("Melting Point", f"{props['melting_point']} °C")
                st.metric("Thermal Conductivity", f"{props['thermal_conductivity']} W/m·K")
                st.metric("Electrical Resistivity", f"{props['electrical_resistivity']:.1e} Ω·m")
                st.metric("Relative Cost", f"${props['cost']}/kg")
        
        with tab2:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                crystal_plot = self.create_crystal_structure_plot(material_key)
                st.plotly_chart(crystal_plot, use_container_width=True)
            
            with col2:
                st.subheader("Crystal Information")
                st.write(f"**Crystal System**: {crystal['crystal_system']}")
                st.write(f"**Structure Type**: {crystal['structure_type']}")
                st.write(f"**Space Group**: {crystal['space_group']}")
                st.write(f"**Lattice Parameter**: {crystal['lattice_parameters']['a']} Å")
                st.write(f"**Coordination Number**: {crystal['coordination_number']}")
                st.write(f"**Atomic Packing Factor**: {crystal['atomic_packing_factor']}")
                
                st.subheader("Structure Insights")
                if crystal['structure_type'] == 'FCC':
                    st.write("• FCC structures have multiple slip systems")
                    st.write("• This enables good ductility and formability")
                    st.write("• Close-packed planes allow dislocation movement")
                elif crystal['structure_type'] == 'Diamond Cubic':
                    st.write("• Diamond cubic has directional covalent bonding")
                    st.write("• This makes materials hard but brittle")
                    st.write("• Four-fold coordination enables semiconductor properties")
                elif crystal['structure_type'] == 'HCP':
                    st.write("• HCP structures have limited slip systems")
                    st.write("• This can lead to anisotropic properties")
                    st.write("• Close-packed basal planes enable specific deformation")
        
        with tab3:
            st.subheader("Real-World Applications")
            for application in material["applications"]:
                st.write(f"• {application}")
            
            st.subheader("Key Characteristics")
            for characteristic in material["characteristics"]:
                st.write(f"• {characteristic}")
        
        with tab4:
            st.subheader("Chemical Composition")
            composition = material["composition"]
            
            fig = px.pie(
                values=list(composition.values()),
                names=list(composition.keys()),
                title=f"Composition of {material['name']}"
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with tab5:
            st.subheader("Educational Insights")
            for insight in material.get("educational_insights", []):
                st.info(f"💡 {insight}")
    
    def run(self):
        """Main application runner"""
        st.title("🔬 Material Science Learning App")
        st.markdown("Explore material properties, crystal structures, and real-world applications!")
        
        # Display material count
        st.sidebar.title("Navigation")
        st.sidebar.write(f"**Database**: {len(self.materials_data)} materials loaded")
        
        app_mode = st.sidebar.selectbox(
            "Choose Module",
            ["🏠 Browse Materials", "📈 Compare Properties", "🔍 Search Materials"]
        )
        
        if app_mode == "🏠 Browse Materials":
            self.browse_materials()
        elif app_mode == "📈 Compare Properties":
            self.compare_properties()
        elif app_mode == "🔍 Search Materials":
            self.search_materials()
    
    def browse_materials(self):
        """Browse materials by category"""
        st.header("Browse Materials Database")
        
        material_options = {data["name"]: key for key, data in self.materials_data.items()}
        selected_material_name = st.selectbox(
            "Select a material to explore:",
            options=list(material_options.keys())
        )
        
        selected_material_key = material_options[selected_material_name]
        self.display_material_details(selected_material_key)
    
    def compare_properties(self):
        """Compare properties of multiple materials"""
        st.header("Compare Material Properties")
        
        material_options = {data["name"]: key for key, data in self.materials_data.items()}
        selected_materials_names = st.multiselect(
            "Select materials to compare (2-3 recommended):",
            options=list(material_options.keys()),
            default=list(material_options.keys())[:2]
        )
        
        if len(selected_materials_names) < 2:
            st.warning("Please select at least 2 materials for comparison.")
            return
        
        selected_material_keys = [material_options[name] for name in selected_materials_names]
        
        comparison_type = st.radio(
            "Comparison Type:",
            ["📊 Single Property Bar Chart", "📈 Multiple Properties Radar Chart"]
        )
        
        if comparison_type == "📊 Single Property Bar Chart":
            properties = list(self.materials_data[selected_material_keys[0]]["properties"].keys())
            selected_property = st.selectbox("Select property to compare:", properties)
            
            bar_chart = self.create_property_comparison_chart(selected_material_keys, selected_property)
            st.plotly_chart(bar_chart, use_container_width=True)
            
        else:
            radar_chart = self.create_radar_chart(selected_material_keys)
            st.plotly_chart(radar_chart, use_container_width=True)
    
    def search_materials(self):
        """Search and filter materials"""
        st.header("Search Materials")
        
        col1, col2 = st.columns(2)
        
        with col1:
            material_class = st.selectbox(
                "Material Class:",
                ["All", "metal", "semiconductor", "ceramic", "polymer"]
            )
            
            min_strength = st.slider("Minimum Yield Strength (MPa):", 0, 1000, 100)
            max_density = st.slider("Maximum Density (g/cm³):", 1.0, 20.0, 10.0)
        
        with col2:
            crystal_structures = ["All", "FCC", "BCC", "HCP", "Diamond Cubic"]
            selected_structure = st.selectbox("Crystal Structure:", crystal_structures)
        
        filtered_materials = []
        
        for material_key, material_data in self.materials_data.items():
            crystal_data = self.crystal_structures[material_key]
            
            if material_class != "All" and material_data["class"] != material_class:
                continue
            
            if material_data["properties"]["yield_strength"] < min_strength:
                continue
                
            if material_data["properties"]["density"] > max_density:
                continue
                
            if selected_structure != "All" and crystal_data["structure_type"] != selected_structure:
                continue
            
            filtered_materials.append((material_key, material_data))
        
        if filtered_materials:
            st.subheader(f"Found {len(filtered_materials)} Materials")
            
            for material_key, material_data in filtered_materials:
                with st.expander(f"🔍 {material_data['name']} - {material_data['class'].title()}"):
                    self.display_material_details(material_key)
        else:
            st.warning("No materials found matching your criteria. Try adjusting filters.")

# Run the application
if __name__ == "__main__":
    mtc = MaterialScienceApp()
    mtc.run()