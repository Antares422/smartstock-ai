# 智能股票交易辅助系统 - API 接口文档

**版本**: v1.0
**最后更新**: 2026-03-09
**文档状态**: 草稿

---

## 1. 文档说明

### 1.1 文档目的

本文档详细描述智能股票交易辅助系统的后端 API 接口，包括请求参数、响应格式、错误码等。

### 1.2 接口规范

- **协议**: HTTP/HTTPS
- **请求格式**: JSON
- **响应格式**: JSON
- **字符编码**: UTF-8
- **Base URL**: `http://localhost:8080/api`

### 1.3 通用响应格式

**成功响应**：
```json
{
  "code": 200,
  "message": "success",
  "data": { ... }
}
```

**错误响应**：
```json
{
  "code": 400,
  "message": "参数错误",
  "data": null
}
```

### 1.4 通用错误码

| 错误码 | 说明 |
|--------|------|
| 200 | 成功 |
| 400 | 请求参数错误 |
| 401 | 未授权（Token 无效或过期） |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 429 | 请求过于频繁 |
| 500 | 服务器内部错误 |

---

## 2. 认证接口

### 2.1 用户注册

**接口**: `POST /auth/register`

**请求参数**：
```json
{
  "email": "user@example.com",
  "password": "password123",
  "nickname": "用户昵称"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "注册成功",
  "data": {
    "userId": 123,
    "email": "user@example.com",
    "nickname": "用户昵称"
  }
}
```

### 2.2 用户登录

**接口**: `POST /auth/login`

**请求参数**：
```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "登录成功",
  "data": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
    "userId": 123,
    "email": "user@example.com",
    "nickname": "用户昵称",
    "expiresIn": 604800
  }
}
```

### 2.3 用户登出

**接口**: `POST /auth/logout`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "登出成功",
  "data": null
}
```

---

## 3. 用户接口

### 3.1 获取用户信息

**接口**: `GET /users/me`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "userId": 123,
    "email": "user@example.com",
    "nickname": "用户昵称",
    "avatar": "https://example.com/avatar.jpg",
    "createdAt": "2026-03-09T10:00:00"
  }
}
```

### 3.2 更新用户信息

**接口**: `PUT /users/me`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "nickname": "新昵称",
  "avatar": "https://example.com/new-avatar.jpg"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "更新成功",
  "data": {
    "userId": 123,
    "nickname": "新昵称",
    "avatar": "https://example.com/new-avatar.jpg"
  }
}
```

---

## 4. 行情接口

### 4.1 搜索股票

**接口**: `GET /market/stocks/search`

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| keyword | String | 是 | 搜索关键词（股票代码或名称） |
| limit | Integer | 否 | 返回数量，默认 10 |

**请求示例**：
```
GET /market/stocks/search?keyword=茅台&limit=10
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "stockCode": "600519",
      "stockName": "贵州茅台",
      "market": "SH",
      "industry": "白酒"
    }
  ]
}
```

### 4.2 获取股票详情

**接口**: `GET /market/stocks/{stockCode}`

**请求示例**：
```
GET /market/stocks/600519
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "market": "SH",
    "industry": "白酒",
    "currentPrice": 1850.00,
    "changeRate": 2.5,
    "volume": 1234567,
    "amount": 2280000000.00,
    "high": 1860.00,
    "low": 1840.00,
    "open": 1845.00,
    "close": 1850.00
  }
}
```

### 4.3 获取 K 线数据

**接口**: `GET /market/stocks/{stockCode}/kline`

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| period | String | 是 | 周期：day-日K，week-周K，month-月K，5min-5分钟，15min-15分钟，30min-30分钟，60min-60分钟 |
| startDate | String | 否 | 开始日期（YYYY-MM-DD） |
| endDate | String | 否 | 结束日期（YYYY-MM-DD） |
| limit | Integer | 否 | 返回数量，默认 100 |

**请求示例**：
```
GET /market/stocks/600519/kline?period=day&limit=100
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "date": "2026-03-09",
      "open": 1845.00,
      "close": 1850.00,
      "high": 1860.00,
      "low": 1840.00,
      "volume": 1234567,
      "amount": 2280000000.00
    }
  ]
}
```

### 4.4 获取技术指标

**接口**: `GET /market/stocks/{stockCode}/indicators`

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| indicators | String | 是 | 指标类型，多个用逗号分隔：macd,kdj,rsi,boll |
| period | String | 是 | 周期：day-日K，week-周K，month-月K |
| limit | Integer | 否 | 返回数量，默认 100 |

**请求示例**：
```
GET /market/stocks/600519/indicators?indicators=macd,kdj&period=day&limit=100
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "macd": [
      {
        "date": "2026-03-09",
        "dif": 12.5,
        "dea": 10.2,
        "macd": 2.3
      }
    ],
    "kdj": [
      {
        "date": "2026-03-09",
        "k": 75.5,
        "d": 70.2,
        "j": 85.8
      }
    ]
  }
}
```

---

## 5. 自选股接口

### 5.1 获取自选股列表

**接口**: `GET /watchlist`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "stockCode": "600519",
      "stockName": "贵州茅台",
      "currentPrice": 1850.00,
      "changeRate": 2.5,
      "sortOrder": 1
    }
  ]
}
```

### 5.2 添加自选股

**接口**: `POST /watchlist`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "stockCode": "600519"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "添加成功",
  "data": {
    "stockCode": "600519",
    "stockName": "贵州茅台"
  }
}
```

### 5.3 删除自选股

**接口**: `DELETE /watchlist/{stockCode}`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "删除成功",
  "data": null
}
```

---

## 6. AI 分析接口

### 6.1 获取 AI 行情解读

**接口**: `POST /ai/analysis/market`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "stockCode": "600519"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "analysis": "该股今日高开高走，成交量较昨日放大30%，显示多头力量较强。从技术指标看，MACD金叉，KDJ指标处于超买区，短期有回调压力。支撑位：45.20元，压力位：48.50元。建议：短线投资者可考虑逢高减仓，中线投资者可持股观望。",
    "createdAt": "2026-03-09T10:30:00"
  }
}
```

### 6.2 智能问答

**接口**: `POST /ai/qa`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "question": "茅台现在可以买吗？"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "question": "茅台现在可以买吗？",
    "answer": "贵州茅台（600519）当前价格1850元，处于历史高位。从基本面看，公司业绩稳健，品牌价值高。从技术面看，短期有回调压力。建议：如果是长期投资，可以考虑分批买入；如果是短线交易，建议等待回调后再介入。",
    "createdAt": "2026-03-09T10:35:00"
  }
}
```

### 6.3 获取新闻情绪

**接口**: `GET /ai/news/{stockCode}`

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| limit | Integer | 否 | 返回数量，默认 20 |

**请求示例**：
```
GET /ai/news/600519?limit=20
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "sentimentSummary": {
      "positive": 60,
      "neutral": 30,
      "negative": 10
    },
    "news": [
      {
        "title": "贵州茅台发布年度报告，营收增长15%",
        "source": "新浪财经",
        "publishTime": "2026-03-09T09:00:00",
        "sentiment": "positive",
        "sentimentScore": 0.85,
        "url": "https://example.com/news/123"
      }
    ]
  }
}
```

---

## 7. 交易接口

### 7.1 获取账户信息

**接口**: `GET /trade/account`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "userId": 123,
    "totalAssets": 1050000.00,
    "availableCash": 500000.00,
    "frozenCash": 0.00,
    "positionValue": 550000.00,
    "totalProfit": 50000.00,
    "profitRate": 5.00
  }
}
```

### 7.2 买入股票

**接口**: `POST /trade/buy`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "stockCode": "600519",
  "price": 1850.00,
  "quantity": 100
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "买入成功",
  "data": {
    "orderId": 456,
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "price": 1850.00,
    "quantity": 100,
    "amount": 185055.50,
    "fee": 55.50,
    "status": "filled",
    "filledTime": "2026-03-09T10:40:00"
  }
}
```

### 7.3 卖出股票

**接口**: `POST /trade/sell`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "stockCode": "600519",
  "price": 1850.00,
  "quantity": 100
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "卖出成功",
  "data": {
    "orderId": 457,
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "price": 1850.00,
    "quantity": 100,
    "amount": 184759.50,
    "fee": 55.50,
    "tax": 185.00,
    "status": "filled",
    "filledTime": "2026-03-09T10:45:00"
  }
}
```

### 7.4 获取持仓列表

**接口**: `GET /trade/positions`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": [
    {
      "stockCode": "600519",
      "stockName": "贵州茅台",
      "quantity": 100,
      "availableQuantity": 100,
      "costPrice": 1800.00,
      "currentPrice": 1850.00,
      "marketValue": 185000.00,
      "profit": 5000.00,
      "profitRate": 2.78
    }
  ]
}
```

### 7.5 获取交易记录

**接口**: `GET /trade/records`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| stockCode | String | 否 | 股票代码 |
| tradeType | String | 否 | 交易类型：buy-买入，sell-卖出 |
| startDate | String | 否 | 开始日期（YYYY-MM-DD） |
| endDate | String | 否 | 结束日期（YYYY-MM-DD） |
| page | Integer | 否 | 页码，默认 1 |
| pageSize | Integer | 否 | 每页数量，默认 20 |

**请求示例**：
```
GET /trade/records?page=1&pageSize=20
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "total": 50,
    "page": 1,
    "pageSize": 20,
    "records": [
      {
        "recordId": 789,
        "stockCode": "600519",
        "stockName": "贵州茅台",
        "tradeType": "buy",
        "price": 1850.00,
        "quantity": 100,
        "amount": 185055.50,
        "fee": 55.50,
        "tradeTime": "2026-03-09T10:40:00"
      }
    ]
  }
}
```

---

## 8. 策略回测接口

### 8.1 创建策略

**接口**: `POST /backtest/strategies`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "strategyName": "均线策略",
  "strategyType": "ma",
  "parameters": {
    "shortPeriod": 5,
    "longPeriod": 20
  },
  "initialCapital": 1000000.00,
  "description": "5日均线上穿20日均线买入，下穿卖出"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "创建成功",
  "data": {
    "strategyId": 101,
    "strategyName": "均线策略",
    "strategyType": "ma",
    "createdAt": "2026-03-09T11:00:00"
  }
}
```

### 8.2 执行回测

**接口**: `POST /backtest/run`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "strategyId": 101,
  "stockCode": "600519",
  "startDate": "2025-01-01",
  "endDate": "2025-12-31"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "回测完成",
  "data": {
    "backtestId": 201,
    "strategyId": 101,
    "stockCode": "600519",
    "startDate": "2025-01-01",
    "endDate": "2025-12-31",
    "initialCapital": 1000000.00,
    "finalCapital": 1150000.00,
    "totalReturn": 150000.00,
    "returnRate": 15.00,
    "maxDrawdown": 8.50,
    "sharpeRatio": 1.85,
    "winRate": 65.00,
    "tradeCount": 25,
    "reportUrl": "https://minio.example.com/reports/201.pdf"
  }
}
```

### 8.3 获取回测结果

**接口**: `GET /backtest/results/{backtestId}`

**请求头**：
```
Authorization: Bearer {token}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "backtestId": 201,
    "strategyId": 101,
    "strategyName": "均线策略",
    "stockCode": "600519",
    "stockName": "贵州茅台",
    "startDate": "2025-01-01",
    "endDate": "2025-12-31",
    "initialCapital": 1000000.00,
    "finalCapital": 1150000.00,
    "totalReturn": 150000.00,
    "returnRate": 15.00,
    "maxDrawdown": 8.50,
    "sharpeRatio": 1.85,
    "winRate": 65.00,
    "tradeCount": 25,
    "reportUrl": "https://minio.example.com/reports/201.pdf",
    "createdAt": "2026-03-09T11:05:00"
  }
}
```

---

## 9. 风险预警接口

### 9.1 获取风险预警列表

**接口**: `GET /risk/alerts`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| isRead | Boolean | 否 | 是否已读：true-已读，false-未读 |
| page | Integer | 否 | 页码，默认 1 |
| pageSize | Integer | 否 | 每页数量，默认 20 |

**响应示例**：
```json
{
  "code": 200,
  "message": "success",
  "data": {
    "total": 10,
    "page": 1,
    "pageSize": 20,
    "records": [
      {
        "alertId": 301,
        "alertType": "concentration",
        "alertLevel": "high",
        "message": "持仓过于集中：贵州茅台占总资产的35%",
        "isRead": false,
        "createdAt": "2026-03-09T11:10:00"
      }
    ]
  }
}
```

### 9.2 设置止损止盈

**接口**: `POST /risk/stop-loss-profit`

**请求头**：
```
Authorization: Bearer {token}
```

**请求参数**：
```json
{
  "stockCode": "600519",
  "stopLossPrice": 1750.00,
  "stopProfitPrice": 1950.00,
  "notifyMethod": "message"
}
```

**响应示例**：
```json
{
  "code": 200,
  "message": "设置成功",
  "data": {
    "configId": 401,
    "stockCode": "600519",
    "stopLossPrice": 1750.00,
    "stopProfitPrice": 1950.00,
    "notifyMethod": "message",
    "isEnabled": true
  }
}
```

---

## 10. WebSocket 接口

### 10.1 连接地址

```
ws://localhost:8080/ws/market
```

### 10.2 订阅行情

**客户端发送**：
```json
{
  "type": "subscribe",
  "stocks": ["600519", "000001"]
}
```

**服务端响应**：
```json
{
  "type": "subscribe_success",
  "stocks": ["600519", "000001"]
}
```

### 10.3 取消订阅

**客户端发送**：
```json
{
  "type": "unsubscribe",
  "stocks": ["600519"]
}
```

### 10.4 实时行情推送

**服务端推送**：
```json
{
  "type": "price_update",
  "stockCode": "600519",
  "stockName": "贵州茅台",
  "price": 1850.00,
  "changeRate": 2.5,
  "volume": 1234567,
  "timestamp": "2026-03-09T11:15:00"
}
```

---

## 11. 附录

### 11.1 Postman 集合

（待补充 Postman Collection JSON 文件）

### 11.2 变更记录

| 版本 | 日期 | 变更内容 | 变更人 |
|------|------|----------|--------|
| v1.0 | 2026-03-09 | 初始版本 | 开发团队 |

---

**文档维护者**：后端团队
**审核人**：待定
**批准人**：待定
