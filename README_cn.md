![NEKOIntel Logo](nekointel-logo.png)

# NEKOIntel

[ [English](README.md) ] < -- > [ 简体中文 ]

*"侦察，更加简单。".*

猫情报是为了安全研究者，渗透测试专家和之间的任何人设计的链式模块化资产收集/侦察工具。

### 一点简述

猫情报专为你的资产收集和渗透前侦察工作而生。以模块化设计和可扩展性为主旨，它提供了：

- 高度模块化的组件。
- 用户友好的交互体验。
- 跨平台支持。
- 快速而可靠的结果。
- 任何人都可提交的在线插件数据库。
- 与你的工作流和猫威胁-SWEP的后继者，我们接下来要开发的漏洞利用和扫描器框架无缝衔接。

正在绝赞开发中，这是一点点预览。

```
# 预期用户体验，不代表最终效果。
# 是的，我们会实现中文支持。弃坑吧，CMD用户。
[NEKOIntel] $ chain new group_subdomain purge group_host_recon purge output_json
生成了CHAIN0，准备了5个模组。
[NEKOIntel] $ chain 0 info
{CHAIN0 subdomain_google/subdomain_sectrails/subdomain_recondev -> purge -> host_recon_shodan/host_recon_dummyscan -> purge -> output_json}
[NEKOIntel] $ chain 0 set target_url https://www.google.com/search/
将target_url设置到了 www.google.com.
[NekoIntel] $ chain 0 parameters
{CHAIN0}
target_url: www.google.com
max_recursive_search: 3
http_request_timeout: 1
http_proxy: socks5://localhost:23333
[NEKOIntel] $ save_preset scan CHAIN0 General
CHAIN0被保存到了 presets/General.json.
[NEKOIntel] $ load_preset scan General
猫猫正在加载预设...
将预设General加载到了 CHAIN1.
[NEKOIntel] $ chain 1 info
{CHAIN1 subdomain_google/subdomain_sectrails/subdomain_recondev -> purge -> host_recon_shodan/host_recon_dummyscan -> purge -> output_json}
[NEKOIntel] $ chain 1 fire
猫猫正在按下大红按钮...
...
```

和一点扫描结果，为了一些好奇的用户。

```
[NEKOIntel] CHAIN0 $ fire
[ 信息 ] 猫猫正在按下大红按钮...
[ 信息 ] 开始对1个域名的侦察。
[ 信息 ] 发射CHAIN0 { subdomain_google/subdomain/sectrails/subdomain_recondev -> purge -> host_recon_shodan/host_recon_nmap/host_recon_dummyscan -> purge -> domain_fidelity_check/domain_tagger -> purge -> output_text }.
...
[ 信息 ] 猫猫正在最终化结果。
sup0rsonic.github.io ( 185.199.110.153, 找到了0个历史解析。 )
|   标签: Github, Github Pages, Github pages blog, Hexo, Nodejs, Ruby
|   置信度(f): Github Pages(100%), Blog(75%), Hexo(100%)	
|	Whois查询: MarkMonitor Inc., CA, US.
上级域名: github.io ( 找到了53个子域名。 )
针对域名找到了1个IP地址。
IP地址: 185.199.110.153
|	状态: [ 在线, 主要地址 ]
|	标签: Github, 网站主机
|	置信度(f): Github(100%), 网站主机(100%), 反向代理(30%), HTTPS(100%)
|	找到了2个开放端口。
|	|   [ 开放 ] 80 HTTP, http-proxy, Varnish
|	|	[ 开放 ] 443 HTTPS ssl/https GitHub.com
|
[ 成功 ] 工具链运行结束。
[ NEKOIntel ] CHAIN0 $
```