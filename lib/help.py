# This content will be painfully long.
# GL HF

# 帮助文件，很长，会长到你怀疑人生。
# 祝好运，玩的开心。

HELP_CHAIN = [
    '''NEKOIntel Chain.
The basic structure of NEKOIntel.
Is a set of modules/tools chained together to an unified output though a pipeline.
chain [new del] [modules/CHAIN_ID]
|   Spawns or delete a recon toolchain.
|   Examples: 
|   |   chain new [modules] - Spawns a new toolchain consists of [modules] in sequence.
|   |   chain del [CHAIN_ID] - Deletes a toolchain.
chain [chain_id] [info parameters]
|   Shows the info/parameters.
|   Examples:
|   |   chain 0 info - Shows info of chain CHAIN0.
|   |   chain 0 parameters - Shows all parameters in-module of CHAIN0.
chain [chain_id] [arm fire]
|   Arm/Fire a chain.
|   Arming a chain checks the potential error and configuration.
|   Fire starts the chain.
|   Examples:
|   |   chain 0 info - Checks all errors and verifies configs in the chain.
|   |   chain 0 fire - Starts chain 0
''', '''
猫情报 工具链
工具链是猫情报的基础结构。一系列工具/模组被链接并使用管线统一输出。
chain [new del] [模块/链ID]
|   生成或者删除一个侦察工具链。
|   示例: 
|   |   chain new [模块] - 生成新的工具链。工具链内的模块按照顺序排列。
|   |   chain del [链ID] - 删除工具链。
chain [链ID] [info parameters]
|   显示链的信息或者参数。
|   示例:
|   |   chain 0 info - 显示CHAIN0的信息，包括链内模块和顺序。
|   |   chain 0 parameters - 显示链内所有模块的参数。
chain [chain_id] [arm fire]
|   预热/发射一个链。
|   预热动作检查链内的错误和配置完整性。
|   发射启动整个链。
|   示例:
|   |   chain 0 arm - 检查CHAIN0的错误和配置完整性。
|   |   chain 0 fire - 启动CHAIN0。
'''
]

HELP_HELP = [
    '''NEKOIntel Help
The general help of NEKOIntel.
help [module_name] *[subcommand_name]
|   Provides the help of [module_name].
|   If a subcommand exists, displays the help of [subcommand_name].
''',
    '''猫情报 帮助
提供猫情报的通常帮助。
help [模块名] *[子命令]
|   提供[模块名]的帮助。
|   如果存在[子命令]，输出[子命令]的帮助。
    '''
]

HELP_PRESET = [
    '''NEKOIntel Presets
Presets are a set of available pre-configured module chain to automate the job.
preset new [preset_file_name]
|   Defines a new chain preset.
preset load [preset_file_name]
|   Loads a a downloaded or defined preset into a new chain.
preset delete [preset_file_name]
|   Deletes a existed preset.
preset list
|   Shows the list of locally available presets.
preset get [preset_name](Upcoming.)
|   Downloads an online preset into preset/ directory.
preset search [key_word](Upcoming.)
|   Search [keyword] from online presets database.
''',
    '''猫情报 预设
预设是一系列可用的预设工具链，用于简化和自动化侦察过程。
preset new [预设文件名]
|   生成一个新的工具链预设。
preset load [预设文件名]
|   将一个已经存在的预设载入进新的工具链内。
preset delete [预设文件名]
|   删除一个已存在的预设。
preset list
|   显示所有本地可用的预设。
preset get [预设名称] (即将上线)
|   将一个在线预设下载至本地的presets/文件夹。
preset search [关键字] (即将上线)
|   根据关键字搜索在线预设。
''',
]

HELP_MODULES = [
    '''NEKOIntel Modules.
Modules are independent scanners or gadgets that composes a chain.
They can be downloaded from the database, or made from scratch.
There's 3 categories of modules: domain, host, gadget.
Domain modules are used to collect domain information, host modules collects host information, and posts functions as gadgets that links the chain.
Domain modules always be the first to executed, gadgets thereafter. They runs in parallel, if grouped.
Gadgets can be executed anytime in the chain, but gadgets can't be grouped.
Modules in the same group shares the same configuration, if not specified, and those outside the groups uses the same configuration.
The configuration can be adjusted independently.
modules list *[category]
|   Shows the list of available module in the specified category. if there's no categories parameter, it shows all modules available.
|   Examples:
|   |   modules list domain - Lists all domain modules.
|   |   modules list - Shows all modules.
modules search [key_word]
|   Searches modules by [key_word].
modules insert [module_name group_name] [CHAIN_ID]
|   Inserts module [module_name] or group [group_name] into chain [CHAIN_ID].
modules pop [CHAIN_ID] [module_id]
|   Removes the [module_id]th module from [CHAIN_ID].
|   If the module is in a group, it will be removed from the group, but the group preset will be intact.
modules   
''',
    ''''''
]