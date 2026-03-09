# 智能股票交易辅助系统（smartstock-ai）

[![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.5.11-brightgreen.svg)](https://spring.io/projects/spring-boot)
[![Java](https://img.shields.io/badge/Java-17-orange.svg)](https://www.oracle.com/java/)
[![License](https://img.shields.io/badge/License-TBD-blue.svg)](LICENSE)

## 项目简介

**smartstock-ai** 是一个基于 AI 技术的智能股票交易辅助系统，为个人投资者和量化交易爱好者提供：

- 🚀 **实时行情监控** - 毫秒级行情推送，WebSocket 实时通信
- 🤖 **AI 智能分析** - Claude API 驱动的行情解读和智能问答
- 💼 **模拟交易** - 零风险模拟交易环境，验证策略
- 📊 **策略回测** - 自定义策略 + AI 参数优化
- ⚠️ **风险预警** - 多维度风险监控和智能提醒

## 技术栈

- **后端**：Spring Boot 3.5.11 + Java 17 + MyBatis Plus
- **前端**：Vue 3 + ECharts + WebSocket
- **中间件**：MySQL 8.0 + Redis 7.x + Kafka 3.x + MinIO
- **AI**：LangChain4j + Claude API

## 快速开始

### 环境要求

- JDK 17+
- Maven 3.6+
- MySQL 8.0+
- Redis 7.0+
- Kafka 3.0+
- MinIO

### 启动步骤

```bash
# 1. 克隆项目
git clone <repository-url>
cd smartstock-ai

# 2. 配置数据库
mysql -u root -p785460 -e "CREATE DATABASE smartstock_ai DEFAULT CHARACTER SET utf8mb4;"

# 3. 启动中间件
systemctl start redis-server kafka minio

# 4. 修改配置文件
# 编辑 src/main/resources/application.yml

# 5. 启动后端服务
mvn clean install
mvn spring-boot:run
```

## 文档

完整的项目文档请查看 [doc](./doc/) 目录：

- [📖 项目概述](./doc/01-项目概述.md) - 项目整体介绍和快速导航
- [📋 产品需求文档](./doc/02-产品需求文档.md) - 详细功能需求（待编写）
- [🏗️ 技术架构文档](./doc/03-技术架构文档.md) - 系统架构设计（待编写）
- [🗄️ 数据库设计](./doc/04-数据库设计.md) - 数据库表结构（待编写）
- [🔌 API 接口文档](./doc/05-API接口文档.md) - 后端接口定义（待编写）
- [👨‍💻 开发指南](./doc/06-开发指南.md) - 开发规范和流程（待编写）

## 项目结构

```
smartstock-ai/
├── doc/                    # 项目文档
├── src/
│   ├── main/
│   │   ├── java/          # Java 源代码
│   │   └── resources/     # 配置文件
│   └── test/              # 测试代码
├── pom.xml                # Maven 配置
└── README.md              # 本文件
```

## 开发状态

🚧 **项目当前处于初始阶段**，正在进行文档体系建设和架构设计。

- [x] 项目初始化
- [x] 文档体系建设
- [ ] 数据库设计
- [ ] 核心功能开发
- [ ] 前端界面开发
- [ ] 测试和部署

## 贡献指南

欢迎贡献代码和提出建议！请先阅读 [开发指南](./doc/06-开发指南.md)（待编写）。

## 许可证

待定

## 联系方式

如有问题或建议，请提交 Issue 或 Pull Request。

---

**版本**：v0.0.1-SNAPSHOT
**最后更新**：2026-03-09
