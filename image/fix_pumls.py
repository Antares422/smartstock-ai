import os
import re

DIR = '/root/project/java/smartstock-ai/image'

COMMON_STYLE = """skinparam shadowing false

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
}"""

for filename in os.listdir(DIR):
    if not filename.endswith('.puml'):
        continue
    filepath = os.path.join(DIR, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 通用的替换去掉 !theme plain 和旧的 skinparams
    if '!theme plain' in content:
        content = content.replace('!theme plain\n', '')
    
    # 将现有的 skinparam nodesep, ranksep 等和自定义的部分剥离，并替换成新的蓝白风格
    # 使用正则将从 skinparam 到 title 之间的全切掉（如果包含的话）
    # 但要小心有些 linetype ortho 需要保留
    
    # 针对 system-architecture.puml 特殊修复连线
    if filename == 'system-architecture.puml':
        content = content.replace('--->', '-down->')
        # 把我加的乱七八糟的颜色给清掉
        content = re.sub(r'skinparam nodesep 30.*?\}\n\n' + r'skinparam cloud \{.*?\n\}\n\n',
                         'skinparam nodesep 40\nskinparam ranksep 60\nskinparam linetype ortho\n\n' + COMMON_STYLE + '\n\n', 
                         content, flags=re.DOTALL)
                 
    elif filename == 'backtest-flow.puml':
        content = content.replace('storage "MinIO" as minio', 'participant "MinIO" as minio <<storage>>')
        content = re.sub(r'skinparam nodesep 30.*?shadowing false\n',
                         'skinparam nodesep 30\nskinparam ranksep 40\n' + COMMON_STYLE + '\n', 
                         content, flags=re.DOTALL)

    elif filename == 'market-data-flow.puml':
        content = content.replace('note bottom of redis', 'note over redis')
        content = re.sub(r'skinparam nodesep 30.*?shadowing false\n',
                         'skinparam nodesep 30\nskinparam ranksep 40\n' + COMMON_STYLE + '\n', 
                         content, flags=re.DOTALL)

    elif filename == 'database-er.puml':
        content = re.sub(r'skinparam class \{\n.*?\}\n', 
                         COMMON_STYLE + '\n', 
                         content, flags=re.DOTALL)
                         
    elif filename == 'class-diagram.puml':
        content = re.sub(r'skinparam class \{\n.*?\}\n', 
                         COMMON_STYLE + '\n', 
                         content, flags=re.DOTALL)

    elif filename == 'trade-flow.puml' or filename == 'user-interaction.puml':
        content = re.sub(r'skinparam nodesep 30.*?shadowing false\n',
                         'skinparam nodesep 30\nskinparam ranksep 40\n' + COMMON_STYLE + '\n', 
                         content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Fixes applied.")
