from PyOpticL import layout, optomech
from datetime import datetime

name = "Doublepass"
date_time = datetime.now().strftime("%m/%d/%Y")
label = name + " " +  date_time

base_dx = 11*layout.inch
base_dy = 5.75*layout.inch
base_dz = layout.inch
gap = 0

x_offset = 0.5
y_offset = 0.5

mount_holes_temp = [(1,2),(6,2),(1,5),(9,5)]

mount_holes = []
for x,y in mount_holes_temp:
    mount_holes.append((11-x-x_offset,5.75-y-y_offset))

# Note that for mirror_mount_c05g, an offset of 6mm is needed as the pos is 
# centered at the optical start, not the drill hole as in openscad. 

d_inch = 25.4

mount_hole_xoff = 13
mount_hole_yoff = 92-3*d_inch

x_tri = 24
aom_axis = 38 # distance to second optical axis
pbs_axis = aom_axis + 38
aom_xpos = 225-2

# input optics
module_output_offset = 19.1+15 ########################
mIn1_xpos = module_output_offset
mIn1_ypos = 78
mIn2_ypos = base_dy - 25
mIn2_xpos = mIn1_xpos + 1.8 * d_inch
mIn3_xpos = mIn2_xpos
fb_xpos = mIn1_xpos
fb_ypos = base_dy

# pbs and fiber out
pbs_xpos = mIn3_xpos + 75
mOut1_xpos = pbs_xpos
mOut1_ypos = pbs_axis+ 47
hwp_xpos = mOut1_xpos+35
hwp_ypos = mOut1_ypos
mOut2_xpos = base_dx - module_output_offset
fb_out_xpos = mOut2_xpos
fb_out_ypos = base_dy

# turning mirrors
m1_xpos = 260 + 2

# telescope
tele1 = True # 1/2
fiber = False # no telescope
pccIn_xpos = aom_xpos + 20

# cat's eye components
left_axis = 60
qwp_xpos = aom_xpos - 60
pcx1_xpos = aom_xpos - 100 # 100mm focal distance lens
pcx1a_xpos = pcx1_xpos - 15
mCat_xpos = pcx1_xpos - 100 - 1
# mCat_ypos = 75 - (pcx1_xpos - mCat1_xpos)

fpout2_xpos = fb_out_xpos + d_inch + 6

# testing
mT1_xpos = mOut1_xpos + 10
mT2_xpos = pcx1_xpos-30
mT3_xpos = mT1_xpos + 40
# mT4_xpos = aom_xpos+15
mT4_xpos = fb_out_xpos + d_inch

# show_test_beams = True
show_test_beams = False

# Start on line 160 in openSCAD
ap3_xpos = mIn3_xpos + 35
ap3_ypos = pbs_axis

hwp3_xpos = mIn2_xpos
hwp3_ypos = mIn2_ypos - 30

pin2_xpos = hwp_xpos+15

ap2_xpos = mCat_xpos + 35
ap2_ypos = aom_axis



def doublepass(x=0, y=0, angle=0, mirror=optomech.mirror_mount_km05, x_split=False, thumbscrews=True):

    baseplate = layout.baseplate(base_dx, base_dy, base_dz, x=x, y=y, angle=angle,
                                 gap=gap, mount_holes=mount_holes,
                                 name=name, label=label)

    # add beam
    beam = baseplate.add_beam_path(x=fb_xpos, y=fb_ypos, angle=layout.cardinal['down'], color = (0,0,255))

    # add input fiberport, defined at the same coordinates as beam
    # baseplate.place_element_along_beam("fp_in", optomech.fiberport_mount_hca3, beam,
    #                                    beam_index=0b1, x=fb_xpos, y=fb_ypos, 
    #                                    angle=layout.cardinal['down'])
    baseplate.place_element("fp_in", optomech.fiberport_mount_hca3, x=fb_xpos, 
                            y=fb_ypos, angle=layout.cardinal['down'])
    baseplate.place_element_along_beam("mIn1", optomech.circular_mirror, beam, 
                                       beam_index=0b1, distance=25,
                                       angle=45, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("mIn2", optomech.circular_mirror, beam, 
                                       beam_index=0b1, distance=mIn2_xpos-mIn1_xpos, 
                                       angle=-135, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element_along_beam("mIn3", optomech.circular_mirror, beam, 
                                       beam_index=0b1, distance=fb_ypos-25-pbs_axis, 
                                       angle=45, mount_type=optomech.mirror_mount_k05s2)
    # baseplate.place_element("mIn3", optomech.circular_mirror, x=mIn3_xpos, y=pbs_axis, 
    #                         angle=45, mount_type=optomech.mirror_mount_k05s2)
    # baseplate.place_element_along_beam("ap3", optomech.mirror_mount_c05g, beam, 
    #                                    beam_index=0b1, distance=35, angle=0)
    baseplate.place_element("ap3", optomech.mirror_mount_c05g, x=ap3_xpos-6, 
                            y=ap3_ypos, angle=0)
    # baseplate.place_element_along_beam("ap4", optomech.mirror_mount_c05g, beam, 
    #                                    beam_index=0b1, distance=105, angle=0)
    baseplate.place_element("ap4", optomech.mirror_mount_c05g, x=ap3_xpos+105-6, 
                            y=ap3_ypos, angle=0)
    baseplate.place_element("hwp", optomech.rotation_stage_rsp05, x=hwp3_xpos, 
                            y=hwp3_ypos, angle=90)
    baseplate.place_element("pin1", optomech.pinhole_ida12, x=mIn2_xpos, 
                            y=mIn2_ypos-15, angle=90)
    # baseplate.place_element_along_beam("pbs", optomech.cube_splitter, beam, 
    #                                    beam_index=0b1, distance=75, angle=270, mount_type=optomech.skate_mount)
    baseplate.place_element("pbs", optomech.cube_splitter, x=pbs_xpos, y=pbs_axis, 
                            angle=0)
    baseplate.place_element("pbs_mount", optomech.skate_mount, x=pbs_xpos, y=pbs_axis, 
                            angle=90)
    # baseplate.place_element_along_beam("mBack", optomech.circular_mirror, beam, 
    #                                    beam_index=0b11, distance=mOut1_ypos-pbs_axis, 
    #                                    angle=-45, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element("mBack", optomech.circular_mirror, x=mOut1_xpos, 
                            y=mOut1_ypos, angle=-45, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element("ap5", optomech.mirror_mount_c05g, x=pbs_xpos, 
                            y=pbs_axis+27-6, angle=90)
    baseplate.place_element("hwp", optomech.rotation_stage_rsp05, x=hwp_xpos, 
                            y=hwp_ypos, angle=0)
    # baseplate.place_element_along_beam("mOut2", optomech.mirror_mount_c05g, beam, 
    #                                    beam_index=0b11, distance=66, angle=180)
    baseplate.place_element("OpmOut", optomech.mirror_mount_c05g, x=hwp_xpos+31+6,
                            y=hwp_ypos, angle=180)
    # baseplate.place_element_along_beam("mOut2", optomech.circular_mirror, beam, 
    #                                    beam_index=0b11, distance=mOut2_xpos-mOut1_xpos, 
    #                                    angle=135, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element("mOut2", optomech.circular_mirror, x=mOut2_xpos, 
                            y=mOut1_ypos, angle=135, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element("fiberOut", optomech.fiberport_mount_hca3, x=fb_out_xpos, 
                            y=fb_out_ypos, angle=layout.cardinal['down'])
    baseplate.place_element("pin2", optomech.pinhole_ida12, x=pin2_xpos, 
                            y=mOut1_ypos, angle=0)
    baseplate.place_element("rot2", optomech.rotation_stage_rsp05, x=qwp_xpos, 
                            y=aom_axis, angle=0)
    baseplate.place_element("mCat", optomech.circular_mirror, x=mCat_xpos, 
                            y=aom_axis, angle=0, mount_type=optomech.mirror_mount_k05s2)
    baseplate.place_element("pin3", optomech.pinhole_ida12, x=mCat_xpos+5, 
                            y=aom_axis, angle=0)
    if fiber:
        baseplate.place_element("m1", optomech.circular_mirror, x=m1_xpos, 
                                y=pbs_axis, angle=-135, mount_type=optomech.mirror_mount_k05s2)
        baseplate.place_element("m2", optomech.circular_mirror, x=m1_xpos, 
                                y=aom_axis, angle=135, mount_type = optomech.mirror_mount_k05s2)
    
    if tele1: # telescope
        baseplate.place_element("m1", optomech.circular_mirror, x=m1_xpos, 
                                y=pbs_axis, angle=-135, mount_type=optomech.mirror_mount_k05s2)
        baseplate.place_element("m2", optomech.circular_mirror, x=m1_xpos, 
                                y=aom_axis, angle=135, mount_type = optomech.mirror_mount_k05s2)
        # Additional for telescope:
        # baseplate.place_element("pccIn", optomech.circular_lens, x=pccIn_xpos, 
        #                         y=pbs_axis, angle=0, mount_type=optomech.lens_holder_l05g)
        baseplate.place_element("pccIn", optomech.lens_holder_l05g, x=pccIn_xpos, 
                                y=pbs_axis, angle=0)
        baseplate.place_element("pccIn2", optomech.lens_holder_l05g, x=pccIn_xpos-50,
                                y=pbs_axis, angle=0)
    
    baseplate.place_element("ap2b", optomech.circular_lens, x=ap2_xpos-6, 
                            y=ap2_ypos, angle=0, mount_type=optomech.mirror_mount_c05g, 
                            focal_length=10000000)
    baseplate.place_element("ap2a", optomech.circular_lens, x=m1_xpos-5-6, 
                            y=ap2_ypos, angle=0, mount_type=optomech.mirror_mount_c05g)
    # baseplate.place_element("mod_mount", optomech.modular1, x=fb_xpos, 
    #                         y=fb_ypos, angle=90, zPos=0, xPos=0, yPos=0, inz=12.7+6.604/2, iny=20) #Change back to 20
    # baseplate.place_element("mod_mount", optomech.modular1, x=fb_out_xpos, 
    #                         y=fb_ypos, angle=90, zPos=12.7, xPos=37.4/2+11-0.5, yPos=26.1, inz=12.7+14.5/2, iny=26.1)

    baseplate.place_element("mod_mountL", optomech.modular1, x=fb_xpos, 
                            y=fb_ypos, angle=90)
    baseplate.place_element("mod_mountR", optomech.modular1, x=fb_out_xpos, 
                            y=fb_ypos, angle=90)
    baseplate.place_element("aom", optomech.isomet_1205c_on_km100pm, x=aom_xpos, 
                            y=aom_axis, angle=0)
    # baseplate.place_element("test_part", optomech.pinhole_ida12, x=aom_xpos,
    #                         y=aom_axis, angle=0)
    baseplate.place_element("cage_mount_pair", optomech.cage_mount_pair, x=pcx1_xpos-1.7*d_inch+1, 
                            y=aom_axis, angle=90, height=0, spread=2.5*d_inch, tolerance=5)
    

        






if __name__ == "__main__":
    doublepass()
    layout.redraw()