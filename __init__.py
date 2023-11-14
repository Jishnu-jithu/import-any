bl_info = {
    "name": "Import Any",
    "author": "Jishnu jithu",
    "version": (1, 0),
    "blender": (2, 93),
    "location": "View3D > Sidebar > Import Any",
    "description": "Adds a panel for centralized control of render settings",
    "doc_url": "https://github.com/Jishnu-jithu/render-palette/wiki/Render-Palette-Documentation",
    "tracker_url": "https://t.me/Blendyhub",
    "category": "Import-Export",
}

import bpy
import os
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, FloatProperty

# Define the operator for importing any file format
class IMPORT_OT_any(bpy.types.Operator, ImportHelper):
    bl_idname = "import.any"
    bl_label = "Import Any"
    bl_description = "Import any file format"
    bl_options = {'REGISTER', 'UNDO'}
    
    filter_glob: StringProperty(
        default="",
        options={'HIDDEN'},
        maxlen=255,
    )

    def invoke(self, context, event):
        # Define a list of allowed file extensions
        allowed_extensions = [
            ".obj", ".fbx", ".dae", ".3ds", ".abc", ".usd", ".usda", ".usdc", ".usdz",
            ".gltf", ".glb", ".svg", ".ply", ".stl", ".dxf", ".bvh", ".x3d", ".wrl",
            ".jpg", ".jpeg", ".png", ".mp4", ".psd", ".xyz",
        ]

        # Set the filter_glob to only allow the specified extensions
        self.filter_glob = ";".join(["*" + ext for ext in allowed_extensions])

        return super().invoke(context, event)

    def execute(self, context):
        file_ext = os.path.splitext(self.filepath)[-1].lower()

        # Store the current selection
        current_selection = bpy.context.selected_objects

        if file_ext == ".obj":
            bpy.ops.import_scene.obj(filepath=self.filepath)
        elif file_ext == ".fbx":
            bpy.ops.import_scene.fbx(filepath=self.filepath)
        elif file_ext == ".dae":
            bpy.ops.wm.collada_import(filepath=self.filepath)
        elif file_ext == ".3ds":
            bpy.ops.import_scene.autodesk_3ds(filepath=self.filepath)
        elif file_ext == ".abc":
            bpy.ops.wm.alembic_import(filepath=self.filepath)
        elif file_ext == ".usd" or file_ext == ".usda" or file_ext == ".usdc" or file_ext == ".usdz":
            bpy.ops.wm.usd_import(filepath=self.filepath)
        elif file_ext == ".gltf" or file_ext == ".glb":
            bpy.ops.import_scene.gltf(filepath=self.filepath)
        elif file_ext == ".svg":
            bpy.ops.import_curve.svg(filepath=self.filepath)
        elif file_ext == ".ply":
            bpy.ops.import_mesh.ply(filepath=self.filepath)
        elif file_ext == ".stl":
            bpy.ops.import_mesh.stl(filepath=self.filepath)
        elif file_ext == ".dxf":
            bpy.ops.import_scene.autocad(filepath=self.filepath)
        elif file_ext == ".bvh":
            bpy.ops.import_anim.bvh(filepath=self.filepath)
        elif file_ext == ".x3d" or file_ext == ".wrl":
            bpy.ops.import_scene.x3d(filepath=self.filepath)
        elif file_ext == ".xyz":
            bpy.ops.import_mesh.xyz(filepath=self.filepath)
        elif file_ext == ".jpg" or file_ext == ".jpeg"  or file_ext == ".png" or file_ext == ".mp4" or file_ext == ".psd":
            bpy.ops.import_image.to_plane(files=[{"name":self.filepath}])
            
        imported_objects = [obj for obj in bpy.context.selected_objects if obj not in current_selection]

        self.report({'INFO'}, "Imported file: " + self.filepath)
        
        return {'FINISHED'}

# Add the import menu function
def menu_func_import(self, context):
    self.layout.operator(IMPORT_OT_any.bl_idname, text="Import any")

# Define the preferences class for enabling/disabling other add-ons
class ImportAnyPreferences(bpy.types.AddonPreferences):
    bl_idname = __name__

    def draw(self, context):
        layout = self.layout

        layout.label(text="This add-on will only work if the corresponding file extension is enabled in the add-on preferences.")
        
        format_1 = [".obj", ".fbx", ".dae", ".3ds", ".abc", ".stl"]
        format_2 = [".ply", ".dxf", ".bvh", ".x3d", ".wrl", ".xyz"]
        format_3 = [".usd", ".usda", ".usdc", ".usdz", ".gltf", ".glb"]
        format_4 = [".ply", ".dxf", ".bvh", ".x3d", ".wrl", ".xyz"]
        
        box = layout.box()

        # Add labels for each format group
        box.label(text="Supported Formats:")
        box.label(text="" + ", ".join(format_1))
        box.label(text="" + ", ".join(format_2))
        box.label(text="" + ", ".join(format_3))
        box.label(text="" + ", ".join(format_4))
        
def register():
    bpy.utils.register_class(IMPORT_OT_any)
    bpy.utils.register_class(ImportAnyPreferences)
    bpy.types.TOPBAR_MT_file_import.prepend(menu_func_import)

def unregister():
    bpy.utils.unregister_class(IMPORT_OT_any)
    bpy.utils.unregister_class(ImportAnyPreferences)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
