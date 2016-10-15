from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

psiStrikeEnum = 6001 # enum for Psy Strike action

def PsychicStrikeRadial(attachee, args, evt_obj):
  isEmbued = attachee.d20_query("PsyStrike Embued")
  if isEmbued:
    return 0
  radial_action = tpdp.RadialMenuEntryPythonAction(-1, D20A_PYTHON_ACTION, psiStrikeEnum, 0, "TAG_INTERFACE_HELP")
  radialAction.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Class)
  return 0
  
def PsychicStrikeDamage(attachee, args, evt_obj):
  if not IsEmbued(args):
    return 0
  # Check if target is living, nonmindless, and not immune to mind affecting effects
  tgt = evt_obj.attack_packet.target
  if tgt == OBJ_HANDLE_NULL:
    return 0
  if tgt.is_category_type(mc_type_undead):
    return 0
  if tgt.is_category_type(mc_type_elemental):
    return 0
  if tgt.is_category_type(mc_type_construct):
    return 0
  # todo immune to mind affecting / mindless
  
  slkLvl = attachee.stat_level_get(stat_level_soulknife)
  bonval = (slkLvl+1)/4 # Psychic Strike bonus damage is bonval d8's
  if bonval <= 0:
    return 0
  
  dice = dice_new('1d8')
  dice.number = bonval
  evt_obj.damage_packet.add_dice(dice, D20DT_UNSPECIFIED, 100) # will add xd8 unspecified damage type, and list the cause as "Weapon" (entry 100 in damage.mes)
  args.set_arg(0, 0)  # Set to unembued
  return 0
  
  
  
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
  
  
def PsyStrikeEffectTooltip(attachee, args, evt_obj):
  isEmbued = attachee.d20_query("PsyStrike Embued")
  if not isEmbued:
    return 0
  evt_obj.append(tpdp.hash("PSY_STRIKE"), -2, -1) # 53 is the indicator graphical index; buffs (indicators above portraits) are in the 0-89 range IIRC; will have to expand this to support new icons
  return 0

psychicStrike = PythonModifier("Psychic Strike", 1)                                                 # arg0 - embued with energy
psychicStrike.AddHook(ET_OnD20PythonQuery, "PsyStrike Embued", PsyStrikeEmbued, ())                 # hook PsyStrikeEmbued to event of python query
psychicStrike.AddHook(ET_OnBuildRadialMenuEntry, EK_NONE, PsychicStrikeRadial, ())                  # Add to radial menu
psychicStrike.AddHook(ET_OnD20PythonActionCheck, psiStrikeEnum, OnPsyStrikeCheck, ())     # Check if valid
psychicStrike.AddHook(ET_OnD20PythonActionPerform, psiStrikeEnum, OnPsyStrikePerform, ()) # Perform if valid
psychicStrike.AddHook(ET_OnDealingDamage, EK_NONE, PsychicStrikeDamage, ())                         # Damage callback, adds xd8 damage dice
psychicStrike.MapToFeat("Psychic Strike")                                                           # Map to feat
