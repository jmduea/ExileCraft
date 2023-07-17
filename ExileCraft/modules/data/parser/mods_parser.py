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

from modules.data.parser.path_utils import get_abs_path, get_base_dir
from modules.shared.config.constants import domain_whitelist

script_path = os.path.realpath(__file__)
base_dir = get_base_dir(script_path)
abs_path_to_json = get_abs_path(base_dir, os.path.join(r'ExileCraft\modules\data', 'json', 'mods.min.json'))


class ModParser:
    def __init__(self):
        self._data = self.parse_json()
        self.abs_path_to_json = abs_path_to_json
        self.mod_list = self.get_all_mods()
        
    def parse_json(self):
        if not hasattr(self, '_data'):
            with open(abs_path_to_json) as json_file:
                self._data = json.load(json_file)
        return self._data
    
    def get_all_mod_data_for_key(self, key):
        data = self._data
        mod_data_list = []
        for mod, mod_data in data.items():
            mod_data_value = mod_data.get(key, None)
            mod_data_dict = {
                key: mod_data_value if mod_data_value is not None else None
            }
            if mod_data_dict not in mod_data_list:
                mod_data_list.append(mod_data_dict)
        return mod_data_list
    
    def get_mod_data_by_key(self, mod_data, key):
        mod_data_value = mod_data.get(key)
        value_dict = {key: mod_data_value}
        return value_dict
    
    def get_all_mod_generation_types(self):
        mod_generation_types_list = self.get_all_mod_data_for_key("generation_type")
        return mod_generation_types_list
    
    def get_mod_generation_type(self, mod_data):
        mod_generation_type = mod_data.get("generation_type")
        return mod_generation_type
    
    def get_all_mod_domains(self):
        mod_domains_list = self.get_all_mod_data_for_key("domain")
        return mod_domains_list
    
    def get_mod_domain(self, mod_data):
        mod_domain = mod_data.get("domain")
        return mod_domain
        
    def get_all_mod_types(self):
        types_list = self.get_all_mod_data_for_key("type")
        mod_types_list = []
        for type in types_list:
            if type not in mod_types_list:
                mod_types_list.append(type)
        return mod_types_list
    
    def get_mod_type(self, mod_data):
        mod_type = mod_data.get("type")
        return mod_type
    
    def get_all_mod_groups(self):
        mod_groups_list = self.get_all_mod_data_for_key("groups")
        groups_list = []
        for group in mod_groups_list:
            group_dict = {
                "group": group["groups"][0]
            }
            if group_dict not in groups_list:
                groups_list.append(group_dict)
        return groups_list
    
    def get_mod_group(self, mod_data):
        mod_group = mod_data.get("groups")
        group = mod_group[0]
        return group
    
    def get_all_mods(self):
        data = self._data
        mod_list = []
        for mod, mod_data in data.items():
            if mod_data.get("domain") not in domain_whitelist:
                continue
            if mod not in mod_list:
                mod_dict = {
                    'mod_name': mod,
                    'level_req': mod_data.get("required_level"),
                    'name': mod_data.get("name"),
                    'is_essence_only': mod_data.get("is_essence_only"),
                    'domain': mod_data.get('domain'),
                    'generation_type': mod_data.get('generation_type'),
                    'group': mod_data.get('groups')[0],
                    'mod_type': mod_data.get('type'),
                    'added_tags_list': self.get_added_tags(mod_data),
                    'implicit_tags_list': self.get_implicit_tags(mod_data),
                    'spawn_weights_list': self.get_spawn_weights(mod_data),
                    'stats_list': self.get_stats(mod_data)
                }
                mod_list.append(mod_dict)
        return mod_list
    
    def get_all_mod_dicts(self):
        data = self._data
        mod_dicts = {}
        for mod, mod_data in data.items():
            if mod_data.get("domain") not in domain_whitelist:
                continue
            mod_dict = {mod: self.get_mod_data(mod_data)}
            mod_dicts.update(mod_dict)
        return mod_dicts
    
    def get_added_tags(self, mod_data):
        added_tags_list = [tag for tag in mod_data.get("adds_tags", [])]
        return added_tags_list
            
    def get_implicit_tags(self, mod_data):
        implicit_tags_list = [tag for tag in mod_data.get("implicit_tags", [])]
        return implicit_tags_list
    
    def get_spawn_weights(self, mod_data):
        spawn_weights_list = []
        spawn_weights_data = mod_data.get("spawn_weights", [])
        for weight_data in spawn_weights_data:
            tag_dict = {
                "tag": weight_data.get("tag"),
                "weight": weight_data.get("weight")
            }
            spawn_weights_list.append(tag_dict)
        return spawn_weights_list
    
    def get_stats(self, mod_data):
        stats_list = []
        stats_data = mod_data.get("stats", [])
        for stat in stats_data:
            stat_data_dict = {
                'stat': stat.get("id"),
                'values': {'min': stat.get("min"), 'max': stat.get("max")},
                # 'stat_min_value': stat_data.get("min"),
                # 'stat_max_value': stat_data.get("max")
            }
            stats_list.append(stat_data_dict)
        return stats_list
            
    def get_mod_data(self, mod_data):
        mod_dict = {
            'level_req': mod_data.get("required_level"),
            'name': mod_data.get("name"),
            'is_essence_only': mod_data.get("is_essence_only"),
            'domain': mod_data.get('domain'),
            'generation_type': mod_data.get('generation_type'),
            'group': mod_data.get('groups')[0],
            'type': mod_data.get('type'),
            'added_tags_list': self.get_added_tags(mod_data),
            'implicit_tags_list': self.get_implicit_tags(mod_data),
            'spawn_weights_list': self.get_spawn_weights(mod_data),
            'stats_list': self.get_stats(mod_data)
        }
        return mod_dict
        
# class OutOfBoundsWarning(UserWarning):
#     pass
#
#
# class ModsHandler(ExporterHandler):
#     def __init__(self, sub_parser):
#         self.parser = sub_parser.add_parser('mods', help='Mods Exporter')
#         self.parser.set_defaults(func=lambda args: self.parser.print_help())
#         lua_sub = self.parser.add_subparsers()
#
#         # Mods
#         mparser = lua_sub.add_parser(
#             'mods',
#             help='Extract all mods.'
#         )
#         mparser.set_defaults(func=lambda args: mparser.print_help())
#
#         sub = mparser.add_subparsers(help='Method of extracting mods')
#
#         self.add_default_subparser_filters(sub, cls=ModParser)
#
#         # mods filter
#         parser = sub.add_parser('filter', help='Filter mods')
#         parser.add_argument(
#             '--domain',
#             dest='domain',
#             help='Mod domain',
#             choices=[k.name for k in MOD_DOMAIN],
#         )
#
#         parser.add_argument(
#             '--generation-type', '--type',
#             dest='generation_type',
#             help='Mod domain',
#             choices=[k.name for k in MOD_GENERATION_TYPE],
#         )
#
#         self.add_default_parsers(
#             parser=parser,
#             cls=ModParser,
#             func=ModParser.filter,
#         )
#
#         # Tempest
#         parser = lua_sub.add_parser(
#             'tempest',
#             help='Extract tempest stuff (DEPRECATED).',
#         )
#         self.add_default_parsers(
#             parser=parser,
#             cls=ModParser,
#             func=ModParser.tempest,
#             wiki=False,
#         )
#
#     def add_default_parsers(self, *args, **kwargs):
#         super().add_default_parsers(*args, **kwargs)
#         parser = kwargs['parser']
#         self.add_format_argument(parser)
#
#
# class ModParser(BaseParser):
#     # Load files in advance
#     _files = [
#         'Mods.dat',
#         'Stats.dat',
#     ]
#
#     # Load translations in advance
#     _translations = [
#         'map_stat_descriptions.txt',
#     ]
#
#     _mod_column_index_filter = partialmethod(
#         BaseParser._column_index_filter,
#         dat_file_name='Mods.dat',
#         error_msg='Several areas have not been found:\n%s',
#     )
#
#     def _append_effect(self, result, mylist, heading):
#         mylist.append(heading)
#
#         for line in result.lines:
#             mylist.append('* %s' % line)
#         for i, stat_id in enumerate(result.missing_ids):
#             value = result.missing_values[i]
#             if hasattr(value, '__iter__'):
#                 value = '(%s to %s)' % tuple(value)
#             mylist.append('* %s %s' % (stat_id, value))
#
#     def by_rowid(self, parsed_args):
#         return self._export(
#             parsed_args,
#             self.rr['Mods.dat'][parsed_args.start:parsed_args.end],
#         )
#
#     def by_id(self, parsed_args):
#         return self._export(parsed_args, self._mod_column_index_filter(
#             column_id='Id', arg_list=parsed_args.id
#         ))
#
#     def by_name(self, parsed_args):
#         return self._export(parsed_args, self._mod_column_index_filter(
#             column_id='Name', arg_list=parsed_args.name
#         ))
#
#     def filter(self, args):
#         mods = []
#
#         filters = []
#         if args.domain:
#             filters.append({
#                 'column': 'Domain',
#                 'comp': getattr(MOD_DOMAIN, args.domain),
#             })
#
#         if args.generation_type:
#             filters.append({
#                 'column': 'GenerationType',
#                 'comp': getattr(MOD_GENERATION_TYPE, args.generation_type),
#             })
#
#         for mod in self.rr['Mods.dat']:
#             for filter in filters:
#                 if mod[filter['column']] != filter['comp']:
#                     break
#             else:
#                 mods.append(mod)
#
#         return self._export(args, mods)
#
#     def _export(self, parsed_args, mods):
#         r = ExporterResult()
#
#         if mods:
#             console('Found %s mods. Processing...' % len(mods))
#         else:
#             console(
#                 'No mods found for the specified parameters. Quitting.',
#                 msg=Msg.warning
#             )
#             return r
#
#         # Needed for localizing sell prices
#         self.rr['BaseItemTypes.dat'].build_index('Id')
#
#         for mod in mods:
#             data = OrderedDict()
#
#             for k in (
#                     ('Id', 'id'),
#                     ('CorrectGroup', 'mod_group'),
#                     ('Domain', 'domain'),
#                     ('GenerationType', 'generation_type'),
#                     ('Level', 'required_level'),
#             ):
#                 v = mod[k[0]]
#                 if v:
#                     data[k[1]] = v
#
#             if mod['Name']:
#                 root = text.parse_description_tags(mod['Name'])
#
#                 def handler(hstr, parameter):
#                     return hstr if parameter == 'MS' else ''
#
#                 data['name'] = root.handle_tags({'if': handler, 'elif': handler})
#
#             if mod['BuffDefinitionsKey']:
#                 data['granted_buff_id'] = mod['BuffDefinitionsKey']['Id']
#                 data['granted_buff_value'] = mod['BuffValue']
#             # todo ID for GEPL
#             if mod['GrantedEffectsPerLevelKeys']:
#                 data['granted_skill'] = ', '.join(
#                     [k['GrantedEffectsKey']['Id'] for k in
#                      mod['GrantedEffectsPerLevelKeys']])
#             data['mod_type'] = mod['ModTypeKey']['Name']
#
#             stats = []
#             values = []
#             for i in MOD_STATS_RANGE:
#                 k = mod['StatsKey%s' % i]
#                 if k is None:
#                     continue
#
#                 stat = k['Id']
#                 value = mod['Stat%sMin' % i], mod['Stat%sMax' % i]
#
#                 if value[0] == 0 and value[1] == 0:
#                     continue
#
#                 stats.append(stat)
#                 values.append(value)
#
#             data['stat_text'] = '<br>'.join(self._get_stats(stats, values, mod))
#
#             for i, (sid, (vmin, vmax)) in enumerate(zip(stats, values), start=1):
#                 data['stat%s_id' % i] = sid
#                 data['stat%s_min' % i] = vmin
#                 data['stat%s_max' % i] = vmax
#
#             for i, tag in enumerate(mod['SpawnWeight_TagsKeys']):
#                 j = i + 1
#                 data['spawn_weight%s_tag' % j] = tag['Id']
#                 data['spawn_weight%s_value' % j] = mod['SpawnWeight_Values'][i]
#
#             for i, tag in enumerate(mod['GenerationWeight_TagsKeys']):
#                 j = i + 1
#                 data['generation_weight%s_tag' % j] = tag['Id']
#                 data['generation_weight%s_value' % j] = \
#                     mod['GenerationWeight_Values'][i]
#
#             tags = ', '.join(
#                 [t['Id'] for t in mod['ModTypeKey']['TagsKeys']] +
#                 [t['Id'] for t in mod['TagsKeys']]
#             )
#             if tags:
#                 data['tags'] = tags
#
#             if mod['ModTypeKey']:
#                 sell_price = defaultdict(int)
#                 for msp in mod['ModTypeKey']['ModSellPriceTypesKeys']:
#                     for i, (item_id, amount) in enumerate(
#                             MOD_SELL_PRICES[msp['Id']].items(), start=1):
#                         data['sell_price%s_name' % i] = self.rr[
#                             'BaseItemTypes.dat'].index['Id'][item_id]['Name']
#                         data['sell_price%s_amount' % i] = amount
#
#                 # Make sure this is always the same order
#                 sell_price = sorted(sell_price.items(), key=lambda x: x[0])
#
#                 for i, (item_name, amount) in enumerate(sell_price, start=1):
#                     data['sell_price%s_name' % i] = item_name
#                     data['sell_price%s_amount' % i] = amount
#
#             # 3+ tildes not allowed
#             page_name = 'Modifier:' + self._format_wiki_title(mod['Id'])
#             cond = ModWikiCondition(data, parsed_args)
#
#             r.add_result(
#                 text=cond,
#                 out_file='mod_%s.txt' % data['id'],
#                 wiki_page=[
#                     {'page': page_name, 'condition': cond},
#                 ],
#                 wiki_message='Mod updater',
#             )
#
#         return r
#
#     @deprecated(message='Will be done in-wiki in the future - non functional')
#     def tempest(self, parsed_args):
#         tf = self.tc['map_stat_descriptions.txt']
#         data = []
#         for mod in self.rr['Mods.dat']:
#             # Is it a tempest mod?
#             if mod['CorrectGroup'] != 'MapEclipse':
#                 continue
#
#             # Doesn't have a name - probably not implemented
#             if not mod['Name']:
#                 continue
#
#             stats = []
#             for i in MOD_STATS_RANGE:
#                 stat = mod['StatsKey%s' % i]
#                 if stat:
#                     stats.append(stat)
#
#             info = {}
#             info['name'] = mod['Name']
#             effects = []
#
#             stat_ids = [st['Id'] for st in stats]
#             stat_values = []
#
#             for i, stat in enumerate(stats):
#                 j = i + 1
#                 values = [mod['Stat%sMin' % j], mod['Stat%sMax' % j]]
#                 if values[0] == values[1]:
#                     values = values[0]
#                 stat_values.append(values)
#
#             try:
#                 index = stat_ids.index('map_summon_exploding_buff_storms')
#             except ValueError:
#                 pass
#             else:
#                 # Value is incremented by 1 for some reason
#                 tempest = self.rr['ExplodingStormBuffs.dat'][stat_values[index] - 1]
#
#                 stat_ids.pop(index)
#                 stat_values.pop(index)
#
#                 if tempest['BuffDefinitionsKey']:
#                     tempest_stats = tempest['BuffDefinitionsKey']['StatKeys']
#                     tempest_values = tempest['StatValues']
#                     tempest_stat_ids = [st['Id'] for st in tempest_stats]
#                     t = tf.get_translation(
#                         tempest_stat_ids, tempest_values, full_result=True,
#                         lang=config.get_option('language')
#                     )
#                     self._append_effect(t, effects, 'The tempest buff provides the following effects:')
#                 # if tempest['MonsterVarietiesKey']:
#                 #    print(tempest['MonsterVarietiesKey'])
#                 #    break
#
#             t = tf.get_translation(
#                 stat_ids, stat_values, full_result=True,
#                 lang=config.get_option('language')
#             )
#             self._append_effect(t, effects, 'The area gets the following modifiers:')
#
#             info['effect'] = '\n'.join(effects)
#             data.append(info)
#
#         data.sort(key=lambda info: info['name'])
#
#         out = []
#         for info in data:
#             out.append('|-\n')
#             out.append('| %s\n' % info['name'])
#             out.append('| %s\n' % info['effect'])
#             out.append('| \n')
#
#         r = ExporterResult()
#         r.add_result(lines=out, out_file='tempest_mods.txt')
#
#         return r


if __name__ == "__main__":
    mod_parser = ModParser()
    # mod_list = mod_parser.get_all_mods()
    mod_dict_list = mod_parser.get_all_mod_dicts()
    print(mod_dict_list)