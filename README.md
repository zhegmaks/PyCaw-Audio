## Usage
```php
require __DIR__.'/vendor/autoload.php';

use cryptopupua\KunaApi\Api;
use cryptopupua\KunaApi\Exception\IncorrectResponseException;
use cryptopupua\KunaApi\KunaApi;
use cryptopupua\KunaApi\Model\History;
use cryptopupua\KunaApi\Model\MyAccount;
use cryptopupua\KunaApi\Model\Order;
use cryptopupua\KunaApi\Model\Ticker;


$api = new KunaApi(
    'https://kuna.io',
    'public key',
    'secret key'
);
$timestamp = $api->shared()->timestamp();
```
### Mapping

Each endpoint response (exclude: timestamp) can be received as `array` or as `object`.

To use mapping response to `object` set parameter `$mapping` to `true`. 

```php
