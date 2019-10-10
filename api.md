## 数据库相关信息：
```
站点命名：S1->S10
线路命名：
R1->R3
R1: S1->S2->S3->S4->S5
R2: S6->S7->S2->S8
R3: S8->S9->S10
```


## API
* http://127.0.0.1:8000/Bus/news/
解释：新闻信息获取
```json
// 返回值格式
[{"title":" ","content":" ","time":" "},]
// 案例
[
  {"title": "线路改变", "content": "增加R1", "time": "2019-09-20"}, {"title": "线路通知", "content": "增加线路R2", "time":"2019-09-20"}, {"title": "线路变更", "content": "增加线路R3", "time":"2019-09-20"}
]
```

* http://127.0.0.1:8000/Bus/busid/
获取对应公交车的线路
```json
// 请求格式
{"busid":" "}
// 返回值格式
{"busid":[" "," "]}

// 案例请求：
{"busid":"R1"}

// 返回：
{"R1": ["S1", "S2", "S3", "S4", "S5"]}
* http://127.0.0.1:8000/Bus/searchroute/
// 乘车线路查询
// 请求格式：
{"startid":" ","endid":" "}
// 返回格式：
{"transferTimes": , " ": ["", ""]}
// 参数解释：
// transferTimes：换乘次数
// 案例1：
// 请求：
{"startid":"S1","endid":"S5"}
// 返回
{"transferTimes": 0, "R1": ["S1", "S2", "S3", "S4", "S5"]}
// 案例2：
// 请求：
{"startid":"S1","endid":"S7"}
// 返回：
{"transferTimes": 1, "R1": ["S1", "S2"], "R2": ["S2", "S7"]}
// 案例3：
// 请求：
{"startid":"S1","endid":"S10"}
// 返回：
{"transferTimes": 2, "R1": ["S1", "S2"], "R2": ["S2", "S8"], "R3": ["S8", "S9", "S10"]}
```

* http://127.0.0.1:8000/Bus/srearchbus/
查询经过此站点的公交车号

```json
// 请求格式：
{"stationname":" "}
// 返回格式：
{"passid": [" ", ...]}
// 案例：
// 请求：
{"stationname":"S2"}
// 返回：
{"passid": ["R1", "R2"]}
```
