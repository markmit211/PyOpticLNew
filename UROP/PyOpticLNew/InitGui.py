import FreeCADGui as Gui

class OpticsWorkbench (Workbench):

    MenuText = "PyOpticL"
    ToolTip = "A workbench for designing baseplates for optical layouts"
    Icon =  """
            /* XPM */
            static char *_0ddddfe6a2d42f3d616a62ec3bb0f7c8Jp52mHVQRFtBmFY[] = {
            /* columns rows colors chars-per-pixel */
            "16 16 6 1 ",
            "  c #ED1C24",
            ". c #ED5C5E",
            "X c #ED9092",
            "o c #EDBDBD",
            "O c #EDDFDF",
            "+ c None",
            /* pixels */
            "+++++++++..XooOO",
            "++++++..+..XXooO",
            "++++++++++. XXoo",
            "+++++++.++  .XXo",
            "++++++.++  .  XX",
            "++++++++  .  ..X",
            "+++++++  .  ++..",
            "++++++  .  +++++",
            "+++++  .  ++.+.+",
            "++++  .  ++.++.+",
            "+++  .  ++++++++",
            "++  .  +++++++++",
            "+  .  ++++++++++",
            "  .  +++++++++++",
            " .  ++++++++++++",
            ".  +++++++++++++"
            };
            """

    def Initialize(self):
        """This function is executed when the workbench is first activated.
        It is executed once in a FreeCAD session followed by the Activated function.
        """
        import guiCommands
        self.toolbar = ["RerunMacro", "RedrawBaseplate", "ShowComponents", "ToggleDrawStyle", "ExportSTLs", "ExportCart", "ReloadModules", "GetOrientation", "GetPosition"] # A list of command names created in the line above
        self.appendToolbar("PyOpticL Commands",self.toolbar) # creates a new toolbar with your commands
        self.appendMenu(["PyOpticL"],self.toolbar) # appends a submenu to an existing menu

    def Activated(self):
        """This function is executed whenever the workbench is activated"""
        return

    def Deactivated(self):
        """This function is executed whenever the workbench is deactivated"""
        return

    def ContextMenu(self, recipient):
        """This function is executed whenever the user right-clicks on screen"""
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("PyOpticL Commands",self.toolbar) # add commands to the context menu

    def GetClassName(self): 
        # This function is mandatory if this is a full Python workbench
        # This is not a template, the returned string should be exactly "Gui::PythonWorkbench"
        return "Gui::PythonWorkbench"

Gui.addWorkbench(OpticsWorkbench())