import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];
const client = createClient();
const app = express();
const PORT = 1245;
const getAsync = promisify(client.get).bind(client);

function getItemById(id) {
  return listProducts.find((element) => element.itemId === id);
}

function reserveStockById(itemId, stock) {
  client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await getAsync(`item.${itemId}`);
  return stock;
}

app.get('/list_products', (req, resp) => {
  resp.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', (req, resp) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    resp.json({ status: 'Product not found' });
  } else {
    getCurrentReservedStockById(req.params.itemId)
      .then((stock) => {
        const reserved = stock || 0;
        item.currentQuantity = item.initialAvailableQuantity - reserved;
        resp.json(item);
      });
  }
});

app.get('/reserve_product/:itemId', (req, resp) => {
  const item = getItemById(parseInt(req.params.itemId, 10));
  if (!item) {
    resp.json({ status: 'Product not found' });
  } else {
    getCurrentReservedStockById(req.params.itemId)
      .then((stock) => {
        const reserved = stock || 0;
        item.currentQuantity = item.initialAvailableQuantity - reserved;
        if (item.currentQuantity < 1) {
          resp.json({ status: 'Not enough stock available', itemId: item.itemId });
        } else {
          reserveStockById(item.itemId, 1);
          resp.json({ status: 'Reservation confirmed', itemId: 1 });
        }
      });
  }
});
app.listen(PORT, () => {
  console.log(`Listening on port ${PORT}`);
});
