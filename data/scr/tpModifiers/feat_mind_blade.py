from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

mindBladeEnum = 6000

def MindBladeRadial(attachee, args, evt_obj):
	radial_action = tpdp.RadialMenuEntryPythonAction(-1, D20A_PYTHON_ACTION, mindBladeEnum, 0, "TAG_INTERFACE_HELP")
	radialAction.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Class)
	
def CanManifestMindBlade(attachee):
	weap = attachee.item_worn_at(3)
	if weap != OBJ_HANDLE_NULL:	# Primary hand is not free
		return 0		# Only manifest in primary hand
			
	weap = attachee.item_worn_at(4)
	if weap!= OBJ_HANDLE_NULL:	# Secondary hand is not free
		# Check weapon type, is it Mind Blade?
			# If yes, return 0
	
	return 1			# Primary hand is free and secondary hand does not hold a mind blade

def OnMindBladeCheck(attachee, args, evt_obj):
	if not CanManifestMindBlade(attachee):
		evt_obj.return_val = AEC_INVALID_ACTION
	return 0

def OnMindBladePerform(attachee, args, evt_obj):
	if not CanManifestMindBlade(attachee):
		return 0
	game.particles("Mind Blade Manifest", attachee)
	# TODO: Find proper SFX and play it here
	# Delay 1.3 seconds (time it takes for effect to get to where Mind Blade should visually appear
	# Create Mind Blade object in primary hand of attachee
	return 0

# Mind Blade feat Modifier
mindBladeFeat = PythonModifier("Feat Mind Blade", 0)
mindBladeFeat.AddHook(ET_OnBuildRadialMenuEntry, EK_NONE, MindBladeRadial, ())                  # Add to radial menu
mindBladeFeat.AddHook(ET_OnD20PythonActionCheck, mindBladeEnum, OnMindBladeCheck, ())     # Check if valid
mindBladeFeat.AddHook(ET_OnD20PythonActionPerform, mindBladeEnum, OnMindBladePerform, ()) # Perform if valid
mindBladeFeat.MapToFeat("Mind Blade")                                                           # Map to feat


# this is the modifier to be applied to the blade itself in protos.tab
def MindBladeMagicDamage(attachee, args, evt_obj):
	evt_obj.damage.attack_power |= D20DAP_MAGIC
	return 0

def MindBladeWeaponGlow(attachee, args, evt_obj):
	evt_obj.damage.attack_power |= D20DAP_MAGIC
	inven_idx = args.get_arg(2)
	item = attachee.inventory_item(inven_idx)
	if item != OBJ_HANDLE_NULL and (item == attachee.item_worn_at(3) or item == attachee.item_worn_at(4)):
		evt_obj.return_val = 3 # originally used in "Weapon Bane", feel free to experiment with this
	return 0


mindBlade = PythonModifier("Mind Blade", 0)
mindBlade.AddHook(ET_OnDealingDamage2, EK_NONE, MindBladeMagicDamage, ())
mindBlade.AddHook(ET_OnWeaponGlowType, EK_NONE, MindBladeWeaponGlow, ())
