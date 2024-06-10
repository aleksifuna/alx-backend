import { createClient } from 'redis';

async function connectServer() {
  const client = createClient();
  client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
  });
  console.log('Redis client connected to the server');
}
connectServer().catch((err) => {
  console.error(err);
});
