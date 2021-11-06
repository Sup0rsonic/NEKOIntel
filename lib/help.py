# This content will be painfully long.
# GL HF

# 帮助文件，很长，会长到你怀疑人生。
# 祝好运，玩的开心。

HELP_CHAIN = [
    '''
NEKOIntel Chain.
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
    '''
NEKOIntel Help
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
    '''
NEKOIntel Presets
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
    '''
猫情报 预设
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
preset find [关键字] (即将上线)
|   根据关键字搜索在线预设。
''',
]

HELP_MODULES = [
    '''
NEKOIntel Modules.
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
modules insert [module_name group_name] [CHAIN_ID] [sequence]
|   Inserts module [module_name] or group [group_name] into chain [CHAIN_ID] by [sequence].
modules pop [CHAIN_ID] [module_id]
|   Removes the [module_id]th module from [CHAIN_ID].
|   If the module is in a group, it will be removed from the group, but the group preset will be intact.   
modules find [key_word] (Upcoming.)
|   Searches the module that matches [key_word] from online database.
modules get [module_name] (Upcoming)
|   Downloads the module with name of [module_name].
modules delete [module_name]
|   Permanently deletes the local module by name [module_name].
''',
    '''
猫情报 模块。
模块是独立的扫描器或者小工具，它们组成工具链。它们可以被从在线数据库下载，或者从零开始编写。
模块有三种类型，domain, host, gadget。
Domain模块用于收集域名相关信息，host模块收集主机情报，而gadget模块被用来串连整个工具链，或者提供输出。
Domain模块总是被最先执行，无论工具链内的顺序，host其次。成组的模块会被并行运行。Gadgets可以被放在工具链的任何部分，但是无法被加入组内。
同组内的模块共享同样的设置，如果未被单独设定，而组外的模块共享同样的参数。单独模块的设定可以被各自设定。
modules list *[分类]
|   显示分类(domain, host, gadget)内的所有可用模块。如果分类参数未被设定，将会输出所有可用的模块。
|   示例:
|   |   modules list domain - 列出所有domain模块。
|   |   modules list - 显示所有模块。
modules search [关键字]
|   根据[关键字]搜索模块。
modules insert [模块名 组名] [链] [顺序]
|   在[CHAIN_ID]链内将[模块名 组名]插入到第[顺序]个位置。
modules pop [CHAIN_ID] [module_id]
|   从[CHAIN_ID]内移除[module_id]。
|   如果模组在组内，它将会被从组内移除，但是组预设将不会被修改。
modules find [关键字] (即将上线)
|   在线上数据库根据[关键字]搜索可用模块。
modules get [模组名] (即将上线)
|   从线上数据库下载名为[模组名]的模块。
modules delete [模组名]
|   在本地永久删除名为[模组名]的模块。
'''
]