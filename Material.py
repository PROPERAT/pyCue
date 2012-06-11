from numpy import float32
class Material:
    def __init__(self):
    
        self.lighting_flag = False
        self.shininess     = float32(0.0)
        self.material_name = ""
        self.is_transperent = False
        self.alpha_blend_equation = None
        self.src_func = None
        self.dest_func = None
        self.textures = [None, None, None]
    
    def set_material(self, driver):
        raise Exception("Method not implemented for " + self.__class__)
        
    def unset_material(self, driver):
        raise Exception("Method not implemented for " + self.__class__)
        
    def set_texture(self, texture_slot, texture):
        if texture_slot > 3:
            raise Exception("Maximum of 3 textures allowed!")
        self.textures[texture_slot] = texture
    
    def is_transperent(self):
        return self.is_transperent
    
    def set_lighting(self, flag):
        self.lighting_flag = flag
        
    def get_lighting(self):
        return self.lighting_flag
    
    def set_name(self, name):
        self.material_name = name
    
    def get_name(self):
        return self.material_name
        
    def get_shininess(self):
        return self.shininess
    
    def set_shininess(self, factor):
        self.shininess = factor
        
    def get_textures(self):
        return self.textures
    
    def set_src_func(self, func):
        self.src_func = func
    
    def get_src_func(self):
        return self.src_func
    
    def set_dst_func(self, func):
        self.dst_func = func
    
    def get_dst_func(self):
        return self.dst_func
        
    def get_alpha_equation(self):
        return self.alpha_blend_equation
        
    def set_alpha_equation(self, alpha_eq):
        alpha_blend_equation = alpha_eq