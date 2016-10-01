from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

def WildTalent(attachee, args, evt_obj):
  attachee.d20_send_signal("Increase Max Psi", 2)
  return 0

feat_wild_talent = PythonModifier("feat_wild_talent", 1)
feat_wild_talent.MapToFeat("feat_wild_talent")
