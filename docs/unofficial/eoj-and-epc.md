## 機器名:DeviceType:EOJ

### 住宅用太陽光発電:pvPowerGeneration:0x0279

https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=211

PropertyResourceName:AccessMethod:DataType:EPC:プロパティ名称|URL1|URL2
--|--|--
instantaneousElectricPowerGeneration:GET:number:0xE0:瞬時発電電力計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=212|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=221
cumulativeElectricEnergyOfGeneration:GET:number:0xE1:積算発電電力量計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=212|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=222
cumulativeElectricEnergySold:GET:number:0xE3:積算売電電力量計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=212|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=222

### 蓄電池:storageBattery:0x027D

https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=256

PropertyResourceName:AccessMethod:DataType:EPC:プロパティ名称|URL1|URL2
--|--|--
acCumulativeDischargingElectricEnergy:GET:number:0xA9:AC積算放電電力量計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=257|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=263
actualOperationMode:GET:string:0xCF:運転動作状態|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=258|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=270
operationMode:GET,PUT:string:0xDA:運転モード設定|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=259|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=274

### 電気自動車充放電器:evChargerDischarger:0x027E

https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=285

PropertyResourceName:AccessMethod:DataType:EPC:プロパティ名称|URL1|URL2
--|--|--
chargeDischargeStatus:GET:string:0xC7:車両接続・充放電可否状態|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=285|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=291
instantaneousElectricPower:GET:number:0xD3:瞬時充放電電力計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=286|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=298
cumulativeDischargingElectricEnergy:GET:number:0xD6:積算放電電力量計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=287|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=299
cumulativeChargingElectricEnergy:GET:number:0xD8:積算充電電力量計測値|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=287|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=299
actualOperationMode:GET:string:0xE1:運転動作状態|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=287|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=305

### 低圧スマート電力量メータ:lvSmartElectricEnergyMeter:0x0288

https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=401

PropertyResourceName:AccessMethod:DataType:EPC:プロパティ名称|URL1|URL2
--|--|--
reverseDirectionCumulativeElectricEnergy:GET:number,string:0xE3:積算電力量計測値 (逆方向計測値)|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=403|https://echonet.jp/wp/wp-content/uploads/pdf/General/Standard/web_api/ECHONET_Lite_Web_API_Dev_Specs_v1.6.1.pdf#page=409
