## ECHONET Lite Web API : OpenAPIドキュメント版について

### 1. 本アーカイブについて

本アーカイブは、ECHONET Lite Web APIガイドラインにて規定されている各種Descriptionに対応するOpenAPIドキュメントを提供する目的で作成されています。  
OpenAPIドキュメントは、[OAI（OpenAPI Initiative）](https://www.openapis.org)によって推進されているREST API定義仕様（[OAS（OpenAPI Specification）](https://spec.openapis.org/oas/latest.html)）に基づき生成されたWeb API仕様書となります。  
OpenAPIドキュメントを用いて、APIサーバのスタブコード（スケルトン）生成や対応クライアントコード生成、モックサーバ生成、API試験自動化、仕様Viewerでの閲覧などが可能となる各種ツールが開発されており、エコシステムが豊富であるといった特徴があります。  

ツールの例：
- Stoplight Studio（エディター）、Prism（モック）、Dredd（テスト）、openapi-generator（コード生成）、redoc（仕様書Viewer）

### 2. 本アーカイブの位置づけ、制約

本アーカイブにおけるOpenAPIドキュメントは、ECHONET Lite Web APIガイドラインをベースに、機器毎に規定されているDevice Descriptionや、応用APIとして提供されているBulk Descriptionなどの各種Descriptionからある一定の規則に基づき変換されたものとなります。各種Descriptionは、基本的に「`/elapi/v1/<サービス種>/<ID>`」へのGETメソッド呼び出しにより取得できる内容となります。  
各OpenAPIドキュメントは変換元の情報として、各種Descriptionの情報のみ使用しているため、Description内のproperties（GETメソッド、PUTメソッド）やactions（POSTメソッド）に規定の内容のみが変換対象となります。ガイドラインではPATCHメソッドやDELETEメソッドに対応したAPIもありますが、対応していません。これらAPIは必要に応じて追記・補完いただく必要がありますので、ご留意ください。  
また、本来OpenAPIドキュメントは1つのファイルとして用意されるものとなりますが、本アーカイブでは対象サービス種やリソース毎に個別のファイルとして提供されています。
個々のAPIを単独で確認する場合はそのままお使いいただけますが、必要であれば、開発されるサーバ向けに所望のOpenAPIドキュメントを複数選択して1つのファイルへマージするなどの作業は各自で適時実施してください。  

その他の制約事項の詳細については後述します。

### 3. 対応するガイドラインのバージョン

本アーカイブは、ECHONET Lite Web APIガイドラインのAPI仕様部V.1.1.7、機器仕様部V.1.6.0に対応しています。  
API仕様部の応用サービス機能では、bulk/group/history/resHistoryの各descriptionに対応しています。  
機器仕様部は、リリースされているすべての機器（device description）に対応しています。なお、ECHONET Liteの機器スーパークラスに相当するOpenAPIドキュメントは、別ファイル（openapi_commonItems.yaml）として提供されますので、各機器用のOpenAPIドキュメントの内容に対してこの機器スーパークラスの内容を適時追加してご利用ください。

### 4. ファイル・フォルダー構成

```
./ 
│  README.md
│  README-en.md
│  LICENSE
│  openapi_elapi_v1_devices.yaml # ベースパス用OpenAPIドキュメント
│
├─dd # 変換元のDevice Description集
│      airCleaner.json
│      ...
│
├─ext-apis # 変換元の応用API用Description集
│      bulks.json
│      groups.json
│      histories.json
│      ...
│
└─openapi # OpenAPIドキュメント（Device Description集や応用API用Description集から変換）
        openapi_airCleaner.yaml
        ...
```

### 5. その他、制約事項など

**バージョン、サーバ情報などの記載**

`openapi`のバージョンは3.0.3としています。OASの最新は3.1.0ですが、現時点で対応ツールが少ない点など考慮し、3.0系での対応としています。

また、`info`, `servers`についてはダミーデータを入れています。開発者のサーバ環境などに合わせて適時変更してください。

**各OpenAPIドキュメントのマージ**

前述の通り、実際にサーバ構築する際には、いくつかのOpenAPIドキュメントをマージする必要があります。ある1つの機器用ECHONET Lite Web API搭載サーバを構築する場合にて、下記ドキュメントを結合することになります。

- ベースパス用OpenAPIドキュメント：openapi_elapi_v1_devices.yaml
- スーパークラス用OpenAPIドキュメント：openapi_commonItems.yaml
- 機器用OpenAPIドキュメント：openapi_xx.yaml（xxはdevice type名）

他にも機器をサポートする場合は、対象となる機器用OpenAPIドキュメントを追加してください。

また、bulksなど応用APIを使用する場合は、openapi_bulks.yamlなど応用API用OpenAPIドキュメントを適時追加します。

各ドキュメント内の項目内容をマージする際には、`openapi`、`servers`、`info`、`security`の項目は1つに統合し、
`tags`は配列内に追加し、`paths`や`components`は重複する項目の回避（後述）を考慮した上で併記することになります。

**各OpenAPIドキュメントをマージする際の注意事項**

ECHONET Lite Web APIでは異なる機器（機種）へのURIは異なりますが、OpenAPI定義上は同一のパスで表現されるケースがあります。たとえば、機器IDが`0001`の機器（蓄電池）と機器IDが`0002`の機器（PV）に対してプロパティ一括取得を試みる場合、ECHONET Lite Web APIでは各々「`/elapi/v1/devices/0001/properties`」、「`/elapi/v1/devices/0002/properties`」のエンドポイントに対してGETメソッドを呼び出します。OpenAPIでは、`0001`や`0002`はパスパラメーターで表現されるため、`paths`の中で、いずれの場合も、`/elapi/v1/devices/{device_id}/properties`のように定義されることになります。呼び出すAPIは同一ですが、機器がXとYの場合のレスポンスボディは異なりますので、マージが必要な場合は、`responses`の成功コード内にある`schema`にてXとYの内容を`oneOf`でまとめることになります。

```yaml
              schema:
                oneOf:
                -  $ref: '#/components/schemas/propertiesStorageBattery'
                -  $ref: '#/components/schemas/propertiesPvPowerGeneration'
```

上記は`properties`の例を示していますが、`properties`配下の各プロパティリソースについても、機器が異なっていながら同一名称が使われる場合がある場合には、同様のマージ処理が必要となる点にご注意ください。

PUTメソッドなどでも同一プロパティリソース名を扱う場合は、リクエストボディが各々異なる場合、同様に`oneOf`でまとめる必要があります。

複数の機器（機種）のOpenAPIドキュメントをマージする場合、同一パスとなる箇所では、`tags`の内容にて各々のタグを列挙する必要があります。

また、`components`内の項目にて重複するケースもありえますので、重複する場合は問題が発生しないよう適時編集してください。


**required指定**

`properties`内の各キーに対する`required`指定は実施していません。
必要に応じて追記ください。

**example値**

example値は記述していません。
必要に応じて追記ください。

**responseのstatus code**

レスポンスにおけるステータスコードは、すべてのAPIに対して200, 401のみ記載しています。
200を201に変更したり、400系、500系のエラーコードが必要な場合は適時修正・追加してください。

**security**

例として、APIキーのみ対応しています。
他の方式（IDトークンなど）を使用したい場合は適時変更してください。

各OpenAPIドキュメントでは、APIキーのキー名として"`X-Elapi-key`"を使用しています。異なるキー名を使う場合は適時変更してください。

### 7. 変換ルールについて

各種DescriptionからのOpenAPIドキュメントへの変換に関して、基本的に次のようなルールを適用しています。

- `tags`: クラス名を使用
- `summary`: HTTPメソッド＋プロパティリソース名
- `operationId`: HTTPメソッド＋`devices`/`bulks`/`groups`/`histories`/`resHistories`のいずれか＋プロパティリソース名＋クラス名
- `description`: GETメソッドの場合、取得＋プロパティリソース名。PUTメソッドの場合、設定＋プロパティリソース名、POSTメソッドの場合、実行＋プロパティリソース名
- `parameters`, `requestBody`, `responses`: 各種Descriptionの対応する`schema`から生成。ただし、下記留意点あり：
  - `schema`では、各種Description内schemaで使用されている`unit`, `values`, `descriptions`, `coefficient`は利用できないため、変換時に削除

### 8. ライセンス

MITライセンスに基づいて配布されます。詳細については、「LICENSE」を参照してください。

