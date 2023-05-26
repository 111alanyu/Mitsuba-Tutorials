import mitsuba as mi

#this sets variant so all uses 'scalar_rgb' for future mi function calls
mi.set_variant('scalar_rgb') 


scene = mi.load_file("/scenes/cbox.xml")

image = mi.render(scene)

mi.Bitmap(image)