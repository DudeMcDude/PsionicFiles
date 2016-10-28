from toee import *
import char_class_utils

###################################################

def GetConditionName(): # used by API
	return "Soulknife"

def GetCategory():
	return "Core 3.5 Ed Classes"

def GetClassDefinitionFlags():
	return CDF_BaseClass

classEnum = stat_level_soulknife

###################################################

class_feats = {
1: (feat_armor_proficiency_light, feat_shield_proficiency, feat_simple_weapon_proficiency, "Mind Blade", "Weapon Focus (mind blade)", "Wild Talent",),
2: ("Throw Mind Blade",),
3: ("Psychic Strike",),
5: ("Free Draw", "Shape Mind Blade",),
6: ("Mind Blade Enhancement", "Speed of Thought",),
9: ("Bladewind", "Greater Weapon Focus (mind blade)",),
13: ("Knife to the Soul",),
17: ("Multiple Throw",),
}

class_skills = ("skill_autohypnosis", skill_concentration, skill_hide, skill_listen, skill_move_silently, skill_spot, skill_tumble)

def IsEnabled():
	return 1

def GetHitDieType():
	return 10

def GetSkillPtsPerLevel():
	return 4
	
def GetBabProgression():
	return base_attack_bonus_type_semi_martial

def IsFortSaveFavored():
	return 0

def IsRefSaveFavored():
	return 1

def IsWillSaveFavored():
	return 1
	
def GetSpellListType():
	return spell_list_type_none

def IsClassSkill(skillEnum):
	return char_class_utils.IsClassSkill(class_skills, skillEnum)

def IsClassFeat(featEnum):
	return char_class_utils.IsClassFeat(class_feats, featEnum)

def GetClassFeats():
	return class_feats

def IsAlignmentCompatible( alignment):
	return 1
	
def ObjMeetsPrereqs( obj ):
	return 1
