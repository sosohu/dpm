# API

## List 
### Request
#### Request Headers
```
POST /cultural/queryList HTTP/1.1
Host: digicol.dpm.org.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Referer:  https://digicol.dpm.org.cn/list?page=1&category=17
X-Requested-With: XMLHttpRequest
Origin: https://digicol.dpm.org.cn
Accept: application/json, text/javascript, */*; q=0.01
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Content-Length: 90
```

#### Request Body
```
page=1&keyWord=&authorizeStatus=false&hasImage=false&cateList=17&ranNum=0.6671848452340445
```

### Response
#### Response Headers
```
HTTP/1.1 200 
Server: nginx
Date: Tue, 05 May 2020 14:38:35 GMT
Content-Type: application/json;charset=UTF-8
Content-Length: 33424
Connection: keep-alive
Set-Cookie: SESSION=NDFlMWI1ZDYtNTQxOS00YjVlLWE4ZjEtNWZkZjk2NTMyYTUz; Domain=digicol.dpm.org.cn; Path=/; HttpOnly
X-Frame-Options: SAMEORIGIN
Strict-Transport-Security: max-age=86400
Referrer-Policy: origin-when-cross-origin
Content-Security-Policy: upgrade-insecure-requests;connect-src *
X-Permitted-Cross-Domain-Policies: none
X-XSS-Protection: 1; mode=block
X-Download-Options: noopen
X-Content-Type-Options: : nosniff
```
#### Response Body
```
{
    "pagesize":32,"pagecount":1429,"recordcount":45706,"currentPage":1,"start":0,
    "rows":
    [
        {"id":1530136,"delFlag":"0","addTime":"2019-05-30 21:55:52","updateTime":"2020-03-05 22:28:42","addTimeStamp":1564024290000,"updateTimeStamp":1583418522000,"uuid":"9b987fc0dcd7416c8ade05781db6b98e","name":"展子虔游春图卷","titleName":"展子虔游春图卷","culturalRelicNo":"新00146610","surveyNo":null,"levelId":3,"levelName":"一级甲","categoryId":17,"categoryName":"绘画","dynastyId":235,"dynastyName":"隋","dynastySort":0,"materialId":null,"materialName":null,"rsize":null,"author":null,"hasImage":"1","smallImage":"/relic/c0ecee84ab454a18a557c5c1b2263777/e5fc8068d7004844832b97e9eb399d74.jpg","centerImage":"/relic/c0ecee84ab454a18a557c5c1b2263777/707961bd160c4af28524c50335769e0a.jpg","centerImgWidth":895.74,"centerImgHeight":100.0,"bigImage":"/relic/c0ecee84ab454a18a557c5c1b2263777/448dda0bb2b543f88f283b2a944de453.jpg","viewCount":7112,"collectCount":null,"position":1.0,"isActive":1,"imageId":null,"suggestName":"展子虔游春图卷","suggestCulturalNo":"新00146610","suggestDynastyName":"隋","suggestCategoryName":"绘画"},
        ...
        {"id":1561176,"delFlag":"0","addTime":"2019-05-30 22:12:09","updateTime":"2019-07-26 00:37:25","addTimeStamp":1560149345000,"updateTimeStamp":1564072645000,"uuid":"6eba8358447c4486a19568cf28d30ae6","name":"文徵明山水册","titleName":"文徵明山水册","culturalRelicNo":"故00004817-2/12","surveyNo":null,"levelId":3,"levelName":"一级甲","categoryId":17,"categoryName":"绘画","dynastyId":8,"dynastyName":"明","dynastySort":0,"materialId":null,"materialName":null,"rsize":null,"author":null,"hasImage":"1","smallImage":"/relic/70656490ae1d4e50a9874c82541f38f6/8bc6a84a5ee046c28f1086319e4a760e.jpg","centerImage":"/relic/70656490ae1d4e50a9874c82541f38f6/43fc9ae3303e4194bc292b669ae24fbb.jpg","centerImgWidth":425.0,"centerImgHeight":355.23,"bigImage":"/relic/70656490ae1d4e50a9874c82541f38f6/bfd174debef04230ab66fb4d229e0a52.jpg","viewCount":1113,"collectCount":null,"position":7183.0,"isActive":1,"imageId":null,"suggestName":"文徵明山水册","suggestCulturalNo":"故00004817-2/12","suggestDynastyName":"明","suggestCategoryName":"绘画"}
    ]
}
```

curl command
```
curl -H "Referer:https://digicol.dpm.org.cn/list?page=1&category=17" -d "page=1&keyWord=&authorizeStatus=false&hasImage=false&cateList=17&ranNum=0.6671848452340445" -X POST https://digicol.dpm.org.cn/cultural/queryList
```

## Data
### Request
#### Request Headers
```
GET /relic/c0ecee84ab454a18a557c5c1b2263777/448dda0bb2b543f88f283b2a944de453.jpg HTTP/1.1
Host: shuziwenwu-1259446244.cos.ap-beijing.myqcloud.com
Accept: */*
User-Agent: Mozilla/5.0 (compatible; Rigor/1.0.0; http://rigor.com)
Referer:  https://digicol.dpm.org.cn/list?page=1&category=17
```

#### Response Headers
```
HTTP/1.1 200 OK
Content-Type: image/jpeg
Content-Length: 7877909
Connection: keep-alive
Accept-Ranges: bytes
Cache-Control: max-age=315360000
Content-Disposition: inline;filename=448dda0bb2b543f88f283b2a944de453.jpg
Date: Tue, 05 May 2020 15:04:25 GMT
ETag: "4e1a4b24b3d9f2b2f7dea10a048b5271"
Last-Modified: Fri, 25 Oct 2019 18:42:31 GMT
Server: tencent-cos
x-cos-request-id: NWViMTgwNzlfZDUyNzVkNjRfNjJiOF8xZTI5NjVk
```
#### Response Body
```
xxx
```

curl command:
```
curl -H "Referer:https://digicol.dpm.org.cn/list?page=1&category=17" -X GET https://shuziwenwu-1259446244.cos.ap-beijing.myqcloud.com/relic/c0ecee84ab454a18a557c5c1b2263777/448dda0bb2b543f88f283b2a944de453.jpg --output 展子虔游春图卷.jpeg
```