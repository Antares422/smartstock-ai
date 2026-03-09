
# 整体布局说明（从左到右五列）：
# Col A: 前端层       x=40,   w=200
# Col B: 网关层       x=290,  w=220
# Col C: 业务服务层    x=560,  w=200
# Col D: 数据层       x=810,  w=185
# Col D2: 外部服务层   x=810,  w=185  (接在数据层下方)
#
# 垂直方向统一从 y=40 开始。

STYLE_PKG     = "swimlane;whiteSpace=wrap;html=1;fillColor=#E3F2FD;strokeColor=#1565C0;startSize=30;fontStyle=1;fontSize=13;"
STYLE_FRONT   = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1565C0;fontSize=12;"
STYLE_GW      = "rounded=1;whiteSpace=wrap;html=1;fillColor=#E8F5E9;strokeColor=#1565C0;fontSize=12;"
STYLE_SVC     = "rounded=1;whiteSpace=wrap;html=1;fillColor=#FFF9C4;strokeColor=#1565C0;fontSize=12;"
STYLE_DB      = "shape=cylinder3;whiteSpace=wrap;html=1;boundedLbl=1;backgroundOutline=1;size=12;fillColor=#E0F7FA;strokeColor=#1565C0;fontSize=12;"
STYLE_EXT     = "ellipse;shape=cloud;whiteSpace=wrap;html=1;fillColor=#FCE4EC;strokeColor=#1565C0;fontSize=12;"
STYLE_EDGE    = "endArrow=classic;html=1;strokeColor=#1565C0;edgeStyle=orthogonalEdgeStyle;rounded=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;"

cells = []
edge_id = 1000

def node(id, val, x, y, w, h, style, parent="1"):
    v = val.replace('\n', '&#xa;')
    cells.append(f'<mxCell id="{id}" value="{v}" style="{style}" vertex="1" parent="{parent}"><mxGeometry x="{x}" y="{y}" width="{w}" height="{h}" as="geometry" /></mxCell>')

def edge(src, tgt, val="", ex=1, ey=0.5, nx=0, ny=0.5):
    global edge_id
    st = f"endArrow=classic;html=1;strokeColor=#1565C0;edgeStyle=orthogonalEdgeStyle;rounded=1;exitX={ex};exitY={ey};exitDx=0;exitDy=0;entryX={nx};entryY={ny};entryDx=0;entryDy=0;"
    cells.append(f'<mxCell id="e{edge_id}" value="{val}" style="{st}" edge="1" parent="1" source="{src}" target="{tgt}"><mxGeometry relative="1" as="geometry" /></mxCell>')
    edge_id += 1

# ─── 尺寸常量 ───────────────────────────────────────────────
PKG_H = 30       # swimlane header 高度
ITEM_H = 50      # 每个子节点高度
ITEM_GAP = 12    # 子节点间距
MARGIN = 14      # 内部边距

# ─── 列 X 坐标 ──────────────────────────────────────────────
X_FRONT = 40
X_GW    = 290
X_SVC   = 560
X_DATA  = 810
W_FRONT = 190
W_GW    = 220
W_SVC   = 200
W_DATA  = 185

# ─── 前端层 ─────────────────────────────────────────────────
# 5个子节点
front_items = ["行情监控", "AI 分析", "模拟交易", "策略回测", "风险预警"]
n_front = len(front_items)
front_inner_h = n_front * ITEM_H + (n_front - 1) * ITEM_GAP + 2 * MARGIN
front_total_h = PKG_H + front_inner_h
front_y = 40

node("pkg_front", "前端层 (Vue 3)", X_FRONT, front_y, W_FRONT, front_total_h, STYLE_PKG)
for i, label in enumerate(front_items):
    y_rel = PKG_H + MARGIN + i * (ITEM_H + ITEM_GAP)
    node(f"ui_{i}", label, X_FRONT + MARGIN, front_y + y_rel, W_FRONT - 2*MARGIN, ITEM_H, STYLE_FRONT)

front_cy = front_y + front_total_h / 2  # 前端层中心 Y

# ─── 网关层 ─────────────────────────────────────────────────
# 2个子节点，垂直居中对齐前端层
gw_items = ["路由转发", "鉴权限流"]
n_gw = len(gw_items)
gw_inner_h = n_gw * ITEM_H + (n_gw - 1) * ITEM_GAP + 2 * MARGIN
gw_total_h = PKG_H + gw_inner_h
gw_y = int(front_cy - gw_total_h / 2)   # 使网关层中心 = 前端层中心

node("pkg_gw", "API 网关层 (Spring Gateway)", X_GW, gw_y, W_GW, gw_total_h, STYLE_PKG)
for i, label in enumerate(gw_items):
    y_rel = PKG_H + MARGIN + i * (ITEM_H + ITEM_GAP)
    node(f"gw_{i}", label, X_GW + MARGIN, gw_y + y_rel, W_GW - 2*MARGIN, ITEM_H, STYLE_GW)

# ─── 业务服务层 ──────────────────────────────────────────────
# 6个子节点，顶部与前端层对齐 (y=40)
svc_items = ["用户服务\nuser-service", "行情服务\nmarket-service", "AI 服务\nai-service",
             "交易服务\ntrade-service", "回测服务\nbacktest-service", "风险服务\nrisk-service"]
svc_ids   = ["svc_user", "svc_market", "svc_ai", "svc_trade", "svc_backtest", "svc_risk"]
n_svc = len(svc_items)
svc_inner_h = n_svc * ITEM_H + (n_svc - 1) * ITEM_GAP + 2 * MARGIN
svc_total_h = PKG_H + svc_inner_h
svc_y = front_y  # 与前端层顶部对齐

node("pkg_svc", "业务服务层", X_SVC, svc_y, W_SVC, svc_total_h, STYLE_PKG)
for i, (label, sid) in enumerate(zip(svc_items, svc_ids)):
    y_rel = PKG_H + MARGIN + i * (ITEM_H + ITEM_GAP)
    node(sid, label, X_SVC + MARGIN, svc_y + y_rel, W_SVC - 2*MARGIN, ITEM_H, STYLE_SVC)

# ─── 数据层 ──────────────────────────────────────────────────
# 4个子节点，顶部与业务服务层对齐
db_items = ["MySQL\n关系型数据库", "Redis\n缓存", "Kafka\n消息队列", "MinIO\n对象存储"]
db_ids   = ["db_mysql", "db_redis", "db_kafka", "db_minio"]
n_db = len(db_items)
db_inner_h = n_db * ITEM_H + (n_db - 1) * ITEM_GAP + 2 * MARGIN
db_total_h = PKG_H + db_inner_h
db_y = svc_y  # 顶部对齐

node("pkg_data", "数据层", X_DATA, db_y, W_DATA, db_total_h, STYLE_PKG)
for i, (label, did) in enumerate(zip(db_items, db_ids)):
    y_rel = PKG_H + MARGIN + i * (ITEM_H + ITEM_GAP)
    node(did, label, X_DATA + MARGIN, db_y + y_rel, W_DATA - 2*MARGIN, ITEM_H, STYLE_DB)

# ─── 外部服务层（紧接数据层下方，两者垂直间隔20px）───────────────
ext_items = ["行情 API\n新浪/东方财富", "Claude API\nAI 大模型", "新闻 API\n财经新闻"]
ext_ids   = ["ext_stock", "ext_ai", "ext_news"]
n_ext = len(ext_items)
ext_inner_h = n_ext * ITEM_H + (n_ext - 1) * ITEM_GAP + 2 * MARGIN
ext_total_h = PKG_H + ext_inner_h
ext_gap = 20
ext_y = db_y + db_total_h + ext_gap

node("pkg_ext", "外部服务层", X_DATA, ext_y, W_DATA, ext_total_h, STYLE_PKG)
for i, (label, eid) in enumerate(zip(ext_items, ext_ids)):
    y_rel = PKG_H + MARGIN + i * (ITEM_H + ITEM_GAP)
    node(eid, label, X_DATA + MARGIN, ext_y + y_rel, W_DATA - 2*MARGIN, ITEM_H, STYLE_EXT)

# ─── 连线 ────────────────────────────────────────────────────
# 前端 -> 网关 (exit right, enter left)
edge("pkg_front", "pkg_gw", "HTTP/WebSocket")

# 网关路由 -> 各服务
for sid in svc_ids:
    edge("gw_0", sid)

# 服务 -> 数据层
edge("svc_user",     "db_mysql")
edge("svc_user",     "db_redis")
edge("svc_market",   "db_mysql")
edge("svc_market",   "db_redis")
edge("svc_market",   "db_kafka")
edge("svc_ai",       "db_mysql")
edge("svc_ai",       "db_redis")
edge("svc_trade",    "db_mysql")
edge("svc_trade",    "db_redis")
edge("svc_backtest", "db_mysql")
edge("svc_backtest", "db_minio")
edge("svc_risk",     "db_mysql")
edge("svc_risk",     "db_redis")

# 服务 -> 外部
edge("svc_market", "ext_stock", "拉取行情")
edge("svc_ai",     "ext_ai",    "AI 分析")
edge("svc_ai",     "ext_news",  "抓取新闻")

# ─── 组装 XML ────────────────────────────────────────────────
xml_out = f'''<mxfile>
  <diagram id="sys_arch" name="System Architecture">
    <mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="1400" pageHeight="900" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />
        {chr(10).join(cells)}
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>'''

with open('/root/project/java/smartstock-ai/image/system-architecture.drawio', 'w', encoding='utf-8') as f:
    f.write(xml_out)

print(f"Done. front_total_h={front_total_h}, gw_total_h={gw_total_h}, svc_total_h={svc_total_h}, db_total_h={db_total_h}, ext_y={ext_y}")
