# NEKOIntel

[ English ] < -- > [ [简体中文 (Simplified Chinese)](README_cn.md) ]

*"Recon, made easy".*

NEKOIntel is a chain-like modular recon framework for security researchers, pentesters and everyone in between.

### Description

NEKOIntel is *the* tool for your assets recon-and-repeat job. With modular design and extensible in mind, it features:

- Highly modular modules.
- User-friendly interaction.
- Cross-Platform frameworks.
- Fast and reliable recon results.
- A plugin database that can be contributed by anyone.
- Seamless integration with your workflow and NEKOThreat, the successor of SWEP, our upcoming exploitation and scanner framework.

Currently under development, so here's some quick peek of in-tool command for you.

```
# The expected user experience of NEKOIntel.
[NEKOIntel] $ chain new group_subdomain purge group_host_recon purge output_json
Chain 0 spawned, 5 modules armed.
[NEKOIntel] $ chain 0 info
{CHAIN0 subdomain_google/subdomain_sectrails/subdomain_recondev -> purge -> host_recon_shodan/host_recon_dummyscan -> purge -> output_json}
[NEKOIntel] $ chain 0 set target_url https://www.google.com/search/
Set target_url of CHAIN0 to www.google.com.
[NekoIntel] $ chain 0 parameters
{CHAIN0}
target_url: www.google.com
max_recursive_search: 3
http_request_timeout: 1
http_proxy: socks5://localhost:23333
[NEKOIntel] $ save_preset scan CHAIN0 General
Saved CHAIN0 preset to presets/General.json.
[NEKOIntel] $ load_preset scan General
The cat is loading presets...
Loaded preset General to CHAIN1.
[NEKOIntel] $ chain 1 info
{CHAIN1 subdomain_google/subdomain_sectrails/subdomain_recondev -> purge -> host_recon_shodan/host_recon_dummyscan -> purge -> output_json}
[NEKOIntel] $ chain 1 fire
The cat is pressing the big red button...
...
```
