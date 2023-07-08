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

from modules.data.models.fossil_models import Fossils
from modules.data.models.tag_models import Tags

from modules.data.parser.path_utils import get_abs_path, get_base_dir

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'fossils.min.json'))


def insert_fossils_into_db(db_manager):
    with open(abs_path_to_json) as json_file:
        fossils_data = json.load(json_file)
        
    with db_manager.transaction() as session:
        for fossil_id, fossil_info in fossils_data.items():
            fossil = Fossils(fossil_id=fossil_id,
                             changes_quality=fossil_info['changes_quality'],
                             enchants=fossil_info['enchants'],
                             mirrors=fossil_info['mirrors'],
                             name=fossil_info['name'],
                             rolls_lucky=fossil_info['rolls_lucky'],
                             rolls_white_sockets=fossil_info['rolls_white_sockets']
                             )
            session.add(fossil)
            
        for tag in fossil_info['allowed_tags']:
            tag_instance = session.query(Tags).get(tag)
            if not tag_instance:
                tag_instance = Tags(tag_id=tag)
                session.add(tag_instance)
            
            allowed_tag = FossilAllowedTags(fossil_id=fossil.id, tag_id=tag_instance.id)
            session.add(allowed_tag)
        
        for tag in fossil_info['forbidden_tags']:
            # First, make sure the tag exists in the Tags table
            tag_instance = session.query(Tags).get(tag)
            if not tag_instance:
                tag_instance = Tags(tag_id=tag)
                session.add(tag_instance)
            
            forbidden_tag = FossilForbiddenTags(fossil_id=fossil.id, tag_id=tag_instance.id)
            session.add(forbidden_tag)
        
        for mod_weight in fossil_info['positive_mod_weights']:
            tag = mod_weight['tag']
            weight = mod_weight['weight']
            
            # First, make sure the tag exists in the Tags table
            tag_instance = session.query(Tags).get(tag)
            if not tag_instance:
                tag_instance = Tags(tag_id=tag)
                session.add(tag_instance)
            
            positive_mod_weight = FossilPositiveModWeights(fossil_id=fossil.fossil_id, tag_id=tag_instance.tag_id,
                                                           weight=weight)
            session.add(positive_mod_weight)
        
        for mod_weight in fossil_info['negative_mod_weights']:
            tag = mod_weight['tag']
            weight = mod_weight['weight']
            
            # First, make sure the tag exists in the Tags table
            tag_instance = session.query(Tags).get(tag)
            if not tag_instance:
                tag_instance = Tags(tag_id=tag)
                session.add(tag_instance)
            
            negative_mod_weight = FossilNegativeModWeights(fossil_id=fossil.fossil_id, tag_id=tag_instance.tag_id,
                                                           weight=weight)
            session.add(negative_mod_weight)
            