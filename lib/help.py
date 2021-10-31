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