import LanguageControls,LaunchControls
from LanguageControls import Variables
import DirControls

#launch with interface
LaunchControls.launch()

# launch without interface
# LaunchControls.preInit()
# LaunchControls.init("prompt",LanguageControls.VARIABLES["CWD"][1])

print(DirControls.getRealPath("~"))