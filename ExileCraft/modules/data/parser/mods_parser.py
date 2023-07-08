# ##############################################################################
#  MIT License
#
#  Copyright (c) 2023 Jon Duea
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# ##############################################################################

import json
import os

from modules.config.constants import domain_whitelist, generation_type_blacklist
from modules.data.models.association_models import mod_adds_tags_association, mod_implicit_tags_association, \
    mod_spawn_weights_association, mod_tags_association, mod_stats_association
from modules.data.models.global_models import Domain, GenerationType
from modules.data.models.mod_models import Mod, ModType, ModGroup
from modules.data.models.stat_models import Stat, StatValue
from modules.data.models.tag_models import Tag
from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'mods.min.json'))


def insert_mods_into_db(db_manager):
    # Load the JSON file
    with open(abs_path_to_json) as json_file:
        data = json.load(json_file)
    
    # Start a new transaction
    with db_manager.transaction() as session:
        # Iterate through the items
        for mod, item_data in data.items():
            if item_data.get("domain") not in domain_whitelist:
                continue
            if item_data.get("generation_type") in generation_type_blacklist:
                continue
            added_tags = []
            for tag in item_data.get("adds_tags"):
                if item_data.get("adds_tags") is not None:
                    tag_record = session.query(Tag).filter_by(tag=tag).first()
                    if not tag_record:
                        tag_record = Tag(tag=tag)
                        session.add(tag_record)
                        session.commit()
                    added_tags.append(tag_record.id)
                else:
                    added_tags = None
                    
            implicit_tags = []
            for tag in item_data.get("implicit_tags"):
                if item_data.get("implicit_tags") is not None:
                    implicit_tag_record = session.query(Tag).filter_by(tag=tag).first()
                    if not implicit_tag_record:
                        implicit_tag_record = Tag(tag=tag)
                        session.add(implicit_tag_record)
                        session.commit()
                    implicit_tags.append(implicit_tag_record.id)
                else:
                    implicit_tags = None
                    
            spawn_weights = []
            spawn_weights_data = item_data.get("spawn_weights", [])
            for weight_data in spawn_weights_data:
                if spawn_weights_data:
                    tag = weight_data.get("tag")
                    spawn_weight_tag_record = session.query(Tag).filter_by(tag=tag).first()
                    if not spawn_weight_tag_record:
                        spawn_weight_tag_record = Tag(tag=tag)
                        session.add(spawn_weight_tag_record)
                        session.commit()
                    weight = weight_data.get("weight")
                    tag_id = spawn_weight_tag_record.id
                    spawn_weights.append({
                        "tag_id": tag_id,
                        "weight": weight
                    })
                else:
                    spawn_weights = None
                
            stats = []
            stats_data = item_data.get("stats", [])
            for stat_data in stats_data:
                if stats_data:
                    stat = stat_data.get("id")
                    stat_record = session.query(Stat).filter_by(stat=stat).first()
                    if not stat_record:
                        stat_record = Stat(stat=stat)
                        session.add(stat_record)
                        session.commit()
                    stat_id = stat_record.id
                    stat_min_value = stat_data.get("min")
                    stat_max_value = stat_data.get("max")
                    stats.append({
                        "stat_id": stat_id,
                        "stat_min_value": stat_min_value,
                        "stat_max_value": stat_max_value
                    })
                else:
                    stats = None
                
            domain = item_data.get("domain")
            domain_obj = session.query(Domain).filter_by(domain=domain).first()
            if not domain_obj:
                domain_obj = Domain(domain=item_data.get("domain"))
                session.add(domain_obj)
                session.commit()
            domain_id = domain_obj.id
            
            generation_type = item_data.get("generation_type")
            generation_type_obj = session.query(GenerationType).filter_by(generation_type=generation_type).first()
            if not generation_type_obj:
                generation_type_obj = GenerationType(generation_type=generation_type)
                session.add(generation_type_obj)
                session.commit()
            generation_type_id = generation_type_obj.id
            
            group = item_data.get("groups")
            group_obj = session.query(ModGroup).filter_by(group=group[0]).first()
            if not group_obj:
                group_obj = ModGroup(group=group[0])
                session.add(group_obj)
                session.commit()
            mod_group_id = group_obj.id
            
            mod_type = item_data.get("type")
            mod_type_obj = session.query(ModType).filter_by(mod_type=mod_type).first()
            if not mod_type_obj:
                mod_type_obj = ModType(mod_type=mod_type)
                session.add(mod_type_obj)
                session.commit()
            mod_type_id = mod_type_obj.id
            
            mod_obj = Mod(
                mod=mod,
                level_req=item_data.get("required_level"),
                name=item_data.get("name"),
                is_essence_only=item_data.get("is_essence_only"),
                domain_id=domain_id,
                generation_type_id=generation_type_id,
                mod_group_id=mod_group_id,
                mod_type_id=mod_type_id
            )
            session.add(mod_obj)
            session.flush()
            
            mod_id = mod_obj.id
            
            # generation_weight = item_data.get("generation_weights")
            # generation_weight_obj = session.query(GenerationWeights).filter_by(generation_weight=
            #                                                                    generation_weight[0]).first()
            # if not generation_weight_obj:
            #     generation_weight_obj = GenerationWeights(generation_weight=generation_weight)
            #     session.add(generation_weight_obj)
            #     session.commit()
            # generation_weight_id = generation_weight_obj.id
            
            # granted_effect = item_data.get("grants_effects")
            # granted_effect_obj = session.query(GrantsEffects).filter_by(granted_effect=granted_effect).first()
            # if not granted_effect_obj:
            #     granted_effect_obj = GrantsEffects(granted_effect=granted_effect)
            #     session.add(granted_effect_obj)
            #     session.commit()
            # grants_effects_id = granted_effect_obj.id
            
            for tag_id in added_tags:
                session.execute(mod_adds_tags_association.insert().values(
                    mod_id=mod_id,
                    tag_id=tag_id,
                ))
            session.commit()
            
            for tag_id in implicit_tags:
                session.execute(mod_implicit_tags_association.insert().values(
                    mod_id=mod_id,
                    tag_id=tag_id,
                ))
            session.commit()
            
            if spawn_weights:
                for weight_data in spawn_weights:
                    tag_id = weight_data.get("tag_id")
                    weight = weight_data.get("weight")
                    
                    session.execute(mod_tags_association.insert().values(
                        mod_id=mod_id,
                        tag_id=tag_id
                    ))
                    
                    session.execute(mod_spawn_weights_association.insert().values(
                        mod_id=mod_id,
                        tag_id=tag_id,
                        weight=weight
                    ))
                session.commit()
            
            if stats:
                for stat_data in stats:
                    stat_id = stat_data.get("stat_id")
                    stat_min_value = stat_data.get("stat_min_value")
                    stat_max_value = stat_data.get("stat_max_value")
                    
                    session.execute(mod_stats_association.insert().values(
                        mod_id=mod_id,
                        stat_id=stat_id,
                        stat_min_value=stat_min_value,
                        stat_max_value=stat_max_value
                    ))
                session.commit()
                