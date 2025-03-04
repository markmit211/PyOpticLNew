from PyOpticL import layout, optomech
from datetime import datetime

name = "qzz ta input"
date_time = datetime.now().strftime("%m/%d/%Y")
label = name + " " +  date_time

base_dx = 12*layout.inch
base_dy = 6*layout.inch
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
start_y = 6*layout.inch-40

out_turn_angle=112.5
out_turn_angle = -124

wpick_x = 285
wpick_y = 6*layout.inch-75

# Note to future users: if beam goes through non permeable object, it will
# not render. It will throw a recursion error, for exampe, in this mount where the beams cross



def qzz_ta_input(x=0, y=0, angle=0, mirror=optomech.mirror_mount_k05s2, x_split=False, thumbscrews=True):

    # Define Baseplate:
    baseplate = layout.baseplate(base_dx, base_dy, base_dz, x=x, y=y, angle=angle,
                                 gap=gap, mount_holes=mount_holes,
                                 name=name, label=label)

    # Define beam path:
    beam = baseplate.add_beam_path(x=start_x, y=start_y, angle=layout.cardinal['right'], color = (0,0,255))


    # Optic Placement Definitions:
    baseplate.place_element("evalminiTA", optomech.eval_miniTA, x=start_x, y=start_y, angle=layout.cardinal['right'], height=0)

    
    baseplate.place_element_along_beam("alignment1", optomech.circular_lens, beam, 
                                       beam_index=0b1, distance=30, angle=0, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("isolator", optomech.isolator_850, beam, beam_index=0b1,
                                       distance=30, angle=0)
    baseplate.place_element_along_beam("alignment2", optomech.circular_lens, beam, 
                                       beam_index=0b1, distance=50, angle=0, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror1_in", optomech.circular_mirror, beam,
                                       beam_index=0b1, distance=100, angle=225,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("alignment3", optomech.circular_lens, beam, 
                                       beam_index=0b10, distance=35, angle=270, 
                                       mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror2_in", optomech.circular_mirror, beam,
                                       beam_index=0b10, distance=15, angle=135,
                                       mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("waveplate1_in", optomech.waveplate, beam, 
                                       beam_index=0b10, distance=20, angle=0, 
                                       mount_type=optomech.rotation_stage_rsp05)
    baseplate.place_element_along_beam("pbs", optomech.cube_splitter, beam, beam_index=0b10,
                                       distance=15, angle=0, mount_type=optomech.skate_mount, invert=True)
    
    # Reflected pbs parts:
    baseplate.place_element_along_beam("alignment4", optomech.circular_lens, beam,
                                       beam_index=0b101, distance=70, angle=90, mount_type=optomech.mirror_mount_c05g)
    baseplate.place_element_along_beam("mirror3_out", optomech.circular_mirror, beam,
                                       beam_index=0b101, distance=25, angle=out_turn_angle,
                                       mount_type=optomech.mirror_mount_k05s1)
    baseplate.place_element_along_beam("mirror3_out", optomech.circular_mirror, beam,
                                       beam_index=0b101, distance=48, angle=out_turn_angle+180,
                                       mount_type=optomech.mirror_mount_k05s1)
    baseplate.place_element_along_beam("fiberport", optomech.fiberport_mount_hca3, beam, 
                                       beam_index=0b101, distance=48, angle=270)
    
    # Transmitted pbs parts:
    baseplate.place_element_along_beam("aom", optomech.isomet_1205c_on_km100pm, beam, 
                                       beam_index=0b100, distance=25, angle=0, diffraction_angle=0)
    baseplate.place_element_along_beam("Quarter Waveplate", optomech.waveplate, beam, 
                                       beam_index=0b1000, distance=60, angle=180, 
                                       mount_type=optomech.rotation_stage_rsp05)
    cage = baseplate.place_element_along_beam("Cage Mount Pair", optomech.cage_mount_pair, beam, 
                                       beam_index=0b1000, distance=10, angle=270)
    align5 = baseplate.place_element_relative("alignment5", optomech.mirror_mount_c05g, cage, 
                                     angle=180, x_off=-100)
    pinhole = baseplate.place_element_relative("pinhole", optomech.pinhole_ida12, align5, 
                                     angle=180, x_off=-10)
    # baseplate.place_element("mirror_end", optomech.circular_mirror, x=30, y=125, angle=0,
    #                         mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_relative("mirror_end", optomech.mirror_mount_k05s2, pinhole, 
                                     angle=0, x_off=-20)
    
    # Wave picking components
    baseplate.place_element("wpick", optomech.circular_splitter, x=wpick_x, 
                            y=wpick_y, angle=90+45, mount_type=optomech.splitter_mount_b05g)
    baseplate.place_element("alignment6", optomech.mirror_mount_c05g, x=wpick_x-150,
                            y=wpick_y, angle=180)
    baseplate.place_element("wmir_out", optomech.circular_mirror, x=wpick_x-170,
                            y=wpick_y, angle=45, mount_type=optomech.mirror_mount_k05s1)
    baseplate.place_element("fiberout2", optomech.fiberport_mount_hca3, x=wpick_x-170,
                            y=6*layout.inch, angle=270)
    
    
if __name__ == "__main__":
    qzz_ta_input()
    layout.redraw()