from PyOpticL import layout, optomech
import math

d_inch = layout.inch
# baseplate constants
base_dx = 278.4
base_dy = 127
base_thick = d_inch
gap = d_inch/8

# Global variables from openSCAD for testing
screw_tap_dia_6_32 = 0.1065*d_inch
screw_tap_dia_8_32 = 0.1360*d_inch
screw_tap_dia_14_20 = 0.201*d_inch
screw_clear_dia_14_20 = 0.260*d_inch
screw_head_clear_dia_14_20 = 9.8
screw_washer_dia_14_20 = 9/16*d_inch # #12 washer

base_dz = 0.5*d_inch

# x-y coordinates of mount holes (in inches)
mount_hole_xoff = 13 # location of lower left mounting hole
mount_hole_yoff = 92-3*d_inch 

x_tri = 24
aom_axis = 38 # distance to second optical axis
pbs_axis = aom_axis + 32

aom_xpos = 225-2

# input optics
mIn1_xpos = 20
mIn1_ypos = 78
mIn2_ypos = mIn1_ypos+30
mIn2_xpos = mIn1_xpos + 30*math.tan(55/180*math.pi)
mIn3_xpos = mIn2_xpos
fb_xpos = mIn1_xpos
fb_ypos = 127

# pbs and fiber out
pbs_xpos = mIn3_xpos + 50
mOut1_xpos = pbs_xpos
mOut1_ypos = pbs_axis+ 35 + 1
hwp_xpos = mOut1_xpos+35
hwp_ypos = mOut1_ypos
mOut2_xpos = hwp_xpos + 65
fb_out_xpos = mOut2_xpos
fb_out_ypos = 127

# turning mirrors
m1_xpos = 260 + 2

# telescope
tele1 = True # 1/2
fiber = False # no telescope
pccIn_xpos = aom_xpos - 12

# cat's eye components
left_axis = 60
qwp_xpos = aom_xpos - 75
pcx1_xpos = aom_xpos - 100	# 100mm focal distance lens
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

# show_test_beams = true;
show_test_beams = False

ap3_xpos = mIn3_xpos + 28
ap3_ypos = pbs_axis

ap4_xpos = m1_xpos-18
ap4_ypos = pbs_axis

ap5_xpos = mIn1_xpos + 8
th_min1_refl = 125/2 - (90-125/2)
th_ap5 = th_min1_refl - 180
ap5_ypos = mIn1_ypos + (ap5_xpos - mIn1_xpos) * math.tan(th_min1_refl*math.pi/180)

hwp3_xpos = pbs_xpos - 15
hwp3_ypos = pbs_axis

pin2_xpos = mOut2_xpos - 82

# xoff = mount_hole_xoff
# yoff = mount_hole_yoff
####################### Changed temporarily until fixed ####################
xoff = 0
yoff = 0

mount_holes_mm = [(xoff, yoff + 3*d_inch),(xoff, yoff),(xoff + 9*d_inch, yoff),(xoff+4*d_inch, yoff)]
# Convert mount holes to inches:
mount_holes = []
for x,y in mount_holes_mm:
    mount_holes.append((x/d_inch, y/d_inch))

# beam start positions in mm
beam_x = 20
beam_y = 127



# function so baseplate can be added to other layouts
def doublepass_aom(x=0, y=0, angle=0):

    # define and place baseplate object
    baseplate = layout.baseplate(base_dx, base_dy, base_thick, x=x, y=y, angle=angle,
                                 gap=0, mount_holes=mount_holes, drill=True)

    # add beam
    beam = baseplate.add_beam_path(x=beam_x, y=beam_y, angle=layout.cardinal['down'], color = (0,0,255))

    # add input fiberport, defined at the same coordinates as beam
    baseplate.place_element("fp_in", optomech.fiberport_mount_hca3,
                            x=beam_x, y=beam_y, angle=layout.cardinal['down'])
    
    baseplate.place_element_along_beam("mIn1", optomech.circular_mirror, beam,
                                       beam_index = 0b1, distance = beam_y-mIn1_ypos,
                                       angle=125/2, mount_type = optomech.mirror_mount_c05g)
    
    # baseplate.place_element("mIn1", optomech.mirror_mount_c05g, 
    #                         x=mIn1_xpos, y=mIn1_ypos, angle=125/2)
    
    mIn2_dist = math.sqrt((mIn2_xpos-mIn1_xpos)**2+(mIn2_ypos-mIn1_ypos)**2)
    baseplate.place_element_along_beam("mIn2", optomech.circular_mirror, beam,
                                       beam_index = 0b1, distance=mIn2_dist,
                                        angle = 125/2-180, mount_type=optomech.mirror_mount_k05s1 )
    
    # baseplate.place_element("mIn2", optomech.circular_mirror,
    #                         x=mIn2_xpos, y=mIn2_ypos, angle=125/2-180, 
    #                         mount_type = optomech.mirror_mount_k05s1)

    baseplate.place_element("mIn3", optomech.circular_mirror, 
                            x=mIn3_xpos, y=pbs_axis, angle=45, 
                            mount_type = optomech.mirror_mount_k05s1)
    
    # baseplate.place_element("ap3", optomech.mirror_mount_c05g,
    #                         x=ap3_xpos, y=ap3_ypos, angle=0)
    
    # baseplate.place_element("ap4", optomech.mirror_mount_c05g,
    #                         x=ap4_xpos, y=ap4_ypos, angle=0)
    
    # baseplate.place_element("ap5", optomech.mirror_mount_c05g,
    #                         x=ap5_xpos, y=ap5_ypos, angle=th_ap5)
    # hwp near input fibercoupler
    baseplate.place_element("hwpl", optomech.rotation_stage_rsp05, 
                            x=fb_xpos, y=fb_ypos-20, angle=90)
    
    baseplate.place_element("hwp3", optomech.rotation_stage_rsp05,
                            x=hwp3_xpos, y=hwp3_ypos, angle=0)
    # pbs and output
    baseplate.place_element("pbs1", optomech.cube_splitter,
                            x=pbs_xpos, y=pbs_axis, angle=90,
                            mount_type=optomech.skate_mount)

    baseplate.place_element("mOut1", optomech.circular_mirror, 
                            x=mOut1_xpos, y=mOut1_ypos, angle=-45, 
                            mount_type = optomech.mirror_mount_k05s1)
    
    baseplate.place_element("hwp2", optomech.rotation_stage_rsp05, 
                            x=hwp_xpos, y=hwp_ypos, angle=0)
    
    baseplate.place_element("mOut2", optomech.circular_mirror, 
                            x=mOut2_xpos, y=mOut1_ypos, angle=135, 
                            mount_type = optomech.mirror_mount_k05s1)
    # Output fiberport
    baseplate.place_element("fp_out1", optomech.fiberport_mount_hca3, 
                            x=fb_out_xpos, y=fb_out_ypos, angle=-90)
    ############ Need to place on slide mount #############
    baseplate.place_element("pin2", optomech.pinhole_ida12, 
                            x=pin2_xpos, y=mOut1_ypos, angle=0)
    
    baseplate.place_element("aom", optomech.isomet_1205c_on_km100pm,
                            x=aom_xpos, y=aom_axis, angle=0)
    
    baseplate.place_element("pcx", optomech.circular_lens, 
                            x=pcx1_xpos, y=aom_axis, angle=0,
                            mount_type = optomech.lens_holder_l05g)
    
    # baseplate.place_element("pcx1a", optomech.circular_lens,
    #                         x=pcx1a_xpos, y=aom_axis, angle=0,
    #                         mount_type = optomech.lens_holder_l05g)
    
    baseplate.place_element("qwp", optomech.rotation_stage_rsp05,
                            x=qwp_xpos, y=aom_axis, angle=0)
    
    baseplate.place_element("mCat", optomech.circular_mirror,
                            x=mCat_xpos, y=aom_axis, angle=0,
                            mount_type = optomech.mirror_mount_k05s1)
    
    baseplate.place_element("mCat_pinhole", optomech.pinhole_ida12,
                            x=mCat_xpos+5, y=aom_axis, angle=0)
    
    if fiber:
        baseplate.place_element("m2", optomech.circular_mirror,
                                x=m1_xpos, y=aom_axis, angle=135,
                                mount_type=optomech.mirror_mount_k05s1)
        
        baseplate.place_element("m1", optomech.circular_mirror,
                                x=m1_xpos, y=pbs_axis, angle=-135,
                                mount_type=optomech.mirror_mount_k05s1)
        
    if tele1:
        baseplate.place_element("m2", optomech.circular_mirror,
                                x=m1_xpos, y=aom_axis, angle=135,
                                mount_type=optomech.mirror_mount_k05s1)
        
        baseplate.place_element("m1", optomech.circular_mirror,
                                x=m1_xpos, y=pbs_axis, angle=-135,
                                mount_type=optomech.mirror_mount_k05s1)
        # Change focal length of circular lens to make columnated beams
        baseplate.place_element("pcc", optomech.circular_lens,
                                x=pccIn_xpos, y=pbs_axis, angle=0,
                                mount_type=optomech.lens_holder_l05g)
        
        baseplate.place_element("pcx+100", optomech.circular_lens,
                                x=pccIn_xpos-50, y=pbs_axis, angle=0,
                                mount_type=optomech.lens_holder_l05g)
        
    ##### Pickup in openSCAD file on line 270
    


# this allows the file to be run as a macro or imported into other files
if __name__ == "__main__":
    doublepass_aom()
    layout.redraw()