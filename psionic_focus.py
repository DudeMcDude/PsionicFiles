from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

psiMeditateEnum = 200
psiFocusExpendConceEnum = 201

def PsionicFocusRadial(attachee, args, evt_obj):
	cur_psi = attachee.d20_query("Current Psi")
	if cur_psi <= 0:
		return 0
	isAdded = attachee.condition_add_with_args("Psionic Focus",0,0) # adds the "Psionic Focus" condition on first radial menu build
	isFocused = 0
	isConcentrate = 0
	if not isAdded: # means it's not a newly added condition
		isFocused = attachee.d20_query("Psionically Focused")
		isConcentrate = attachee.d20_query("Psionic Concentration")
	if not isFocused:
		if (attachee.d20_query("Current Psi") > 0) and (attachee.skill_level_get(skill_concentration) > 0): # attachee has 1 or more power points currently available and at least 1 point in concentration
			#radialAction = tpdp.RadialMenuEntryPythonAction(?, D20A_PYTHON_ACTION, "Meditate", ?, ?)
		else:
			return 0 # do not add to radial skill menu
	else:
		if not isConcentrate:
			# we are already focused, but not concentrated, so we want to always display checkbox action in radial menu, as psi and conce points are only a prereq for meditating, not after the fact
			#radialAction = tpdp.RadialmenuEntryPythonAction(?, D20A_PYTHON_ACTION, "Concentrate Expend", ?, ?)
		else:
			# we are already focused and concentrated, so we want the same as above but with the box already checked
	radialAction.add_child_to_standard(attachee, tpdp.RadialMenuStandardNode.Skills) # add meditate to radial skill menu
	return 0

#skillSpecObj = PythonModifier(?, 0) # condition needs to be one that applies to all PC's!
skillSpecObj.AddHook(ET_OnBuildRadialMenuEntry, EK_NONE, PsionicFocusRadial, ())
		
def OnPsionicFocusCheck(attachee, args, evt_obj):
	if IsFocused(args): # if already focused
		evt_obj.return_val = AEC_INVALID_ACTION
	return 0
	
def OnPsionicFocusPerform(attachee, args, evt_obj):
	if IsFocused(args): # if already focused
		return 0	
	args.set_arg(0, 1) # set to focused
	args.set_arg(1, 0) # set to unchecked
	# add buff to character portrait
	return 0
	
def OnPsionicConceCheck(attachee, args, evt_obj):
	if not IsFocused(args): # if not focused
		evt_obj.return_val = AEC_INVALID_ACTION
	return 0
	
def OnPsionicConcePerform(attachee, args, evt_obj):
	if not IsFocused(args): # if not focused
		return 0
	if IsConcentrate(args): # if already concentrated
		args.set_arg(1, 0) #set to unchecked
	else:
		args.set_arg(1, 1)
	return 0
	
def PsionicallyFocused(attachee, args, evt_obj):
	evt_obj.return_val = IsFocused(args)
	return 0
	
def PsionicConcentration(attachee, args, evt_obj):
	evt_obj.return_val = IsConcentrate(args)
	return 0
	
def IsFocused(args):
	if args.get_arg(0)
		return 1
	return 0

def IsConcentrate(args):
	if args.get_arg(1)
		return 1
	return 0
	
def PsionicFocusLost(attachee, args, evt_obj):
	args.set_arg(0, 0) # set to unfocused
	args.set_arg(1, 0) # set to unchecked
	# remove buff from character portrait
	#args.set_arg(2, 0) # unused
	#args.set_arg(3, 0) # unused
	return 0
	
psiFocus = PythonModifier("Psionic Focus", 4) 							# arg0 - is focused; arg1 - is checked for concentration; arg2 - unused; arg3 - unused
psiFocus.AddHook(ET_OnD20PythonQuery, "Psionically Focused", PsionicallyFocused, ()) 		# hook PsionicallyFocused to event of python call
psiFocus.AddHook(ET_OnD20PythonQuery, "Psionic Concentration", PsionicConcentration, ()) 	# hook PsionicConcentration to event of python call
psiFocus.AddHook(ET_OnNewDay, EK_NEWDAY_REST, PsionicFocusLost, ()) 				# hook PsionicFocusLost to event of resting 8 hours safely
#psiFocus.AddHook(?, ?, PsionicFocusLost, ()) 							# hook PsionicFocusLost to event of becoming unconscious
psiFocus.AddHook(ET_OnD20PythonSignal, "Psi Depleted", PsionicFocusLost, ()) 			# hook PsionicFocusLost to event of having 0 psi points
psiFocus.AddHook(ET_OnD20PythonSignal, "Expend Focus", PsionicFocusLost, ())			# hook PsionicFocusLost to event of python signal
psiFocus.AddHook(ET_OnD20PythonActionCheck, psiMeditateEnum, OnPsionicFocusCheck, ())		# hook OnPsionicFocusCheck to event of radial menu option
psiFocus.AddHook(ET_OnD20PythonActionPerform, psiMeditateEnum, OnPsionicFocusPerform, ())	# hook OnPsionicFocusPerform to event of radial menu option
psiFocus.AddHook(ET_OnD20PythonActionCheck, psiFocusExpendConceEnum, OnPsionicConceCheck, ())	# hook OnPsionicConceCheck to event of radial menu option
psiFocus.AddHook(ET_OnD20PythonActionCheck, psiFocusExpendConceEnum, OnPsionicConcePerform, ())	# hook OnPsionicConcePerform to event of radial menu option


# TODO figure out how to add a buff to the character portrait, simply the little flag that will be named "Psionic Focus", simply for player output purpose
# TODO make it so meditating is a full round action and provokes an attack of opportunity
# TODO allow psionic focus toggle somehow so when you are already focused, you can make it so the next concentration check expends your focus for a free 15 roll
