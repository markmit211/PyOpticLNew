from PyOpticL import layout, optomech
from datetime import datetime

name = "Butterfly Splitter"
date_time = datetime.now().strftime("%m/%d/%Y")
label = name + " " +  date_time

base_dx = 6*layout.inch #160
base_dy = 218 #173
base_dz = layout.inch
gap = 0

x_offset = -9-25.4/2
y_offset = 10-25.4/2

# mount_holes_temp = [(1,3),(3,4),(4,0),(9,0),(9,4),(10,2),(12,3)]

mount_holes = []
# for x,y in mount_holes_temp:
#     mount_holes.append((x+x_offset/25.4,y+y_offset/25.4))

# Note that for mirror_mount_c05g, an offset of 6mm is needed as the pos is 
# centered at the optical start, not the drill hole as in openscad. 

d_inch = 25.4

# Positioning for Mount Placement

hca3_width = 41

fiber_in_x = hca3_width/2
fiber_in_y = 4*d_inch

start_x = 75
start_y = 40



def butterfly_input_splitter(x=0, y=0, angle=0, mirror=optomech.mirror_mount_k05s2, x_split=False, thumbscrews=True):

    # Define Baseplate:
    baseplate = layout.baseplate(base_dx, base_dy, base_dz, x=x, y=y, angle=angle,
                                 gap=gap, mount_holes=mount_holes,
                                 name=name, label=label)

    # Define beam path:
    beam = baseplate.add_beam_path(x=start_x, y=start_y, angle=layout.cardinal['right'], color = (0,0,255))


    # Optic Placement Definitions:
    baseplate.place_element("butterfly_laser_input", optomech.butterfly_laser_on_koheron_driver, 
                            x=start_x, y=start_y, angle=layout.cardinal['right'])
    
    baseplate.place_element_along_beam("mirror1_in", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=50, angle=135,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("isolator", optomech.isolator_895, beam, beam_index=0b1,
                                       distance=30, angle=layout.cardinal['down'])
    baseplate.place_element_along_beam("pinhole1", optomech.circular_lens, beam, 
                                       beam_index=0b1, distance=40, angle=90, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror2_in", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=15, angle=225,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("waveplate1_in", optomech.waveplate, beam, 
                                       beam_index=0b1, distance=23, angle=0, 
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("pbs", optomech.cube_splitter, beam,
                                       beam_index=0b1, distance=20, angle=0, invert=True,
                                       mount_type=optomech.skate_mount)

    # Transmitted pbs parts:
    baseplate.place_element_along_beam("pinhole2", optomech.circular_lens, beam,
                                       beam_index=0b10, distance=32, angle=180, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror1_out", optomech.circular_mirror, beam,
                                       beam_index=0b10, distance=15, angle=45,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("mirror2_out", optomech.circular_mirror, beam,
                                       beam_index=0b10, distance=25, angle=225,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("waveplate1_out", optomech.waveplate, beam, 
                                       beam_index=0b10, distance=20, angle=0, 
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("fiberport_out_1", optomech.fiberport_mount_hca3, beam,
                                       beam_index=0b10, distance=15, angle=0)

    # Reflected pbs parts:
    baseplate.place_element_along_beam("mirror3_out", optomech.circular_mirror, beam,
                                       beam_index=0b11, distance=65, angle=-45,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("pinhole3", optomech.circular_lens, beam,
                                       beam_index=0b11, distance=28, angle=0, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror4_out", optomech.circular_mirror, beam,
                                       beam_index=0b11, distance=20, angle=135,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("waveplate1_out", optomech.waveplate, beam, 
                                       beam_index=0b11, distance=18, angle=270, 
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("fiberport_out_1", optomech.fiberport_mount_hca3, beam,
                                       beam_index=0b11, distance=10, angle=270)



if __name__ == "__main__":
    butterfly_input_splitter()
    layout.redraw()