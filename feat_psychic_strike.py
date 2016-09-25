from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

def PsychicStrikeRadial(attachee, args, evt_obj):
  isEmbued = attachee.d20_query("PsyStrike Embued")
  if isEmbued:
    return 0
  radial_action = tpdp.RadialMenuEntryPythonAction(-1, D20A_PYTHON_ACTION, "Psychic Strike Radial", 0, "TAG_INTERFACE_HELP")
  radialAction.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Class)
  return 0
  
def PsychicStrikeDamage(attachee):
  slkLvl = attachee.stat_level_get(Soulknife)
  bonval = (slkLvl+1)/4 # Psychic Strike bonus damage is bonval d8's
  return bonval
  
def PsyStrikeEmbued(attachee, args, evt_obj):
  evt_obj.return_val = IsEmbued(args)
  return 0
  
def IsEmbued(args):
  if args.get_arg(0):
    return 1
  return 0

def OnPsyStrikeCheck(attachee, args, evt_obj):
  return 0

def OnPsyStrikePerform(attachee, args, evt_obj):
	args.set_arg(0, 1)  # Set to embued
  return 0 

def PsyStrikeHit(attachee, args, evt_obj):
  isEmbued = attachee.d20_query("PsyStrike Enbued")
  if isEnbued:
    return 0
  # Check if weapon hitting is a mind blade type
  # If not, return 0
  # Check if target is living, nonmindless, and not immune to mind affecting effects
  # If not, return 0
  # add to bonus value = PsychicStrikeDamage d8's
  args.set_arg(0, 0)  # Set to unembued
  
def PsyStrikeEffectTooltip(attachee, args, evt_obj):
  isEmbued = attachee.d20_query("PsyStrike Enbued")
  if not isEmbued:
    return 0
  evt_obj.append(?, ?, ?) # 53 is the indicator graphical index; buffs (indicators above portraits) are in the 0-89 range IIRC; will have to expand this to support new icons
return 0

psychicStrike = PythonModifier("Psychic Strike", 1)                                                 # arg0 - embued with energy
psiFocus.AddHook(ET_OnD20PythonQuery, "PsyStrike Embued", PsyStrikeEmbued, ())                      # hook PsyStrikeEmbued to event of python query
psychicStrike.AddHook(ET_OnBuildRadialMenuEntry, EK_NONE, PsychicStrikeRadial, ())                  # Add to radial menu
psychicStrike.AddHook(ET_OnD20PythonActionCheck, "Psychic Strike Radial", OnPsyStrikeCheck, ())     # Check if valid
psychicStrike.AddHook(ET_OnD20PythonActionPerform, "Psychic Strike Radial", OnPsyStrikePerform, ()) # Perform if valid
psychicStrike.MapToFeat("Psychic Strike")                                                           # Map to feat
