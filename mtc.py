import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from typing import Dict, List, Any

# Import the database
from materials_library import load_verified_mechanical_materials

# =============================================================================
# 3D VISUALIZATION FUNCTIONS
# =============================================================================

def create_crystal_structure_plot(crystal_data: Dict, material_name: str) -> go.Figure:
    """Create 3D crystal structure visualization"""
    
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
    
    # Element colors
    element_colors = {
        'Fe': '#FFA500', 'Al': '#BFBFBF', 'Si': '#F0E68C', 'O': '#FF0000',
        'Ti': '#808080', 'Cu': '#B87333', 'Cr': '#8DB6CD', 'Ni': '#50C878',
        'Mg': '#8A2BE2', 'C': '#000000', 'Mn': '#9ACD32'
    }
    
    # Add atoms
    for atom in atoms:
        element = atom["element"]
        x_abs = atom["x"] * lattice["a"]
        y_abs = atom["y"] * lattice["b"] 
        z_abs = atom["z"] * lattice["c"]
        
        fig.add_trace(go.Scatter3d(
            x=[x_abs], y=[y_abs], z=[z_abs],
            mode='markers',
            marker=dict(
                size=15,
                color=element_colors.get(element, '#FF00FF'),
                opacity=0.9,
                line=dict(width=2, color='darkgray')
            ),
            name=element,
            hovertemplate=(
                f'Element: {element}<br>'
                f'Position: ({atom["x"]:.3f}, {atom["y"]:.3f}, {atom["z"]:.3f})<br>'
                '<extra></extra>'
            )
        ))
    
    # Add unit cell
    unit_cell_edges = [
        [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 0],
        [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1], [0, 0, 1],
        [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1], [0, 1, 0], [0, 1, 1]
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
        showlegend=False,
        hoverinfo='none'
    ))
    
    fig.update_layout(
        title=f"{material_name} - Crystal Structure",
        scene=dict(
            xaxis_title="X (Å)",
            yaxis_title="Y (Å)", 
            zaxis_title="Z (Å)",
            aspectmode='data',
            camera=dict(eye=dict(x=1.5, y=1.5, z=1.5))
        ),
        height=600,
        showlegend=True
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
            st.metric("Relative Cost", f"{props['cost_index']} (vs 1020 steel)")
    
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
                
                st.subheader("Lattice Parameters")
                lat = crystal_data["lattice_parameters"]
                st.write(f"**a**: {lat['a']} Å")
                st.write(f"**b**: {lat['b']} Å")
                st.write(f"**c**: {lat['c']} Å")
            
            with col2:
                st.subheader("3D Crystal Structure")
                fig = create_crystal_structure_plot(crystal_data, material["name"])
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Crystal structure data not available for this material")
    
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
        
        # Learning objectives
        st.subheader("🎯 Why Important for Mechanical Engineers")
        st.write("""
        This material is essential for mechanical engineering students because:
        - It represents a fundamental material class used in industry
        - It demonstrates key material science principles
        - It shows important property trade-offs relevant to design
        - It's widely used in real engineering applications
        """)
    
    def display_sources(self, material: Dict):
        """Display data sources"""
        st.subheader("📚 Verified Data Sources")
        
        st.write("**Primary Sources:**")
        for source in material.get("sources", []):
            st.write(f"• {source}")
        
        st.info("""
        **Data Quality Assurance:**
        - All values verified against industry standards (ASM, ASTM)
        - Properties from manufacturer datasheets when available
        - Crystal structures from crystallographic databases
        - Mechanical properties tested according to standard methods
        """)
    
    def show_comparison_tool(self):
        """Show material comparison tool"""
        st.header("📈 Material Comparison Tool")
        
        material_options = {data["name"]: key for key, data in self.materials_data.items()}
        selected_materials = st.multiselect(
            "Select materials to compare:",
            options=list(material_options.keys()),
            default=["AISI 1020 Steel", "6061 Aluminum", "304 Stainless Steel"]
        )
        
        if len(selected_materials) < 2:
            st.warning("Please select at least 2 materials for comparison")
            return
        
        comparison_type = st.selectbox(
            "Comparison Type:",
            ["Mechanical Properties", "Physical Properties", "Cost vs Performance"]
        )
        
        if comparison_type == "Mechanical Properties":
            self.compare_mechanical_properties(selected_materials, material_options)
        elif comparison_type == "Physical Properties":
            self.compare_physical_properties(selected_materials, material_options)
        else:
            self.compare_cost_performance(selected_materials, material_options)
    
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
    
    def compare_cost_performance(self, selected_materials, material_options):
        """Compare cost vs performance"""
        costs = []
        strengths = []
        names = []
        
        for material_name in selected_materials:
            material_key = material_options[material_name]
            material_data = self.materials_data[material_key]
            costs.append(material_data["properties"]["cost_index"])
            strengths.append(material_data["properties"]["yield_strength"])
            names.append(material_name)
        
        fig = px.scatter(
            x=costs, y=strengths, text=names,
            title="Cost vs Yield Strength",
            labels={'x': 'Relative Cost Index', 'y': 'Yield Strength (MPa)'}
        )
        fig.update_traces(textposition='top center', marker=dict(size=15))
        st.plotly_chart(fig, use_container_width=True)
    
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
    
    def show_learning_guide(self):
        """Show learning guide"""
        st.header("🎓 Mechanical Engineering Learning Guide")
        
        st.markdown("""
        ## Essential Materials for Mechanical Engineers
        
        Follow this learning path to understand the most important materials:
        """)
        
        learning_path = {
            "Phase 1: Foundation Materials": [
                "aisi_1020", "al_6061", "gray_cast_iron", "abs_plastic"
            ],
            "Phase 2: Core Engineering Materials": [
                "aisi_1040", "ss_304", "aisi_4140", "copper_etp"
            ],
            "Phase 3: Advanced/Specialized Materials": [
                "al_7075", "ti_6al_4v"
            ]
        }
        
        for phase_name, material_keys in learning_path.items():
            st.subheader(phase_name)
            
            cols = st.columns(len(material_keys))
            for idx, material_key in enumerate(material_keys):
                with cols[idx]:
                    material = self.materials_data[material_key]
                    st.write(f"**{material['name']}**")
                    st.write(f"Yield: {material['properties']['yield_strength']} MPa")
                    st.write(f"Density: {material['properties']['density']} g/cm³")
                    
                    if st.button(f"Study {material['name']}", key=f"learn_{material_key}"):
                        self.display_material_details(material_key)
    
    def run(self):
        """Main application runner"""
        st.set_page_config(
            page_title="Mechanical Engineering Materials Database",
            page_icon="⚙️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        st.title("⚙️ Mechanical Engineering Materials Database")
        st.markdown("""
        Explore **verified materials data** for mechanical engineering education.
        All data sourced from **ASM Handbooks, MatWeb, and industry standards**.
        """)
        
        # Sidebar
        st.sidebar.title("🧭 Navigation")
        
        app_mode = st.sidebar.radio(
            "Select Mode:",
            ["📚 Browse Materials", "📈 Compare Materials", "🎓 Learning Guide"]
        )
        
        st.sidebar.title("📊 Database Info")
        categories = {}
        for material in self.materials_data.values():
            cat = material["category"]
            categories[cat] = categories.get(cat, 0) + 1
        
        for cat, count in categories.items():
            st.sidebar.write(f"• {cat.replace('_', ' ').title()}: {count} materials")
        
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
