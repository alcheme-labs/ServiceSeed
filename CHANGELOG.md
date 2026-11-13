# Changelog / 变更记录

## 0.1.0 — 2026-11-13 / Initial edition · 首版

- Adopt ServiceSeed as the public project name and `serviceseed` as the Skill name; ServerAgent and `serveragent-service` were unpublished working names.

- Package the existing ServiceSeed protocol draft 0.3 in Chinese and a corresponding English translation. No new wire binding or runtime capability is claimed.
- Add the English `serviceseed` Skill and corresponding Chinese translation, with bundled protocol references for standalone installation.
- Explain FDE service delivery and personal service spaces in both READMEs and Skill editions as applications of the same protocol, without adding normative profiles or claiming runtime support.
- Define practical host mappings for creation, authorized observation, candidate validation/activation, dependency calls and operation recovery. Optional Agent Bridge integration leaves these service responsibilities with ServiceSeed and existing owners.
- Version the Skill independently from the protocol and Bridge. Record the reviewed Bridge document baseline without claiming a tested compatibility range.
- Reuse the published Bridge Skill 0.1.0 update-notice algorithm under a separate source/state namespace: on-use checks, cached results, once-per-version notices, explicit snooze/ignore, no automatic install. Configure `alcheme-labs/ServiceSeed` Releases with the `serviceseed-v` tag prefix and record the reviewed public Bridge commit and release.
- Prepare Apache-2.0 licensing, source attribution and a curated public package excluding runtime/private project artifacts.

对应中文：

- 公开项目名定为 ServiceSeed，Skill 名定为 `serviceseed`；ServerAgent 与 `serveragent-service` 为此前未发布工作名。
- 打包现有 ServiceSeed 协议草案 0.3 中文与对应英文，不新增线格式绑定，也不声称新增运行能力。
- 新增英文 `serviceseed` Skill 与中文译文，内含完整协议，可独立安装。
- 在双语 README 与 Skill 中说明 FDE 服务交付、个人服务空间这两个应用场景，共用一份协议，不新增规范分支或运行支持声明。
- 补清创建、获准观察、候选验证/启用、依赖调用和操作恢复的宿主映射；Bridge 可选接入不接管 ServiceSeed 及已有负责方的服务职责。
- Skill、协议与 Bridge 独立版本化，记录 Bridge 文档核对基线，不声明已验证兼容范围。
- 沿用已公开 Bridge Skill 0.1.0 更新提醒算法，使用独立来源/状态：使用时检查、缓存、同版一次提醒、明确选择稍后/忽略、不自动安装；配置 `alcheme-labs/ServiceSeed` Releases 与 `serviceseed-v` 标签前缀，记录核对过的 Bridge 公开提交和发布。
- 准备 Apache-2.0 许可、来源说明及明确限定内容的公开包，排除运行库和私有项目产物。
