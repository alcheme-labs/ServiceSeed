# ServiceSeed

中文 | [English](README.md)

官方仓库：[alcheme-labs/ServiceSeed](https://github.com/alcheme-labs/ServiceSeed) · [版本发布](https://github.com/alcheme-labs/ServiceSeed/releases)。

**一份让服务在授权范围内维护自身实现、持续履行调用方承诺的开放规范。** AI 在服务空间中创建服务，宿主约束维护 Agent，其他服务按照明确契约和权限使用其能力。

面向 **FDE 服务交付与个人服务空间**：让 AI 创建、互联和持续维护服务，同时守住权限边界与服务契约。

本包包含协议及配套 Skill，指导 AI 创建、维护、连接和评审此类服务；不包含运行中的宿主或参考运行库。仅连接 Agent 不代表已经提供服务专属维护能力。

## 阅读入口

- [中文协议](skills/serviceseed/references/protocol.zh-CN.md) · [English](skills/serviceseed/references/protocol.md)
- [英文 Skill](skills/serviceseed/SKILL.md) · [中文译文](skills/serviceseed/SKILL.zh-CN.md)
- [宿主能力与可选 Bridge 接入](skills/serviceseed/references/host-integration.zh-CN.md) · [English](skills/serviceseed/references/host-integration.md)
- [版本与更新机制](skills/serviceseed/references/updates.zh-CN.md) · [English](skills/serviceseed/references/updates.md)

协议规定共同含义与行为义务，各服务契约确定业务含义和承诺，宿主自行选择实现并落实授权、候选验证、受控启用和结果恢复。Skill 提供实际工作流程与宿主入口映射，不另立规范。

核心路径是：**目标与授权 → 候选 → 独立验证 → 受控启用 → 消费者确认 → 观察与维护**。服务可独立创建，再依据兼容描述、契约和绑定建立授权调用关系。普通调用可以直接执行活动实现，无须逐次调用模型。

## 应用场景：FDE 服务协议与个人服务协议

这里的“FDE 服务协议”和“个人服务协议”是同一通用技术协议的两个应用场景，共用身份、契约、授权、受控维护及恢复约定，不另设两套规范，也不限制其他服务场景。

| 场景 | 要解决的事情 | 用这份协议约定什么 |
| --- | --- | --- |
| **FDE 服务交付与持续维护** | 将面向客户业务的工程交付沉淀为可持续运行、可接续维护的服务；数据源、依赖或内部实现变化时，保持客户已接受的调用承诺 | 客户认可的业务契约与验收、实际资源授权、维护委托、变更启用和结果确认；工程师、供应商或 Agent 的身份不自动产生客户数据访问权或变更权 |
| **个人服务空间** | 个人借助 AI 创建自己的服务，并按权限向指定的人或其他服务提供能力，由获委托的 Agent 持续维护 | 服务归属、资源与数据使用范围、谁能调用、谁能维护、哪些信息能交给模型、如何撤权及恢复；对外开放能力不自动开放原始数据或内部维护上下文 |

这两个场景沿用同一 Skill 工作流程。具体业务承诺、共享对象、维护期限和适用条件由相应服务契约与授权确定。以上是应用定位；是否实际满足承诺，仍须由具体宿主和服务验证，不能将场景介绍当成已完成的运行支持。

## 安装与使用 Skill

取得官方仓库或对应发布包：

```sh
git clone https://github.com/alcheme-labs/ServiceSeed.git
```

将完整 `ServiceSeed/skills/serviceseed` 目录复制到 Agent 宿主的技能目录，支持链接时也可建立链接。目录已包含双语协议与参考，使用 Skill 不依赖仓库外其他文件。覆盖已有安装前先核对并保留本地改动。下载本包不等于已安装到 Agent 宿主。首个公开 Skill 名为 `serviceseed`，之前未发布工作副本使用的名称为 `serveragent-service`。

使用宿主的正常技能选择方式；支持名称调用时，可这样提出任务：

> 使用 `$serviceseed`，根据这个目标和获认可业务规则，使用附带资源说明、授权与现有宿主创建服务。维护时保持已接受的调用方契约。交付实际运行、调用、维护入口及验证结果。

提供真实目标、含义、权限与可用资源，不需要工种专用服务模板。Skill 不能补造授权或运行能力，会指出具体缺口，并只在用户授权范围内实现。只要求评审时，不开发或部署服务。回答跟随用户语言。

## Agent Bridge 与版本

[Agent Bridge Spec](https://github.com/alcheme-labs/agent-bridge-spec) 及其 `agent-bridge-integration` Skill 是应用与 Agent 连接、会话和工具接入的可选参考。ServiceSeed 仍负责服务契约、维护委托/上下文、候选验证/启用、依赖关系与消费者确认。原生适配也可落实相同要求。

版本分别管理。[VERSION](skills/serviceseed/VERSION) 为 Skill 版本，[compatibility.json](skills/serviceseed/compatibility.json) 记录随包协议与核对过的 Bridge 基线，不强制同步升级，也不声明未经验证的 Bridge 版本兼容范围。接入变化时检查受影响角色、绑定与能力。

Skill 使用时检查更新，默认网络检查间隔 24 小时，可配置，并持久化按版本去重。发现新版后说明真实获取的变化，询问现在更新、稍后或忽略，不自动安装。没有闲置时的后台调度。[更新源](skills/serviceseed/update-source.json)已配置为 `alcheme-labs/ServiceSeed`，读取 `serviceseed-v<版本>` 标签对应的 GitHub Release。网络或 API 失败如实报告检查失败，不据此认定已是最新版。

## 当前状态与验证

首版日期 2026-11-13：协议草案 **0.3**，Skill **0.1.0**。公开项目正式命名 ServiceSeed，ServerAgent 为原工作名。协议定义共同语义，统一具体线格式/绑定尚未定型，也未完成独立实现互通验证。不能仅安装 Skill 就声称生成服务已互通，仍须共同绑定及运行验证。

Bridge 的 [Skill 0.1.0 发布](https://github.com/alcheme-labs/agent-bridge-spec/releases/tag/agent-bridge-integration-v0.1.0)及规范 draft 0.3 已公开；兼容元数据记录了核对的提交版本。这是文档对照，不是运行兼容证明。本包不包含 Bridge 运行库，也不声称已有公共 SDK。

可用 Python 3.9+ 检查本包：

```sh
python3 scripts/validate_package.py
python3 -B -m unittest discover -s tests -p 'test_skill_updates.py' -v
python3 skills/serviceseed/scripts/check_updates.py check
```

测试以临时状态与受控响应验证提醒决定、持久化、并发和网络失败，不证明真实发布发现或服务符合性。运行验收仍按协议及具体服务承诺完成。

## 贡献与发布

协议要求集中在正文，宿主选型与具体任务限制不写成通用要求。协议和 Skill 均维护双语对应。协议译文差异以中文原文核对，Skill 中文对应英文入口；不能只在 Skill 内解决规范歧义。

发布 Skill 时更新 `VERSION`、相关兼容元数据和[变更记录](CHANGELOG.md)。不改变要求行为的修正升 patch，兼容的工作流程补充升 minor；破坏性变化明确标出，`0.x` 阶段 minor 可含已披露的不兼容变化。这是 Skill 发布策略，不是互通保证。

每版 Skill 按 `serviceseed-v<version>` 创建 GitHub Release，提供实际变化与兼容说明。检查导出内容、许可/来源和验证结果，保留已发布版本及产物。仅创建普通标签不会触发更新提醒。不得把私有服务状态、凭据或内部证据随包发布。

采用 [Apache-2.0](LICENSE)，见 [NOTICE](NOTICE) 和[更新脚本来源](update-helper-origin.json)。许可覆盖这些文档、Skill 和辅助脚本，不授予运行数据访问、调用或维护权限。
