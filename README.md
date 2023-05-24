# BUPT-KG-lab3
bupt 芝士图谱期末大作业。<br>
## 语料数据预处理部分<br>
执行如下指令下载所需的包：<br>
```bash
pip install -r requirements.txtpre
```
您还需安装好neo4j数据库与jdk环境，这里使用的neo4j版本为：neo4j-community-5.8.0，jdk版本为17，可以参考网上的教程进行安装。<br>
先从语料中提取出实体与关系的标注信息：
```bash
python process.py
```
然后根据提取出的标注信息构建rdf格式的三元组数据：
```bash
python rdf_builder.py
```
最后将数据写入到neo4j中：
```bash
python neo4j_builder.py
```
您可能需要将neo4j_builder.py中的参数进行修改，如下：
```python
if __name__ == '__main__':
    builder = Neo4jBuilder(neo4j_url='http://localhost:7474', neo4j_user='neo4j', neo4j_password='20020601',
                           database_name='neo4j', entity_path='data/entity_result.json')
    builder.build()
```
