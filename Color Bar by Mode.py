bl_info = {
    "name": "Color_Bars_by_Mode",
    "author": "BRT",
    "version": (1, 0),
    "blender": (2, 80, 0),
    "location": "View3D > Add > Mesh > New Object",
    "description": "Add color to bars for status",
    "warning": "",
    "doc_url": "",
    "category": "TB",
}

import bpy
from bpy.props import BoolProperty, FloatProperty, StringProperty, IntProperty, FloatVectorProperty, EnumProperty

class ModalColorsBar(bpy.types.Operator):
    """Operator which runs its self from a timer"""
    bl_idname = "wm.modal_timer_operator"
    bl_label = "Modal Timer Operator"

    _timer = None
        
    def modal(self, context, event):
        def chth_col(col):
            th.topbar.space.header = col
            th.statusbar.space.header = col
        def chth_col_prp(col):
            th.properties.space.header = col
            th.properties.space.navigation_bar = col
        context = bpy.context
        prefs = context.preferences
        th = prefs.themes['Default']
        header = th.topbar.space.header
        status = th.statusbar.space.header
        if bpy.context.active_object:
            mode = bpy.context.active_object.mode
            if mode:
                if bpy.context.active_object.mode == 'OBJECT':
                    chth_col([0.1,0.1,0.11,1.0])
                if bpy.context.active_object.mode == 'EDIT' or bpy.context.active_object.mode == 'EDIT_GPENCIL':
                    chth_col([0.7,0.4,0.09,1.0])
                if bpy.context.active_object.mode == 'SCULPT' or bpy.context.active_object.mode == 'SCULPT_GPENCIL':
                    chth_col([0.5,0.2,0.2,1.0])        
                if bpy.context.active_object.mode == 'WEIGHT_PAINT' or bpy.context.active_object.mode == 'POSE' or bpy.context.active_object.mode == 'WEIGHT_GPENCIL':
                    chth_col([0.15,0.2,0.3,1.0])
                if bpy.context.active_object.mode == 'TEXTURE_PAINT':
                    chth_col([0.4,0.1,0.4,1.0])             
                if bpy.context.active_object.mode == 'VERTEX_PAINT' or bpy.context.active_object.mode == 'VERTEX_GPENCIL':
                    chth_col([0.15,0.3,0.1,1.0])                                 
                if bpy.context.active_object.mode == 'PAINT_GPENCIL':
                    chth_col([0.1,0.3,0.3,1.0]) 
                return {'PASS_THROUGH'}
        
            return {'PASS_THROUGH'}
        return {'PASS_THROUGH'}

    def execute(self, context):
        wm = context.window_manager
        self._timer = wm.event_timer_add(0.1, window=context.window)
        wm.modal_handler_add(self)
        return {'RUNNING_MODAL'}

    def cancel(self, context):
        wm = context.window_manager
        wm.event_timer_remove(self._timer)

def menu_func(self, context):
    self.layout.operator(ModalColorsBar.bl_idname, text=ModalColorsBar.bl_label)

def register():
    bpy.utils.register_class(ModalColorsBar)
    bpy.types.VIEW3D_MT_view.append(menu_func)

def unregister():
    bpy.utils.unregister_class(ModalColorsBar)
    bpy.types.VIEW3D_MT_view.remove(menu_func)

if __name__ == "__main__":
    register()

    bpy.ops.wm.modal_timer_operator()