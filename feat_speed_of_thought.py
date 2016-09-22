from templeplus.pymod import PythonModifier
from toee import *
import tpdp
import char_class_utils
import d20_action_utils

def SpeedOfThought(attachee, args, evt_obj):
  isFocused = attachee.d20_query("Psionically Focused") # Character must be psionically focused
  if not isFocused:
    return 0
  
  armor = obj.item_worn_at(5)                           # Character must not be wearing heavy armor
    if armor != OBJ_HANDLE_NULL:
        armorFlags = armor.obj_get_int(obj_f_armor_flags)
        if armorFlags == ARMOR_TYPE_HEAVY:
            return 0
          
  evt_obj.bonus_list.add(10, ?, 114)                    # Add 10 insight bonus to move speed
  return 0

feat_speed_of_thought = PythonModifier("feat_speed_of_thought", 1)
feat_speed_of_thought.AddHook(ET_OnGetMoveSpeed, EK_NONE, SpeedOfThought, ())
feat_speed_of_thought.MapToFeat("Speed of Thought")
