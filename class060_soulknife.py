from toee import *
import char_class_utils

class_feats = {
1: (feat_armor_proficiency_light, feat_shield_proficiency, feat_simple_weapon_proficiency, "feat_exotic_weapon_proficiency_mind blade", "feat_weapon_focus_mind_blade", "feat_wild_talent",),
6: ("feat_speed_of_thought",),
9: ("feat_greater_weapon_focus_mind_blade",),
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
