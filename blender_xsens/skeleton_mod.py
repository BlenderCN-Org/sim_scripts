import bpy


from blender_xsens.xsens_mocap.mvn_filereader import MvnFileReader


class SkeletonModifier():
    
    def __init__(self):
        print(foo)
        self.scene = bpy.context.scene
        scene.frame_start = 1
        scene.frame_end = 1
        self.current_frame = 1
        self.skeleton = slef.scene.objects.active
        
    def update_skeleton(self):
        self.scene.frame_set(frame = self.current_frame)
        self.current_frame += 1
        bpy.ops.anim.keyframe_insert_menu(type='Rotation')
        bpy.ops.anim.keyframe_insert_menu(type='Location')
        bpy.ops.anim.keyframe_insert_menu(type='Scale')
        bone=self.skeleton.bones['Hips']
        
        