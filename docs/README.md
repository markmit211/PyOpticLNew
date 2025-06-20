# Auto-Generated Documentation  
## Layout  
### baseplate
  
    A class for defining new baseplates  
  
    Args:  
        dx, dy, dz (float): The footprint of the baseplate including the gaps  
        x, y (float): The coordinates the baseplate (and all elements) should be placed at (in inches)  
        gap (float): The amount of material to remove around the edge of the baseplate  
        name (string): Name of the baseplate object  
        drill (bool): Whether or not the baseplate should be drilled  
        mount_holes (tuple[]): An array representing the x and y coordinates of each mount point (in inches)  
        label (string): The label to be embossed into the side of the baseplate  
        x_offset, y_offset (float): Additional offset from the grid in the x and y directions  
        optics_dz (float): The optical height of baseplate  
        invert_label (bool): Wheather to switch the face the label is embossed on  
    
### baseplate_cover
  
    Add an optical table mounting grid  
  
    Args:  
        dx, yy (float): The dimentions of the table grid (in inches)  
        z_off (float): The z offset of the top of the grid surface  
    
### table_grid
  
    Add an optical table mounting grid  
  
    Args:  
        dx, yy (float): The dimentions of the table grid (in inches)  
        z_off (float): The z offset of the top of the grid surface  
    
### baseplate.add_cover
  
        Place an element at a fixed coordinate on the baseplate  
  
        Args:  
            name (string): Label for the object  
            obj_class (class): The object class associated with the part to be placed  
            x, y (float): The coordinates the object should be placed at  
            angle (float): The rotation of the object about the z axis  
            optional (bool): If this is true the object will also transmit beams  
            args (any): Additional args to be passed to the object (see object class docs)  
        
### baseplate.place_element_along_beam
  
        Place an element at along a given beam path  
  
        Args:  
            name (string): Label for the object  
            obj_class (class): The object class associated with the part to be placed  
            beam_obj (beam_path): The beam path object to be associated with this object  
            beam_index (int): The beam index the object should be placed along (binary format recommended)  
            angle (float): The rotation of the object about the z axis  
            distance, x, y (float): The constraint of the placement, either a distance from the last object or a single coordinate value  
            pre_refs (int): The number of interactions which must take place before this object can be placed along the beam  
            optional (bool): If this is true the object will also transmit beams  
            args (any): Additional args to be passed to the object (see object class docs)  
        
### baseplate.place_element_relative
  
        Place an element relative to another object  
  
        Args:  
            name (string): Label for the object  
            obj_class (class): The object class associated with the part to be placed  
            rel_obj (obj): The parent object which this object will be relative to  
            angle (float): The rotation of the object about the z axis  
            x_off, y_off (float): The offset between the parent object and this object  
            optional (bool): If this is true the object will also transmit beams  
            args (any): Additional args to be passed to the object (see object class docs)  
        
### baseplate.add_beam_path
  
        Add a new dynamic beam path  
  
        Args:  
            x, y (float): The coordinate the beam should enter at  
            angle (float): The angle the beam should enter at  
            name (string): Label for the beam path object  
            color (float[3]): Color of the beam path object in RGB format  
        
### baseplate.execute
  
        Place an element at a fixed coordinate on the baseplate  
  
        Args:  
            name (string): Label for the object  
            obj_class (class): The object class associated with the part to be placed  
            x, y, z (float): The coordinates the object should be placed at in inches  
            angle (float): The rotation of the object about the z axis  
            optional (bool): If this is true the object will also transmit beams  
            args (any): Additional args to be passed to the object (see object class docs)  
        
## Optomech  
### example_component
  
    An example component class for reference on importing new components  
    creates a simple cube which mounts using a single bolt  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### drill_test
  
    An example component class for reference on importing new components  
    creates a simple cube which mounts using a single bolt  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### surface_adapter_for_chromatic
  
    Surface adapter for chromatic waveplate module  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mount_hole_dy (float) : The spacing between the two mount holes of the adapter  
        adapter_height (float) : The height of the suface adapter  
        outer_thickness (float) : The thickness of the walls around the bolt holes  
        tolerance (float) : Space between adapter and baseplate cutout in millimeters  
    
### chromatic_rotation_stage
  
    Rotation stage, model FBR-AH2  
  
    Args:  
        invert (bool) : Whether the mount should be offset 90 degrees from the component  
        mount_hole_dy (float) : The spacing between the two mount holes of it's adapter  
        wave_plate_part_num (string) : The Thorlabs part number of the wave plate being used  
  
    Sub-Parts:  
        surface_adapter (adapter_args)  
    
### isolator_895_high_power
  
    Isolator 895 On Mount; Larger power range for TA usage  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
        cage (bool) : Whether the isolator should be mounted using a side post cage system  
        or not (default set to False to indicate mounting directly to baseplate)  
    
### fiberport_12mm
  
    12mm Fiberport Mount with Drill only in top face of mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
        port (int) : 0 if no port, 1 if long port, 2 if short port  
    
### fiberport_12mm_sidemount
  
    12mm Fiberport Mount with drill in top and side of baseplate  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
        port (int) : 0 if no port, 1 if long port, 2 if short port  
    
### mirror_mount_m05
  
    New Mirror mount: Newport m05  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
    
### miniTA
  
    Butterfly laser shape to be placed on driver  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### eval_miniTA
  
    Evaluation board for miniTA  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### isolator_895
  
    Isolator 895 On Mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### isolator_850
  
    Isolator 850 On Mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### butterfly_laser
  
    Butterfly laser shape to be placed on driver  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### butterfly_laser_on_koheron_driver
  
    Butterfly laser on Koheron CTL200_V5 Driver  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### cage_mount_adapter
  
    Surface adapter for cage mount import.  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### cage_mount_pair
  
    Cage Mount Pair CP33 with baseplate adapter mounts  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        side_length (float) : The side length of the cube  
    
### modular1
  
    Modular Cutouts for mounting 14_20 bolts to connect adjacent baseplates.  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        z_offset (float) : How far down to offset the mount from the laser height (default flush)  
        Spread (float) : Distance between cutout centers  
        female (bool) : True if female cutout, False(default) if male  
    
### baseplate_mount
  
    Mount holes for attaching to an optical table  
    Uses 14_20 bolts with washers  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        bore_depth (float) : The depth for the counterbore of the mount hole  
    
### surface_adapter
  
    Surface adapter for post-mounted parts  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mount_hole_dy (float) : The spacing between the two mount holes of the adapter  
        adapter_height (float) : The height of the suface adapter  
        outer_thickness (float) : The thickness of the walls around the bolt holes  
        adjust (bool) : Whether mounted part movement should be allowed  
        adjust_dist (float) : Amount mounted part may move in millimeters  
        tolerance : Space between surface adapter and baseplate cutout in millimeters  
    
### skate_mount
  
    Skate mount for splitter cubes  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        cube_dx, cube_dy (float) : The side length of the splitter cube  
        mount_hole_dy (float) : The spacing between the two mount holes of the adapter  
        cube_depth (float) : The depth of the recess for the cube  
        outer_thickness (float) : The thickness of the walls around the bolt holes  
        cube_tol (float) : The tolerance for size of the recess in the skate mount  
    
### slide_mount
  
    Slide mount adapter for post-mounted parts  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        slot_length (float) : The length of the slot used for mounting to the baseplate  
        drill_offset (float) : The distance to offset the drill hole along the slot  
        adapter_height (float) : The height of the suface adapter  
        post_thickness (float) : The thickness of the post that mounts to the element  
        outer_thickness (float) : The thickness of the walls around the bolt holes  
    
### fiberport_mount_hca3
  
    Part for mounting an HCA3 fiberport coupler to the side of a baseplate  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### rotation_stage_rsp05
  
    Rotation stage, model RSP05  
  
    Args:  
        invert (bool) : Whether the mount should be offset 90 degrees from the component  
        mount_hole_dy (float) : The spacing between the two mount holes of it's adapter  
        wave_plate_part_num (string) : The Thorlabs part number of the wave plate being used  
  
    Sub-Parts:  
        surface_adapter (adapter_args)  
    
### rotation_stage_rsp1
  
    Rotation stage, model RSP1  
  
    Args:  
        invert (bool) : Whether the mount should be offset 90 degrees from the component  
        mount_hole_dy (float) : The spacing between the two mount holes of it's adapter  
        wave_plate_part_num (string) : The Thorlabs part number of the wave plate being used  
  
    Sub-Parts:  
        surface_adapter (adapter_args)  
    
### mirror_mount_k05s2
  
    Mirror mount, model K05S2  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
    
### mirror_mount_k05s1
  
    Mirror mount, model K05S1  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
    
### splitter_mount_b05g
  
    Splitter mount, model B05G  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        splitter (bool) : Whether to add a splitter plate component to the mount  
  
    Sub-Parts:  
        circular_splitter (mirror_args)  
    
### splitter_mount_b1g
  
    Splitter mount, model B1G  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        splitter (bool) : Whether to add a splitter plate component to the mount  
  
    Sub-Parts:  
        circular_splitter (mirror_args)  
    
### mirror_mount_c05g
  
    Mirror mount, model C05G  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### mirror_mount_km05
  
    Mirror mount, model KM05  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
        bolt_length (float) : The length of the bolt used for mounting  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### mirror_mount_km100
  
    Mirror mount, model KM100  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
        bolt_length (float) : The length of the bolt used for mounting  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### fixed_mount_smr05
  
    Fixed mount, model SMR05  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        bolt_length (float) : The length of the bolt used for mounting  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### prism_mount_km05pm
  
    Mount, model KM05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### grating_mount_on_km05pm
  
    Grating and Parallel Mirror Mounted on MK05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        littrow_angle (float) : The angle of the grating and parallel mirror  
  
    Sub_Parts:  
        mount_mk05pm (mount_args)  
        square_grating (grating_args)  
        square_mirror (mirror_args)  
    
### grating_mount_on_km05pm_no_arm
  
    Grating and Parallel Mirror Mounted on MK05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        littrow_angle (float) : The angle of the grating and parallel mirror  
  
    Sub_Parts:  
        mount_mk05pm (mount_args)  
        square_grating (grating_args)  
        square_mirror (mirror_args)  
    
### mount_tsd_405sluu
  
    Mount, model KM05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### mirror_mount_ks1t
  
    Mirror mount, model KS1T  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### fiberport_mount_km05
  
    Mirror mount, model KM05, adapted to use as fiberport mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        mirror_mount_km05 (mount_args)  
        fiber_adapter_sm05fca2  
        lens_tube_sm05l05  
        lens_adapter_s05tm09  
        mounted_lens_c220tmda  
    
### fiberport_mount_ks1t
  
    Mirror mount, model KM05, adapted to use as fiberport mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        mirror_mount_km05 (mount_args)  
        fiber_adapter_sm05fca2  
        lens_tube_sm05l05  
        lens_adapter_s05tm09  
        mounted_lens_c220tmda  
    
### km05_50mm_laser
  
    Mirror mount, model KM05, adapted to use as laser mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        tec_thickness (float) : The thickness of the TEC used  
  
    Sub-Parts:  
        mirror_mount_km05 (mount_args)  
        km05_tec_upper_plate (upper_plate_args)  
        km05_tec_lower_plate (lower_plate_args)  
    
### mirror_mount_mk05
  
    Mirror mount, model MK05  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### mount_mk05pm
  
    Mount, model MK05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### dichoric_mirror_mount_km05fl
  
    Mirror mount, model MK05  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### dichoric_mirror_mount_km05fR
  
    Mirror mount, model KM05FR  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        circular_mirror (mirror_args)  
    
### grating_mount_on_mk05pm
  
    Grating and Parallel Mirror Mounted on MK05PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        littrow_angle (float) : The angle of the grating and parallel mirror  
  
    Sub_Parts:  
        mount_mk05pm (mount_args)  
        square_grating (grating_args)  
        square_mirror (mirror_args)  
    
### lens_holder_l05g
  
    Lens Holder, Model L05G  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        circular_lens (lens_args)  
    
### pinhole_ida12
  
    Pinhole Iris, Model IDA12  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        slide_mount (adapter_args)  
    
### prism_mount_km100pm
  
    Kinematic Prism Mount, Model KM100PM  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### mount_for_km100pm
  
    Adapter for mounting isomet AOMs to km100pm kinematic mount  
  
    Args:  
        mount_offset (float[3]) : The offset position of where the adapter mounts to the component  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        slot_length (float) : The length of the slots used for mounting to the km100pm  
        countersink (bool) : Whether to drill a countersink instead of a counterbore for the AOM mount holes  
        counter_depth (float) : The depth of the countersink/bores for the AOM mount holes  
        arm_thickness (float) : The thickness of the arm the mounts to the km100PM  
        arm_clearance (float) : The distance between the bottom of the adapter arm and the bottom of the km100pm  
        stage_thickness (float) : The thickness of the stage that mounts to the AOM  
        stage_length (float) : The length of the stage that mounts to the AOM  
    
### isomet_1205c_on_km100pm
  
    Isomet 1205C AOM on KM100PM Mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        diffraction_angle (float) : The diffraction angle (in degrees) of the AOM  
        forward_direction (integer) : The direction of diffraction on forward pass (1=right, -1=left)  
        backward_direction (integer) : The direction of diffraction on backward pass (1=right, -1=left)  
  
    Sub-Parts:  
        prism_mount_km100pm (mount_args)  
        mount_for_km100pm (adapter_args)  
    
### isolator_670
  
    Isolator Optimized for 670nm, Model IOT-5-670-VLP  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        surface_adapter (adapter_args)  
    
### isolator_405
  
    Isolator Optimized for 405nm, Model IO-3D-405-PBS  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        surface_adapter  
    
### rb_cell
  
    Rubidium Cell Holder  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### rb_cell_cube
  
    Rubidium Cell Holder  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### rb_cell_holder
  
    Rubidium Cell Holder  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### rb_cell_holder_old
  
    Rubidium Cell Holder  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
    
### photodetector_pda10a2
  
    Photodetector, model pda10a2  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
  
    Sub-Parts:  
        surface_adapter (adapter_args)  
      
    
### lens_tube_SM1L03
  
    SM1 Lens Tube, model SM1L03  
    
### periscope
  
    Custom periscope mount  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        lower_dz (float) : Distance from the bottom of the mount to the center of the lower mirror  
        upper_dz (float) : Distance from the bottom of the mount to the center of the upper mirror  
        mirror_type (obj class) : Object class of mirrors to be used  
        table_mount (bool) : Whether the periscope is meant to be mounted directly to the optical table  
  
    Sub-Parts:  
        mirror_type x2 (mirror_args)  
    
### thumbscrew_hkts_5_64
  
    Thumbscrew for 5-64 hex adjusters, model HKTS 5-64  
  
    Sub-Parts:  
        slide_mount (adapter_args)  
    
### fiber_adapter_sm05fca2
  
    Fiber Adapter Plate, model SM05FCA2  
    
### fiber_adapter_sm1fca2
  
    Fiber Adapter Plate, model SM1FCA2  
    
### lens_adapter_s05tm09
  
    SM05 to M9x0.5 Lens Cell Adapter, model S05TM09  
    
### lens_adapter_s1tm09
  
    SM1 to M9x0.5 Lens Cell Adapter, model S1TM09  
    
### lens_tube_sm05l05
  
    Lens Tube, model SM05L05  
    
### lens_tube_sm1l05
  
    Lens Tube, model SM1L05  
    
### mounted_lens_c220tmda
  
    Mounted Aspheric Lens, model C220TMD-A  
    
### diode_adapter_s05lm56
  
    Diode Mount Adapter, model S05LM56  
    
### photodiode_fds010
  
    Photodiode, model FDS010  
    
### Room_temp_chamber
  
    Nishat importing the room temperature schamber  
    Room_temperature_Chamber_simplified_version  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
    
### Room_temp_chamber_Mechanical
  
    Nishat importing the room temperature schamber  
    Room_temperature_Chamber_version  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        mirror (bool) : Whether to add a mirror component to the mount  
        thumbscrews (bool): Whether or not to add two HKTS 5-64 adjusters  
    
### square_grating
  
    Square Grating  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        thickness (float) : The thickness of the grating  
        width (float) : The width of the grating  
        height (float) : The height of the grating  
        part_number (string) : The part number of the grating being used  
    
### circular_splitter
  
    Circular Beam Splitter Plate  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        thickness (float) : The edge thickness of the plate  
        diameter (float) : The width of the plate  
        part_number (string) : The part number of the plate being used  
    
### cube_splitter
  
    Beam-splitter cube  
  
    Args:  
        cube_size (float) : The side length of the splitter cube  
        invert (bool) : Invert pick-off direction, false is left, true is right  
        cube_part_number (string) : The Thorlabs part number of the splitter cube being used  
    
### circular_lens
  
    Circular Lens  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        focal_length (float) : The focal length of the lens  
        thickness (float) : The edge thickness of the lens  
        diameter (float) : The width of the lens  
        part_number (string) : The part number of the lens being used  
    
### cylindrical_lens
  
    Cylindrical Lens  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        focal_length (float) : The focal length of the lens  
        thickness (float) : The edge thickness of the lens  
        width (float) : The width of the lens  
        height (float) : The width of the lens  
        part_number (string) : The part number of the lens being used  
    
### waveplate
  
    Waveplate  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        thickness (float) : The thickness of the waveplate  
        diameter (float) : The width of the waveplate  
        part_number (string) : The part number of the waveplate being used  
    
### circular_mirror
  
    Circular Mirror  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        thickness (float) : The thickness of the mirror  
        diameter (float) : The width of the mirror  
        part_number (string) : The part number of the mirror being used  
    
### square_mirror
  
    Square Mirror  
  
    Args:  
        drill (bool) : Whether baseplate mounting for this part should be drilled  
        thickness (float) : The thickness of the mirror  
        width (float) : The width of the mirror  
        height (float) : The height of the mirror  
        part_number (string) : The part number of the mirror being used  
    
