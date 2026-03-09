import re

content = """@startuml system-architecture

skinparam nodesep 40
skinparam ranksep 60
skinparam shadowing false

skinparam {
    BackgroundColor white
    BorderColor #1565C0
    ArrowColor #1565C0
    DefaultFontColor #2C3E50
    
    NoteBackgroundColor #E3F2FD
    NoteBorderColor #1565C0
    
    ComponentBackgroundColor #E3F2FD
    RectangleBackgroundColor #E3F2FD
    DatabaseBackgroundColor #E3F2FD
    QueueBackgroundColor #E3F2FD
    StorageBackgroundColor #E3F2FD
    CloudBackgroundColor #E3F2FD
    
    ParticipantBackgroundColor #E3F2FD
    ActorBackgroundColor #E3F2FD
    
    ClassBackgroundColor #E3F2FD
}

title 智能股票交易辅助系统 - 整体架构

package "前端层" <<frontend>> {
    rectangle "Vue 3 前端应用" as frontend {
        rectangle "行情监控" as market_ui
        rectangle "AI 分析" as ai_ui
        rectangle "模拟交易" as trade_ui
        rectangle "策略回测" as backtest_ui
        rectangle "风险预警" as risk_ui
        
        market_ui -[hidden]right- ai_ui
        ai_ui -[hidden]right- trade_ui
        trade_ui -[hidden]right- backtest_ui
        backtest_ui -[hidden]right- risk_ui
    }
}

package "API 网关层" <<gateway>> {
    rectangle "Spring Gateway" as gateway {
        rectangle "路由转发" as route
        rectangle "鉴权限流" as auth
        
        route -[hidden]right- auth
    }
}

package "业务服务层" <<service>> {
    rectangle "用户服务\\nuser-service" as user_service
    rectangle "行情服务\\nmarket-service" as market_service
    rectangle "AI 服务\\nai-service" as ai_service
    rectangle "交易服务\\ntrade-service" as trade_service
    rectangle "回测服务\\nbacktest-service" as backtest_service
    rectangle "风险服务\\nrisk-service" as risk_service
    
    user_service -[hidden]right- market_service
    market_service -[hidden]right- ai_service
    ai_service -[hidden]right- trade_service
    trade_service -[hidden]right- backtest_service
    backtest_service -[hidden]right- risk_service
}

package "数据层" <<data>> {
    database "MySQL\\n关系型数据库" as mysql
    database "Redis\\n缓存" as redis
    queue "Kafka\\n消息队列" as kafka
    storage "MinIO\\n对象存储" as minio
    
    mysql -[hidden]right- redis
    redis -[hidden]right- kafka
    kafka -[hidden]right- minio
}

package "外部服务层" <<external>> {
    cloud "行情 API\\n新浪/东方财富" as stock_api
    cloud "Claude API\\nAI 大模型" as claude_api
    cloud "新闻 API\\n财经新闻" as news_api
    
    stock_api -[hidden]right- claude_api
    claude_api -[hidden]right- news_api
}

' 前端到网关
frontend ---> gateway : HTTP/WebSocket

' 网关到服务
gateway ---> user_service : HTTP
gateway ---> market_service : HTTP
gateway ---> ai_service : HTTP
gateway ---> trade_service : HTTP
gateway ---> backtest_service : HTTP
gateway ---> risk_service : HTTP

' 服务到数据层
user_service ---> mysql
user_service ---> redis

market_service ---> mysql
market_service ---> redis
market_service ---> kafka

ai_service ---> mysql
ai_service ---> redis

trade_service ---> mysql
trade_service ---> redis

backtest_service ---> mysql
backtest_service ---> minio

risk_service ---> mysql
risk_service ---> redis

' 服务到外部服务
market_service ---> stock_api : 拉取行情
ai_service ---> claude_api : "AI 分析"
ai_service ---> news_api : "抓取新闻"

note right of gateway
  - JWT Token 验证
  - 限流：100次/分钟/用户
  - 路由转发到各服务
end note

note right of kafka
  - 实时行情数据流
  - 异步消息处理
  - 3 个分区
end note

@enduml
"""

with open('/root/project/java/smartstock-ai/image/system-architecture.puml', 'w') as f:
    f.write(content)
